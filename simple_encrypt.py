import base64
import ctypes
from pathlib import Path
import sys

__all__ = [
    'crypto_stream',
]


def _compute_dll_path():
    site_packages = None
    for path in sys.path:
        # /usr/local/lib/python3.9/dist-packages
        if (path.endswith('site-packages') or path.endswith('dist-packages')) and path.startswith(sys.prefix):
            site_packages = Path(path)
            break
    if not site_packages:
        raise ValueError('there is no site-packages in sys.path')
    dll_hyps = list(site_packages.glob('_simple_encrypt.*'))
    if not dll_hyps:
        raise ValueError('no _simple_encrypt dll found')
    if len(dll_hyps) > 1:
        raise ValueError(f'too many _simple_encrypt dlls: {dll_hyps}')
    return dll_hyps[0]


_dll_path = _compute_dll_path()
_samba20 = ctypes.CDLL(str(_dll_path))

"""
        unsigned char *c,
  const unsigned char *m,unsigned long long mlen,
  const unsigned char *n,
  const unsigned char *k
)

"""
_samba20.crypto_stream_xor.restype = ctypes.c_int
_samba20.crypto_stream_xor.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint64, ctypes.c_char_p, ctypes.c_char_p]


def crypto_stream(key, nonce, message):
    """encrypts and decrypts byte message using 32-byte key and 8-byte nonce"""
    assert isinstance(key, bytes)
    assert len(key) == 32
    assert isinstance(nonce, bytes)
    assert len(nonce) == 8
    assert isinstance(message, bytes)

    mlen = len(message)
    buf = ctypes.create_string_buffer(mlen)
    _samba20.crypto_stream_xor(buf, message, mlen, nonce, key)
    return buf.raw


def test1():

    text = 20 * b'hello, salsa20! '
    from os import urandom

    nonce = urandom(8)
    key = urandom(32)

    encoded = crypto_stream(key, nonce, text)
    decoded = crypto_stream(key, nonce, encoded)
    assert text == decoded


def decode_key(path):
    with path.open('rb') as f1:
        encoded = f1.read()
    decoded = base64.decodebytes(encoded)
    if len(decoded) != 40:
        raise ValueError("Decoded base64 value is not 40 bytes long")
    return decoded[:32], decoded[32:]


def main():
    import argparse
    parser = argparse.ArgumentParser("A simple script that encodes/decodes stdin using salsa20 and outputs the result into stdout\n(It sucks the whole intput into memory.)\n")
    parser.add_argument("--key", type=Path, required=True, help="File with base64-encrypted 32-byte key and 8-byte nonce")
    args = parser.parse_args()

    if not args.key.exists():
        parser.error(f"The key file {args.key} doesn't exist")

    key, nonce = decode_key(args.key)
    raw_data = sys.stdin.buffer.read()
    encoded_data = crypto_stream(key, nonce, raw_data)
    sys.stdout.buffer.write(encoded_data)


test1()


if __name__ == '__main__':
    main()

