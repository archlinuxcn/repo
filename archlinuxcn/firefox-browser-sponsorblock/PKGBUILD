# Maintainer: Kimiblock Moe

pkgname=(zen-browser-sponsorblock firefox-extension-sponsorblock librewolf-extension-sponsorblock)
pkgbase=firefox-browser-sponsorblock
pkgver=5.13.4
pkgrel=1
arch=('any')
url='https://github.com/ajayyy/SponsorBlock'
license=('GPL-3.0-only')
groups=('zen-browser-addons')
pkgdesc='Skip YouTube video sponsors'
makedepends=('nodejs' 'npm' 'unzip' 'zip' 'git' 'jq')
source=("source::git+https://github.com/ajayyy/SponsorBlock.git#tag=${pkgver}")
b2sums=('73722351b69eca236210fc5adc44bb1c4159c557fe3081eaf2f76a88d30d1a150243ac21eefebbbf6f8d334e93a3ac081dbae9add69e1a8d9c4210248fa3a936')

function prepare() {
	cd "${srcdir}/source"
	git submodule update --init --recursive
	ln -srf config.json.example config.json
	npm ci
}

build() {
    cd "${srcdir}/source"
    npm run build:firefox
    cd dist
    zip ../addon.zip -r .
}

package_firefox-extension-sponsorblock() {
    cd "${srcdir}/source"
    install -Dm644 "${srcdir}/source/addon.zip" "${pkgdir}/usr/lib/firefox/browser/extensions/sponsorBlocker@ajay.app.xpi"
}

package_zen-browser-sponsorblock() {
    cd "${srcdir}/source"
    install -Dm644 "${srcdir}/source/addon.zip" "${pkgdir}/usr/lib/zen-browser/browser/extensions/sponsorBlocker@ajay.app.xpi"
}

package_librewolf-extension-sponsorblock() {
    cd "${srcdir}/source"
    install -Dm644 "${srcdir}/source/addon.zip" "${pkgdir}/usr/lib/librewolf/browser/extensions/sponsorBlocker@ajay.app.xpi"
}
