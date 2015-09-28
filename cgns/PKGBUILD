# Maintainer: eolianoe <eolianoe At GoogleMAIL DoT com>
# Contriburor: Mathias Anselmann <mathias.anselmann@gmail.com>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: lainme <lainme993@gmail.com>
# Contributor: Klimov Max <cleemmi@gmail.com>

pkgname=cgns
_PKGNAME=CGNS
pkgver=3.2.1
pkgrel=1
pkgdesc='Standard for recording and recovering computer data associated with the numerical solution of fluid dynamics equations'
arch=('i686' 'x86_64')
url='http://www.cgns.org'
license=('custom')
provides=('libcgns' 'libcgns-paraview')
conflicts=('ligcgns2')
depends=('tk' 'hdf5' 'libxmu' 'glu')
makedepends=('gcc-fortran' 'cmake')
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/${_PKGNAME}/${_PKGNAME}/archive/v${pkgver}.tar.gz")
sha256sums=('677d0da94f0892b72b96da7cf4de51f661acfff1141c585af50a531fa161773f')

# need to tell cmake when to build 64bit version
if [[ $CARCH == "x86_64" ]]
then
  _64bits=ON
else
  _64bits=OFF
fi

prepare(){
  cd "${srcdir}"

  # Out of source build
  rm -rf build
  mkdir -p build
}

build() {
  cd "${srcdir}/build"

  cmake \
    -DCGNS_BUILD_CGNSTOOLS:BOOL=ON \
    -DCGNS_BUILD_SHARED:BOOL=ON \
    -DCGNS_ENABLE_64BIT:BOOL=${_64bits} \
    -DCGNS_ENABLE_FORTRAN:BOOL=ON \
    -DCGNS_ENABLE_HDF5:BOOL=ON \
    -DCGNS_ENABLE_LEGACY:BOOL=ON \
    -DCGNS_ENABLE_SCOPING:BOOL=OFF \
    -DCGNS_ENABLE_TESTS:BOOL=ON \
    -DCMAKE_BUILD_TYPE:STRING="Release" \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    "../${_PKGNAME}-${pkgver}"

  make
}


check() {
  cd "${srcdir}/build"

  make test
}

package() {
  cd "${srcdir}/build"

  make DESTDIR="${pkgdir}" install

  # install license
  install -Dm644 "${srcdir}/${_PKGNAME}-${pkgver}/license.txt" \
    "${pkgdir}/usr/share/licenses/${pkgname}/license.txt"
}
