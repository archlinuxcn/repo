# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Forked from extra/strace. Original contributors:
# Contributor: Giovanni Scafora <giovanni@archlinux.org>
# Contributor: Tom Newsom <Jeepster@gmx.co.uk>

_pkgname=strace
_pkg_arch=x86_64
pkgname=android-${_pkg_arch/_/-}-$_pkgname
pkgver=5.11
pkgrel=4
pkgdesc="A diagnostic, debugging and instructional userspace tracer (Android, $_pkg_arch)"
arch=(any)
url='https://strace.io/'
license=(BSD)
makedepends=(android-ndk)
options=(!buildflags !strip)
source=(https://github.com/strace/strace/releases/download/v$pkgver/strace-$pkgver.tar.xz{,.asc}
        issue174.patch)
sha256sums=('ffe340b10c145a0f85734271e9cce56457d23f21a7ea5931ab32f8cf4e793879'
            'SKIP'
            '169dc3b66e2a2ec364dc30e792b1d8e9fb9357ad3797ba84d88f478b63f393d0')
validpgpkeys=('296D6F29A020808E8717A8842DB5BD89A340AEB7') # Dmitry V. Levin <ldv@altlinux.org>

prepare() {
  cd $_pkgname-$pkgver
  # https://github.com/strace/strace/issues/174
  patch -Np1 -i ../issue174.patch
  autoreconf -ifv
}

build() {
  cd $_pkgname-$pkgver
  export PATH="/opt/android-ndk/toolchains/llvm/prebuilt/linux-x86_64/bin:$PATH"
  CC=$_pkg_arch-linux-android21-clang \
  ./configure --prefix=/opt/android-libs/${_pkg_arch/_/-} \
    --host=$_pkg_arch-linux-android \
    --without-libunwind \
    --enable-mpers=no \
    --disable-gcc-Werror
  make
}

package() {
  cd $_pkgname-$pkgver
  make DESTDIR="$pkgdir" install-exec
  rm -v "$pkgdir"/opt/android-libs/${_pkg_arch/_/-}/bin/strace-*
  install -Dm644 COPYING "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
