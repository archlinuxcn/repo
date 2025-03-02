pkgname=ttf-noto-serif-cjk-vf
pkgver=2.003
pkgrel=1
pkgdesc='Noto CJK fonts (Serif, Variable TTF/OTC)'
provides=(noto-fonts-cjk)
arch=(any)
url='https://www.google.com/get/noto/help/cjk'
license=('OFL-1.1')
source=(https://github.com/notofonts/noto-cjk/releases/download/Serif${pkgver}/03_NotoSerifCJK-TTF-VF.zip)
sha256sums=('ad58364bca7c70a15b40e941df0ce0da85b1e4a882ab176f14e661cf1a0af05e')

package() {
  install -Dm644 Variable/OTC/NotoSerifCJK-VF.ttf.ttc -t "$pkgdir"/usr/share/fonts/noto-cjk
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
