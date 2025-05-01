# Maintainer: Rocket Aaron <i at rocka dot me>

pkgname=ttf-noto-megamerge
pkgver=2025.05.01
pkgrel=1
pkgdesc='Single font covering all of the living and historical scripts in Noto'
provides=(noto-fonts)
arch=(any)
url='https://github.com/notofonts/notofonts.github.io/tree/main/megamerge'
source=("https://github.com/notofonts/notofonts.github.io/raw/noto-monthly-release-$pkgver/megamerge/Noto"{Sans,Serif}{Historical,Living}"-Regular.ttf"
        "46-noto-megamerge.conf"
        "66-noto-megamerge.conf")
sha256sums=('a2ffada0d447682ef27bfc1e92b995fcef5640fe6ad9f2d1640082abea3e8418'
            '2dd6229eca686200c403c03e6974d2b806cbbeb66cc86312edad22134c135127'
            'f37887a1551521e27da59bb66933ba62813911de667ebddf94d95a3b81671d82'
            'ff776e4e929942e4bcd03733962722a62e6d2b2d05b47bab395f103d167583df'
            '59a91de3c01546d91803420528cff9739cfb5da218b133291573fb2e3bb0bd2b'
            '9711324b0dbbc11b81f7e87c72d1a574414663a6cafc3ffc511274c7a2ab51d7')

package() {
  install -Dm644 Noto*.ttf -t "$pkgdir"/usr/share/fonts/noto
  install -Dm644 "$srcdir"/*-noto-*.conf -t "$pkgdir"/usr/share/fontconfig/conf.avail/
  install -d "$pkgdir"/usr/share/fontconfig/conf.default
  ln -rs "$pkgdir"/usr/share/fontconfig/conf.avail/* "$pkgdir"/usr/share/fontconfig/conf.default
}
