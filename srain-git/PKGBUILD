# Maintainer: Shengyu Zhang <arch at srain.im>

pkgname=srain-git
pkgver=0.679.28fac2b
pkgrel=1
pkgdesc="Modern, beautiful IRC client written in GTK+ 3"
arch=('i686' 'x86_64')
license=('GPL')
url="https://github.com/SilverRainZ/srain"
makedepends=('git' 'make' 'gcc' 'pkg-config' 'gettext' 'imagemagick')
depends=('gtk3' 'python' 'curl' 'libnotify' 'libconfig')
optdepends=(
    'glib-networking: TLS connection support'
    'python-sphinx: for generating documentation'
    'python-urllib3: avatar and pastebin support'
    'python-requests: avatar and pastebin support'
    )
conflicts=('srain')
provides=('srain')
source=("git+https://github.com/SilverRainZ/srain.git")
sha256sums=('SKIP')

pkgver() {
    cd ${pkgname%-git}
    echo "0.$(git rev-list --count HEAD).$(git describe --always)"
}

build() {
    cd ${pkgname%-git}

    mkdir build || true
    ./configure --prefix=/usr --config-dir=/etc --disable-debug
    make
}

package() {
    cd ${pkgname%-git}

    make DESTDIR=$pkgdir install
}
