# Maintainer: Caleb Bassi <calebjbassi@gmail.com>

pkgname=gotop-bin
pkgver=2.0.2
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
sha256sums=("65f19c772e9618009f499d7a4ce967c805d2873adc640579d84fba075837fcc1")

package() {
  install -Dm755 "$srcdir/gotop" "$pkgdir/usr/bin/gotop"
}
