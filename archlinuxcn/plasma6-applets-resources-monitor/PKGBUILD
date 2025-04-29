# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=plasma6-applets-resources-monitor
_name=plasma-applet-resources-monitor
pkgver=3.0.2
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
conflicts=(
    plasma5-applets-resources-monitor
    plasma5-applets-resources-monitor-git
    plasma6-applets-resources-monitor-git
)
source=($pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz)
b2sums=('bd5658474991e268f674a936e41b73bd0047ace815620638b05739506021346beb89f2c8f2fc271667b1896650fc7b2c0c778f868d3d43cf34ccd8bd8a623f89')

# TODO: change to cmake when upstream porting to Plasma 6
package() {
    cd $_name-$pkgver
    mkdir -p "$pkgdir"/usr/share/plasma/plasmoids/org.kde.plasma.resources-monitor/
    cp -r package/* "$pkgdir"/usr/share/plasma/plasmoids/org.kde.plasma.resources-monitor/
}
