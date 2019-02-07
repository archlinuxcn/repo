# Maintainer: Caleb Bassi <calebjbassi@gmail.com>

pkgname=gotop-bin
pkgver=2.0.1
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
sha256sums=("e1c46bd14fc37956b85c0dc1dd969731061b4c62e214b1e4466ad81b5b6249bc")

package() {
  install -Dm755 "$srcdir/gotop" "$pkgdir/usr/bin/gotop"
}
