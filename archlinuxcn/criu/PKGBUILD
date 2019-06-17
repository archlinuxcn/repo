# Contributor: Pavel Borzenkov <pavel@voidptr.ru>
# Maintainer: aksr <aksr at t-com dot me>
pkgname=criu
pkgver=3.12
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
md5sums=('408ff60418db114caaf6bfed384e2e71')
sha1sums=('b2ceaf9705aa8239915010136a59664d31044fe3')
sha256sums=('0ef276cefa4bad2ab9f3ac63c975fe95d0522fd2b8469852c7524487aabf0efc')

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

