pkgname=med
pkgver=3.3.1
pkgrel=2
pkgdesc="MED stands for Modelisation et Echanges de Donnees, i.e. Data Modelization and Exchanges - MED is code-aster exchange module linked to hdf5"
url="http://www.code-aster.org/outils/med/"
license=('LGPL')
depends=('hdf5' 'openmpi' 'swig')
makedepends=('gcc-fortran' 'python2')
optdepends=('tk')
arch=('x86_64')
source=("http://files.salome-platform.org/Salome/other/${pkgname}-${pkgver}.tar.gz"
        "hdf5-1.10-support.patch")
sha256sums=('dd631ef813838bc7413ff0dd6461d7a0d725bcfababdf772ece67610a8d22588'
            '55cf95f1a3b7abf529bb2ded6c9a491459623c830dc16518058ff53ab203291c')

prepare () {
  cd ${srcdir}/${pkgname}-${pkgver}_SRC
  # https://salsa.debian.org/science-team/med-fichier/tree/master/debian/patches
  patch -p1 -i "${srcdir}"/hdf5-1.10-support.patch
  autoreconf -i
}

build() {
  cd ${srcdir}/${pkgname}-${pkgver}_SRC
  export FFLAGS="-fopenmp -fPIC -fdefault-double-8 -fdefault-integer-8 -fdefault-real-8 -ffixed-line-length-0 ${CFLAGS}"
  export FCFLAGS="-fopenmp -fPIC -fdefault-double-8 -fdefault-integer-8 -fdefault-real-8 -ffixed-line-length-0 ${CFLAGS}"
  export CPPFLAGS="-DHAVE_F77INT64 ${CPPFLAGS}"
  export F77=mpif90
  export FC=mpif90
  export PYTHON=/usr/bin/python2
  ./configure --with-f90=mpif90 --prefix=/usr --datadir=/usr/share/med --with-swig=yes --disable-dependency-tracking
  make
}

package() {
  cd ${srcdir}/${pkgname}-${pkgver}_SRC
  make DESTDIR=${pkgdir} install
}
