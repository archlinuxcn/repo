# Maintainer: Kimiblock Moe

pkgname=(zen-browser-sponsorblock firefox-extension-sponsorblock librewolf-extension-sponsorblock)
pkgbase=firefox-browser-sponsorblock
pkgver=6.1.4
pkgrel=1
arch=('any')
url='https://github.com/ajayyy/SponsorBlock'
license=('GPL-3.0-only')
groups=('zen-browser-addons')
pkgdesc='Skip YouTube video sponsors'
makedepends=('nodejs' 'npm' 'unzip' 'zip' 'git' 'jq')
source=("source::git+https://github.com/ajayyy/SponsorBlock.git#tag=${pkgver}")
b2sums=('53059c213058bdc21722ba74864edfed0ba68c1ab6600876a9305cfec9e3e92f777fca089adbec0d2f2129c204d9dd96c8c8f71dc4ccc81654812af27d3c94e1')

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
