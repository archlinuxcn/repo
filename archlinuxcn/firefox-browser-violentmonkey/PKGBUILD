# Maintainer: Kimiblock Moe

pkgname=(zen-browser-violentmonkey firefox-extension-violentmonkey)
pkgbase=firefox-browser-violentmonkey
pkgver=2.37.0
pkgrel=1
arch=('any')
url='https://github.com/Violentmonkey/Violentmonkey'
license=('MIT')
groups=('zen-browser-addons')
pkgdesc='Web Extension for saving a faithful copy of a complete web page in a single HTML file'
makedepends=('nodejs' 'npm' 'unzip' 'zip' 'git' 'jq' 'yarn')
source=("source::git+https://github.com/Violentmonkey/Violentmonkey.git#tag=v${pkgver}")
b2sums=('c82c8e203b8c2a22faf78e4f0a23c0a76cbdbba4e077ddc664e2c02f0a97b08d7774c98ca58ec79c0ea311aa8d9d6d15346b79f915433f34ee4d9999416456c7')

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

