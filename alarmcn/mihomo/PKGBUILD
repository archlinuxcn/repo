# Maintainer: Izumi Wang <aur at izumis dot moe>

pkgname=mihomo
pkgver=1.19.20
pkgrel=1
pkgdesc="Mihomo Kernel by MetaCubeX, formerly known as Clash.Meta"
arch=("x86_64" 'aarch64')
url="https://github.com/MetaCubeX/mihomo"
license=("GPL3")
depends=('glibc' 'clash-geoip')
makedepends=('go')
conflicts=('clash-meta')
provides=('clash-meta')
backup=('etc/mihomo/config.yaml')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
        "${pkgname}.service"
        "${pkgname}@.service"
        "${pkgname}.sysusers"
        "${pkgname}.tmpfiles"
        "config.yaml")
sha256sums=('e2c6b8a3a86d979a826c8e6dd36cf04148773931b75bac72069717d5297b640d'
            '7b60925a78c9a4b726833e194b395cabddf89b364a5c721522cb78aaece33e79'
            '81a93a53a59dee006bfaa3f8b6490e654ea8a929cd2acb136136b5f7d569aad4'
            '60b5e5308d9aec711e797c402b82899ea0f20951de9baca1594884fbe21f8acc'
            '60b60d84c52443d976265f0be68b13ae1700daffd8de35edf63990380f4c93d9'
            '90f7fdacecd5928e37865b4f841517f925c8bedc769f16f7a7a1e89b923f1fb9')

build(){
    cd "${srcdir}"/mihomo-${pkgver}
    BUILDTIME=$(date -u --rfc-3339=seconds)
    GOOS=linux go build \
    -trimpath \
    -buildmode=pie \
    -mod=readonly \
    -modcacherw \
    -ldflags "-linkmode external -extldflags \"${LDFLAGS}\" \
    -X \"github.com/metacubex/mihomo/constant.Version=${pkgver}\" \
    -X \"github.com/metacubex/mihomo/constant.BuildTime=${BUILDTIME}\" \
    " \
    -tags with_gvisor -o ${pkgname}-${pkgver}
}
package() {
    cd "${srcdir}"/mihomo-${pkgver}
    install -Dm755 "${pkgname}-${pkgver}" "${pkgdir}/usr/bin/${pkgname}"
    cd $srcdir
    install -Dm644 ${pkgname}.sysusers "${pkgdir}/usr/lib/sysusers.d/${pkgname}.conf"
    install -Dm644 ${pkgname}.tmpfiles "${pkgdir}/usr/lib/tmpfiles.d/${pkgname}.conf"
    install -Dm644 "config.yaml" -t "${pkgdir}/etc/${pkgname}"
    install -Dm644 "${pkgname}.service"  -t "${pkgdir}/usr/lib/systemd/system"
    install -Dm644 "${pkgname}@.service" -t "${pkgdir}/usr/lib/systemd/system"
    ln -sf /etc/clash/Country.mmdb ${pkgdir}/etc/${pkgname}/Country.mmdb
    # Compability with applications executing /usr/bin/clash-meta
    ln -sf /usr/bin/mihomo ${pkgdir}/usr/bin/clash-meta
}
