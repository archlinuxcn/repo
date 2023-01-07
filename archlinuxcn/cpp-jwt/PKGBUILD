# Maintainer: Marco Rubin <marco.rubin@protonmail.com>

pkgname=cpp-jwt
pkgver=1.4
pkgrel=3
pkgdesc="JSON Web Token library for C++"
arch=('any')
url="https://github.com/arun11299/cpp-jwt"
license=('MIT')
depends=('nlohmann-json' 'openssl')
makedepends=('cmake')
checkdepends=('gtest')
provides=("$pkgname=$pkgver")
conflicts=($pkgname-git)
source=("$url/archive/refs/tags/v$pkgver.tar.gz")
b2sums=('5ded054cca527b803507d49edac82946cea2e9458ca783c5e693bba18313db1aba5c021eb79447bd4d2a077cb3483b9cf11e3119b9920eb4a9b35c43ea8a188e')

prepare() {
    # fix outdated version
    cd $pkgname-$pkgver
    sed -i s/1.2.0/1.4.0/ CMakeLists.txt
}

build() {
    cd $pkgname-$pkgver
    cmake -B build \
		-DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DCPP_JWT_BUILD_EXAMPLES=OFF \
		-DCPP_JWT_BUILD_TESTS="$CHECKFUNC" \
		-DCPP_JWT_USE_VENDORED_NLOHMANN_JSON=OFF \
		-Wno-dev
    cmake --build build
}

check() {
    cd $pkgname-$pkgver
    ctest --test-dir build
}

package() {
    cd $pkgname-$pkgver
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
