# Maintainer: cupnoodles <nwwdles@gmail.com>

pkgname=plasma5-applets-virtual-desktop-bar-git
pkgver=r524.3c42104
pkgrel=1
pkgdesc='KDE Plasma panel applet for managing virtual desktops'
arch=(i686 x86_64)
url='https://github.com/wsdfhjxc/virtual-desktop-bar'
license=(GPL3)
depends=(plasma-workspace)
makedepends=(git gcc extra-cmake-modules)
source=('git+https://github.com/wsdfhjxc/virtual-desktop-bar.git')
md5sums=('SKIP')

pkgver() {
    cd virtual-desktop-bar
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
    mkdir -p build
}

build() {
    cd build
    cmake ../virtual-desktop-bar
    make
}

package() {
    cd build
    make DESTDIR="$pkgdir" install
}
