# $Id: PKGBUILD 299071 2017-06-20 16:53:25Z juergen $
# Maintainer: Jörg Schuck <joerg_schuck@web.de>
# Contributor: Juergen Hoetzel <juergen@archlinux.org>
# Contributor: Mark Schneider <queueRAM@gmail.com>

pkgname=gnucash
pkgver=2.6.19
pkgrel=2
pkgdesc="A personal and small-business financial-accounting application"
arch=('i686' 'x86_64')
url="http://www.gnucash.org"
license=("GPL")
depends=('guile2.0' 'slib' 'goffice0.8' 'libdbi-drivers' 'libmariadbclient' 'postgresql-libs' 'aqbanking' 'desktop-file-utils' 'webkitgtk2' 'libgnome-keyring' 'libgnomecanvas' 'dconf')
makedepends=('intltool')
optdepends=('evince: for print preview'
	    'yelp: help browser'
            'perl-finance-quote: for stock information lookups'
            'perl-date-manip: for stock information lookups')
options=('!makeflags' '!emptydirs')
backup=(
	'etc/gnucash/config'
	'etc/gnucash/environment'
) 
source=(https://github.com/Gnucash/${pkgname}/releases/download/${pkgver}/${pkgname}-${pkgver}.tar.bz2)
sha1sums=('d2ae5c7855fac30d88fe889d47a441e8a887b19c')
sha256sums=('50b89367246ec2d51e9765bd6bd8c669e35ceb4ac5ab92636f76758a9f3f7fd1')
sha512sums=('0a979caf48ba96d6f37a929036e7172855cfb03af8832f479966bce72fad3400903925134d33aaa31eb6b36a2041f5e0d3f74b88e95b83c7d76e96b1503bec13')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  ./configure --prefix=/usr --mandir=/usr/share/man --sysconfdir=/etc \
    --libexecdir=/usr/lib --disable-schemas-compile --enable-ofx --enable-aqbanking
  make GUILD=/usr/bin/guild2.0
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 DESTDIR="${pkgdir}" install
  cd src/doc/design
  make DESTDIR="${pkgdir}" install-info

  install -dm755 "${pkgdir}/usr/share/gconf/schemas"
  gconf-merge-schema "${pkgdir}/usr/share/gconf/schemas/${pkgname}.schemas" --domain gnucash "${pkgdir}"/etc/gconf/schemas/*.schemas
  rm -f "${pkgdir}"/etc/gconf/schemas/*.schemas

  # Delete the gnucash-valgrind executable because the source files
  # are not included with the package and the executable is hardlinked
  # to the location that it was built at.
  rm -f "${pkgdir}"/usr/bin/gnucash-valgrind

}
