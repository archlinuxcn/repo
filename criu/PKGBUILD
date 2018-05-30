# Contributor: Pavel Borzenkov <pavel@voidptr.ru>
# Maintainer: aksr <aksr at t-com dot me>
pkgname=criu
pkgver=3.9
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
md5sums=('35413706419cb777d65bcbf575c25b24')
sha1sums=('4391d17f23893b276b9f59bc912663a4e4d8a33d')
sha256sums=('dd95d35ae6a4eb160926d1b86405e90ba98dfcb9f39e21976057904c67a5e150')

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

