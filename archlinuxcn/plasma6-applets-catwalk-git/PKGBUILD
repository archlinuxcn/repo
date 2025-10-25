# Maintainer: Yuzu Vita <g311571057 at gmail dot com>
# Contributor: mcfd <mcfd at noreply dot github dot com>
pkgname=plasma6-applets-catwalk-git
pkgver=r11.01a51e7
pkgrel=2
pkgdesc="A simple plasmoid showing the total CPU usage. Visually made like RunCat."
arch=('any')
url="https://invent.kde.org/rocka/applet-catwalk"
license=('GPL-2.0-or-later')
provides=(plasma6-applets-catwalk)
conflicts=(plasma6-applets-catwalk)
depends=(ksvg libksysguard libplasma qt6-declarative kcmutils kirigami)
makedepends=(cmake git extra-cmake-modules ki18n)
source=("$pkgname::git+https://invent.kde.org/rocka/applet-catwalk.git")
sha256sums=('SKIP')
# options=(!emptydirs)

pkgver() {
    cd "$pkgname"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
}

build() {
    cd "$pkgname"
    cmake -B build -S . -DCMAKE_INSTALL_PREFIX=/usr -Wno-dev
    cmake --build build
}

package() {
    cd "$pkgname"
    DESTDIR="$pkgdir" cmake --install build
}
