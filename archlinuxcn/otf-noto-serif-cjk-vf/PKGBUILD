pkgname=otf-noto-serif-cjk-vf
pkgver=2.003
pkgrel=1
pkgdesc='Noto CJK fonts (Serif, Variable OTC)'
provides=(noto-fonts-cjk)
arch=(any)
url='https://www.google.com/get/noto/help/cjk'
license=('OFL-1.1')
source=(https://github.com/notofonts/noto-cjk/releases/download/Serif${pkgver}/02_NotoSerifCJK-OTF-VF.zip)
sha256sums=('279c27b6314d103c068f90fa4451ba64dcfb0a0d2d4549f02ff82a57f399f200')

package() {
  install -Dm644 Variable/OTC/NotoSerifCJK-VF.otf.ttc -t "$pkgdir"/usr/share/fonts/noto-cjk
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
