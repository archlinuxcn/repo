# Contributor: Pavel Borzenkov <pavel@voidptr.ru>
# Maintainer: aksr <aksr at t-com dot me>
pkgname=criu
pkgver=3.10
pkgrel=1
pkgdesc="A Checkpoint/Restore functionality for Linux in Userspace."
url="http://criu.org"
license=("GPL2")
arch=("x86_64")
source=("http://download.openvz.org/$pkgname/$pkgname-$pkgver.tar.bz2")
depends=('protobuf-c' 'libnl' 'libnet')
makedepends=('xmlto' 'asciidoc' 'python')
options=("!buildflags")
changelog=Changelog
md5sums=('98abd45f9461ecf086e4322443d1a076')
sha1sums=('a3598bc51ee354d7300b9862be92dc9f41e8b372')
sha256sums=('9b6fca443c10c45512cf532b43b2d52712a48b3ba653589fbc3c25b0ec126abe')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir/" \
       PREFIX=/usr \
       SBINDIR=/usr/bin \
       LOGROTATEDIR=/etc/logrotate.d \
       LIBDIR=/usr/lib install
}

