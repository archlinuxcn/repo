# Maintainer: Andrii Derhach <thequasar7 at gmail dot com>>
# Contributor: Honghao Li <hh.li99@outlook.com>
# Contributor: Michael Yang <ohmyarchlinux@pm.me>
# Contributor: Kuan-Yen Chou <kuanyenchou@gmail.com>

pkgname=vcpkg
pkgver=2024.04.26
pkgrel=1
pkgdesc='C++ library manager for Windows, Linux, and MacOS'
depends=('curl' 'zip' 'unzip')
makedepends=('cmake>=3.3.0' 'ninja')
optdepends=()
arch=('x86_64' 'aarch64')
url='https://github.com/microsoft/vcpkg'
license=('MIT')
provides=('vcpkg')
conflicts=('vcpkg')
source=(
    "${pkgname}-${pkgver}.tar.gz::https://github.com/microsoft/vcpkg/archive/refs/tags/${pkgver}.tar.gz"
    'vcpkg.conf'
)
source_x86_64=(
    'vcpkg-x86_64.csh'
    'vcpkg-x86_64.sh'
)
source_aarch64=(
    'vcpkg-aarch64.csh'
    'vcpkg-aarch64.sh'
)
sha256sums=(
    '2d7eaeaf0318f25306cf995d4f399b43953c9cb1e54b689d850f6ce0f0e7ef48'
    '02a6d2bca471adedfc7acc9ba57860d976ec5115b282cb1a96341850e1c7b221'
)
sha256sums_x86_64=(
    '6afa87afff491f6090c4ade5a9249942f9d503708f81c4cfea5ca22f6b96adba'
    '851f32d41ce7ec0140b8fe4cf1acbb1e8bab18b0d899d12a202558a270d5a4bb'
)
sha256sums_aarch64=(
    '0f26682199cf81c3f9f8c86d7bfbcd0992c9758028e404d4daa63fea8945a947'
    '4c6a7ae3f537d2299ad6b3bbde568987d79bd899243460207736a2f1bc6829ea'
)
install=${pkgname}.install

build() {
    if [ ${CARCH} == "aarch64" ]; then
        export VCPKG_FORCE_SYSTEM_BINARIES=1
    fi
    "${srcdir}/${pkgname}-${pkgver}/bootstrap-vcpkg.sh" -disableMetrics
}

package() {
    export VCPKG_ROOT=/opt/vcpkg
    export VCPKG_DOWNLOADS=/var/cache/vcpkg

    # vcpkg root
    install -Dm755 "${srcdir}/${pkgname}-${pkgver}/vcpkg" "${pkgdir}/${VCPKG_ROOT}/vcpkg"
    cp --preserve=mode -r \
        "${srcdir}/${pkgname}-${pkgver}"/{docs,ports,scripts,triplets,.vcpkg-root,LICENSE.txt} \
        "${pkgdir}/${VCPKG_ROOT}/"

    # default downloads root directory
    install -dm1777 "${pkgdir}/${VCPKG_DOWNLOADS}"

    # reset ownerships and permissions
    chmod -R g+w "${pkgdir}/${VCPKG_ROOT}"
    chgrp -hR 499 "${pkgdir}/${VCPKG_ROOT}" "${pkgdir}/${VCPKG_DOWNLOADS}"

    # license
    install -Dm644 "${srcdir}/${pkgname}-${pkgver}/LICENSE.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

    # systemd-sysusers.service
    install -Dm644 "${srcdir}/vcpkg.conf" "${pkgdir}/usr/lib/sysusers.d/vcpkg.conf"

    # environment variables
    install -Dm755 "${srcdir}/${pkgname}-${CARCH}.sh" "${pkgdir}/etc/profile.d/${pkgname}.sh"
    install -Dm755 "${srcdir}/${pkgname}-${CARCH}.csh" "${pkgdir}/etc/profile.d/${pkgname}.csh"

    # executable entry point
    install -dm755 "${pkgdir}/usr/bin"
    ln -s "${VCPKG_ROOT}/vcpkg" "${pkgdir}/usr/bin/${pkgname}"
}
