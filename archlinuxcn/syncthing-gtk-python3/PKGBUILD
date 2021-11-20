# Maintainer: Salamandar <felix@piedallu.me>
# Contributor: Jaroslav Lichtblau <svetlemodry@archlinux.org>
# Contributor: Martin Wimpress <code@flexion.org>
# Contributor: kozec <kozec at kozec dot com>

_pkgname=syncthing-gtk
pkgname=syncthing-gtk-python3
pkgver=0.9.4.4
pkgrel=3
epoch=1
pkgdesc='GTK3 based GUI and notification area icon for Syncthing. Python 3 port with Debian sources.'
arch=('any')
url='https://salsa.debian.org/debian/syncthing-gtk'
license=('GPL2')
conflicts=( 'syncthing-gtk' )
replaces=(  'syncthing-gtk' )
depends=(
    'syncthing>=0.14.50' 'gtk3' 'libnotify'
    'python-bcrypt' 'python-cairo' 'python-dateutil' 'python-gobject'
)
makedepends=('python-setuptools' 'git')
source=(
    "git+${url}.git#tag=debian/0.9.4.4+ds+git20200927+d09a2ef-3"
    # $pkgname-$pkgver.tar.gz::https://github.com/syncthing/$pkgname/archive/v$pkgver.tar.gz
    kde-statusicon.patch
)
sha256sums=(
    'SKIP'
    '109d8c970045e60251fc64865f05322b23a0995ee6725be02905941cb3a1ae0d'
)

prepare() {
    cd "$_pkgname"
    # Enable Gtk.StatusIcon in KDE
    patch -Np1 -i ../kde-statusicon.patch
}

build() {
    cd "$_pkgname"
    python3 setup.py build
}

package() {
    cd "$_pkgname"
    python3 setup.py install --root="$pkgdir" --optimize=1
}
