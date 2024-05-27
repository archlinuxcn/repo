# Maintainer: Andrii Derhach <thequasar7@gmail.com>
# Contributor: Honghao Li <hh.li99@outlook.com>
# Contributor: Michael Yang <ohmyarchlinux@pm.me>
# Contributor: Kuan-Yen Chou <kuanyenchou@gmail.com>

pkgname=vcpkg
pkgver=2024.04.26
pkgrel=2
pkgdesc='C++ library manager'
depends=('curl' 'zip' 'unzip')
makedepends=('cmake' 'ninja')
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
source_x86_64=('vcpkg-x86_64.sh')
source_aarch64=('vcpkg-aarch64.sh')
sha256sums=(
    '2d7eaeaf0318f25306cf995d4f399b43953c9cb1e54b689d850f6ce0f0e7ef48'
    '02a6d2bca471adedfc7acc9ba57860d976ec5115b282cb1a96341850e1c7b221'
)
sha256sums_x86_64=('65c6e38406f5c9b519343f5ea1c7bf61c5dafcf165f61c020b8f2308d1da286c')
sha256sums_aarch64=('681372285eda5137ec00b20d7f8d12e9e4d72596125ab725d4fdeddca9783ac6')
install="${pkgname}.install"

build() {
    if [ ${CARCH} == "aarch64" ]; then
        export VCPKG_FORCE_SYSTEM_BINARIES=1
    fi
    "${srcdir}/${pkgname}-${pkgver}/bootstrap-vcpkg.sh" -disableMetrics
}

package() {
    export VCPKG_ROOT=/usr/lib/vcpkg
    export VCPKG_DOWNLOADS=/var/cache/vcpkg

    # vcpkg root
    install -Dm755 "${srcdir}/${pkgname}-${pkgver}/vcpkg" "${pkgdir}/${VCPKG_ROOT}/vcpkg"
    cp --preserve=mode -r \
        "${srcdir}/${pkgname}-${pkgver}"/{docs,ports,scripts,triplets,.vcpkg-root,LICENSE.txt,vcpkg.disable-metrics} \
        "${pkgdir}/${VCPKG_ROOT}/"

    # default downloads root directory
    install -dm1775 "${pkgdir}/${VCPKG_DOWNLOADS}"

    # reset ownerships and permissions
    chmod -R g+w "${pkgdir}/${VCPKG_ROOT}"
    chgrp -hR 499 "${pkgdir}/${VCPKG_ROOT}" "${pkgdir}/${VCPKG_DOWNLOADS}"

    # license
    install -Dm644 "${srcdir}/${pkgname}-${pkgver}/LICENSE.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

    # systemd-sysusers.service
    install -Dm644 "${srcdir}/vcpkg.conf" "${pkgdir}/usr/lib/sysusers.d/vcpkg.conf"

    # environment variables
    install -Dm755 "${srcdir}/${pkgname}-${CARCH}.sh" "${pkgdir}/etc/profile.d/${pkgname}.sh"

    # executable entry point
    install -dm755 "${pkgdir}/usr/bin"
    ln -s "${VCPKG_ROOT}/vcpkg" "${pkgdir}/usr/bin/${pkgname}"
}
