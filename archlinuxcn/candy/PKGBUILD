# Maintainer: lanthora <lanthora@outlook.com>

pkgname=candy
pkgver=6.1.4
pkgrel=1
pkgdesc="A tool for creating and managing a virtual network implemented in C++"
url="https://github.com/lanthora/candy"
license=('MIT')
arch=('x86_64' 'aarch64' 'armv7h' 'riscv64' 'loong64')
source=("$pkgname-$pkgver.tar.gz::https://github.com/lanthora/candy/archive/refs/tags/v$pkgver.tar.gz" )
sha256sums=('88b30fd9f0cdc57c7ffa0553cb35aaf9b574256242bd4670af2592724d0ec05f')
makedepends=('cmake' 'ninja' 'pkgconf' 'gcc' 'git')
depends=('fmt' 'glibc' 'gcc-libs' 'openssl' 'spdlog' 'poco')
backup=('etc/candy.cfg')

build() {
        cd "$pkgname-$pkgver"
        cmake -B build -G Ninja -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=RelWithDebInfo
        cmake --build build
}

package() {
        cd "$pkgname-$pkgver"
        install -Dm644 candy.cfg "$pkgdir/etc/candy.cfg"
        install -Dm644 candy.service "$pkgdir/usr/lib/systemd/system/candy.service"
        install -Dm644 candy@.service "$pkgdir/usr/lib/systemd/system/candy@.service"
        install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"
        DESTDIR="$pkgdir" cmake --install build
}
