pkgbase=otf-noto-sans-cjk-vf
pkgname=(otf-noto-{sans,sans-mono}-cjk-vf)
pkgver=2.004
pkgrel=3
pkgdesc='Noto CJK fonts'
provides=(noto-fonts-cjk)
arch=(any)
url='https://www.google.com/get/noto/help/cjk'
license=('OFL-1.1')
source=(https://github.com/notofonts/noto-cjk/releases/download/Sans${pkgver}/01_NotoSansCJK-OTF-VF.zip)
sha256sums=('d5e33aebad9f8a0c0896a4a29199ef85ca966134db164426c74e83e6f13c43cd')

package_otf-noto-sans-cjk-vf() {
  pkgdesc+=' (Sans, Variable OTF)'
  install -Dm644 Variable/OTC/NotoSansCJK-VF.otf.ttc -t "$pkgdir"/usr/share/fonts/noto-cjk
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}

package_otf-noto-sans-mono-cjk-vf() {
  pkgdesc+=' (Sans Mono, Variable OTF)'
  install -Dm644 Variable/OTC/NotoSansMonoCJK-VF.otf.ttc -t "$pkgdir"/usr/share/fonts/noto-cjk
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
