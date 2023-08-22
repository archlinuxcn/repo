# Maintainer: Dct Mei <dctxmei@yandex.com>
# Maintainer: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Maintainer: Eli schwartz <eschwartz@archlinux.org>

pkgname=firefox-esr-noscript
pkgver=11.4.26
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
sha256sums=('283db0eaebbd2888c1a852f5acabaa8e0225ff1eb1a97a25bceaedfd14d9f44c')
b2sums=('cfc57113579e8c86126966747710c3f46a82215367e259f73f2e9529e3a002ab157dc8f6faed614b34b7db9f483fdf52d87ca6e3fc0b1404bf1bdc1c89d94ca5')

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
