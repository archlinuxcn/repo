# Maintainer: Dct Mei <dctxmei@yandex.com>
# Maintainer: AkinoKaede <autmaple@protonmail.com>
# Maintainer: DuckSoft <realducksoft@gmail.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: pandada8 <pandada8@gmail.com>

pkgname=xray
pkgver=1.7.1
pkgrel=1
pkgdesc="The best v2ray-core, with XTLS support"
arch=('x86_64')
url="https://github.com/XTLS/Xray-core"
license=('MPL2')
depends=('glibc' 'xray-domain-list-community' 'xray-geoip')
makedepends=('go')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz"
        "xray.sysusers"
        "xray.tmpfiles"
        "xray.service"
        "xray@.service")
sha256sums=('631b7910bdabd7fff1e5024d804ed38ff9996207b51d6b26a6c894a36d727523'
            '801131bf2eb079750f17d3e703e414eab8494db0d512164cdef3cc68cef308b8'
            '2d301e9f2fae728da55f33a15b2c36e90cdb657deafb5d6ab7d74375ce9fdf38'
            '66a8a3280aa5b3ed41b9855ba3de3f884bd2113b4a965cf097fcb31c3a6066ed'
            '05d16acd6e00989ece245bf0df919accae858555c7165a50ce2b3db9c0c5a725')

build() {
    cd "${srcdir}"/"Xray-core-${pkgver}"/
    export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external"
    export CGO_LDFLAGS="${LDFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CPPFLAGS="${CPPFLAGS}"
    go build -o xray ./main
}

check() {
    cd "${srcdir}"/"Xray-core-${pkgver}"/
    go test -p 1 -tags json -v -timeout 30m github.com/xtls/xray-core/core/...
}

package() {
    cd "${srcdir}"/"Xray-core-$pkgver"/
    install -d "${pkgdir}"/etc/xray/
    install -Dm 755 xray -t "${pkgdir}"/usr/bin/
    install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/xray/
    install -Dm 644 "${srcdir}"/xray.sysusers "${pkgdir}"/usr/lib/sysusers.d/xray.conf
    install -Dm 644 "${srcdir}"/xray.tmpfiles "${pkgdir}"/usr/lib/tmpfiles.d/xray.conf
    install -Dm 644 "${srcdir}"/xray.service -t "${pkgdir}"/usr/lib/systemd/system/
    install -Dm 644 "${srcdir}"/xray@.service -t "${pkgdir}"/usr/lib/systemd/system/
}
