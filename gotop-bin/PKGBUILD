# Maintainer: Caleb Bassi <calebjbassi@gmail.com>

pkgname=gotop-bin
pkgver=1.7.0
pkgrel=1
pkgdesc="A terminal based graphical activity monitor inspired by gtop and vtop"
arch=("x86_64" "i686")
url="https://github.com/cjbassi/gotop"
license=("AGPL3")
provides=("gotop")

case "$CARCH" in
    x86_64)
        _arch=amd64
        ;;
    i686)
        _arch=386
        ;;
esac

source=("https://github.com/cjbassi/gotop/releases/download/$pkgver/gotop_${pkgver}_linux_$_arch.tgz")
md5sums=("SKIP")

package() {
    mkdir -p "$pkgdir/usr/bin"
    mv $srcdir/gotop $pkgdir/usr/bin
}
