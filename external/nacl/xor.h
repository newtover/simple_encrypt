#ifndef _XOR_H
#define _XOR_H

#include "crypto_core_salsa20.h"
#include "crypto_stream.h"


int crypto_stream_xor(
        unsigned char *c,
  const unsigned char *m,unsigned long long mlen,
  const unsigned char *n,
  const unsigned char *k
);

#endif /* _XOR_H */
