# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Forked from community/networkmanager-l2tp. Original contributors:
# Contributor: Alexander F. Rødseth <xyproto@archlinux.org>
# Contributor: Miles McLean <mills00013@gmail.com>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: Brad Pitcher <bradpitcher@gmail.com>
# Contributor: Moritz Lipp <mlq@pwmt.org>

pkgname=networkmanager-l2tp-git
pkgver=1.8.6.r17.g3ce3ca3
_pppver=2.4.9
pkgrel=1
pkgdesc='L2TP support for NetworkManager'
arch=(x86_64)
url='https://github.com/nm-l2tp/NetworkManager-l2tp'
license=(GPL2)
depends=(libnma libsecret openssl "ppp=$_pppver" xl2tpd)
makedepends=(intltool python git)
optdepends=('libreswan: IPSec support (recommended)'
            'strongswan: IPSec support')
provides=("networkmanager-l2tp=$pkgver")
conflicts=(networkmanager-l2tp)
source=("git+$url")
sha256sums=('SKIP')

prepare() {
  ln -sf NetworkManager-l2tp $pkgname
  cd $pkgname
  NOCONFIGURE=1 ./autogen.sh
}

pkgver() {
  cd $pkgname
  ( set -o pipefail
    git describe --long --tag 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/^v//'
  )
}

build() {
  cd $pkgname
  ./configure \
    --localstatedir=/var \
    --libexecdir=/usr/lib/NetworkManager \
    --prefix=/usr \
    --sysconfdir=/etc \
    --with-pppd-plugin-dir=/usr/lib/pppd/$_pppver
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  make
}

package() {
  make -C $pkgname DESTDIR="$pkgdir" install
  install -Dm644 $pkgname/NEWS "$pkgdir/usr/share/doc/$pkgname/NEWS"
}
