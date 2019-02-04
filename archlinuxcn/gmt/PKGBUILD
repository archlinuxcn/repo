# Contributor: Benjamin Sick
# Contributor: Rich Li <rich@dranek.com>

pkgname=gmt
pkgver=5.4.5
pkgrel=1
pkgdesc="Generic Mapping Tools: Collection of tools for manipulating geographic and Cartesian data sets, and generating EPS maps."
arch=(i686 x86_64)
url="http://gmt.soest.hawaii.edu/"
license=('GPL')
makedepends=('cmake')
depends=('gdal' 'fftw' 'lapack')
optdepends=(
    'ghostscript'
    'python-sphinx'
    'python2-sphinx'
    'gmt-coast: coastlines'
    'gmt-dcw: digital chart of the world polygon map')
conflicts=('gmt4')
install='gmt.install'
#source=("ftp://ftp.soest.hawaii.edu/gmt/${pkgname}-${pkgver}-src.tar.xz")
#source=("ftp://ftp.star.nesdis.noaa.gov/pub/sod/lsa/gmt/${pkgname}-${pkgver}-src.tar.xz")
#source=("ftp://ftp.iris.washington.edu/pub/gmt/${pkgname}-${pkgver}-src.tar.xz")
#source=("ftp://ftp.iag.usp.br/pub/gmt/${pkgname}-${pkgver}-src.tar.xz")
source=("https://mirrors.ustc.edu.cn/gmt/${pkgname}-${pkgver}-src.tar.xz")
md5sums=('846c7717ca8a6e2c76cc5538331ff59e')

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  rm -fr build && mkdir build
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
