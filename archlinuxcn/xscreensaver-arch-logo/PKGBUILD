# Maintainer: Geballin <macniaque [at] free [dot] fr>
# Maintainer: Morgenstern <charles [at] charlesbwise [dot] com>
# Contributor: Thomas Mudrunka <harvie [at] email [dot] cz>
# Contributor: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Eric Bélanger <eric@archlinux.org>

pkgname=xscreensaver-arch-logo
pkgver=5.45
pkgrel=2
pkgdesc="Screen saver and locker for the X Window System with Arch Linux branding"
url="https://www.jwz.org/${pkgname%%-*}/"
arch=('x86_64')
license=('BSD')
depends=('gdk-pixbuf-xlib'
         'glu' 
         'gtk2'
         'libxmu'         
         'perl-libwww' 
         'xorg-appres') 
makedepends=('bc' 
             'intltool' 
             'libxpm'
             'systemd')
optdepends=('gdm: for login manager support')
conflicts=('xscreensaver')
provides=('xscreensaver')
backup=('etc/pam.d/xscreensaver')
source=(https://www.jwz.org/xscreensaver/${pkgname%%-*}-${pkgver}.tar.gz
LICENSE logo-50.xpm logo-180.xpm logo-50.png logo-180.png)
sha256sums=('7016df6736ba0126a68c1f35abcf411a695fe93bc01a18ebd9df46c9a9f4d50d'
            'c0247a0328f07656f6b7a5854f57fe735579f161b6f40df967cf9a5eab772d63'
            '82366926a2a81bd08459327936ba144e8b3ea5ee4a386c268bd898e1791ab1a0'
            '253f0d5bbdd841f21a7bbdbb0fd7ded21f711751d5cb1b7914952bdd6541b36d'
            '8027bdb2b4328d154a8e517bdb94f5ef4a9eb031e79a285dabedd62acfa77317'
            '8357f9e631b80ae373cb0fc8e27fa96fd032c3d5e3869bd04dde843b79260b19')

build() {
  cp logo-* "${srcdir}"/${pkgname%%-*}-${pkgver}/hacks/images/
  install -Dm0644 "$srcdir"/logo-180.xpm -t "${srcdir}"/${pkgname%%-*}-${pkgver}/utils/images
  cd "${pkgname%%-*}-${pkgver}"
  ./configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --localstatedir=/var \
    --libexecdir=/usr/lib \
    --with-app-defaults=/usr/share/X11/app-defaults \
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
  install -Dm0644 ../LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  # Remove sticky bit
  chmod 755 "${pkgdir}/usr/bin/xscreensaver"
  echo "NotShowIn=KDE;GNOME;" >> "${pkgdir}/usr/share/applications/xscreensaver-properties.desktop"
}

# vim: ts=2 sw=2 et:
