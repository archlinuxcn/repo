# Maintainer: Padfoot <padfoot at exemail dot com dot au>
# Contributor: Andrey Vihrov <andrey.vihrov at gmail.com>
# Contributor: ava1ar <mail.avatar at gmail.com>
# Contributor: Alessio Sergi <asergi at archlinux dot us>

pkgname=xfce4-volumed
pkgver=0.1.13
pkgrel=7
pkgdesc="A volume keys control daemon for Xfce"
arch=('i686' 'x86_64')
license=('GPL3')
url="http://git.xfce.org/apps/xfce4-volumed/"
depends=('gstreamer0.10-base' 'libkeybinder2' 'libnotify' 'xfconf')
optdepends=('gstreamer0.10-base-plugins: for sound card support'
'xfce4-notifyd: for OSD notifications')
source=(http://archive.xfce.org/src/apps/${pkgname}/0.1/${pkgname}-${pkgver}.tar.bz2)
md5sums=('03c0ee58aa0a080d35313ac517a975ea')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  ./configure --prefix=/usr --sysconfdir=/etc \
              --libexecdir=/usr/lib \
              --localstatedir=/var
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  make DESTDIR="${pkgdir}" install
}
