pkgbase=ttf-noto-sans-cjk-vf
pkgname=(ttf-noto-{sans,sans-mono}-cjk-vf)
pkgver=2.004
pkgrel=1
pkgdesc='Noto CJK fonts'
provides=(noto-fonts-cjk)
arch=(any)
url='https://www.google.com/get/noto/help/cjk'
license=('OFL-1.1')
source=(https://github.com/notofonts/noto-cjk/releases/download/Sans${pkgver}/02_NotoSansCJK-TTF-VF.zip)
sha256sums=('b73a1f90988d6ccc3f60ce44ee3d1e82479a92710cd49cd950950c9adab50f1e')

package_ttf-noto-sans-cjk-vf() {
  pkgdesc+=' (Sans, Variable TTF/OTC)'
  install -Dm644 Variable/OTC/NotoSansCJK-VF.ttf.ttc -t "$pkgdir"/usr/share/fonts/noto-cjk
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}

package_ttf-noto-sans-mono-cjk-vf() {
  pkgdesc+=' (Sans Mono, Variable TTF/OTC)'
  install -Dm644 Variable/OTC/NotoSansMonoCJK-VF.ttf.ttc -t "$pkgdir"/usr/share/fonts/noto-cjk
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
