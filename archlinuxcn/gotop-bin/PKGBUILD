# Maintainer: Caleb Bassi <calebjbassi@gmail.com>

pkgname=gotop-bin
pkgver=3.0.0
pkgrel=1
pkgdesc="A terminal based graphical activity monitor inspired by gtop and vtop"
arch=("x86_64" "i686")
url="https://github.com/cjbassi/gotop"
license=("AGPL3")
provides=("gotop")
conflicts=("gotop")

case "$CARCH" in
    x86_64)
        _arch=amd64
        ;;
    i686)
        _arch=386
        ;;
esac

source=("https://github.com/cjbassi/gotop/releases/download/$pkgver/gotop_${pkgver}_linux_$_arch.tgz")
sha256sums=("7fd4c34398a63dcf3189db91ba2dbe9c1d8b96a0a04814ef56b8e764b145e608")

package() {
  install -Dm755 "$srcdir/gotop" "$pkgdir/usr/bin/gotop"
}
