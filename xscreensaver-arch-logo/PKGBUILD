# Maintainer: graysky <graysky AT archlinux DOT us>
# Contributor: Thomas Mudrunka <harvie@@email..cz>
# Contributer: Eric Belanger <eric@archlinux.org>

pkgname=xscreensaver-arch-logo
pkgver=5.33
pkgrel=1
pkgdesc="Screen saver and locker for the X Window System with Arch Linux branding"
arch=('i686' 'x86_64')
url="http://www.jwz.org/xscreensaver/"
license=('BSD')
depends=('libglade' 'libxmu' 'glu' 'xorg-appres' 'perl-libwww')
makedepends=('bc' 'intltool' 'libxpm' 'gdm')
optdepends=('gdm: for login manager support')
conflicts=('xscreensaver')
provides=('xscreensaver')
backup=('etc/pam.d/xscreensaver')
source=(http://www.jwz.org/xscreensaver/${pkgname%%-*}-${pkgver}.tar.gz
xscreensaver-add-electricsheep.diff LICENSE
logo-50.xpm logo-180.xpm logo-50.png logo-180.png)
sha256sums=('d4a0c1619219f2843fa8b68d4ae337ab0e9fcb79a6d231540adeb16b3d313f4d'
            'c78db4518d1e439811e177638015c7152c5714f13d1cdb32e5d1f53695c52fec'
            '164903ea70ff499c32a54a940d08cd0510893decbabed7707f6c29a5887ec730'
            '82366926a2a81bd08459327936ba144e8b3ea5ee4a386c268bd898e1791ab1a0'
            '253f0d5bbdd841f21a7bbdbb0fd7ded21f711751d5cb1b7914952bdd6541b36d'
            '8027bdb2b4328d154a8e517bdb94f5ef4a9eb031e79a285dabedd62acfa77317'
            '8357f9e631b80ae373cb0fc8e27fa96fd032c3d5e3869bd04dde843b79260b19')

prepare() {
  cd "${pkgname%%-*}-${pkgver}"
  patch -p0 -i "${srcdir}/xscreensaver-add-electricsheep.diff"
}

build() {
  cd "${pkgname%%-*}-${pkgver}"
  install -Dm644 "$srcdir"/logo-180.xpm  "${srcdir}"/${pkgname%%-*}-${pkgver}/utils/images/logo-180.xpm
  ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var \
    --libexecdir=/usr/lib --with-x-app-defaults=/usr/share/X11/app-defaults \
    --with-pam --with-login-manager --with-gtk --with-gl \
    --without-gle --with-pixbuf --with-jpeg
  make
}

package() {
  cd "${pkgname%%-*}-${pkgver}"
  install -d "${pkgdir}/etc/pam.d"
  make install_prefix="${pkgdir}" install
  install -D -m644 ../LICENSE "${pkgdir}/usr/share/licenses/${pkgname%%-*}/LICENSE"
  chmod 755 "${pkgdir}/usr/bin/xscreensaver"
  echo "NotShowIn=KDE;GNOME;" >> "${pkgdir}/usr/share/applications/xscreensaver-properties.desktop"
}
