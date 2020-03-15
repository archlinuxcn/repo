# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=geph-client-git
_pkgname=geph-client
pkgver=r144.f29acd3
pkgrel=1
pkgdesc='A command-line Geph client'
arch=('x86_64')
url="https://github.com/geph-official/geph2"
license=('GPL3')
groups=('geph2-git')
depends=('glibc')
makedepends=('go-pie' 'git')
provides=("$_pkgname")
conflicts=("$_pkgname")
source=("git+$url.git")
sha512sums=('SKIP')

pkgver() {
    cd geph2
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    cd "geph2/cmd/$_pkgname"
    go build
}

package() {
    cd "geph2/cmd/$_pkgname"
    install -Dm 755 $_pkgname "$pkgdir/usr/bin/$_pkgname"
}
