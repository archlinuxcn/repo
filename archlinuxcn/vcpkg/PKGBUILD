# Maintainer: Andrii Derhach <thequasar7@gmail.com>

pkgname=vcpkg
pkgver=2024.06.10
pkgrel=1
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
sha256sums=('80818c29b255ac4be9f22f8a179f1c146d19df951d3ffe28f06455425aa6d9e3')
sha256sums_x86_64=('abfde7dcdea927497f9a7b49e153b8388082f9f12011501c50bcabcf61954c5b')
sha256sums_aarch64=('1a66556e0460f486be6452b608b9cc83f73dd2aad84eb36211c7fa43ae19ae0a')
install="${pkgname}.install"

prepare() {
    if [ ! -d "${pkgname}-${pkgver}" ]; then
        mv --no-copy "${_srcname}-${_tag}" "${pkgname}-${pkgver}"
    fi
}

build() {
    cmake -S "${pkgname}-${pkgver}" -B build -G Ninja \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX='/usr' \
        -DVCPKG_DEVELOPMENT_WARNINGS=OFF \
        -DVCPKG_DEPENDENCY_EXTERNAL_FMT=ON \
        -DVCPKG_BASE_VERSION="${_tag}"
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 "${pkgname}-${pkgver}/README.md" "${pkgdir}/usr/share/doc/vcpkg/README.md"
    install -Dm644 "${pkgname}-${pkgver}/LICENSE.txt" "${pkgdir}/usr/share/licenses/vcpkg/LICENSE.txt"
    install -Dm644 "${pkgname}-${pkgver}/NOTICE.txt" "${pkgdir}/usr/share/licenses/vcpkg/NOTICE.txt"
    install -Dm644 "${pkgname}-${CARCH}.sh" "${pkgdir}/etc/profile.d/vcpkg.sh"
}
