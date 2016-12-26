# Maintainer: Andrea Scarpino <andrea@archlinux.org>

pkgname=arch-audit
pkgver=0.1.7
pkgrel=1
pkgdesc='An utility like pkg-audit based on Arch CVE Monitoring Team data'
url='https://github.com/ilpianista/arch-audit'
depends=('curl')
makedepends=('cargo' 'pkg-config')
arch=('i686' 'x86_64')
license=('MIT')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ilpianista/arch-audit/archive/$pkgver.tar.gz")
md5sums=('b465718446ed2d3250535f8ebeb52ca2')

build() {
  cd "$pkgname-$pkgver"
  cargo build --release
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 "target/release/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"

  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  install -Dm644 doc/arch-audit.1 "${pkgdir}/usr/share/man/man1/arch-audit.1"

  install -Dm644 systemd/arch-audit.service "${pkgdir}/usr/share/${pkgname}/arch-audit.service"
  install -Dm644 systemd/arch-audit.timer "${pkgdir}/usr/share/${pkgname}/arch-audit.timer"
}
