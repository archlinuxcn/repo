# Maintainer: Alejandro Valdes <alejandro valdes at live dot com>

_pkgbase=Nordic
pkgbase=nordic-kde-git
pkgname=(nordic-kde-git kvantum-theme-nordic-git sddm-nordic-theme-git)
pkgver=2.0.0.r24.gdd1a659
pkgrel=1
pkgdesc="Theme for KDE Plasma 5 using the awesome Nord color pallete"
arch=(any)
url="https://github.com/EliverLara/${_pkgbase}"
license=(GPL3)
options=(!strip)
source=("git+${url}.git"
        "git+${url}-kde.git")
sha256sums=(SKIP SKIP)
makedepends=(git)

pkgver() {
    cd ${_pkgbase}
    git describe --long --tags | sed 's/^[vV-]//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
    echo -e "X-KDE-fallbackPackage=org.kde.breezedark.desktop\n" >> ${srcdir}/${_pkgbase}/kde/plasma/look-and-feel/Nordic/metadata.desktop
    echo -e "X-KDE-fallbackPackage=org.kde.breezedark.desktop\n" >> ${srcdir}/${_pkgbase}/kde/plasma/look-and-feel/Nordic-darker/metadata.desktop
}

package_nordic-kde-git() {
    optdepends=('nordic-theme-git: Matching GTK theme'
                'kvantum-theme-nordic-git: Nordic theme for Kvantum Qt style (recommended)'
                'sddm-nordic-theme-git: Nordic theme for SDDM')
    provides=(nordic-kde)

    cd ${_pkgbase}/kde
    install -d "${pkgdir}"/usr/share
    mkdir -p "${pkgdir}"/usr/share/aurorae/themes
    cp -r aurorae/Nordic "${pkgdir}"/usr/share/aurorae/themes
    mkdir -p "${pkgdir}"/usr/share/color-schemes
    cp -r colorschemes/* "${pkgdir}"/usr/share/color-schemes
    cp -r konsole "${pkgdir}"/usr/share
    mkdir -p "${pkgdir}"/usr/share/plasma/look-and-feel
    cp -r plasma/look-and-feel/* "${pkgdir}"/usr/share/plasma/look-and-feel
    cd ${srcdir}/${_pkgbase}-kde
    rm -r LICENSE
    mkdir -p "${pkgdir}"/usr/share/plasma/desktoptheme/Nordic
    cp -r * "${pkgdir}"/usr/share/plasma/desktoptheme/Nordic
}

package_kvantum-theme-nordic-git() {
    pkgdesc="Nordic theme for KDE Plasma 5"
    depends=(kvantum-qt5)
    provides=(kvantum-theme-nordic)

    cd ${_pkgbase}/kde
    install -d "${pkgdir}"/usr/share
    mkdir -p "${pkgdir}"/usr/share/Kvantum
    cp -r kvantum/* "${pkgdir}"/usr/share/Kvantum
}

package_sddm-nordic-theme-git() {
    pkgdesc="Nordic theme for SDDM"
    depends=(sddm)
    provides=(sddm-nordic-theme)

    cd ${_pkgbase}/kde
    install -d "${pkgdir}"/usr/share/sddm/themes/Nordic
    cp -r sddm/* "${pkgdir}"/usr/share/sddm/themes/Nordic
}

