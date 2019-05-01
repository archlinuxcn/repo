# Maintainer: Jeremy MJ <jskier@gmail.com>
# Contributor: Charles Bos <charlesbos1 AT gmail>
# Contributor: Alessio Sergi <asergi at archlinux dot us>

pkgname=xfce4-places-plugin
pkgver=1.8.0
pkgrel=1
pkgdesc="Places menu plugin for the Xfce panel"
arch=('i686' 'x86_64')
url="http://goodies.xfce.org/projects/panel-plugins/xfce4-places-plugin"
license=('GPL2')
depends=('libnotify' 'xfce4-panel')
makedepends=('intltool')
source=("http://archive.xfce.org/src/panel-plugins/$pkgname/${pkgver%.*}/$pkgname-${pkgver}.tar.bz2"
        "mounts.patch")
sha256sums=('7ba3f46f88c2845cbf413efeefaed29157f8b98571856c6e2bf35e4de5d8ecce'
            '0f772f067bff34dd94a473b192494335eb73c4c3d867e4f5bf81828f825d95eb')

prepare() {
  cd "$pkgname-$pkgver"

  # Show other mounts that are non disks (eg. NFS)
  patch -Np1 -i "${srcdir}/mounts.patch"
}

build() {
  cd "$pkgname-$pkgver"

  ./configure \
	--prefix=/usr \
        --sysconfdir=/etc \
        --libexecdir=/usr/lib \
        --localstatedir=/var \
        --disable-static \
        --disable-debug
  make
}
package() {
  cd "$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
}
