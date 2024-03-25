pkgbase=ttf-noto-vf
pkgname=(ttf-noto-{sans,serif,sans-mono}-vf)
pkgver=24.3.1
pkgrel=1
provides=(ttf-font noto-fonts noto-fonts-extra)
arch=(any)
url='https://fonts.google.com/noto'
license=('OFL-1.1')
source=(https://github.com/notofonts/notofonts.github.io/archive/refs/tags/noto-monthly-release-$pkgver.tar.gz
        46-noto-sans.conf 46-noto-serif.conf 46-noto-sans-mono.conf
        66-noto-sans.conf 66-noto-serif.conf 66-noto-sans-mono.conf)
sha256sums=('abcef824e61aa99626b6ad331c1cba875f28b3d87cc9ff8c87d46d55fe344369'
            '83a8faf6a47954075f97a2d555048e2a6689c38603b2ca00150157bf645f4593'
            'c94368b24506770767d003e5bcba589a8e402e489c240ee52453bf3ac7e9b5fa'
            'f5c09b37280d7569b6c99a78511639be4ae25b8c5406464422fe0421fe13a884'
            '52684bebf6447be22618d2a04ff37623ec92f9d8ccf6b6f972e5bcbcfee90d69'
            '4459944b63dc083107280f5d7375c69746bf80a09416a4a4909a100e58e5a33a'
            '4526289f59654e2a81dc734669a1ae4e416f9a56d0896ec3741c6bf065baf8a8')

package_ttf-noto-sans-vf() {
  pkgdesc='	Google Noto Sans font (Variable weight and width, TTF)'

  cd notofonts.github.io-noto-monthly-release-$pkgver
  install -Dm644 fonts/NotoSans/full/variable-ttf/*.ttf -t "$pkgdir"/usr/share/fonts/noto
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname

  install -Dm644 "$srcdir"/*-noto-sans.conf -t "$pkgdir"/usr/share/fontconfig/conf.avail/
  install -d "$pkgdir"/usr/share/fontconfig/conf.default
  ln -rs "$pkgdir"/usr/share/fontconfig/conf.avail/* "$pkgdir"/usr/share/fontconfig/conf.default
}

package_ttf-noto-serif-vf() {
  pkgdesc='	Google Noto Serif font (Variable weight and width, TTF)'

  cd notofonts.github.io-noto-monthly-release-$pkgver
  install -Dm644 fonts/NotoSerif/unhinted/variable-ttf/*.ttf -t "$pkgdir"/usr/share/fonts/noto
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname

  install -Dm644 "$srcdir"/*-noto-serif.conf -t "$pkgdir"/usr/share/fontconfig/conf.avail/
  install -d "$pkgdir"/usr/share/fontconfig/conf.default
  ln -rs "$pkgdir"/usr/share/fontconfig/conf.avail/* "$pkgdir"/usr/share/fontconfig/conf.default
}

package_ttf-noto-sans-mono-vf() {
  pkgdesc='	Google Noto Sans Mono font (Variable weight and width, TTF)'

  cd notofonts.github.io-noto-monthly-release-$pkgver
  install -Dm644 fonts/NotoSansMono/unhinted/variable-ttf/*.ttf -t "$pkgdir"/usr/share/fonts/noto
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname

  install -Dm644 "$srcdir"/*-noto-sans-mono.conf -t "$pkgdir"/usr/share/fontconfig/conf.avail/
  install -d "$pkgdir"/usr/share/fontconfig/conf.default
  ln -rs "$pkgdir"/usr/share/fontconfig/conf.avail/* "$pkgdir"/usr/share/fontconfig/conf.default
}
