# Maintainer: w0rty <mawo97 at gmail.com>
# Contributor:  4679 <admin@libnull.com>
# Contributor:  Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Jochem Kossen <j.kossen@home.nl>

pkgname=fakeroot-tcp
_pkgname=fakeroot
pkgver=1.25.3
pkgrel=2
pkgdesc='Tool for simulating superuser privileges,with tcp ipc'
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
license=('GPL')
url='https://tracker.debian.org/pkg/fakeroot'
install=fakeroot.install
depends=('glibc' 'filesystem' 'sed' 'util-linux' 'sh')
makedepends=('po4a' 'automake' 'autoconf')
provides=("${_pkgname}=${pkgver}-${pkgrel}")
conflicts=("${_pkgname}")
source=(http://ftp.debian.org/debian/pool/main/f/$_pkgname/${_pkgname}_${pkgver}.orig.tar.gz
        fakeroot-1.25.3-glibc-2.33-fix-1.patch
        fakeroot-1.25.3-glibc-2.33-fix-2.patch
        fakeroot-1.25.3-glibc-2.33-fix-3.patch)
sha256sums=('8e903683357f7f5bcc31b879fd743391ad47691d4be33d24a76be3b6c21e956c'
            '7b1ea49a4123a6d95329b370cc9edb51dc0c292ee3eeaa034757b555607026ea'
            '1d2b3c9de24a4249f71e4ed1465ccac462c4ae36bd0a72c796cbfc51fb88a5e6'
            '669dc27fc4a63d265adffbd7fe04521d9e91f46fdba5465c55c6b2d281aae0dc')


prepare() {
  cd $_pkgname-$pkgver

  patch -p1 -i $srcdir/fakeroot-1.25.3-glibc-2.33-fix-1.patch
  patch -p1 -i $srcdir/fakeroot-1.25.3-glibc-2.33-fix-2.patch
  patch -p1 -i $srcdir/fakeroot-1.25.3-glibc-2.33-fix-3.patch
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

