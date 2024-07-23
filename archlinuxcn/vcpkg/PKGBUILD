# Maintainer: Andrii Derhach <thequasar7@gmail.com>

pkgname=vcpkg
pkgver=2024.07.10
pkgrel=2
pkgdesc='C++ library manager'
depends=('curl' 'fmt' 'gcc-libs' 'glibc' 'tar' 'unzip' 'zip')
makedepends=('cmake' 'ninja')
optdepends=()
arch=('x86_64' 'aarch64')
url='https://github.com/microsoft/vcpkg-tool'
license=('MIT')
provides=('vcpkg')
conflicts=('vcpkg')
_srcname='vcpkg-tool'
_tag="${pkgver//./-}"
source=("${_srcname}-${_tag}.tar.gz::${url}/archive/refs/tags/${_tag}.tar.gz")
source_x86_64=("${pkgname}-x86_64.sh")
source_aarch64=("${pkgname}-aarch64.sh")
sha256sums=('ead9c9b046962c3ed0bbd135db3746bbcbf776b7460731d4ef71c3bafeb3009a')
sha256sums_x86_64=('abfde7dcdea927497f9a7b49e153b8388082f9f12011501c50bcabcf61954c5b')
sha256sums_aarch64=('1a66556e0460f486be6452b608b9cc83f73dd2aad84eb36211c7fa43ae19ae0a')
install="${pkgname}.install"

build() {
    cmake -S "${_srcname}-${_tag}" -B build -G Ninja --fresh \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX='/usr' \
        -DVCPKG_DEVELOPMENT_WARNINGS=OFF \
        -DVCPKG_DEPENDENCY_EXTERNAL_FMT=ON \
        -DVCPKG_BASE_VERSION="${_tag}"
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 "${_srcname}-${_tag}/README.md" "${pkgdir}/usr/share/doc/vcpkg/README.md"
    install -Dm644 "${_srcname}-${_tag}/LICENSE.txt" "${pkgdir}/usr/share/licenses/vcpkg/LICENSE.txt"
    install -Dm644 "${_srcname}-${_tag}/NOTICE.txt" "${pkgdir}/usr/share/licenses/vcpkg/NOTICE.txt"
    install -Dm644 "${pkgname}-${CARCH}.sh" "${pkgdir}/etc/profile.d/vcpkg.sh"
}
