# Maintainer: Kimiblock Moe

pkgname=(zen-browser-single-file firefox-extension-single-file)
pkgbase=firefox-browser-single-file
pkgver=1.32.0
pkgrel=1
arch=('any')
url='https://github.com/gildas-lormeau/SingleFile'
license=('AGPL-3.0-only')
groups=('zen-browser-addons')
pkgdesc='Web Extension for saving a faithful copy of a complete web page in a single HTML file'
makedepends=('nodejs' 'npm' 'unzip' 'zip' 'git' 'jq')
source=("source::git+https://github.com/gildas-lormeau/SingleFile.git#tag=v${pkgver}")
b2sums=('c1c62aaaefd5964ac3596c4c3508aa39872261d991310653802f864cd950b9f211d1ca48d1549ce57c20dd4d6c8c1d12659ca1a39ffdd36b7e30869177eea9f4')

prepare() {
  cd "${srcdir}/source"
  npm install
  npm update
}

build() {
    cd "${srcdir}/source"
    npx rollup -c rollup.config.js
    cp package.json package.copy.json
    jq 'del(.dependencies."single-file-cli")' package.copy.json > package.json
    zip -r singlefile-extension-source.zip manifest.json package.json _locales src rollup*.js .eslintrc.js build-extension.sh
    mv package.copy.json package.json
    rm -f singlefile-extension-firefox.zip
    cp src/core/bg/config.js config.copy.js
    cp src/core/bg/companion.js companion.copy.js
    #sed -i "" 's/forceWebAuthFlow: false/forceWebAuthFlow: true/g' src/core/bg/config.js
    #sed -i "" 's/enabled: true/enabled: false/g' src/core/bg/companion.js
    zip -r singlefile-extension-firefox.zip manifest.json lib _locales src
    mv config.copy.js src/core/bg/config.js
    mv companion.copy.js src/core/bg/companion.js
}

package_firefox-extension-single-file() {
    cd "${srcdir}/source"
    install -Dm644 "${srcdir}/source/singlefile-extension-firefox.zip" "${pkgdir}/usr/lib/firefox/browser/extensions/{531906d3-e22f-4a6c-a102-8057b88a1a63}.xpi"
}

package_zen-browser-single-file() {
    cd "${srcdir}/source"
    install -Dm644 "${srcdir}/source/singlefile-extension-firefox.zip" "${pkgdir}/usr/lib/zen-browser/browser/extensions/{531906d3-e22f-4a6c-a102-8057b88a1a63}.xpi"
}

