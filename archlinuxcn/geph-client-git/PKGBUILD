# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=geph-client-git
_pkgname=geph-client
pkgver=r144.f29acd3
pkgrel=2
pkgdesc='A command-line Geph client'
arch=('x86_64')
url="https://github.com/geph-official/geph2"
license=('GPL3')
groups=('geph2-git')
depends=('glibc')
makedepends=('go-pie' 'git')
provides=("$_pkgname")
conflicts=("$_pkgname")
source=("git+$url.git"
        "geph-client.service")
sha512sums=('SKIP'
            'd23b669396f8bd6c99d78a478de233b211f4202812348dc2c78050ad2646870027a766a0bca51ead70b06947fb6dc49d646e462682e0d3fb685b3a00840d104a')

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

    install -d "$pkgdir/etc/geph2"
    "$pkgdir/usr/bin/$_pkgname" -dumpflags > "$pkgdir/etc/geph2/$_pkgname.ini"

    install -Dm 644 "$srcdir/$_pkgname.service" "$pkgdir/usr/lib/systemd/system/$_pkgname.service"
    sed 's/geph-client.ini/%i.ini/' "$srcdir/$_pkgname.service" -i
    install -Dm 644 "$srcdir/$_pkgname.service" "$pkgdir/usr/lib/systemd/system/$_pkgname@.service"
}
