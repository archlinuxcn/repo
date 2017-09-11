# Maintainer: Shengyu Zhang <arch at srain.im>

pkgname=srain
pkgver=0.06.2
pkgrel=1
pkgdesc="Modern, beautiful IRC client written in GTK+ 3"
arch=('i686' 'x86_64')
license=('GPL')
url="https://srain.im"
depends=('gtk3' 'python' 'curl' 'libnotify' 'libconfig' 'libsoup')
makedepends=('git' 'make' 'gcc' 'pkg-config' 'gettext' 'imagemagick')
optdepends=(
    'glib-networking: TLS connection support'
    'python-sphinx: for generating documentation'
    'python-urllib3: avatar and pastebin support'
    'python-requests: avatar and pastebin support'
    )
conflicts=('srain-git')
provides=('srain')
source=("https://github.com/SilverRainZ/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('286f84b3177edfcffbff751b7f556cc07142304cc0df5634762cf7b6d0267cf8')

build() {
    cd ${pkgname}-${pkgver}

    ./configure --prefix=/usr --config-dir=/etc --disable-debug
    make
}

package() {
    cd ${pkgname}-${pkgver}

    make DESTDIR=$pkgdir install
}
