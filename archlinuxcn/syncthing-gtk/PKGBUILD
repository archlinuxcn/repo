# Maintainer: Salamandar <felix@piedallu.me>
# Contributor: Jaroslav Lichtblau <svetlemodry@archlinux.org>
# Contributor: Martin Wimpress <code@flexion.org>
# Contributor: kozec <kozec at kozec dot com>

pkgname=syncthing-gtk
pkgver=0.9.4.5
pkgrel=1
pkgdesc='GTK3 based GUI and notification area icon for Syncthing.'
arch=('any')
url='https://github.com/syncthing-gtk/syncthing-gtk'
license=('GPL2')
replaces=( 'syncthing-gtk-python3' )
provides=( 'syncthing-gtk-python3' )
conflicts=('syncthing-gtk-python3' )
depends=(
    'syncthing>=1.0' 'gtk3' 'libnotify'
    'python-bcrypt' 'python-cairo' 'python-dateutil' 'python-gobject'
)
makedepends=('python-setuptools' 'git')
source=(
    "$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz"
)
sha256sums=(
    '42758c3490a7f2ab1323c2ee6a6bef460ceb13b1f5d412c02f3b9347e798573c'
)

prepare() {
    cd "$pkgname-$pkgver"
}

build() {
    cd "$pkgname-$pkgver"
    python3 setup.py build
}

package() {
    cd "$pkgname-$pkgver"
    python3 setup.py install --root="$pkgdir" --optimize=1
}
