# Maintainer: Benjamin Valdez <b.valdez.0509+aur<at>gmail.com>
# Contributor: Bruce Zhang <zttt183525594<at>gmail.com>
pkgname=kwin-gestures
pkgver=0.5.1
pkgrel=1
pkgdesc="Custom touchpad gestures for Plasma 6"
arch=('x86_64')
url="https://github.com/taj-ny/kwin-gestures"
license=('GPL-3.0-only')
depends=('kwin' 'yaml-cpp' 'kcmutils' 'gcc-libs' 'qt6-base' 'glibc' 'kcoreaddons' 'ki18n')
makedepends=('extra-cmake-modules' 'cmake')
source=("$pkgname-$pkgver.src.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('582db7bb9d627ce4b917a13b8e528bc1e92a7606f51ed444848fc0c8e53575c7')

build() {
  export CXXFLAGS+=" -DQT_NO_DEBUG_OUTPUT"
  local cmake_options=(
    -B build
    -S "$pkgname-$pkgver"
    -W no-dev
    -D CMAKE_BUILD_TYPE=None
    -D CMAKE_INSTALL_PREFIX=/usr
    #-D BUILD_TESTS
  )
  cmake "${cmake_options[@]}"
  cmake --build build
}

# tests are broken https://github.com/taj-ny/kwin-gestures/issues/27
# check() {
#   local excluded_tests=""
#   local ctest_flags=(
#     --test-dir build
#     # show the stdout and stderr when the test fails
#     --output-on-failure
#     # execute tests in parallel
#     --parallel $(nproc)
#     # exclude problematic tests
#     --exclude-regex "$excluded_tests"
#   )
#   ctest "${ctest_flags[@]}"
# }

package() {
  DESTDIR="$pkgdir" cmake --install build
}
