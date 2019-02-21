# Maintainer: Einhard Leichtfuß <archer@respiranto.de>
# Contributor: Padfoot <padfoot at exemail dot com dot au>
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
sha512sums=('7241b53f88b44e18a7501e775498701fe622c35b9304e883159dd98fc76745d50f23a192bb0416ccf301ddf393af7a3dc10c3057d77898c8e13d11fd058c801e')

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
