# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=ariang-allinone
pkgver=1.2.2
pkgrel=1
pkgdesc="A modern web frontend making aria2 easier to use (all-in-one version)"
arch=('any')
url="https://github.com/mayswind/AriaNg"
license=('MIT')
depends=('xdg-utils')
makedepends=('git' 'nvm')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz"
        "${pkgname}.desktop"
        "${pkgname}.sh")
sha256sums=('c4a6eaa009bd7dc746deacd1b74171c2fb02c6315664205abe8e5631cde5b913'
            '37ddfc79173070226c053a6e4efcae5113162e152a3d472ceb2408b886311a5a'
            'c6c617a9bc32885b8f89c8b7120b67f98f6df52e141db6cfd24ffcd89435ec6a')

build() {
    cd "${srcdir}"/"AriaNg-${pkgver}"/
    source /usr/share/nvm/init-nvm.sh
    nvm install 8.17.0
    npm install --devDependencies
    node_modules/gulp/bin/gulp.js clean build-bundle
}

package() {
    cd "${srcdir}"/"AriaNg-${pkgver}"/
    install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/"${pkgname}"/
    install -Dm 644 dist/index.html -t "${pkgdir}"/usr/share/"${pkgname}"/
    install -Dm 644 src/favicon.png "${pkgdir}"/usr/share/icons/hicolor/32x32/apps/"${pkgname}.png"
    install -Dm 644 src/touchicon.png "${pkgdir}"/usr/share/icons/hicolor/114x114/apps/"${pkgname}.png"
    install -Dm 644 src/tileicon.png "${pkgdir}"/usr/share/icons/hicolor/144x144/apps/"${pkgname}.png"
    install -Dm 644 "${srcdir}"/"${pkgname}.desktop" -t "${pkgdir}"/usr/share/applications/
    install -Dm 755 "${srcdir}"/"${pkgname}.sh" "${pkgdir}"/usr/bin/"${pkgname}"
}
