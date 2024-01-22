# Maintainer: lanthora <lanthora@outlook.com>

pkgname=candy
pkgver=3.8
pkgrel=1
pkgdesc="Another virtual private network that supports point-to-point connections"
url="https://github.com/lanthora/candy"
license=('MIT')
arch=('x86_64' 'aarch64' 'armv7h' 'riscv64')
source=("$pkgname-$pkgver.tar.gz::https://github.com/lanthora/candy/archive/refs/tags/v$pkgver.tar.gz" )
sha256sums=('29f8a094caa7b44902925b98f792d80882efeed6dd0fedee0103a0dd36b5b1d7')
makedepends=('cmake' 'make' 'pkgconf' 'gcc' 'git' 'spdlog')
depends=('zlib' 'fmt' 'glibc' 'gcc-libs' 'openssl' 'libconfig' 'uriparser')
depends_aarch64=('spdlog')
depends_armv7h=('spdlog')
backup=('etc/candy.conf')

build() {
        cd "$pkgname-$pkgver/build"
        cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release ..
        make
}

package() {
        cd "$pkgname-$pkgver"
        install -Dm644 candy.conf "$pkgdir/etc/candy.conf"
        install -Dm644 candy.service "$pkgdir/usr/lib/systemd/system/candy.service"
        install -Dm644 candy@.service "$pkgdir/usr/lib/systemd/system/candy@.service"
        install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"
        cd build
        make DESTDIR="$pkgdir/" install
}
