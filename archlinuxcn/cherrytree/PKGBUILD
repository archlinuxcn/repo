# Maintainer: Morgenstern <charles [at] charlesbwise [dot] com>

pkgname=cherrytree
pkgver=0.99.27
pkgrel=1
pkgdesc="Hierarchical note-taking application"
arch=('x86_64')
url="https://www.giuspen.com/${pkgname}/"
license=('GPL3')
depends=('gspell'
	 'gtksourceviewmm'
	 'libxml++2.6'
	 'uchardet')
makedepends=('cmake'
	     'python')
source=(https://www.giuspen.com/software/${pkgname}_${pkgver}.tar.xz)
sha256sums=('1c10020eef6e222bbdaa87b9d15d85b703380aba4727a2fbd0f09f8cc353c606')

prepare() {
  # Fix automatic optimisation flag override
  sed -i 's/-O3/-O2/' "${pkgname}_${pkgver}/CMakeLists.txt"
}

# Remove GMOCK and TESTING options to build and run tests
# If utilising tests, make sure cherrytree is NOT already running!
build() {
  cmake \
	-B "${pkgname}_${pkgver}/build" \
	-S "${pkgname}_${pkgver}" \
	-DBUILD_GMOCK:BOOL='OFF' \
	-DBUILD_TESTING:BOOL='OFF' \
	-DINSTALL_GTEST:BOOL='OFF' \
	-Wno-dev
  make -C "${pkgname}_${pkgver}/build"
}

package() {
  make -C "${pkgname}_${pkgver}/build" DESTDIR="${pkgdir}" install
}
