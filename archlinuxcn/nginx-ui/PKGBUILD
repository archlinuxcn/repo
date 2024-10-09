# Maintainer: devome <evinedeng@hotmail.com>

pkgname="nginx-ui"
pkgver=2.0.0_beta.36
_pkgver=${pkgver//_/-}
pkgrel=1
pkgdesc="Yet another WebUI for Nginx"
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64' 'riscv64')
url="https://github.com/0xJacky/${pkgname}"
backup=("etc/${pkgname}/config.ini")
license=("AGPL-3.0-or-later")
depends=("nginx")
makedepends=("pnpm" "go")
source=("${pkgname}-${_pkgver}.tar.gz::${url}/archive/refs/tags/v${_pkgver}.tar.gz")
sha256sums=('e0b2c9dc76e3a5dc123304cf8c96ed5e659568cd805ac9d42967b41d8e22670c')

build() {
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"

    cd "${pkgname}-${_pkgver}"
    pnpm --prefix app install
    pnpm --prefix app build

    local ldflags="
        -s -w \
        -extldflags '${LDFLAGS}' \
        -X 'github.com/0xJacky/Nginx-UI/settings.buildTime=$(date +%s)'
    "

    go build \
        -trimpath \
        -tags jsoniter \
        -ldflags="${ldflags}" \
        -o "${pkgname}" \
        ./main.go
    
    sed -E \
        -e "s|^(ExecStart=).+|\1/usr/bin/${pkgname} --config /etc/${pkgname}/config.ini|g" \
        -e "s|^(Documentation=).+|\1https://nginxui.com|g" \
        -i "${pkgname}.service"
}

package() {
    cd "${pkgname}-${_pkgver}"
    install -Dm755 "${pkgname}"         "${pkgdir}/usr/bin/${pkgname}"
    install -Dm644 "${pkgname}.service" "${pkgdir}/usr/lib/systemd/system/${pkgname}.service"
    install -Dm644 app.example.ini      "${pkgdir}/etc/${pkgname}/config.ini"
    install -Dm644 *.md             -t "${pkgdir}/usr/share/doc/${pkgname}"
}
