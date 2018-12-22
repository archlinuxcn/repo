# Maintainer: Iwan Timmer <irtimmer@gmail.com>
# Contributor: Mark Constable <markc@renta.net>
# Contributor: Anatol Pomozov <anatol.pomozov@gmail.com>

pkgname=cockpit
pkgver=184
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
sha1sums=('bab07e01616e4f1f8c41fa11ceef6377d7d1beff'
          '4d67be534af53d90839b40825528819f25dd8ad1')

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
