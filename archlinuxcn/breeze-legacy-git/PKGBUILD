# Maintainer: axionl <axionl@aosc.io>
pkgname=breeze-legacy-git
pkgver=r6.d660c4c
pkgrel=2
pkgdesc="A semi-transparent theme based on default Breeze Light and MacBreeze-Shadowless."
arch=('any')
makedepends=('git')
conflicts=("breeze-legacy")
provides=("breeze-legacy")
url="https://gitlab.com/vmorenomarin/Legacy_breeze"
license=("GPL3")

source=("${pkgname}::git+${url}.git")

sha256sums=('SKIP')

pkgver() {
    cd "$srcdir/$pkgname"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
    cd ${srcdir}/${pkgname}
    install -Dm644 LICENSE ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
    install -dm755 ${pkgdir}/usr/share/plasma/desktoptheme/breeze-legacy
    install -Dm644 metadata.desktop ${pkgdir}/usr/share/plasma/desktoptheme/breeze-legacy/metadata.desktop
    install -Dm644 colors ${pkgdir}/usr/share/plasma/desktoptheme/breeze-legacy/colors
    cp -r icons widgets ${pkgdir}/usr/share/plasma/desktoptheme/breeze-legacy/
}
