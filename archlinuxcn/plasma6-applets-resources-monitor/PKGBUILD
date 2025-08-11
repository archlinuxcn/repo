# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=plasma6-applets-resources-monitor
_name=plasma-applet-resources-monitor
pkgver=3.1.1
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
b2sums=('7e59f0178ea57987a6b9d749ca5d2a020e89afa67a60f8fbcba51cd32001637ba5efe5518043408c1a142a26e1abf3a6fafacca81c3aaa9b557735875b810a4f')

# TODO: change to cmake when upstream porting to Plasma 6
package() {
    cd $_name-$pkgver
    mkdir -p "$pkgdir"/usr/share/plasma/plasmoids/org.kde.plasma.resources-monitor/
    cp -r package/* "$pkgdir"/usr/share/plasma/plasmoids/org.kde.plasma.resources-monitor/
}
