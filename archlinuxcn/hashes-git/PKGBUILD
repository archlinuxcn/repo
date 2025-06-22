#Maintainer:	mumi jim <echo "=02bj5yav9Gb0V3bA1Waq9VatVXb" | rev | base64 -d>

pkgname="hashes-git"
_appname="hashes"
pkgver=1.1.2.r0.ge1b3a8b
pkgrel=2
pkgdesc='Simple hash algorithm identification GUI using GTK4+Adwaita'
url='https://github.com/zefr0x/hashes'
arch=('aarch64' 'x86_64')
license=('GPL-3.0-or-later')
depends=('gtk4' 'libadwaita' 'python-name-that-hash' 'python-gobject')
makedepends=('git' 'meson')
source=("git+${url}.git")
sha512sums=('SKIP')

pkgver() {
    cd "${_appname}/"
    git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    cd "${_appname}/"
    arch-meson . build
    meson compile -C build
}

package() {
    cd "${_appname}/"
    meson install -C build --destdir "$pkgdir"
}
