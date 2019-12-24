# Maintainer: Yardena Cohen <yardenack at gmail dot com>

# check for new commits:
#   https://github.com/gorhill/uBlock/commits/master

gitname=uMatrix
pkgname=chromium-umatrix-git
pkgver=1.4.1b1.1.g0db579d
pkgrel=1
pkgdesc="Point and click matrix to filter net requests according to source, destination and type"
arch=('any')
url="https://github.com/gorhill/${gitname}"
license=('GPL3')
makedepends=(git zip python)
source=("git+${url}.git" "git+https://github.com/uBlockOrigin/uAssets.git")
sha512sums=('SKIP' 'SKIP')

pkgver() {
    cd "${srcdir}/${gitname}"
    local ver="$(git describe --tags | sed 's|-|\.|g')"
    printf "%s" "${ver//-/.}"
}
build() {
    cd "${srcdir}/${gitname}"
    ./tools/make-chromium.sh
}
package() {
   mkdir -p "${pkgdir}/usr/share/${pkgname}"
   cp -dr --no-preserve=ownership "${srcdir}/${gitname}/dist/build/uMatrix.chromium"/* "${pkgdir}/usr/share/${pkgname}/"
}
