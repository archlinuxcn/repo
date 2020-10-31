OSTYPE = $(shell uname)

CFLAGS= -O3  -w -fPIC $(arch_flags) -L./cspice  -I./cspice
CC           = gcc
LIBS          = -lcspice -lm

ifneq ($(findstring Darwin,$(OSTYPE)),)
SO_Name       = libpasspice.dylib
CFLAGS        = -O3 -fPIC $(arch_flags) -L./cspice  -I./cspice -Wno-implicit-function-declaration
LIBFLAGS      = -Wl,-single_module -dynamiclib  -lc -lm -mmacosx-version-min=10.6
else
SOName        = libpasspice.so.1
SO_Name       = libpasspice.so.1.1
LIBFLAGS      = -shared -Wl,-soname,$(SOName)
endif

SRC =	passpice.c 

.PHONY: all cspice clean

all: cspice $(SO_Name)

$(SO_Name): cspice $(OBJS)
	$(CC) $(CFLAGS) $(LIBFLAGS) -o $@ $(SRC) $(LIBS)

cspice:
	$(MAKE) -C cspice  all

clean:
	$(MAKE) -C cspice clean
	rm -f *.a *.o $(SO_Name)
