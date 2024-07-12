# Maintainer: Carl Smedstad <carl.smedstad at protonmail dot com>
# Contributor: Luis Martinez <luis dot martinez at disroot dot org>
# Contributor: Caltlgin Stsodaat <contact@fossdaily.xyz>
# Contributor: Sandy Carter <bwrsandman+aur@gmail.com>

pkgname=fuzzylite
pkgver=6.0
pkgrel=7
pkgdesc="C++ fuzzy logic control library"
arch=(x86_64 aarch64 i686)
url="https://github.com/fuzzylite/fuzzylite"
license=(GPL-3.0-only)
depends=(
  gcc-libs
  glibc
)
makedepends=(cmake)
provides=(libfuzzylite.so)
changelog=CHANGELOG

source=(
  "$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz"
  "remove-werror.patch"
  "fix-catch-glibc-compatibility.patch"
)
sha256sums=(
  '7e9f56deb9baf063de2232bfd8285f57ddccb651dae842fe3f587d0ac65ecdb0'
  '397f8888000225c4ee2b4a1b639c04dc59979e041dd3b8a6e7f65344f68d5b3b'
  '02474d9d973f65338d95d00b72cf7370b00c8e5c1c3cb42f63d844d967e267a7'
)

_archive="$pkgname-$pkgver"

prepare() {
  cd "$_archive"

  patch --forward --strip=1 --input="$srcdir/remove-werror.patch"
  patch --forward --strip=1 --input="$srcdir/fix-catch-glibc-compatibility.patch"

  sed -i '/BenchmarkTest.cpp/d' fuzzylite/FL_TESTS
}

build() {
  cd "$_archive"

  cmake -S fuzzylite -B build \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -Wno-dev \
    -DFL_BUILD_STATIC=OFF \
    -DFL_BUILD_TESTS=ON
  cmake --build build
}

check() {
  cd "$_archive/build/bin"

  ./fuzzylite-tests
}

package() {
  cd "$_archive"

  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 -t "$pkgdir/usr/share/doc/$pkgname" README.md
  install -Dm644 -t "$pkgdir/usr/share/man/man1" fuzzylite/fuzzylite.1
}
