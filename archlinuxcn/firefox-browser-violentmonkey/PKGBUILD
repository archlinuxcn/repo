# Maintainer: Kimiblock Moe

pkgname=(zen-browser-violentmonkey firefox-extension-violentmonkey)
pkgbase=firefox-browser-violentmonkey
pkgver=2.35.0
pkgrel=1
arch=('any')
url='https://github.com/Violentmonkey/Violentmonkey'
license=('MIT')
groups=('zen-browser-addons')
pkgdesc='Web Extension for saving a faithful copy of a complete web page in a single HTML file'
makedepends=('nodejs' 'npm' 'unzip' 'zip' 'git' 'jq' 'yarn')
source=("source::git+https://github.com/Violentmonkey/Violentmonkey.git#tag=v${pkgver}")
b2sums=('26aa7ef680e95f1269fdf2b62b7b36949830672818fa85efdd1456904cb3171dca75d77a24c67adeee2387d42f01aecfffeff78c2456b78738c690ae059f01dd')

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

