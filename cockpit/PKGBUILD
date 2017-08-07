# Maintainer: Iwan Timmer <irtimmer@gmail.com>
# Contributor: Mark Constable <markc@renta.net>
# Contributor: Anatol Pomozov <anatol.pomozov@gmail.com>

pkgname=cockpit
pkgver=148
pkgrel=1
pkgdesc='A systemd web based user interface for Linux servers'
arch=(i686 x86_64 armv6h armv7h)
url='http://www.cockpit-project.org/'
license=(LGPL2.1)
conflicts=(cockpit-git)
depends=(libssh krb5 sshpass accountsservice perl-json perl-locale-po json-glib pcp glib-networking)
makedepends=(git intltool python2-pyscss gtk-doc perl-javascript-minifier-xs gobject-introspection networkmanager libgsystem xmlto npm tar)
optdepends=("udisks2: manage hard disks"
	    "networkmanager: manage network connections"
	    "packagekit: manage packages"
	    "docker: manage containers"
	    "libvirt: manage virtual machines"
	    "kubernetes: manage cluster")
source=(https://github.com/cockpit-project/cockpit/releases/download/${pkgver}/cockpit-${pkgver}.tar.xz
	https://github.com/cockpit-project/cockpit/releases/download/${pkgver}/cockpit-cache-${pkgver}.tar.xz)
noextract=(cockpit-${pkgver}.tar.xz)
sha1sums=('d587727f4e9e6812ba78c049f3a4868d4d9d3d53'
          'ecf74b47326a8bf49ea12a8361d2ad25fe5a1e86')

prepare() {
  cd $srcdir

  #bsdtar can't extract cockpit
  tar -xf cockpit-${pkgver}.tar.xz
}

build() {
  cd cockpit-${pkgver}

  ./configure --prefix=/usr --sbindir=/usr/bin --sysconfdir=/etc --localstatedir=/var
  make
}

package() {
  cd cockpit-${pkgver}
  make DESTDIR="$pkgdir" install
}
