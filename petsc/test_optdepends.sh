#!/bin/bash

# Test if external packages for PETSC are installed

CONFOPTS=""

## External downloads
#for external_pkg in hypre; do
	#CONFOPTS="${CONFOPTS} --download-${external_pkg}=1"
#done

# Add hypre support
if [ -f "/usr/lib/libHYPRE.so" ]; then
	CONFOPTS="${CONFOPTS} --with-hypre=1"
fi

# Add mumps support
if [ -f "/usr/lib/libmumps_common.so" ]; then
	CONFOPTS="${CONFOPTS} --with-mumps=1"
fi

# Add fftw support
if [ -f "/usr/lib/libfftw3_mpi.so" ]; then
	CONFOPTS="${CONFOPTS} --with-fftw=1"
fi

# Add hdf5 support
if [[ "$(h5stat -V)" ]]; then
	CONFOPTS="${CONFOPTS} --with-hdf5=1"
fi

# Add scalapack support
if [ -f "/usr/lib/pkgconfig/scalapack.pc" ]; then
	CONFOPTS="${CONFOPTS} --with-scalapack=1"
fi

# Add suitesparse support
if [ -f "/usr/include/SuiteSparse_config.h" ]; then
	CONFOPTS="${CONFOPTS} --with-suitesparse=1"
fi
 
# Add metis support
if [ -f "/usr/include/metis.h" ]; then
	CONFOPTS="${CONFOPTS} --with-metis=1"
	# Add parmetis support
	if [ -f "/usr/include/parmetis.h" ]; then
		CONFOPTS="${CONFOPTS} --with-parmetis=1"
	fi
fi

# Add scotch support
SCOTCH_DIR="/usr/include/scotch"
if [ -d "${SCOTCH_DIR}" ]; then
	SCOTCH_LIBS="libesmumps.so,libptscotch.so,libptscotcherr.so,libscotch.so,libscotcherr.so"
	# Include bzip2 if scotch was build with bzip2 support
	if [ -f /usr/include/bzlib.h ];then
		SCOTCH_LIBS="${SCOTCH_LIBS},libbz2.so"
	fi
	SCOTCH_LIBS="[${SCOTCH_LIBS}]"
	CONFOPTS="${CONFOPTS} --with-ptscotch=1 --with-ptscotch-lib=${SCOTCH_LIBS} --with-ptscotch-include=${SCOTCH_DIR}"
fi

# Add superlu support
SUPERLU_DIR="/usr/include/superlu"
if [ -d "${SUPERLU_DIR}" ]; then
	CONFOPTS="${CONFOPTS} --with-superlu=1 --with-superlu-lib=-lsuperlu --with-superlu-include=${SUPERLU_DIR}"
fi

# Add pastix support
PASTIX_CONF=$(which pastix-conf)
if [ -f "${PASTIX_CONF}" ]; then
	PASTIX_DIR="$($PASTIX_CONF --incs | sed 's/-I//')"
	if [ ! -d ${PASTIX_DIR} ]; then
		PASTIX_DIR="[]"
	fi
	#PASTIX_LIBS="$($PASTIX_CONF --libs)"
	PASTIX_LIBS="[libpastix.a,librt.so,libhwloc.so,libpthread.a]"
	CONFOPTS="${CONFOPTS} --with-pastix=1 --with-pastix-lib=${PASTIX_LIBS} --with-pastix-include=${PASTIX_DIR}"
fi

# Add trilinos support
if [ "${TRILINOS_DIR}" ]; then
	CONFOPTS="${CONFOPTS} --with-ml-dir=${TRILINOS_DIR}"
	# Add boost support (may be useful for trilinos)
	#CONFOPTS="${CONFOPTS} --with-boost=1"
fi

echo "${CONFOPTS}"
