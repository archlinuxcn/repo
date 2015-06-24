# Maintainer: Cedric Leporcq <cedric at gmail dot com>

pkgname=xfce4-windowck-plugin
pkgver=0.4.4
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
sha256sums=('92b6c9e199d32cf96619c31e2cfac19e375575d581e78fa043f9f6a59c1df13f')

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
