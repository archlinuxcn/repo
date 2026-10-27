# Maintainer: Kimiblock Moe

pkgname=(zen-browser-violentmonkey firefox-extension-violentmonkey)
pkgbase=firefox-browser-violentmonkey
pkgver=2.50.0
pkgrel=1
arch=('any')
url='https://github.com/Violentmonkey/Violentmonkey'
license=('MIT')
groups=('zen-browser-addons')
pkgdesc='Web Extension for saving a faithful copy of a complete web page in a single HTML file'
makedepends=('nodejs' 'npm' 'unzip' 'zip' 'git' 'jq' 'pnpm')
source=("source::git+https://github.com/Violentmonkey/Violentmonkey.git#tag=v${pkgver}")
b2sums=('3edbbbf4329f9d959e27253638f7efb8a24087d0055b40370edb7d5833a962e302a3701e824ff71b54636a83a8ae1ffa447ad0ed6e8c470ff3b5e59de686e5fc')

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

