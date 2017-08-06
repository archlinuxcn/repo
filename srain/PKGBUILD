# Maintainer: Shengyu Zhang <arch at srain.im>

pkgname=srain
pkgver=0.06
pkgrel=2
pkgdesc="Modern, beautiful IRC client written in GTK+ 3"
arch=('i686' 'x86_64')
license=('GPL')
url="https://srain.im"
depends=('gtk3' 'python' 'curl' 'libnotify' 'libconfig')
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
sha256sums=('2bbe3b9e76965ca3d7b9742c823be2468b611383404ada52cf3962c462e49057')

build() {
    cd ${pkgname}-${pkgver}

    ./configure --prefix=/usr --config-dir=/etc --disable-debug
    make
}

package() {
    cd ${pkgname}-${pkgver}

    make DESTDIR=$pkgdir install
}
