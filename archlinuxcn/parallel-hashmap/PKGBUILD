# Maintainer: KokaKiwi <kokakiwi+aur at kokakiwi dot net>

pkgname=parallel-hashmap
pkgver=2.0.0
pkgrel=1
pkgdesc='A family of header-only, very fast and memory-friendly hashmap and btree containers.'
url='https://greg7mdp.github.io/parallel-hashmap/'
license=('Apache-2.0')
arch=('any')
makedepends=('cmake' 'make' 'git' 'gtest')
optdepends=('python: For Conan python package manager.')
source=("$pkgname-$pkgver.tar.gz::https://github.com/greg7mdp/parallel-hashmap/archive/v$pkgver.tar.gz"
        0001-makepkg-Use-system-gtest.patch)
sha256sums=('4f462f51a3468166ea4cf87c80e001dc1999093264cf55cbda3492ca39a7730b'
            '361c5b363fca4a247ba940f2bca1ee60e6ed889a1aebfd13b057a1e31e5c170e')
b2sums=('982297943a7044787b4280cefd62200cfe57dc318b1590cb6bd98a653b6297f9f359428e52b29831a544ba85c6be39d8aded94340df2009975b0926b9bf98754'
        '7cea2282dd3787d94fa86ea37c01bed855f9163311ca3d91f5c0df27b273960ecea10ba13f94a434d56c5fdf568645aa3fb8c581337f1d93fee933c9b724078a')

prepare() {
  cd "$pkgname-$pkgver"

  patch -Np1 -i "$srcdir/0001-makepkg-Use-system-gtest.patch"
}

build() {
  rm -rf build
  cmake -B build -S "$pkgname-$pkgver" \
    -D CMAKE_BUILD_TYPE=None \
    -D CMAKE_INSTALL_PREFIX=/usr \
    -D PHMAP_BUILD_TESTS=ON \
    -D PHMAP_BUILD_EXAMPLES=OFF

  make -C build
}

check() {
  cmake --build build --target test
}

package() {
  cmake --install build --prefix "$pkgdir/usr"
}
