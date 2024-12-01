# Maintainer: Rocket Aaron <i at rocka dot me>

pkgname=ttf-noto-megamerge
pkgver=2024.12.01
pkgrel=1
pkgdesc='Single font covering all of the living and historical scripts in Noto'
provides=(noto-fonts)
arch=(any)
url='https://github.com/notofonts/notofonts.github.io/tree/main/megamerge'
source=("https://github.com/notofonts/notofonts.github.io/raw/noto-monthly-release-$pkgver/megamerge/Noto"{Sans,Serif}{Historical,Living}"-Regular.ttf"
        "46-noto-megamerge.conf"
        "66-noto-megamerge.conf")
sha256sums=('48e974fc47496b06e40e462fe20c67518012cb71a4dd74c722d57c1f02b90d9e'
            '3d51c6a203d612533ef75456055feb44fdb342d2fda3301eb38e1c4cb5ac9d30'
            'f75949e29c66df1d4e03e1458fc58e66f4b1416268d582f2427d3406112a112e'
            'e028385fc23a6a546dd4f55cbaff712097b5d8198330443d076398f8f91792b5'
            '59a91de3c01546d91803420528cff9739cfb5da218b133291573fb2e3bb0bd2b'
            '9711324b0dbbc11b81f7e87c72d1a574414663a6cafc3ffc511274c7a2ab51d7')

package() {
  install -Dm644 Noto*.ttf -t "$pkgdir"/usr/share/fonts/noto
  install -Dm644 "$srcdir"/*-noto-*.conf -t "$pkgdir"/usr/share/fontconfig/conf.avail/
  install -d "$pkgdir"/usr/share/fontconfig/conf.default
  ln -rs "$pkgdir"/usr/share/fontconfig/conf.avail/* "$pkgdir"/usr/share/fontconfig/conf.default
}
