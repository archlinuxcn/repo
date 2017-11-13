# Maintainer:  4679 <admin@libnull.com>
# Contributor:  Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Jochem Kossen <j.kossen@home.nl>

pkgname=fakeroot-tcp
_pkgname=fakeroot
pkgver=1.21
pkgrel=2
pkgdesc='Tool for simulating superuser privileges,with tcp ipc'
arch=('i686' 'x86_64' 'armv7h')
license=('GPL')
url="http://packages.debian.org/fakeroot"
groups=('base-devel')
install=fakeroot.install
depends=('glibc' 'filesystem' 'sed' 'util-linux' 'sh')
makedepends=('po4a')
source=(http://ftp.debian.org/debian/pool/main/f/$_pkgname/${_pkgname}_${pkgver}.orig.tar.gz
        silence-dlerror.patch)
md5sums=('be5c9a0e516869fca4a6758105968e5a'
         '5fba0b541b5af39d804265223fda525c')

prepare() {
  cd $_pkgname-$pkgver
  patch -p1 -i "$srcdir"/silence-dlerror.patch
}

build() {
  cd $_pkgname-$pkgver

  ./bootstrap
  ./configure --prefix=/usr \
    --libdir=/usr/lib/libfakeroot \
    --disable-static \
    --with-ipc=tcp

  make

  cd doc
  po4a -k 0 --rm-backups --variable "srcdir=../doc/" po4a/po4a.cfg
}

package() {
  cd $_pkgname-$pkgver
  make DESTDIR="$pkgdir" install

  install -dm755 "$pkgdir"/etc/ld.so.conf.d/
  echo '/usr/lib/libfakeroot' > "$pkgdir"/etc/ld.so.conf.d/fakeroot.conf

  # install README for sysv/tcp usage
  install -Dm644 README "$pkgdir"/usr/share/doc/$_pkgname/README
}

