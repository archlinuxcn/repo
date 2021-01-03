# Maintainer: Morgenstern <charles [at] charlesbwise [dot] com>
# Contributor: NicoHood <archlinux {cat} nicohood {dog} de>

pkgname=cherrytree
pkgver=0.99.28
pkgrel=1
pkgdesc="Hierarchical note-taking application"
arch=('x86_64')
url="https://www.giuspen.com/${pkgname}/"
license=('GPL3')
depends=('fmt'
	 'gspell'
	 'gtksourceviewmm'
	 'libxml++2.6'
	 'uchardet')
optdepends=('xorg-xhost: allow chroot access to X server for running tests')
makedepends=('cmake'
	     'python'
	     'spdlog')
source=(https://www.giuspen.com/software/${pkgname}_${pkgver}.tar.xz{,.asc})
sha256sums=('54d246dcd15ce699d6260a9322289a5fcba40fa2490cfea68dc394541c0d74c9'
            'SKIP')
validpgpkeys=('C7BF38CE0BD442C2369AA984049128A20CE0648D') # Giuseppe Penone <giuspen [at] gmail [dot] com>

build() {
  cmake \
	-B "${pkgname}_${pkgver}/build" \
	-S "${pkgname}_${pkgver}" \
	-DBUILD_GMOCK:BOOL='OFF' \
	-DBUILD_TESTING:BOOL='OFF' \
	-Wno-dev
  make -C "${pkgname}_${pkgver}/build"
}

# NOTE: In order to run tests in a clean chroot, you must allow it access your X server:
# xhost +local:
# https://wiki.archlinux.org/index.php/chroot#Run_graphical_applications_from_chroot
#check() {
#  export DISPLAY=:0
#  cmake \
#	-B "${pkgname}_${pkgver}/test-build" \
#	-S "${pkgname}_${pkgver}" \
#	-DINSTALL_GTEST:BOOL='OFF' \
#	-Wno-dev
#  make -C "${pkgname}_${pkgver}/test-build/tests"
#}

package() {
  make -C "${pkgname}_${pkgver}/build" DESTDIR="${pkgdir}" install
}
