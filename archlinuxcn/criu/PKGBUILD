# Contributor: Pavel Borzenkov <pavel@voidptr.ru>
# Maintainer: aksr <aksr at t-com dot me>
pkgname=criu
pkgver=3.14
pkgrel=1
pkgdesc="A Checkpoint/Restore functionality for Linux in Userspace."
url="http://criu.org"
license=("GPL2")
arch=("x86_64")
source=("http://download.openvz.org/$pkgname/$pkgname-$pkgver.tar.bz2")
depends=('protobuf-c' 'libnl' 'libnet')
makedepends=('xmlto' 'asciidoc' 'python')
options=("!buildflags")
md5sums=('73398c3db4b3535393b04546a4cc5bc9')
sha1sums=('548d575d89e872c153a756c274e438995eb4e823')
sha256sums=('f63f30188b84e9a611429f732381f27e37c60cde0afc9821600f8597d21e39cb')
sha512sums=('97d064c5ffc41daf6e89edd6208b30e4198f313afc6d621d0dc74dadf94c303be70ba448d4e1ced9500f1c65f1bd12206eb88883be398911cc2c995310b17cc6')

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

