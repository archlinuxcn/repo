# Maintainer: devome <evinedeng@hotmail.com>

pkgname="ddns-go"
pkgver=6.16.4
pkgrel=1
pkgdesc="A simple, easy-to-use ddns service"
license=('MIT')
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64' 'riscv64')
url="https://github.com/jeessy2/${pkgname}"
provides=("${pkgname}")
conflicts=("${pkgname}")
backup=("etc/${pkgname}/${pkgname}.env" "etc/${pkgname}/config.yml")
install="${pkgname}.install"
license=("MIT")
makedepends=("go")
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
        "${pkgname}.env"
        "${pkgname}.service"
        "${pkgname}.user.service"
        "${pkgname}.sysusers"
        "${pkgname}.tmpfiles")
sha256sums=('15622bad59e897d1cf7fb52e3977b89b0653c9b2389f9993143f416bae195d7a'
            'adc5116f5b965e642a826dd2ac5680a112b85b89963658dae18242cffb9224dc'
            'f73ab3874cc61c7a23c9acfa3efc807dd64955ab3ac48351d1c05a15792e11b3'
            'd65103549ed5dd14f58ce84fba873afc3cc9ea46e679c79c48397d018adacf87'
            '558a170cae11f423591c5487dfe5f5e72f4aa88aaf62055f79a6656b6a98235a'
            '1d8bffaf2683e72d13d18e4208b91ac96e440159069a94f34068c42ec98ed5c2')

build() {
    cd "${pkgname}-${pkgver}"

    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_ENABLED=1

    local build_time="$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
    local ldflags=" \
        -s -w \
        -X main.version=${pkgver} \
        -X main.buildTime=${build_time} \
        -extldflags '${LDFLAGS}'
    "
    go build \
        -trimpath \
        -ldflags="$ldflags"
}

package() {
    install -Dm644 "${pkgname}.env"          "${pkgdir}/etc/${pkgname}/${pkgname}.env"
    install -Dm644 "${pkgname}.service"      "${pkgdir}/usr/lib/systemd/system/${pkgname}.service"
    install -Dm644 "${pkgname}.user.service" "${pkgdir}/usr/lib/systemd/user/${pkgname}.service"
    install -Dm644 "${pkgname}.sysusers"     "${pkgdir}/usr/lib/sysusers.d/${pkgname}.conf"
    install -Dm644 "${pkgname}.tmpfiles"     "${pkgdir}/usr/lib/tmpfiles.d/${pkgname}.conf"

    cd "${pkgname}-${pkgver}"
    install -Dm755 "${pkgname}"              "${pkgdir}/usr/bin/${pkgname}"
    install -Dm644 "LICENSE"                 "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -Dm644 "README.md"               "${pkgdir}/usr/share/doc/${pkgname}/README.md"
    install -Dm644 "README_EN.md"            "${pkgdir}/usr/share/doc/${pkgname}/README_EN.md"
}
