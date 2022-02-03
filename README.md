# simple_encrypt
A POC for a simple encryption tool based on an algorithm in public domain. The idea is to depend on an algorithm instead of a specific application.

I decided to take Daniel J. Bernstein's [Salsa20](https://en.wikipedia.org/wiki/Salsa20) as a base. There are many implementations on his [site](https://cr.yp.to/snuffle.html). And an implementation is included in [NACL](https://nacl.cr.yp.to/) as well.

I took two C files from there and added the simplest header files to make them work. Then I wrapped the only required function `crypto_stream_xor` in a python wrapper. In python it is:

```
crypto_stream(key, nonce, message)
    encrypts and decrypts byte message using 32-byte key and 8-byte nonce
```

```
>>> import os
>>> key = os.urandom(32)
>>> nonce = os.urandom(8)
>>> import simple_encrypt
>>> message = b'Salsa20 and the closely related ChaCha are stream ciphers developed by Daniel J. Bernstein.'
>>> simple_encrypt.crypto_stream(key, nonce, message)
b'\x01\'\xc4\xdfJ\xc2!\x88\x94\x9a\xc4\xc2@\x08\x16\n\xafD="\xfc\xb2\x96?C|=\xde\r\xac;\x17\xd0\xcb\xf1J\x9c\xb13\xa59\xe0*\x0b \xfd\xb0!\xd6\x8d\x89U\xb23c\x15d\xc8\xb8bn&b\x93\xbb\xb9w\x1c(\xcc8e\xaf\xd5\r\xc7r\xc9\xe6\xaa\x9c\x1f\x9b\xd9\xfew\xe7cRa~'
>>> simple_encrypt.crypto_stream(key, nonce, _)
b'Salsa20 and the closely related ChaCha are stream ciphers developed by Daniel J. Bernstein.'
```


The module can be installed as 

```
pip install .
```

It requires tools to compile the C extension.

The module works as a script:

```
usage: A simple script that encodes/decodes stdin using salsa20 and outputs the result into stdout
(It sucks the whole intput into memory.)
 [-h] --key KEY

optional arguments:
  -h, --help  show this help message and exit
  --key KEY   File with base64-encrypted 32-byte key and 8-byte nonce
```
