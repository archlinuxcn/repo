# Maintainer: sukanka <su975853527 at gmail dot com>

pkgname=clash-meta
pkgver=1.17.0
pkgrel=2
pkgdesc="Another Clash Kernel by MetaCubeX"
arch=('x86_64' 'aarch64' 'riscv64' 'loong64')
url="https://github.com/MetaCubeX/Clash.Meta"
license=("GPL3")
depends=('glibc' 'clash-geoip')
makedepends=('go')
conflicts=(clash-meta)
backup=('etc/clash-meta/config.yaml')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
        "clash-meta.service"
        "clash-meta@.service"
        "${pkgname}.sysusers"
        "${pkgname}.tmpfiles"
        "config.yaml")
sha256sums=('6d18813d3f0cd1f0e47a36b39fc1bcd9c3d872145591a5399bafabc0abba1af1'
            'b6b7ce11489a6f6322a41ce840b3f999b1ec88914f8bd6864c220269231bf759'
            'ec4de877464e595124a5f2752c3f4be157adc85ec5f7f8392c0331cb70fc906a'
            '655e8e2edcd82a6bdf2fd12430b7ab6f8e32db8dffce70e7342685a7cc65ebfb'
            '50737592c7bd743fe8f543924034718337477a203fa11ef4272cae496df3769c'
            '90f7fdacecd5928e37865b4f841517f925c8bedc769f16f7a7a1e89b923f1fb9')

prepare(){
    cd "${srcdir}"
    mv mihomo-${pkgver} Clash.Meta-${pkgver}
    cd Clash.Meta-${pkgver}
    sed -i 's|^const.*|const Name = "clash"|g' constant/path.go
}
build(){
    cd "${srcdir}"/Clash.Meta-${pkgver}
    BUILDTIME=$(date -u)
    NAME=clash-meta
    GOOS=linux CGO_ENABLED=0 go build \
    -trimpath \
    -buildmode=pie \
    -mod=readonly \
    -modcacherw \
    -ldflags "-linkmode external -extldflags \"${LDFLAGS}\" \
    -X \"github.com/Dreamacro/clash/constant.Version=${pkgver}\" \
    -X \"github.com/Dreamacro/clash/constant.BuildTime=${BUILDTIME}\" \
    " \
    -tags with_gvisor -o ${pkgname}-${pkgver}
}
package() {
    cd "${srcdir}"/Clash.Meta-${pkgver}
    install -Dm755 "${pkgname}-${pkgver}" "${pkgdir}/usr/bin/clash-meta"
    cd $srcdir
    install -Dm644 ${pkgname}.sysusers "${pkgdir}/usr/lib/sysusers.d/${pkgname}.conf"
    install -Dm644 ${pkgname}.tmpfiles "${pkgdir}/usr/lib/tmpfiles.d/${pkgname}.conf"
    install -Dm644 "config.yaml" -t "${pkgdir}/etc/clash-meta"
    install -Dm644 "clash-meta.service"  -t "${pkgdir}/usr/lib/systemd/system"
    install -Dm644 "clash-meta@.service" -t "${pkgdir}/usr/lib/systemd/system"
    ln -sf /etc/clash/Country.mmdb ${pkgdir}/etc/${pkgname}/Country.mmdb
    #geosite.dat from community repo does not work
    # ln -sf /usr/share/v2ray/geosite.dat ${pkgdir}/etc/${pkgname}/GeoSite.dat
}
