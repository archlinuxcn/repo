# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=ariang-allinone
pkgver=1.2.3
pkgrel=1
pkgdesc="A modern web frontend making aria2 easier to use (all-in-one version)"
arch=('any')
url="https://github.com/mayswind/AriaNg"
license=('MIT')
depends=('xdg-utils')
makedepends=('git' 'nvm')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz"
        "ariang-allinone-1.2.3.patch"
        "${pkgname}.desktop"
        "${pkgname}.sh")
b2sums=('ed39b83b0ca6479f0d00044a82e6ed46c3b233c024d6f844fd075d956ec42baf1237849698e68a5921071fa86fae50f1b160b2902bd9a7d25bf6f566e18bce90'
        '6304b46d9e58abc2e0b58b3446d6293cafb55617ecf0694b682f4f12f77d1c3cb55b2618f1180b4ece431af30cd7cc2336566c112a53e8b502cc240cc080fbbe'
        '75f9cd947d78ff94a20104cc2d138d82fdb47d8ba994292b27bf88f5e9a5204e989af39a738821bd4dfb500b63e45103cf70ddddc7523e3175b53652241c4701'
        '8585359a12bf26f10923a073fc2b7cb4bcef95ee46c67664356819d959bfbb2f4b8279fd57664e44d569077ff63a4da298b3a36276a423af0c3e8a1e3641133a')

prepare() {
    cd "${srcdir}"/"AriaNg-${pkgver}"/
    patch -p1 -i ../ariang-allinone-1.2.3.patch
}

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
