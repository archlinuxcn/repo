# $Id$
# Maintainer: PhotonX <photon89@googlemail.com>
# Contributor: Jan de Groot <jan@archlinux.org>

pkgname=orbit2
pkgver=2.14.19
pkgrel=4
pkgdesc="Thin/fast CORBA ORB"
arch=('i686' 'x86_64')
license=('LGPL' 'GPL')
depends=('libidl2')
makedepends=('gtk-doc')
options=('!makeflags' 'staticlibs')
url="https://projects.gnome.org/ORBit2/"
source=(https://download.gnome.org/sources/ORBit2/2.14/ORBit2-${pkgver}.tar.bz2
        git-fixes.patch
        libname-server-2.a)
noextract=(libname-server-2.a)
sha256sums=('55c900a905482992730f575f3eef34d50bda717c197c97c08fa5a6eafd857550'
            '7f145ed715d5a1d7f6ccf1e9bcce6a6a584a6b125845a84a3d69bfe30b0d6e04'
            '41a7f7b169676a30a3b1a312dc9cd12ead58f1ef9674dc10deb2941cc86a5fb5')

prepare() {
  cp libname-server-2.a ORBit2-$pkgver/src/services/name/
  cd ORBit2-$pkgver
  patch -Np1 -i ../git-fixes.patch
}

build() {
  cd ORBit2-$pkgver
  autoreconf -fi
  ./configure --prefix=/usr --disable-static
  make
}

package() {
  cd ORBit2-$pkgver
  make DESTDIR="${pkgdir}" install
}
