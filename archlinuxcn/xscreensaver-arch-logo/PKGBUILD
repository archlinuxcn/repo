# Maintainer: graysky <graysky AT archlinux DOT us>
# Contributor: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Thomas Mudrunka <harvie@@email..cz>
# Contributer: Eric Belanger <eric@archlinux.org>

pkgname=xscreensaver-arch-logo
pkgver=5.43
pkgrel=1
pkgdesc='Screen saver and locker for the X Window System with Arch Linux branding'
url='https://www.jwz.org/xscreensaver/'
arch=('x86_64')
license=('BSD')
depends=('libglade' 'libxmu' 'glu' 'xorg-appres' 'perl-libwww')
makedepends=('bc' 'intltool' 'libxpm')
optdepends=('gdm: for login manager support')
conflicts=('xscreensaver')
provides=('xscreensaver')
backup=('etc/pam.d/xscreensaver')
source=(http://www.jwz.org/xscreensaver/${pkgname%%-*}-${pkgver}.tar.gz
LICENSE logo-50.xpm logo-180.xpm logo-50.png logo-180.png)
sha1sums=('26f5f2535869ec90926e3e6f6df342cf96548c8f'
          '3eedb8b91b13c29df9b1fe5cbb027e1470b802d2'
          '5ff6dfd0a14ca484d4287647c3e00af8e417163c'
          '63ed187b08864993684f826dc87b1c5f42ea5bf4'
          '203ca4f21e0d42263fc0ebb796eaf968c457d93a'
          '619cff60b77812545493dbedb0ba247a37f381e5')
prepare() {
  cd "${pkgname%%-*}-${pkgver}"
  sed 's|-std=c89||' -i configure.in
  autoreconf -fiv
}

build() {
  cd "${pkgname%%-*}-${pkgver}"
  install -Dm644 "$srcdir"/logo-180.xpm  "${srcdir}"/${pkgname%%-*}-${pkgver}/utils/images/logo-180.xpm
    ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --localstatedir=/var \
    --libexecdir=/usr/lib \
    --with-x-app-defaults=/usr/share/X11/app-defaults \
    --with-pam \
    --with-login-manager \
    --with-gtk \
    --with-gl \
    --without-gle \
    --with-pixbuf \
    --with-jpeg
  make
}

package() {
  cd "${pkgname%%-*}-${pkgver}"
  install -d "${pkgdir}/etc/pam.d"
  make install_prefix="${pkgdir}" install
  install -Dm 644 ../LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname%%-*}"
  chmod 755 "${pkgdir}/usr/bin/xscreensaver"
  echo "NotShowIn=KDE;GNOME;" >> "${pkgdir}/usr/share/applications/xscreensaver-properties.desktop"
}

# vim: ts=2 sw=2 et:
