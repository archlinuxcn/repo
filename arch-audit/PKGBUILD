# Maintainer: Andrea Scarpino <andrea@archlinux.org>

pkgname=arch-audit
pkgver=0.1.5
pkgrel=2
pkgdesc='An utility like pkg-audit based on Arch CVE Monitoring Team data'
url='https://github.com/ilpianista/arch-audit'
depends=('curl')
makedepends=('cargo')
arch=('i686' 'x86_64')
license=('MIT')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ilpianista/arch-audit/archive/$pkgver.tar.gz")
md5sums=('6d131cf142f685c081326924c3380b64')

build() {
  cd "$pkgname-$pkgver"
  cargo build --release
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 "target/release/${pkgname}" "$pkgdir/usr/bin/${pkgname}"

  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  install -Dm644 systemd/arch-audit.service "${pkgdir}/usr/share/${pkgname}/arch-audit.service"
  install -Dm644 systemd/arch-audit.timer "${pkgdir}/usr/share/${pkgname}/arch-audit.timer"
}
