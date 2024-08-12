pkgname=otf-noto-serif-cjk
pkgver=2.003
pkgrel=1
pkgdesc='Noto CJK fonts (Serif, Static OTC)'
provides=(noto-fonts-cjk)
arch=(any)
url='https://www.google.com/get/noto/help/cjk'
license=(OFL-1.1)
source=(https://github.com/notofonts/noto-cjk/releases/download/Serif${pkgver}/04_NotoSerifCJKOTC.zip)
sha256sums=('941985d9fd860492d15640b53edc9668d568877140c524ccd83deb3d9b7a2950')

package_otf-noto-serif-cjk() {
  install -Dm644 OTC/NotoSerifCJK-*.ttc -t "$pkgdir"/usr/share/fonts/noto-cjk
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
