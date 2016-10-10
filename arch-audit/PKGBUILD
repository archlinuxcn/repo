# Maintainer: Andrea Scarpino <andrea@archlinux.org>

pkgname=arch-audit
pkgver=0.1.4
pkgrel=1
pkgdesc='An utility like pkg-audit based on Arch CVE Monitoring Team data'
url='https://github.com/ilpianista/arch-audit'
depends=('curl')
makedepends=('cargo')
arch=('i686' 'x86_64')
license=('MIT')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ilpianista/arch-audit/archive/$pkgver.tar.gz"
        'arch-audit.service' 'arch-audit.timer')
md5sums=('c01ec99bfced593ba083962e73824186'
         'a076cd0ee1a6a898720fa929875e6484'
         '4ea3d2ef7d9543d69469cdaa537a94b2')

build() {
  cd "$pkgname-$pkgver"
  cargo build --release
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 "target/release/${pkgname}" "$pkgdir/usr/bin/${pkgname}"

  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  install -Dm644 "${srcdir}/arch-audit.service" "${pkgdir}/usr/share/${pkgname}/arch-audit.service"
  install -Dm644 "${srcdir}/arch-audit.timer" "${pkgdir}/usr/share/${pkgname}/arch-audit.timer"
}
