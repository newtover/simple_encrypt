#ifndef _CORE_H
#define _CORE_H

#include "crypto_core.h"

int crypto_core(
        unsigned char *out,
  const unsigned char *in,
  const unsigned char *k,
  const unsigned char *c
);

#define crypto_core_salsa20 crypto_core

#endif /* _CORE_H */
