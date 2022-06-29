# Makefile of Sample program
# Written by NAKATA, Maho <maho@FreeBSD.org>, modified by mickele <mimocciola@yahoo.com>

all: densg

densg: example1.f
	mpif77 -o densg example1.f -L/usr/lib -lscalapack -lblacs -lblacsf77 -lblacs -llapack -lf77blas -lcblas -latlas
