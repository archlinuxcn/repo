# Maintainer: Brian Bidulock <bidulock@openss7.org>
# Contributor: Jan de Groot <jgc@archlinux.org>

pkgname=gnome-vfs-nosmb
_pkgname=gnome-vfs
pkgver=2.24.4
pkgrel=9
pkgdesc="The GNOME Virtual File System"
arch=(i686 x86_64)
license=('LGPL')
depends=('gconf' 'bzip2' 'gamin' 'dbus' 'avahi' 'gnome-mime-data' 'krb5' 'gnutls' 'libgcrypt')
makedepends=('pkgconfig' 'intltool' 'gtk-doc' 'gnome-common')
options=('!emptydirs')
url="http://www.gnome.org"
install=gnome-vfs.install
provides=($_pkgname)
conflicts=($_pkgname)
source=(http://ftp.gnome.org/pub/gnome/sources/${_pkgname}/2.24/gnome-vfs-${pkgver}.tar.bz2
        gnutls-config.patch
        gnutls-3.4.0.patch
        gcrypt-config.patch
        enable-deprecated.patch)
sha256sums=('62de64b5b804eb04104ff98fcd6a8b7276d510a49fbd9c0feb568f8996444faa'
            '66c7cfb12995c0dd94a2caea95c7e3c55981993f05a79c585d60915ff131955d'
            '5fe5e2e1ad8d8d36deb2d38db621d5b8350aafe3876f722467465c3b3fa304d3'
            'c059e218f310da683778919d36e7862f7e763384805f6453d328fbaf507a8114'
            'ca2b9dffb1fa202c0d1f0d3648ef37cd8e84657a22d4c6746bb46e9a6cf1ee47')

prepare() {
  cd ${_pkgname}-${pkgver}
  #Fix build with new gnutls
  patch -Np1 -i ../gnutls-config.patch
  patch -Np1 -i ../gnutls-3.4.0.patch
  #fix build with new libgcrypt >= 1.5.0
  patch -Np1 -i ../gcrypt-config.patch
  # remove -DG_DISABLE_DEPRECATED
  patch -Np1 -i ../enable-deprecated.patch

  sed -i -s 's|$(srcdir)/auto-test|auto-test|' test/Makefile.am
}
build() {
  cd ${_pkgname}-${pkgver}
  libtoolize --force
  gtkdocize
  aclocal
  autoconf
  automake --add-missing
  CFLAGS="$CFLAGS -fno-strict-aliasing" ./configure \
      --prefix=/usr --sysconfdir=/etc \
      --localstatedir=/var --disable-static \
      --libexecdir=/usr/lib/gnome-vfs-2.0 \
      --disable-samba \
      --disable-hal --enable-avahi --disable-howl \
      --disable-openssl --enable-gnutls
  make
}

package() {
  cd ${_pkgname}-${pkgver}
  make GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 DESTDIR="${pkgdir}" install

  install -d -m755 "${pkgdir}/usr/share/gconf/schemas"
  gconf-merge-schema "${pkgdir}/usr/share/gconf/schemas/${_pkgname}.schemas" --domain gnome-vfs-2.0 ${pkgdir}/etc/gconf/schemas/*.schemas
  rm -f ${pkgdir}/etc/gconf/schemas/*.schemas
}
