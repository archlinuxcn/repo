# Maintainer: Morgenstern <charles [at] charlesbwise [dot] com>

pkgname=cherrytree
pkgver=0.99.25
pkgrel=2
pkgdesc="Hierarchical note-taking application"
arch=('x86_64')
url="https://www.giuspen.com/cherrytree/"
license=('GPL3')
depends=('gspell'
	 'gtksourceviewmm'
	 'libxml++2.6'
	 'uchardet')
makedepends=('cmake'
	     'python')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/giuspen/cherrytree/archive/${pkgver}.tar.gz")
sha256sums=('fc35b15655b25299576cfceb73bb69c8b1201ceb82fe6e75591e529506b5177d')

prepare() {
  # Fix automatic optimisation flag override
  sed -i 's/-O3/-O2/' "${pkgname}-${pkgver}/CMakeLists.txt"
}

build() {
  cmake \
	-B "${pkgname}-${pkgver}/build" \
	-S "${pkgname}-${pkgver}" \
	-DBUILD_TESTING:BOOL=OFF \
	-Wno-dev
  make -C "${pkgname}-${pkgver}/build"
}

package() {
  make -C "${pkgname}-${pkgver}/build" DESTDIR="${pkgdir}" install
}
