# Maintainer: Kimiblock Moe

pkgname=(zen-browser-violentmonkey firefox-extension-violentmonkey)
pkgbase=firefox-browser-violentmonkey
pkgver=2.48.0
pkgrel=1
arch=('any')
url='https://github.com/Violentmonkey/Violentmonkey'
license=('MIT')
groups=('zen-browser-addons')
pkgdesc='Web Extension for saving a faithful copy of a complete web page in a single HTML file'
makedepends=('nodejs' 'npm' 'unzip' 'zip' 'git' 'jq' 'pnpm')
source=("source::git+https://github.com/Violentmonkey/Violentmonkey.git#tag=v${pkgver}")
b2sums=('b62ff08396c71d7416a3fd7ba2a137804f822b35bca6c046e6acd0c7849a4db71024e6c994fc69e1caf76edbeda249b490ba3fd9799d8452f7f00cdb677c265a')

prepare() {
	cd "${srcdir}/source"
	pnpm install --frozen-lockfile
}

build() {
	cd "${srcdir}/source"
	pnpm build
	cd dist
	zip ../addon.zip -r .
}

package_firefox-extension-violentmonkey() {
    cd "${srcdir}/source"
    install -Dm644 "${srcdir}/source/addon.zip" "${pkgdir}/usr/lib/firefox/browser/extensions/{aecec67f-0d10-4fa7-b7c7-609a2db280cf}.xpi"
}

package_zen-browser-violentmonkey() {
    cd "${srcdir}/source"
    install -Dm644 "${srcdir}/source/addon.zip" "${pkgdir}/usr/lib/zen-browser/browser/extensions/{aecec67f-0d10-4fa7-b7c7-609a2db280cf}.xpi"
}

