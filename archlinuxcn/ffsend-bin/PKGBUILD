# Maintainer: Tim Visee <tim@visee.me>
# Contributor: Ariel AxionL <i at axionl dot me>

pkgname=ffsend-bin
pkgver=0.2.39
pkgrel=1
pkgdesc="Easily and securely share files from the command line. A Firefox Send client."
url="https://gitlab.com/timvisee/ffsend"
license=('GPL3')
provides=('ffsend')
conflicts=('ffsend-git' 'ffsend')
source=("ffsend::https://github.com/timvisee/ffsend/releases/download/v$pkgver/ffsend-v$pkgver-linux-x64-static")
sha256sums=('920887f505925963a40388e1a8553eb5cca7ee59c03dc285eb541ab0f02c7da0')
arch=('x86_64')
depends=('ca-certificates')
optdepends=('xclip: clipboard support')

package() {
    install -Dm755 "${srcdir}/ffsend" "${pkgdir}/usr/bin/ffsend"
}
