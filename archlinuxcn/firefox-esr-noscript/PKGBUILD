# Maintainer: Dct Mei <dctxmei@yandex.com>
# Maintainer: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Maintainer: Eli schwartz <eschwartz@archlinux.org>

pkgname=firefox-esr-noscript
pkgver=11.4.1
pkgrel=1
#_file=3910951
pkgdesc="Extension for firefox which disables javascript"
arch=('any')
url="https://noscript.net/"
license=('GPL2')
makedepends=('unzip' 'jq')
#groups=('firefox-addons')
#source=("noscript-${pkgver}.xpi::https://addons.mozilla.org/firefox/downloads/file/${_file}/")
source=("noscript-${pkgver}.xpi::https://secure.informaction.com/download/releases/noscript-$pkgver.xpi")
noextract=("noscript-${pkgver}.xpi")
sha256sums=('68bdf014e3c102b3b3fbb86b7c07a9ecb7ee8e6a1da253cd6aea31d4c86a04d7')
b2sums=('74b18f2b864496571e857553361b409fca273635f8fb4a23db161f018dd79ccdc04c6a8d698477f537bb37a62c24e568e1d2a67652b696698d94f0b4345b3582')

check() {
  unzip noscript-$pkgver.xpi manifest.json
  jq '.version' manifest.json | grep -E '^"'$pkgver'"$'
}

package() {
  depends=('firefox-esr')
  _extension_id="{73a6fe31-595d-460b-a920-fcc0f8843232}"
  _extension_dest="${pkgdir}/usr/lib/firefox-esr/browser/extensions/${_extension_id}"
  install -Dm644 noscript-${pkgver}.xpi "${_extension_dest}.xpi"
}
