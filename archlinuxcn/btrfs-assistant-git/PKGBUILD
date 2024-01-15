# Maintainer: dr460nf1r3 <dr460nf1r3 at garudalinux dot org>

pkgname=btrfs-assistant-git
_pkgname=btrfs-assistant
pkgver=1.9.r2.ge602da7
pkgrel=1
pkgdesc="An application for managing BTRFS subvolumes and Snapper snapshots"
arch=('x86_64' 'aarch64')
url="https://gitlab.com/$_pkgname/$_pkgname"
license=('GPL3')
depends=('qt6-base' 'qt6-svg' 'ttf-font' 'polkit' 'util-linux' 'btrfs-progs' 'diffutils')
optdepends=('snapper' 'btrfsmaintenance')
makedepends=('git' 'cmake' 'qt6-tools')
conflicts=('btrfs-assistant')
provides=('btrfs-assistant')
backup=(etc/btrfs-assistant.conf)
source=(git+$url.git)
md5sums=('SKIP')

pkgver() {
    cd "$srcdir/$_pkgname"
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}


build() {
    cd "$srcdir/$_pkgname"
    cmake -B build -S . -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE='Release'
	make -C build
}

package() {
    cd "$srcdir/$_pkgname"
    make -C build DESTDIR="$pkgdir" install
}
