# Maintainer: Cedric Leporcq <cedric at gmail dot com>

pkgname=xfce4-windowck-plugin
pkgver=0.4.3
pkgrel=1
pkgdesc="Xfce panel plugin which allows to put the maximized window title and buttons on the panel."
arch=('i686' 'x86_64')
url="https://github.com/cedl38/xfce4-windowck-plugin"
license=('GPL3')
groups=('xfce4')
depends=('xfce4-panel')
makedepends=('intltool' 'xfce4-dev-tools' 'python3' 'imagemagick')
options=('!libtool')
install=$pkgname.install
source=("$pkgname-$pkgver.tar.gz::https://github.com/cedl38/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('2888fe904f2f911cd43c532ff53678d86201a9435a300a982242e378beeecd26')

build() {
  cd "$srcdir/${pkgname}-$pkgver"

    ./autogen.sh \
    --prefix=/usr 

  make
}

package() {
  cd "$srcdir/${pkgname}-$pkgver"
  make DESTDIR="$pkgdir" install
}
