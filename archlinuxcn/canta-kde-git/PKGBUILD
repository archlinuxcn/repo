# Maintainer: Edward Pacman <edward at edward-p dot xyz>

_srcname=canta-kde
pkgname=canta-kde-git
pkgdesc="Canta theme for kde plasma desktop"
pkgver=r12.c476fc5
pkgrel=1
arch=('any')
url="https://github.com/vinceliuice/Canta-kde"
license=('GPL')
depends=()
makedepends=('git')
backup=('usr/share/sddm/themes/Canta/theme.conf.user')
optdepends=('canta-gtk-theme-git' 'canta-icon-theme-git' 'kvantum-qt5')

source=("${_srcname}::git+https://github.com/vinceliuice/Canta-kde.git")
md5sums=('SKIP')

pkgver() {
    cd "${srcdir}/${_srcname}"
    ( set -o pipefail
    git describe --long 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
    )
}

package() {
    cd "${srcdir}/${_srcname}"
    
    mkdir -p "${pkgdir}/usr/share/"{aurorae/themes,color-schemes,plasma/desktoptheme,plasma/look-and-feel,Kvantum}

    _AURORAE_DIR="${pkgdir}/usr/share/aurorae/themes"
    _SCHEMES_DIR="${pkgdir}/usr/share/color-schemes"
    _PLASMA_DIR="${pkgdir}/usr/share/plasma/desktoptheme"
    _LOOKFEEL_DIR="${pkgdir}/usr/share/plasma/look-and-feel"
    _KVANTUM_DIR="${pkgdir}/usr/share/Kvantum"

    cp -r aurorae/Canta-* ${_AURORAE_DIR}
    cp -r color-schemes/*.colors ${_SCHEMES_DIR}
    cp -r Kvantum/Canta-* ${_KVANTUM_DIR}
    cp -r plasma/desktoptheme/Canta-* ${_PLASMA_DIR}
    cp -r plasma/look-and-feel/com.github.vinceliuice.* ${_LOOKFEEL_DIR}
    cp color-schemes/Cantadark.colors ${_PLASMA_DIR}/Canta-dark/colors
    cp color-schemes/Cantalight.colors ${_PLASMA_DIR}/Canta-light/colors

    cd sddm
    mkdir -p "${pkgdir}/usr/share/sddm/themes"
    cp -ur Canta "${pkgdir}/usr/share/sddm/themes"
}

