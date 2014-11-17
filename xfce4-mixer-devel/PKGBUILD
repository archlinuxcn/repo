# $Id: PKGBUILD 198556 2014-04-22 15:35:11Z allan $
# Contributor: Tobias Kieslich <tobias funnychar archlinux.org>
# Maintainer: Silvio Knizek <killermoehre funnychar gmx.net

_pkgname=xfce4-mixer
pkgname=${_pkgname}-devel
pkgver=4.11.0
pkgrel=3
pkgdesc="The volume control plugin for the Xfce panel"
arch=('i686' 'x86_64')
url="http://www.xfce.org/"
license=('GPL2')
groups=('xfce4')
depends=('xfce4-panel' 'gstreamer0.10-base-plugins' 'libunique' 'libkeybinder2')
optdepends=('gstreamer0.10-good-plugins: for OSS and PulseAudio support')
makedepends=('intltool')
provides=("${_pkgname}=${pkgver}")
conflicts=("${_pkgname}")
install=$pkgname.install
source=(http://archive.xfce.org/src/apps/${_pkgname}/${pkgver%.*}/${_pkgname}-$pkgver.tar.bz2)
sha256sums=('fb0c1df201ed1130f54f15b914cbe5a59286e994a137acda5609570c57112de2')
md5sums=('1b3753b91224867a3a2dfddda239c28d')

build() {
  cd "$srcdir/${_pkgname}-$pkgver"

  ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --libexecdir=/usr/lib \
    --localstatedir=/var \
    --disable-static \
    --disable-debug \
    --enable-keybinder
  make
}

package() {
  cd "$srcdir/${_pkgname}-$pkgver"
  make DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
