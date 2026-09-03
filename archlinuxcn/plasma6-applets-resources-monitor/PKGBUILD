# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=plasma6-applets-resources-monitor
_name=plasma-applet-resources-monitor
pkgver=3.5.0
pkgrel=1
pkgdesc='Plasmoid for monitoring CPU, memory, network traffic, GPUs and disks IO'
arch=(any)
url=https://github.com/orblazer/plasma-applet-resources-monitor
license=(GPL-3.0-or-later)
depends=(
    kitemmodels
    kquickcharts
    libksysguard
    libplasma
    plasma5support
)
optdepends=(
    "kdeplasma-addons: to support easier click action"
)
makedepends=(
    cmake
    extra-cmake-modules
)
conflicts=(
    plasma5-applets-resources-monitor
    plasma5-applets-resources-monitor-git
    plasma6-applets-resources-monitor-git
)
source=($pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz)
b2sums=('e99e0afa5839299227eb58626ea72ece8933afba2ac2e8d1888627e163a1f1b5205a973d181c8babb9e44699ae7547ee60c776be90978bfcd2f0acd0a3c09d63')

build() {
    local cmake_options=(
        -B build
        -S $_name-$pkgver
        -W no-author
        -D CMAKE_BUILD_TYPE=None
        -D CMAKE_INSTALL_PREFIX=/usr
    )
    cmake "${cmake_options[@]}"
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}
