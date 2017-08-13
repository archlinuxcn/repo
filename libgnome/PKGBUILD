# $Id$ 
# Maintainer: PhotonX <photon89@googlemail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>

pkgbase=libgnome
pkgname=('libgnome' 'libgnome-data')
pkgver=2.32.1
pkgrel=6
arch=('i686' 'x86_64')
license=('LGPL')
makedepends=('intltool' 'gnome-vfs' 'libbonobo' 'gconf' 'gvfs' 'libcanberra')
options=('!emptydirs')
url="http://www.gnome.org"
source=(https://download.gnome.org/sources/${pkgbase}/2.32/${pkgbase}-${pkgver}.tar.bz2
        0001-Don-t-use-G_DISABLE_DEPRECATED.patch)
sha256sums=('b2c63916866485793b87398266dd7778548c1734923c272a94d84ee011b6f7a4'
            'c2521ed5985159b33a0a5bf53b89012abd9521391fc8ce4c9c73289ca18eb147')

prepare() {
  cd $pkgbase-$pkgver
  patch -Np1 -i ../0001-Don-t-use-G_DISABLE_DEPRECATED.patch
}

build() {
  cd $pkgbase-$pkgver
  autoreconf -fi
  ./configure --prefix=/usr --sysconfdir=/etc \
      --localstatedir=/var --disable-static --disable-esd
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  make
}

package_libgnome() {
    pkgdesc="Common libraries for GNOME"
    depends=("libgnome-data=${pkgver}" 'gnome-vfs' 'libbonobo' 'gconf' 'gvfs' 'libcanberra')

    cd $pkgbase-$pkgver

    make -C libgnome DESTDIR="${pkgdir}" install
    make -C monikers DESTDIR="${pkgdir}" install
}

package_libgnome-data() {
   pkgdesc="Common data from libgnome"
   depends=('gconf')

   cd $pkgbase-$pkgver

   for dir in doc gnome-data po schemas
   do
       make -C $dir GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 DESTDIR="${pkgdir}" install
   done

   install -m755 -d "${pkgdir}/usr/share/gconf/schemas"
   gconf-merge-schema "${pkgdir}/usr/share/gconf/schemas/${pkgbase}.schemas" --domain libgnome-2.0 ${pkgdir}/etc/gconf/schemas/*.schemas
   rm -f "${pkgdir}"/etc/gconf/schemas/*.schemas
}
