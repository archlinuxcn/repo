# Maintainer: PhotonX <photon89@googlemail.com>
# Contributor: Jan de Groot <jan@archlinux.org>

pkgname=orbit2
pkgver=2.14.19
_commit=144be2e9860286c83f009e7689250e0af977cc5e
pkgrel=7
pkgdesc="Thin/fast CORBA ORB"
arch=('i686' 'x86_64')
license=('LGPL' 'GPL')
depends=('libidl2')
makedepends=('gtk-doc' 'gnome-common')
options=('staticlibs' '!makeflags')
url="https://projects.gnome.org/ORBit2/"
source=("https://gitlab.gnome.org/GNOME/$pkgname/-/archive/$_commit/$pkgname-$_commit.tar.bz2")
sha256sums=('03e71752a6e0212af11d9c32aa40a22679157b4597b1f5e2c25399e0b78c7a55')

prepare() {
    cd "$pkgname-$_commit"
    msg2 'Running autogen. Please wait...'
    ./autogen.sh --prefix=/usr --disable-static --enable-gtk-doc
}

build() {
    cd "$pkgname-$_commit"
    make
}

package() {
    cd "$pkgname-$_commit"
    make DESTDIR="$pkgdir" install

    # add license
    install -Dm644 COPYING "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}