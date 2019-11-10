pkgname='mingw-w64-headers'
pkgver=7.0.0
pkgrel=1
pkgdesc="MinGW-w64 headers for Windows"
arch=('any')
url="http://mingw-w64.sourceforge.net"
license=('custom')
groups=('mingw-w64-toolchain' 'mingw-w64')
options=('!strip' '!libtool' '!emptydirs')
validpgpkeys=('CAF5641F74F7DFBA88AE205693BDB53CD4EBC740')
source=(https://sourceforge.net/projects/mingw-w64/files/mingw-w64/mingw-w64-release/mingw-w64-v${pkgver}.tar.bz2{,.sig})
sha256sums=('f5c9a04e1a6c02c9ef2ec19b3906ec4613606d1b5450d34bbd3c4d94ac696b3b'
            'SKIP')

_targets="i686-w64-mingw32 x86_64-w64-mingw32"

build() {
  for _target in ${_targets}; do
    msg "Configuring ${_target} headers"
    mkdir -p "$srcdir"/headers-${_target} && cd "$srcdir"/headers-${_target}
    "$srcdir"/mingw-w64-v6.0.0/mingw-w64-headers/configure --prefix=/usr/${_target} --enable-sdk=all --enable-secure-api --host=${_target}
  done
}

package() {
  for _target in ${_targets}; do
    msg "Installing ${_target} headers"
    cd "$srcdir"/headers-${_target}
    make DESTDIR="$pkgdir" install
    rm "$pkgdir"/usr/${_target}/include/pthread_signal.h
    rm "$pkgdir"/usr/${_target}/include/pthread_time.h
    rm "$pkgdir"/usr/${_target}/include/pthread_unistd.h
  done

  msg "Installing MinGW-w64 licenses"
  install -Dm644 "$srcdir"/mingw-w64-v6.0.0/COPYING.MinGW-w64/COPYING.MinGW-w64.txt "$pkgdir"/usr/share/licenses/${pkgname}/COPYING.MinGW-w64.txt
  install -Dm644 "$srcdir"/mingw-w64-v6.0.0/COPYING.MinGW-w64-runtime/COPYING.MinGW-w64-runtime.txt "$pkgdir"/usr/share/licenses/${pkgname}/COPYING.MinGW-w64-runtime.txt
  install -Dm644 "$srcdir"/mingw-w64-v6.0.0/mingw-w64-headers/ddk/readme.txt "$pkgdir"/usr/share/licenses/${pkgname}/ddk-readme.txt
  install -Dm644 "$srcdir"/mingw-w64-v6.0.0/mingw-w64-headers/direct-x/COPYING.LIB "$pkgdir"/usr/share/licenses/${pkgname}/direct-x-COPYING.LIB
  install -Dm644 "$srcdir"/mingw-w64-v6.0.0/mingw-w64-headers/direct-x/readme.txt "$pkgdir"/usr/share/licenses/${pkgname}/direct-x-readme.txt
}
