# Upstream Maintainer: josephgbr <rafael.f.f1 at gmail.com>
# Contributor: Maribu <leonidas200 at web dot de>
# Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbase=gdbm
pkgname=libx32-$_pkgbase
pkgver=1.10
pkgrel=1.1
pkgdesc="GNU database library (x32 ABI)"
license=('GPL')
url="http://www.gnu.org/software/gdbm/gdbm.html"
arch=('x86_64')
depends=('libx32-glibc' "$_pkgbase")
makedepends=('gcc-multilib-x32')
source=(ftp://ftp.gnu.org/gnu/gdbm/${_pkgbase}-${pkgver}.tar.gz
        gdbm-1.10-zeroheaders.patch)
options=('!libtool' '!makeflags')
md5sums=('88770493c2559dc80b561293e39d3570'
         '2a5979910c338dabda6935263b3d8af9')

build() {
  export CC='gcc -mx32'
  
  cd "${srcdir}/${_pkgbase}-${pkgver}"

  # Prevent gdbm from storing uninitialized memory content
  # to database files. This patch improves security, as the
  # uninitialized memory might contain sensitive informations
  # from other applications.
  # https://bugzilla.redhat.com/show_bug.cgi?id=4457
  # http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=208927
  patch -Np1 -i ../gdbm-1.10-zeroheaders.patch

  ./configure --prefix=/usr \
              --mandir=/usr/share/man \
              --infodir=/usr/share/info \
              --enable-libgdbm-compat \
              --libdir=/usr/libx32

  make prefix=/usr
}

check() {
  cd "${srcdir}/${_pkgbase}-${pkgver}"
  make check
}

package() {
  cd "${srcdir}/${_pkgbase}-${pkgver}"
  
  make prefix="$pkgdir/usr" \
       manprefix="$pkgdir/usr/share/man" \
       man3dir="$pkgdir/usr/share/man/man3" \
       infodir="$pkgdir/usr/share/info" \
       libdir="$pkgdir/usr/libx32" \
       install

  rm -rf "${pkgdir}/usr"/{bin,share,include}
}
