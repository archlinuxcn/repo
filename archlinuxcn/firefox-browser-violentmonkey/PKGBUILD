# Maintainer: Kimiblock Moe

pkgname=(zen-browser-violentmonkey firefox-extension-violentmonkey)
pkgbase=firefox-browser-violentmonkey
pkgver=2.34.0
pkgrel=1
arch=('any')
url='https://github.com/Violentmonkey/Violentmonkey'
license=('MIT')
groups=('zen-browser-addons')
pkgdesc='Web Extension for saving a faithful copy of a complete web page in a single HTML file'
makedepends=('nodejs' 'npm' 'unzip' 'zip' 'git' 'jq' 'yarn')
source=("source::git+https://github.com/Violentmonkey/Violentmonkey.git#tag=v${pkgver}")
b2sums=('2978a3d9043741c9644f824d126bf8e6e7b812caff474aa2a435cef948f1203530c7834b47e73e32296b748cda42520c4c8afc72f1ecbb367264b9530e79acba')

prepare() {
  cd "${srcdir}/source"
  yarn
}

build() {
    cd "${srcdir}/source"
    yarn build
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

