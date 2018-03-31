# Maintainer: Shengyu Zhang <arch at srain.im>

pkgname=srain-git
pkgver=0.912.1652368
pkgrel=1
pkgdesc="Modern, beautiful IRC client written in GTK+ 3, git version"
arch=('i686' 'x86_64')
license=('GPL')
url="https://srain.im"
makedepends=('git' 'make' 'gcc' 'pkg-config' 'gettext' 'imagemagick')
depends=('gtk3' 'python' 'curl' 'libnotify' 'libconfig' 'libsoup')
optdepends=(
    'glib-networking: TLS connection support'
    'python-sphinx: for generating documentation'
    'python-urllib3: avatar and pastebin support'
    'python-requests: avatar and pastebin support'
    )
conflicts=('srain')
provides=('srain')
source=("git+https://github.com/SilverRainZ/srain.git#branch=v0.6-stable")
sha256sums=('SKIP')

pkgver() {
    cd ${pkgname%-git}
    echo "0.$(git rev-list --count HEAD).$(git describe --always)"
}

build() {
    cd ${pkgname%-git}

    ./configure --prefix=/usr --config-dir=/etc --disable-debug
    make
}

package() {
    cd ${pkgname%-git}

    make DESTDIR=$pkgdir install
}
