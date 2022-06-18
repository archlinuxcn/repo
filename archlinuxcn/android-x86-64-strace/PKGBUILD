# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Forked from extra/strace. Original contributors:
# Contributor: Giovanni Scafora <giovanni@archlinux.org>
# Contributor: Tom Newsom <Jeepster@gmx.co.uk>

_pkgname=strace
_pkg_arch=x86_64
pkgname=android-${_pkg_arch/_/-}-$_pkgname
pkgver=5.18
pkgrel=1
pkgdesc="A diagnostic, debugging and instructional userspace tracer (Android, $_pkg_arch)"
arch=(any)
url='https://strace.io/'
license=(BSD)
makedepends=(android-ndk)
options=(!buildflags !strip)
source=(https://github.com/strace/strace/releases/download/v$pkgver/strace-$pkgver.tar.xz{,.asc})
sha256sums=('60293ea79ac9253d600cdc9be077ad2988ca22284a439c9e66be5150db3d1187'
            'SKIP')
validpgpkeys=('296D6F29A020808E8717A8842DB5BD89A340AEB7') # Dmitry V. Levin <ldv@altlinux.org>

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
