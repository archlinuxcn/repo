pkgname=otf-noto-sans-cjk
pkgver=2.004
pkgrel=3
pkgdesc='Noto CJK fonts (Sans, Static OTC)'
provides=(noto-fonts-cjk)
arch=(any)
url='https://www.google.com/get/noto/help/cjk'
license=(custom:SIL)
source=(https://github.com/notofonts/noto-cjk/releases/download/Sans${pkgver}/03_NotoSansCJK-OTC.zip)
sha256sums=('528f4e1b25ff3badb0321b38d015d954c4c0de926c7830ef50e4a1948f6a3eed')

package_otf-noto-sans-cjk() {
  install -Dm644 NotoSansCJK-*.ttc -t "$pkgdir"/usr/share/fonts/noto-cjk
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
