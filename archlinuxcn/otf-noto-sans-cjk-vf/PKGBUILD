pkgbase=otf-noto-sans-cjk-vf
pkgname=(otf-noto-{sans,sans-mono}-cjk-vf)
pkgver=2.004
pkgrel=2
pkgdesc='Noto CJK fonts'
provides=(noto-fonts-cjk)
arch=(any)
url='https://www.google.com/get/noto/help/cjk'
license=(custom:SIL)
source=(https://github.com/notofonts/noto-cjk/releases/download/Sans${pkgver}/01_NotoSansCJK-OTF-VF.zip
        70-noto-sans-cjk.conf
        70-noto-sans-mono-cjk.conf)
sha256sums=('d5e33aebad9f8a0c0896a4a29199ef85ca966134db164426c74e83e6f13c43cd'
            '17281bc6225331e3619cd20fdb647220110bea54bdea4a81462da0a75702d56b'
            '58be25f0a71a2bf42f20d4c5fb9e516904b77ef1924e9a0f7275d1595889f278')

package_otf-noto-sans-cjk-vf() {
  pkgdesc+=' (Sans, Variable OTC)'
  install -Dm644 Variable/OTC/NotoSansCJK-VF.otf.ttc -t "$pkgdir"/usr/share/fonts/noto-cjk
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
  install -Dm644 70-noto-sans-cjk.conf -t "$pkgdir"/usr/share/fontconfig/conf.avail
  install -d "$pkgdir"/usr/share/fontconfig/conf.default
  ln -rs "$pkgdir"/usr/share/fontconfig/conf.avail/* "$pkgdir"/usr/share/fontconfig/conf.default
}

package_otf-noto-sans-mono-cjk-vf() {
  pkgdesc+=' (Sans Mono, Variable OTC)'
  install -Dm644 Variable/OTC/NotoSansMonoCJK-VF.otf.ttc -t "$pkgdir"/usr/share/fonts/noto-cjk
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
  install -Dm644 70-noto-sans-mono-cjk.conf -t "$pkgdir"/usr/share/fontconfig/conf.avail
  install -d "$pkgdir"/usr/share/fontconfig/conf.default
  ln -rs "$pkgdir"/usr/share/fontconfig/conf.avail/* "$pkgdir"/usr/share/fontconfig/conf.default
}
