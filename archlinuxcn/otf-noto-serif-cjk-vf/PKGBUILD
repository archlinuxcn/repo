pkgname=otf-noto-serif-cjk-vf
pkgver=2.002
pkgrel=2
pkgdesc='Noto CJK fonts (Serif, Variable OTC)'
provides=(noto-fonts-cjk)
arch=(any)
url='https://www.google.com/get/noto/help/cjk'
license=(custom:SIL)
source=(https://github.com/notofonts/noto-cjk/releases/download/Serif${pkgver}/02_NotoSerifCJK-OTF-VF.zip
        70-noto-serif-cjk.conf)
sha256sums=('279c27b6314d103c068f90fa4451ba64dcfb0a0d2d4549f02ff82a57f399f200'
            'ad900dbcbf6f6427d86adfb78d5d395d97a2bb5182468ae6a09bbb13a74c0765')

package() {
  install -Dm644 Variable/OTC/NotoSerifCJK-VF.otf.ttc -t "$pkgdir"/usr/share/fonts/noto-cjk
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
  install -Dm644 70-noto-serif-cjk.conf -t "$pkgdir"/usr/share/fontconfig/conf.avail
  install -d "$pkgdir"/usr/share/fontconfig/conf.default
  ln -rs "$pkgdir"/usr/share/fontconfig/conf.avail/* "$pkgdir"/usr/share/fontconfig/conf.default
}
