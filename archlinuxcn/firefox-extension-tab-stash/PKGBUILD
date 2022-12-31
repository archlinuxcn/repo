# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=firefox-extension-tab-stash
_pkgname=tab-stash
pkgver=2.12.0.1
pkgrel=1
pkgdesc="Firefox extension to save and restore tabs as bookmarks"
arch=('any')
url="https://github.com/josh-berry/tab-stash"
license=('MPL2')
#groups=('firefox-addons')
depends=('firefox')
makedepends=('git' 'inkscape' 'nodejs' 'npm' 'p7zip' 'rsync' 'strip-nondeterminism')
source=("git+${url}.git#tag=v${pkgver}")
sha256sums=('SKIP')

build() {
    cd "${srcdir}"/"${_pkgname}"/
    make
}

package() {
    _extension_id="$(sed -n 's/.*"id": "\(.*\)".*/\1/p' ${_pkgname}/assets/manifest.json)"
    _extension_dest="${pkgdir}/usr/lib/firefox/browser/extensions/${_extension_id}"
    cd "${srcdir}"/"${_pkgname}"/
    cd dist/
    find . -type d -exec chmod 755 {} \;
    find . -type f -exec chmod 644 {} \;
    7z a -mx=9 ../"${_extension_id}.zip" .
    strip-nondeterminism -t zip ../"${_extension_id=}.zip"
    install -Dm 644 ../"${_extension_id}.zip" "${_extension_dest}.xpi"
}
