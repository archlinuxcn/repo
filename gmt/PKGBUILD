# Contributor: Benjamin Sick
# Contributor: Rich Li <rich@dranek.com>

pkgname=gmt
pkgver=5.2.1
pkgrel=3
pkgdesc="Generic Mapping Tools: Collection of tools for manipulating geographic and Cartesian data sets, and generating EPS maps."
arch=(i686 x86_64)
url="http://gmt.soest.hawaii.edu/"
license=('GPL')
makedepends=('cmake')
depends=('gdal' 'fftw')
optdepends=(
    'ghostscript'
    'python-sphinx'
    'python2-sphinx'
    'gmt-coast: coastlines'
    'gmt-dcw: digital chart of the world polygon map')
conflicts=('gmt4')
install='gmt.install'
source=(
    "ftp://ftp.soest.hawaii.edu/gmt/${pkgname}-${pkgver}-src.tar.xz"
    "float_cast.patch")
md5sums=('4823ab45965a55d5d8869181ae3b0cca'
         'e8f073eba78712e5a773f1abeb9dfb4f')

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  rm -fr build && mkdir build
  patch -d "src/" < "${srcdir}/float_cast.patch"
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"
  # -DLICENSE_RESTRICTED=off \
  cmake -DCMAKE_INSTALL_PREFIX=/usr \
    -DGSHHG_ROOT=/usr/share/gmt/coast \
    -DGMT_LIBDIR=lib \
    -DDCW_ROOT=/usr/share/gmt/dcw \
    -DGMT_DATADIR=share/gmt \
    -DGMT_MANDIR=share/man \
    -DGMT_DOCDIR=share/doc/gmt \
    -DCMAKE_BUILD_TYPE=Release \
    ..
  export MAKEFLAGS="-j1"
  make || return 1
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}/build"
  make "DESTDIR=${pkgdir}" install || return 1
}

# vim:set ts=2 sw=2 et:
