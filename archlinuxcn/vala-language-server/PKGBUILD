# Maintainer: benwaffle <vala@iofel.me>
# Maintainer: Prince781 <princetonferro@gmail.com>
pkgname=vala-language-server
_pkgver=0.48.3
pkgver=${_pkgver/-/+}
pkgrel=1
pkgdesc='Language Server for Vala'
arch=('x86_64')
url="https://github.com/prince781/vala-language-server"
license=('LGPL-2.1')
depends=('libgee' 'jsonrpc-glib' 'vala' 'meson')
makedepends=('scdoc')
source=("https://github.com/prince781/vala-language-server/archive/$_pkgver.tar.gz")
sha256sums=('1a752515efda561aec535d088a6f52888b13ad2d52f2d27770ddf6a519f0028b')
 
#prepare() {
#	cd "$pkgname"
#}
 
build() {
    cd "$pkgname-$_pkgver"
    arch-meson build
    ninja -C build
}
 
package() {
    cd "$pkgname-$_pkgver"
    DESTDIR="${pkgdir}" ninja -C build install
}

