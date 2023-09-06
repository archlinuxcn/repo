# Maintainer: tytan652 <tytan652 at tytanium dot xyz>

pkgbase=qrcodegen-cmake
pkgname=(qrcodegen-cmake qrcodegencpp-cmake)
pkgver=1.8.0
pkgrel=3
epoch=1 # Copy paste miss sorry
pkgdesc="High-quality C and C++ QR Code generator library with CMake and pkgconfig"
arch=("i686" "x86_64" "aarch64")
url="https://github.com/nayuki/QR-Code-generator"
license=("MIT")
depends=(glibc)
makedepends=("cmake" "git")
options=('debug')
source=(
  "QR-Code-generator::git+https://github.com/nayuki/QR-Code-generator.git#tag=v$pkgver"
  "qrcodegen-cmake::git+https://github.com/EasyCoding/qrcodegen-cmake.git#tag=v${pkgver}-cmake2"
)
sha256sums=(
  "SKIP"
  "SKIP"
)

prepare()
{
  cp -R qrcodegen-cmake/{cmake,CMakeLists.txt} QR-Code-generator
}

build() {
  cmake -B build -S QR-Code-generator \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DBUILD_SHARED_LIBS=ON

  cmake --build build
}

package_qrcodegen-cmake() {
  pkgdesc="High-quality C QR Code generator library with CMake and pkgconfig"
  provides=(qrcodegen)
  conflicts=(qrcodegen)

  DESTDIR="$pkgdir" cmake --install build

  rm -rf "$pkgdir"/usr/include/qrcodegencpp
  rm -rf "$pkgdir"/usr/lib/cmake/qrcodegencpp
  rm -rf "$pkgdir"/usr/lib/pkgconfig/qrcodegencpp.pc
  rm -rf "$pkgdir"/usr/lib/libqrcodegencpp.*

  install -Dm644 QR-Code-generator/Readme.markdown "$pkgdir/usr/share/licenses/qrcodegen-cmake/Readme.markdown"
  install -Dm644 qrcodegen-cmake/LICENSE "$pkgdir/usr/share/licenses/qrcodegen-cmake/LICENSE"
}

package_qrcodegencpp-cmake() {
  pkgdesc="High-quality C++ QR Code generator library with CMake and pkgconfig"
  depends+=(gcc-libs)
  provides=(qrcodegencpp)
  conflicts=(qrcodegencpp)

  DESTDIR="$pkgdir" cmake --install build

  rm -rf "$pkgdir"/usr/include/qrcodegen
  rm -rf "$pkgdir"/usr/lib/cmake/qrcodegen
  rm -rf "$pkgdir"/usr/lib/pkgconfig/qrcodegen.pc
  rm -rf "$pkgdir"/usr/lib/libqrcodegen.*

  install -Dm644 QR-Code-generator/Readme.markdown "$pkgdir/usr/share/licenses/qrcodegencpp-cmake/Readme.markdown"
  install -Dm644 qrcodegen-cmake/LICENSE "$pkgdir/usr/share/licenses/qrcodegencpp-cmake/LICENSE"
}
