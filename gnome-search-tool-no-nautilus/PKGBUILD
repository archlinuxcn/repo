# $Id: PKGBUILD 183396 2013-04-21 22:10:19Z heftig $
# Maintainer: Colin Keenan <colinnkeenan at gmail dot com>
# Contributor: Ionut Biru <ibiru@archlinux.org>

# The difference between this PKGBUILD and the one for gnome-search-tool is "depends..."
# This will build gnome-search-tool without depending on nautilus.
# It depends on nautilus-data instead, also available in AUR, and so avoids gnome-desktop

pkgname=gnome-search-tool-no-nautilus
pkgver=3.6.0
pkgrel=3
pkgdesc="installs gnome-search-tool to search for files without nautilus or gnome-desktop"
arch=(i686 x86_64)
url="http://gnome.org"
license=('GPL2')
depends=('nautilus-data' 'libsm')
makedepends=('intltool' 'yelp-tools')
provides=('gnome-search-tool=3.6.0')
install=gnome-search-tool.install
conflicts=('gnome-search-tool')
options=('!emptydirs')
source=(http://download.gnome.org/sources/gnome-search-tool/${pkgver%.*}/gnome-search-tool-$pkgver.tar.xz)
sha256sums=('a33000cd7d033be4ea50422f0f2cca611da5b79bd0f0875017f105a1bc177f42')

build() {
  cd "gnome-search-tool-$pkgver"
  ./configure --prefix=/usr --sysconfdir=/etc
  make
}

package() {
  cd "gnome-search-tool-$pkgver"
  make DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:
