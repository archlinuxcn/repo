# Maintainer: Kimiblock Moe

pkgname=(zen-browser-sponsorblock firefox-extension-sponsorblock librewolf-extension-sponsorblock)
pkgbase=firefox-browser-sponsorblock
pkgver=6.1.2
pkgrel=1
arch=('any')
url='https://github.com/ajayyy/SponsorBlock'
license=('GPL-3.0-only')
groups=('zen-browser-addons')
pkgdesc='Skip YouTube video sponsors'
makedepends=('nodejs' 'npm' 'unzip' 'zip' 'git' 'jq')
source=("source::git+https://github.com/ajayyy/SponsorBlock.git#tag=${pkgver}")
b2sums=('16f24b5a3312fa31344e1fafcfa06b7e6a9f57845dd461759ddea662a1c593dc357ed22697ef78117655ecb42fcd06b9a4f081fdd290273c46cfb2afe36fdd85')

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
