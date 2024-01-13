# Maintainer: Dct Mei <dctxmei@yandex.com>
# Maintainer: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Maintainer: Eli schwartz <eschwartz@archlinux.org>

pkgname=firefox-esr-noscript
pkgver=11.4.29
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
sha256sums=('05b98840b05ef2acbac333543e4b7c3d40fee2ce5fb4e29260b05e2ff6fe24cd')
b2sums=('409947675258d95961b6c4368cc449fd81c6281e4b2bb73e916fd1cc53a26f2681085f500510dffa75774e921da2d8cc9e255e13071933a8369fed427982daee')

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
