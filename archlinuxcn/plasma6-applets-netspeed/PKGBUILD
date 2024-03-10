# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=plasma6-applets-netspeed
pkgver=2.0.r7.gdb8ff30
_commit="db8ff307fd4e6748fd988ecc77e473c828b47f9c"
pkgrel=1
pkgdesc="Plasma 6 widget that displays the currently used network bandwidth"
arch=('any')
url="https://github.com/dfaust/plasma-applet-netspeed-widget"
license=('GPL-2.0-only')
conflicts=('plasma5-applets-netspeed')
replaces=('plasma5-applets-netspeed')
depends=(
    'awk'
    'plasma-workspace'
)
makedepends=(
    'cmake'
    'extra-cmake-modules'
    'git'
)
source=("${pkgname}::git+https://github.com/dfaust/plasma-applet-netspeed-widget#commit=${_commit}")
b2sums=(SKIP)

pkgver() {
    cd "$pkgname"
    git describe --long --tags --abbrev=7 | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    cmake -B build -S ${pkgname} \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/usr' \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}

