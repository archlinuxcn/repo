# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=bkcrack
pkgver=1.8.0
pkgrel=1
pkgdesc="Crack legacy zip encryption with Biham and Kocher's known plaintext attack."
arch=(x86_64)
url="https://github.com/kimci86/bkcrack"
license=(Zlib)
depends=(gcc-libs glibc)
makedepends=(cmake doxygen git)
optdepends=('python: deflate/inflate tools')
source=(git+$url.git#tag=v$pkgver)
sha256sums=('6bae3b5a59cc1ab452b185030c8f1a417b58823c084cade2b2f1f72cb97eb25c')

build() {
  local cmake_options=(
    -B build
    -S $pkgname
    -W no-dev
    -D CMAKE_BUILD_TYPE=None
    -D CMAKE_INSTALL_PREFIX=/usr
    -D BKCRACK_BUILD_DOC=ON
    -D BKCRACK_BUILD_TESTING=ON
  )
  cmake "${cmake_options[@]}"
  cmake --build build
}

check() {
  local excluded_tests=""
  local ctest_flags=(
    --test-dir build
    # show the stdout and stderr when the test fails
    --output-on-failure
    # execute tests in parallel
    --parallel $(nproc)
    # exclude problematic tests
    --exclude-regex "$excluded_tests"
  )
  ctest "${ctest_flags[@]}"
}

package() {
  cd build
  install -Dm755 src/bkcrack "$pkgdir/usr/bin/bkcrack"
  install -dm755 "$pkgdir/usr/share/doc/$pkgname"
  cp -r doc/html "$pkgdir/usr/share/doc/$pkgname"
  cd ../$pkgname
  install -Dm644 license.txt -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 readme.md -t "$pkgdir/usr/share/doc/$pkgname"
  cp -r example "$pkgdir/usr/share/doc/$pkgname"
  install -dm755 "$pkgdir/usr/share/$pkgname"
  cp -r tools "$pkgdir/usr/share/$pkgname"
}
