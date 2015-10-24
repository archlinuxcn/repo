#
# Copyright (c) 2002-2006 Hewlett-Packard Development Company, L.P.
# Contributed by Stephane Eranian <eranian@hpl.hp.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
# of the Software, and to permit persons to whom the Software is furnished to do so, 
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.  
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# This file is part of libpfm, a performance monitoring support library for
# applications on Linux.
#

#
# This file defines the global compilation settings.
# It is included by every Makefile
#
#
SYS  := $(shell uname -s)
ARCH := $(shell uname -m)
ifeq (i686,$(findstring i686,$(ARCH)))
override ARCH=i386
endif
ifeq (i586,$(findstring i586,$(ARCH)))
override ARCH=i386
endif
ifeq (i486,$(findstring i486,$(ARCH)))
override ARCH=i386
endif
ifeq (i386,$(findstring i386,$(ARCH)))
override ARCH=i386
endif
ifeq (i86pc,$(findstring i86pc,$(ARCH)))
override ARCH=i386
endif
ifeq ($(ARCH),x86_64)
override ARCH=x86_64
endif
ifeq ($(ARCH),amd64)
override ARCH=x86_64
endif
ifeq (ppc,$(findstring ppc,$(ARCH)))
override ARCH=powerpc
endif
ifeq (sparc64,$(findstring sparc64,$(ARCH)))
override ARCH=sparc
endif
ifeq (armv7,$(findstring armv7,$(ARCH)))
override ARCH=arm
endif
ifeq (mips64,$(findstring mips64,$(ARCH)))
override ARCH=mips
endif
ifeq (mips,$(findstring mips,$(ARCH)))
override ARCH=mips
endif

#
# CONFIG_PFMLIB_SHARED: y=compile static and shared versions, n=static only
# CONFIG_PFMLIB_DEBUG: enable debugging output support
# CONFIG_PFMLIB_NOPYTHON: do not generate the python support, incompatible
# with PFMLIB_SHARED=n
#
CONFIG_PFMLIB_SHARED?=y
CONFIG_PFMLIB_DEBUG?=y
CONFIG_PFMLIB_NOPYTHON?=y

#
# Cell Broadband Engine is reported as PPC but needs special handling.
#
ifeq ($(SYS),Linux)
MACHINE := $(shell grep -q 'Cell Broadband Engine' /proc/cpuinfo && echo cell)
ifeq (cell,$(MACHINE))
override ARCH=cell
endif
endif

#
# Library version
#
VERSION=4
REVISION=4
AGE=0

#
# Where should things (lib, headers, man) go in the end.
#
PREFIX=/usr
LIBDIR=$(PREFIX)/lib
INCDIR=$(PREFIX)/include
MANDIR=$(PREFIX)/share/man
DOCDIR=$(PREFIX)/share/doc/libpfm-$(VERSION).$(REVISION).$(AGE)

#
# System header files
#
# SYSINCDIR : where to find standard header files (default to .)
SYSINCDIR=.

#
# Configuration Paramaters for libpfm library
#
ifeq ($(ARCH),ia64)
CONFIG_PFMLIB_ARCH_IA64=y
endif

ifeq ($(ARCH),x86_64)
CONFIG_PFMLIB_ARCH_X86_64=y
CONFIG_PFMLIB_ARCH_X86=y
endif

ifeq ($(ARCH),i386)
CONFIG_PFMLIB_ARCH_I386=y
CONFIG_PFMLIB_ARCH_X86=y
endif

ifeq ($(ARCH),mips)
CONFIG_PFMLIB_ARCH_MIPS=y
endif

ifeq ($(ARCH),powerpc)
CONFIG_PFMLIB_ARCH_POWERPC=y
endif

ifeq ($(ARCH),sparc)
CONFIG_PFMLIB_ARCH_SPARC=y
endif

ifeq ($(ARCH),arm)
CONFIG_PFMLIB_ARCH_ARM=y
endif

ifeq ($(XTPE_COMPILE_TARGET),linux)
CONFIG_PFMLIB_ARCH_CRAYXT=y
endif

ifeq ($(ARCH),cell)
CONFIG_PFMLIB_CELL=y
endif

# handle special cases for 64-bit builds
ifeq ($(BITMODE),64)
ifeq ($(ARCH),powerpc)
CONFIG_PFMLIB_ARCH_POWERPC64=y
endif
endif

#
# you shouldn't have to touch anything beyond this point
#

#
# The entire package can be compiled using 
# icc the Intel Itanium Compiler (7.x,8.x, 9.x)
# or GNU C
#CC=icc
CC?=gcc
LIBS=
INSTALL=install
LN?=ln -sf
PFMINCDIR=$(TOPDIR)/include
PFMLIBDIR=$(TOPDIR)/lib
DBG?=-g -Wall -Werror
CFLAGS+=$(OPTIM) $(DBG) -I$(SYSINCDIR) -I$(PFMINCDIR)
MKDEP=makedepend
PFMLIB=$(PFMLIBDIR)/libpfm.a

ifeq ($(CONFIG_PFMLIB_ARCH_POWERPC64),y)
CFLAGS+= -m64
LDFLAGS+= -m64
LIBDIR=$(DESTDIR)/lib64
endif

ifeq ($(CONFIG_PFMLIB_DEBUG),y)
CFLAGS += -DCONFIG_PFMLIB_DEBUG
endif

CTAGS?=ctags

#
# Python is for use with perf_events
# so it only works on Linux
#
ifneq ($(SYS),Linux)
CONFIG_PFMLIB_NOPYTHON=y
endif

#
# mark that we are compiling on Linux
#
ifeq ($(SYS),Linux)
CFLAGS+= -DCONFIG_PFMLIB_OS_LINUX
endif

#
# compile examples statically if library is
# compile static
# not compatible with python support, so disable for now
#
ifeq ($(CONFIG_PFMLIB_SHARED),n)
LDFLAGS+= -static
CONFIG_PFMLIB_NOPYTHON=y
endif
