# Maintainer: KokaKiwi <kokakiwi+aur at kokakiwi dot net>

pkgname=parallel-hashmap
pkgver=2.1.0
pkgrel=1
pkgdesc='A family of header-only, very fast and memory-friendly hashmap and btree containers.'
url='https://greg7mdp.github.io/parallel-hashmap/'
license=('Apache-2.0')
arch=('any')
makedepends=('cmake' 'make' 'git' 'gtest')
optdepends=('python: For Conan python package manager.')
source=("$pkgname-$pkgver.tar.gz::https://github.com/greg7mdp/parallel-hashmap/archive/v$pkgver.tar.gz")
sha256sums=('d2c94659a5301c94cd5bbd6cf4b01c1dd635bba15c76cc188cdd82b928136838')
b2sums=('d50b2553f9c5f7581d295b8c8b47ccc2ed437c6bf0dc7e9f3be9d1ca51cc1ebe14a1b9e9739a1119bf780adae89d671ebfbca9f1c2a8e458236b167f6d2266e3')

build() {
  rm -rf build
  cmake -B build -S "$pkgname-$pkgver" \
    -D CMAKE_BUILD_TYPE=None \
    -D CMAKE_INSTALL_PREFIX=/usr \
    -D PHMAP_BUILD_TESTS=ON \
    -D PHMAP_DOWNLOAD_GTEST=OFF \
    -D PHMAP_BUILD_EXAMPLES=OFF

  make -C build
}

check() {
  cmake --build build --target test
}

package() {
  cmake --install build --prefix "$pkgdir/usr"
}
