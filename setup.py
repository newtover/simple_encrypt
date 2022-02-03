from distutils.core import setup, Extension

salsa20_lib = Extension(
    '_simple_encrypt',
    sources = [
         'external/nacl/xor.c',
         'external/nacl/core.c',
    ],
)

setup(
    name='simple_encrypt',
    version='0.0.1',
    py_modules = ['simple_encrypt'],
    ext_modules=[salsa20_lib],
)

