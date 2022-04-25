# Maintainer: benwaffle <vala@iofel.me>
# Maintainer: Prince781 <princetonferro@gmail.com>
pkgname=vala-language-server
_pkgver=0.48.4
pkgver=${_pkgver/-/+}
pkgrel=1
pkgdesc='Language Server for Vala'
arch=('x86_64')
url="https://github.com/prince781/vala-language-server"
license=('LGPL-2.1')
depends=('libgee' 'jsonrpc-glib' 'vala' 'meson')
makedepends=('scdoc')
source=("https://github.com/prince781/vala-language-server/archive/$_pkgver.tar.gz")
sha256sums=('9de5d476a3d3b5d4f22f50af6c2417abd44066ab4231cbc00628e9fdab735100')
 
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

