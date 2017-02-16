# Maintainer: Martin Kostolný <clearmartin at zoho dot com>

pkgname=plasma5-applets-active-window-control-git
_pkgname=plasma5-applets-active-window-control
_gitpkgname=plasma-applet-active-window-control
pkgver=r74.4d399d3
pkgrel=1
pkgdesc="Plasmoid for Plasma 5. Allowes advanced control of active window."
arch=('i686' 'x86_64')
url="https://github.com/kotelnik/$_gitpkgname"
license=('GPL')
depends=('plasma-workspace' 'qt5-graphicaleffects')
makedepends=('git' 'extra-cmake-modules')
conflicts=("${_pkgname-*}" 'plasma-applet-active-window-control-git')
provides=("${_pkgname-*}")
source=("git+https://github.com/kotelnik/$_gitpkgname.git")
md5sums=('SKIP')

pkgver() {
    cd "${_gitpkgname}"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    cd "${_gitpkgname}"

    mkdir -p build
    cd build
    rm -rf *

    cmake .. \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_BUILD_TYPE=Release \
        -DKDE_INSTALL_LIBDIR=lib \
        -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
}

package() {
    cd "${_gitpkgname}"/build
    make install DESTDIR="${pkgdir}"
}
