# Maintainer: Andrea Scarpino <andrea@archlinux.org>

pkgname=arch-audit
pkgver=0.1.8
pkgrel=1
pkgdesc='An utility like pkg-audit based on Arch CVE Monitoring Team data'
url='https://github.com/ilpianista/arch-audit'
depends=('curl')
makedepends=('cargo' 'pkg-config')
arch=('i686' 'x86_64')
license=('MIT')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ilpianista/arch-audit/archive/$pkgver.tar.gz")
md5sums=('e71f9d6d2f557097db3c552808b4603e')

build() {
  cd "$pkgname-$pkgver"
  cargo build --release
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 "target/release/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"

  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  install -Dm644 doc/arch-audit.1 "${pkgdir}/usr/share/man/man1/arch-audit.1"

  install -Dm644 systemd/arch-audit.service \
    "${pkgdir}/usr/share/${pkgname}/arch-audit.service"
  install -Dm644 systemd/arch-audit.timer \
    "${pkgdir}/usr/share/${pkgname}/arch-audit.timer"

  install -Dm644 completions/zsh/_arch-audit \
    "${pkgdir}"/usr/share/zsh/site-functions/_arch-audit
}
