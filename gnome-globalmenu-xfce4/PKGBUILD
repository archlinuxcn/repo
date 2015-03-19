# Maintainer: SpepS <dreamspepser at yahoo dot it>
# Contributor: Aliaksandr Stelmachonak <mail.avatar at gmail dot com>

_pkg=gnome-globalmenu
pkgname=$_pkg-xfce4
pkgver=0.7.8
pkgrel=9
pkgdesc="Global Menu Bar built for using with Xfce desktop"
url="http://code.google.com/p/gnome2-globalmenu/"
arch=('i686' 'x86_64')
license=('GPL')
depends=('xfce4-panel')
makedepends=('intltool' 'gconf')
options=('!libtool')
conflicts=('gtk2-aqd' 'gtk2-globalmenu' 'gnome-globalmenu-svn'
           'gnome-globalmenu' 'gnome-globalmenu-git')
install=$pkgname.install
options=(!emptydirs)
source=(http://gnome2-globalmenu.googlecode.com/files/$_pkg-$pkgver.tar.bz2 globalmenu.sh configure.ac.patch dyn-patch-utils.patch)
md5sums=('c2900eb3ff345457f65d9be2793cc2dc'
         'c3ff23800efdae1ab393de8941ecc441'
         'fbf0c72444d3d46a52514b1ecf784bb4'
         '4f93edaf8eea12879b1ceaaba3ab26c3')

build() {
  cd "$srcdir/$_pkg-$pkgver"

  # Does not build with --as-needed
  export LDFLAGS="${LDFLAGS//,--as-needed}"

  # remove libgnome-menu dep and fix xfce4 paths retrieving with pkg-config
  patch -Np0 -i "$srcdir/configure.ac.patch"
  patch -Np0 -i "$srcdir/dyn-patch-utils.patch"
  autoconf

  ./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--libexecdir=/usr/lib \
	--without-gnome-panel \
	--with-xfce4-panel \
	--disable-tests

  make
}

package() {
  cd "$srcdir/$_pkg-$pkgver"

  make -j1 DESTDIR="$pkgdir/" GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 install
  install -Dm755 "$srcdir/globalmenu.sh" "${pkgdir}/etc/profile.d/globalmenu.sh"
  rm -rf "${pkgdir}/etc/gconf"
}
