# Maintainer: Rocket Aaron <i at rocka dot me>

pkgname=ttf-noto-megamerge
pkgver=2025.03.01
pkgrel=1
pkgdesc='Single font covering all of the living and historical scripts in Noto'
provides=(noto-fonts)
arch=(any)
url='https://github.com/notofonts/notofonts.github.io/tree/main/megamerge'
source=("https://github.com/notofonts/notofonts.github.io/raw/noto-monthly-release-$pkgver/megamerge/Noto"{Sans,Serif}{Historical,Living}"-Regular.ttf"
        "46-noto-megamerge.conf"
        "66-noto-megamerge.conf")
sha256sums=('c798a09302f4fb9869f2b8065f8c596f0212dea587fef88f2941d68af0396e72'
            'cd9724caac410c294efa80f91fdebde0afb084cd9576a69449e6833176e0074e'
            '8d778c6f1b3d74fbd74f50a3bdeb6d9aa664d0f5b942c7500bb458aa2f68d23a'
            '6294b5c881328a94d89a0845005d6b0bec1065d82b5017098486ac2bcf19cc75'
            '59a91de3c01546d91803420528cff9739cfb5da218b133291573fb2e3bb0bd2b'
            '9711324b0dbbc11b81f7e87c72d1a574414663a6cafc3ffc511274c7a2ab51d7')

package() {
  install -Dm644 Noto*.ttf -t "$pkgdir"/usr/share/fonts/noto
  install -Dm644 "$srcdir"/*-noto-*.conf -t "$pkgdir"/usr/share/fontconfig/conf.avail/
  install -d "$pkgdir"/usr/share/fontconfig/conf.default
  ln -rs "$pkgdir"/usr/share/fontconfig/conf.avail/* "$pkgdir"/usr/share/fontconfig/conf.default
}
