TARGET = simple_encrypt

$(TARGET): main.c external/nacl/core.c external/nacl/xor.c
	cc -Iexternal/nacl -o $(TARGET) $^
