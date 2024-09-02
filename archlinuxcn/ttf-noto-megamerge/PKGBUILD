# Maintainer: Rocket Aaron <i at rocka dot me>

pkgname=ttf-noto-megamerge
pkgver=24.9.1
pkgrel=1
pkgdesc='Single font covering all of the living and historical scripts in Noto'
provides=(noto-fonts)
arch=(any)
url='https://github.com/notofonts/notofonts.github.io/tree/main/megamerge'
source=("https://github.com/notofonts/notofonts.github.io/raw/noto-monthly-release-$pkgver/megamerge/Noto"{Sans,Serif}{Historical,Living}"-Regular.ttf"
        "46-noto-megamerge.conf"
        "66-noto-megamerge.conf")
sha256sums=('7265b1534f9f31215a787c4e46b8e7d23a0e836e34f61f5a911d787cd2207ce5'
            'fe4f90aa25b246d6b5102189ac8764faaf6858ebbcbdb3bb8a36f65324ef9cdc'
            'b755ec1fa92ba91b832257456688de80bae40f24811b212aa7a34b421f41719a'
            '24294d72ebe83f3fb4ed514b1271ef38ddfadece92f4d7bc328a106db5cb12f6'
            '59a91de3c01546d91803420528cff9739cfb5da218b133291573fb2e3bb0bd2b'
            '9711324b0dbbc11b81f7e87c72d1a574414663a6cafc3ffc511274c7a2ab51d7')

package() {
  install -Dm644 Noto*.ttf -t "$pkgdir"/usr/share/fonts/noto
  install -Dm644 "$srcdir"/*-noto-*.conf -t "$pkgdir"/usr/share/fontconfig/conf.avail/
  install -d "$pkgdir"/usr/share/fontconfig/conf.default
  ln -rs "$pkgdir"/usr/share/fontconfig/conf.avail/* "$pkgdir"/usr/share/fontconfig/conf.default
}
