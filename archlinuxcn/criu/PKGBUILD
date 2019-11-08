# Contributor: Pavel Borzenkov <pavel@voidptr.ru>
# Maintainer: aksr <aksr at t-com dot me>
pkgname=criu
pkgver=3.13
pkgrel=1
pkgdesc="A Checkpoint/Restore functionality for Linux in Userspace."
url="http://criu.org"
license=("GPL2")
arch=("x86_64")
source=("http://download.openvz.org/$pkgname/$pkgname-$pkgver.tar.bz2")
depends=('protobuf-c' 'libnl' 'libnet')
makedepends=('xmlto' 'asciidoc' 'python')
options=("!buildflags")
changelog=
md5sums=('5b7da88e1c68582a131674f891294adf')
sha1sums=('b56a647f6b80b413b31abc125a4a85430e062cb9')
sha256sums=('ea027f2acb55c62d47aec0c7776c723e5a877978e60d3574961b6f4c538fc9fa')
sha512sums=('ef93ec9977512711fbcedd52807cc91b1ab582f1c031c4beda93dac7530ccf40bca45b3dee6b5d08a676ec28036caa55ad3746c450265429880e114fde0a071d')

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

