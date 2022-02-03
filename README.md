# simple_encrypt
A POC for a simple encryption tool based on an algorithm in public domain. The idea is to depend on an algorithm instead of a specific application.

I decided to take Daniel J. Bernstein's [Salsa20](https://en.wikipedia.org/wiki/Salsa20) as a base. There are many implementations on his [site](https://cr.yp.to/snuffle.html). And an implementation is included in [NACL](https://nacl.cr.yp.to/) as well.

I took two C files from there and added the simplest header files to make them work. Then I wrapped the only required function `crypto_stream_xor` in a python wrapper. In python it is:

```
crypto_stream(key, nonce, message)
    encrypts and decrypts byte message using 32-byte key and 8-byte nonce
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
