# Maintainer: Andrii Derhach <thequasar7 at gmail dot com>>
# Contributor: Honghao Li <hh.li99@outlook.com>
# Contributor: Michael Yang <ohmyarchlinux@pm.me>
# Contributor: Kuan-Yen Chou <kuanyenchou@gmail.com>

pkgname=vcpkg
pkgver=2023.04.15
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
    'vcpkg.csh'
    'vcpkg.sh'
    'vcpkg.conf'
)
sha256sums=(
    '7b5a7fd9a9019773e7a09dbc9aa167e01cc7745e819994d458af23e56e25e658'
    '6afa87afff491f6090c4ade5a9249942f9d503708f81c4cfea5ca22f6b96adba'
    '851f32d41ce7ec0140b8fe4cf1acbb1e8bab18b0d899d12a202558a270d5a4bb'
    '02a6d2bca471adedfc7acc9ba57860d976ec5115b282cb1a96341850e1c7b221'
)
install=${pkgname}.install

build() {
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
    install -Dm755 "${srcdir}/${pkgname}.sh" "${pkgdir}/etc/profile.d/${pkgname}.sh"
    install -Dm755 "${srcdir}/${pkgname}.csh" "${pkgdir}/etc/profile.d/${pkgname}.csh"

    # executable entry point
    install -dm755 "${pkgdir}/usr/bin"
    ln -s "${VCPKG_ROOT}/vcpkg" "${pkgdir}/usr/bin/${pkgname}"
}
