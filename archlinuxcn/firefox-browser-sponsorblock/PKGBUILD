# Maintainer: Kimiblock Moe

pkgname=(zen-browser-sponsorblock firefox-extension-sponsorblock librewolf-extension-sponsorblock)
pkgbase=firefox-browser-sponsorblock
pkgver=6.1.1
pkgrel=1
arch=('any')
url='https://github.com/ajayyy/SponsorBlock'
license=('GPL-3.0-only')
groups=('zen-browser-addons')
pkgdesc='Skip YouTube video sponsors'
makedepends=('nodejs' 'npm' 'unzip' 'zip' 'git' 'jq')
source=("source::git+https://github.com/ajayyy/SponsorBlock.git#tag=${pkgver}")
b2sums=('4e3c6d4606637832ff2a4c94bbf7953d321579491e203099cff39bc6b0d7ac495b74f980fb29d5c76d44fc95fdf56ad5b3e72c03c8b4a27083c49e627b4d5713')

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
