# Maintainer: Alex D'Andrea <alex@dandrea.io>
# Contributor: Salamandar <felix@piedallu.me>
# Contributor: Jaroslav Lichtblau <svetlemodry@archlinux.org>
# Contributor: Martin Wimpress <code@flexion.org>
# Contributor: kozec <kozec at kozec dot com>

pkgname=syncthing-gtk
pkgver=0.10.0
pkgrel=1
pkgdesc='GTK3 based GUI and notification area icon for Syncthing.'
arch=('any')
url='https://github.com/syncthing-gtk/syncthing-gtk'
license=('GPL2')
conflicts=('syncthing-gtk-git' )
depends=(
    'syncthing>=2.0' 'gtk3>=3.12' 'libnotify'
    'python-bcrypt' 'python-cairo' 'python-dateutil' 'python-gobject'
    'psmisc'
)
makedepends=('python-setuptools' 'git' 'meson' 'ninja')
source=(
    "$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
)
sha256sums=('2ec7ff33d7d159f7edda2f381aba84cb50b0d11286f68eda318164c7fa6f9fad')

build() {
    arch-meson "$srcdir/build" "$srcdir/$pkgname-$pkgver"
    ninja -C "$srcdir/build"
}

package() {
    DESTDIR="$pkgdir" ninja -C "$srcdir/build" install
}
