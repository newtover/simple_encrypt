The directory contains two files taken from nacl-20110221 (taken from https://nacl.cr.yp.to/install.html):

- crypto_stream/salsa20/ref/xor.c (fixed int to uint32 on line 23)
- crypto_core/salsa20/ref/core.c

Header files contain just enough code to make the the two *.c files work.
