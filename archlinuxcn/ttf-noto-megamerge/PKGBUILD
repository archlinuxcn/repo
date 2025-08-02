# Maintainer: Rocket Aaron <i at rocka dot me>

pkgname=ttf-noto-megamerge
pkgver=2025.08.01
pkgrel=1
pkgdesc='Single font covering all of the living and historical scripts in Noto'
provides=(noto-fonts)
arch=(any)
url='https://github.com/notofonts/notofonts.github.io/tree/main/megamerge'
source=("https://github.com/notofonts/notofonts.github.io/raw/noto-monthly-release-$pkgver/megamerge/Noto"{Sans,Serif}{Historical,Living}"-Regular.ttf"
        "46-noto-megamerge.conf"
        "66-noto-megamerge.conf")
sha256sums=('cd5326035376c845ba5fac952205b648f9785878d0053147dd0def9a6ab6cd98'
            'ff2bc2ad56f7f2fde161eaa4bddbe72c9fcace7f38928f0b60c6fbdcac66b075'
            '1c508c92786a82939954e9be086c3af6b1d21fdc105ec32f752b7449c380a9d8'
            '809b0184303cb0acdbe81e7075997bd4374cd0734386a53ae098d43614eefbf3'
            '59a91de3c01546d91803420528cff9739cfb5da218b133291573fb2e3bb0bd2b'
            '9711324b0dbbc11b81f7e87c72d1a574414663a6cafc3ffc511274c7a2ab51d7')

package() {
  install -Dm644 Noto*.ttf -t "$pkgdir"/usr/share/fonts/noto
  install -Dm644 "$srcdir"/*-noto-*.conf -t "$pkgdir"/usr/share/fontconfig/conf.avail/
  install -d "$pkgdir"/usr/share/fontconfig/conf.default
  ln -rs "$pkgdir"/usr/share/fontconfig/conf.avail/* "$pkgdir"/usr/share/fontconfig/conf.default
}
