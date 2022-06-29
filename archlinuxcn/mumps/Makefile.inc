#
#  This file is part of MUMPS 5.1.2, released
#  on Mon Oct  2 07:37:01 UTC 2017
#
################################################################################
#
#   Makefile.inc.generic
#
#   This defines some parameters dependent on your platform; you should
#   look for the approriate file in the directory ./Make.inc/ and copy it
#   into a file called Makefile.inc. For example, from the MUMPS root
#   directory, use
#   "cp Make.inc/Makefile.inc.generic ./Makefile.inc"
#   (see the main README file for details)
#
#   If you do not find any suitable Makefile in Makefile.inc, use this file:
#   "cp Make.inc/Makefile.inc.generic ./Makefile.inc" and modify it according
#   to the comments given below. If you manage to build MUMPS on a new platform,
#   and think that this could be useful to others, you may want to send us
#   the corresponding Makefile.inc file.
#
################################################################################


########################################################################
#Begin orderings
#
# NOTE that PORD is distributed within MUMPS by default. It is recommended to
# install other orderings. For that, you need to obtain the corresponding package
# and modify the variables below accordingly.
# For example, to have Metis available within MUMPS:
#          1/ download Metis and compile it
#          2/ uncomment (suppress # in first column) lines
#             starting with LMETISDIR,  LMETIS
#          3/ add -Dmetis in line ORDERINGSF
#             ORDERINGSF  = -Dpord -Dmetis
#          4/ Compile and install MUMPS
#             make clean; make   (to clean up previous installation)
#
#          Metis/ParMetis and SCOTCH/PT-SCOTCH (ver 6.0 and later) orderings are recommended.
#

SCOTCHDIR  = /usr
ISCOTCH    = -I$(SCOTCHDIR)/include/scotch
#
# You have to choose one among the following two lines depending on
# the type of analysis you want to perform. If you want to perform only
# sequential analysis choose the first (remember to add -Dscotch in the ORDERINGSF
# variable below); for both parallel and sequential analysis choose the second
# line (remember to add -Dptscotch in the ORDERINGSF variable below)

LSCOTCH    = -L$(SCOTCHDIR)/lib -lesmumps -lbz2 -lz -lscotch -lscotcherr
#LSCOTCH    = -L$(SCOTCHDIR)/lib -lptesmumps -lptscotch -lptscotcherr


LPORDDIR = $(topdir)/PORD/lib/
IPORD    = -I$(topdir)/PORD/include/
LPORD    = -L$(LPORDDIR) -lpord

LMETISDIR = /usr/lib
IMETIS    = -I/usr/include/metis

# You have to choose one among the following two lines depending on
# the type of analysis you want to perform. If you want to perform only
# sequential analysis choose the first (remember to add -Dmetis in the ORDERINGSF
# variable below); for both parallel and sequential analysis choose the second
# line (remember to add -Dparmetis in the ORDERINGSF variable below)

LMETIS    = -L$(LMETISDIR) -lmetis
#LMETIS    = -L$(LMETISDIR) -lparmetis -lmetis

# The following variables will be used in the compilation process.
# Please note that -Dptscotch and -Dparmetis imply -Dscotch and -Dmetis respectively.
# If you want to use Metis 4.X or an older version, you should use -Dmetis4 instead of -Dmetis
# or in addition with -Dparmetis (if you are using parmetis 3.X or older).
#ORDERINGSF = -Dscotch -Dmetis -Dpord -Dptscotch -Dparmetis
ORDERINGSF  = -Dscotch -Dmetis -Dpord
ORDERINGSC  = $(ORDERINGSF)

LORDERINGS = $(LMETIS) $(LPORD) $(LSCOTCH)
IORDERINGSF = $(ISCOTCH)
IORDERINGSC = $(IMETIS) $(IPORD) $(ISCOTCH)

#End orderings
########################################################################

########################################################################
# DEFINE HERE SOME COMMON COMMANDS, THE COMPILER NAMES, ETC...

# PLAT : use it to add a default suffix to the generated libraries
PLAT    =
# Library extension, + C and Fortran "-o" option
# may be different under Windows
LIBEXT  = .so
OUTC    = -o
OUTF    = -o
# RM : remove files
RM      = /bin/rm -f
# CC : C compiler
CC      = mpicc
# FC : Fortran 90 compiler
FC      = mpif90
# FL : Fortran linker
FL      = mpif90
# AR : Archive object in a library
#      keep a space at the end if options have to be separated from lib name
AR      = $(CC) -shared $(OPTC) -o
# RANLIB : generate index of an archive file
#   (optionnal use "RANLIB = echo" in case of problem)
# RANLIB  = ranlib
RANLIB  = echo

# DEFINE HERE YOUR LAPACK LIBRARY

#LAPACK = -llapack

# SCALAP should define the SCALAPACK and  BLACS libraries.
SCALAP  = -lscalapack -llapack

# INCLUDE DIRECTORY FOR MPI
INCPAR = -I/usr/include/openmpi

# LIBRARIES USED BY THE PARALLEL VERSION OF MUMPS: $(SCALAP) and MPI
LIBPAR = $(SCALAP) -L/usr/lib/openmpi -lmpi_usempif08 -lmpi_usempi_ignore_tkr -lmpi_mpifh -lmpi

# The parallel version is not concerned by the next two lines.
# They are related to the sequential library provided by MUMPS,
# to use instead of ScaLAPACK and MPI.
INCSEQ  = -I$(topdir)/libseq
LIBSEQ  = -L$(topdir)/libseq -lmpiseq

# DEFINE HERE YOUR BLAS LIBRARY

LIBBLAS = -lblas

# DEFINE YOUR PTHREAD LIBRARY
LIBOTHERS = -lpthread

# FORTRAN/C COMPATIBILITY:
#  Use:
#    -DAdd_ if your Fortran compiler adds an underscore at the end
#              of symbols,
#     -DAdd__ if your Fortran compiler adds 2 underscores,
#
#     -DUPPER if your Fortran compiler uses uppercase symbols
#
#     leave empty if your Fortran compiler does not change the symbols.
#

CDEFS = -DAdd_

#COMPILER OPTIONS
OPTF    = -DALLOW_NON_INIT ${CFLAGS} -fPIC -fallow-argument-mismatch
OPTC    = ${CFLAGS} -fPIC
OPTL    = ${CFLAGS} -fPIC

# CHOOSE BETWEEN USING THE SEQUENTIAL OR THE PARALLEL VERSION.

#Sequential:
#INCS = $(INCSEQ)
#LIBS = $(LIBSEQ)
#LIBSEQNEEDED = libseqneeded

#Parallel:
INCS = $(INCPAR)
LIBS = $(LIBPAR)
LIBSEQNEEDED =

