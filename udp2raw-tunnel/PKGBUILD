# Maintainer: Peter Cai <peter at typeblog dot net>
pkgname=udp2raw-tunnel
pkgver=20170826.0
pkgrel=1
pkgdesc='An Encrpyted,Anti-Replay,Multiplexed Udp Tunnel,tunnels udp traffic through fake-tcp or icmp by using raw socket'
arch=('x86_64' 'i686')
depends=('gcc-libs')
makedepends=('gcc' 'make')
install=udp2raw-tunnel.install
url='https://github.com/wangyu-/udp2raw-tunnel'
license=('MIT')
source=(
  "$pkgname-$pkgver.tar.gz::https://github.com/wangyu-/udp2raw-tunnel/archive/$pkgver.tar.gz"
  "udp2raw_script.sh"
  "udp2raw@.service"
)

build() {
  cd "$srcdir/$pkgname-$pkgver"
  make fast
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  mkdir -p "$pkgdir/usr/bin/"
  install -m755 udp2raw "$pkgdir/usr/bin/"
  mkdir -p "$pkgdir/etc/udp2raw"
  install -m644 config.example "$pkgdir/etc/udp2raw/example.conf"
  mkdir -p "$pkgdir/usr/lib/udp2raw"
  install -m755 "$srcdir/udp2raw_script.sh" "$pkgdir/usr/lib/udp2raw/"
  mkdir -p "$pkgdir/usr/lib/systemd/system"
  install -m644 "$srcdir/udp2raw@.service" "$pkgdir/usr/lib/systemd/system/"
}
md5sums=('5391108eb40cdef8e2f98b4f4faebc19'
         'ef27e09d068abf7222158f66168ff353'
         '1c73eb54f737b77dae29e8f6c7f137f9')
