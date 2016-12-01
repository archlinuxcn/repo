# Maintainer: korjjj <korjjj+aur[at]gmail[dot]com>
# Contributor: TDY <tdy at archlinux dot info>
# Contributor: Adam Ehlers Nyholm Thomsen <adament at gmail dot com>
# Contributor: Nathan Jones <nathanj at insightbb dot com>

pkgname=ledger
pkgver=3.1.1
pkgrel=3
pkgdesc='A double-entry accounting system with a command-line reporting interface.'
arch=('i686' 'x86_64')
url='https://github.com/ledger/ledger'
license=('BSD')
depends=('python2' 'boost' 'libedit')
makedepends=('cmake')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/ledger/${pkgname}/archive/v${pkgver}.tar.gz"
"${pkgname}-boost-1.61.patch::https://github.com/ledger/${pkgname}/commit/1856b8c4902498843f4da37a7aaeb2ce85acc1d3.patch"
)
md5sums=('eae070cbbc1a40a277f1394d72ef0fe6'
         '004062eca8add315a125ecf1db39f2fb')

prepare() {
  cd ${srcdir}/${pkgname}-${pkgver}
  patch -p1 < ${srcdir}/${pkgname}-boost-1.61.patch
  sed -i '/enable_testing()\|add_subdirectory(test)/d' ./CMakeLists.txt
  cmake ./ \
  -DCMAKE_INSTALL_PREFIX:PATH=/usr \
  -DCMAKE_INSTALL_LIBDIR:PATH=lib \
  -DCMAKE_SKIP_RPATH:BOOL=TRUE \
  -DDISABLE_ASSERTS:BOOL=TRUE \
  -DBUILD_DEBUG:BOOL=FALSE \
  -DBUILD_DOCS:BOOL=FALSE \
  -DUSE_PYTHON:BOOL=TRUE \
  -DBUILD_EMACSLISP:BOOL=TRUE
}

build() {
  cd ${srcdir}/${pkgname}-${pkgver}
  make
}

package() {
  cd ${srcdir}/${pkgname}-${pkgver}
  make DESTDIR=${pkgdir} install
  install -Dm644 ${srcdir}/${pkgname}-${pkgver}/LICENSE.md ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
}

# vim:set ts=2 sw=2 et:
