# Contributor: Pavel Borzenkov <pavel@voidptr.ru>
# Maintainer: aksr <aksr at t-com dot me>
pkgname=criu
pkgver=3.15
pkgrel=1
pkgdesc="A Checkpoint/Restore functionality for Linux in Userspace."
url="http://criu.org"
license=("GPL2")
arch=("x86_64")
source=("http://download.openvz.org/$pkgname/$pkgname-$pkgver.tar.bz2")
depends=('protobuf-c' 'libnl' 'libnet')
makedepends=('xmlto' 'asciidoc' 'python')
options=("!buildflags")
md5sums=('eb47303cda4b1fca8504333df0529a0d')
sha1sums=('91eb1ccac61a7d538db14884091883c6dab5481a')
sha256sums=('447cc1f350da94d190bcfda753695bf34ce91eee969df8263fcc33d08990a025')
sha512sums=('7bfd32053e47b95d10cdd5e99494bff6a21aa3179518179f8c72e870f0aab960dd76c9f6cb6982e5b881472cf6962eefee3cf7d8ae9128b3379bcaecc937ebbc')

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

