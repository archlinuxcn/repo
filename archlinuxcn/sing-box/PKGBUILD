# Maintainer: everyx <lunt.luo#gmail.com>

pkgname=sing-box
pkgver=1.12.8
pkgrel=1

pkgdesc='The universal proxy platform.'
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64')
url='https://sing-box.sagernet.org/'
license=("LicenseRef-${pkgname}")

makedepends=('go')
source=("$pkgname-$pkgver.tar.gz::https://github.com/SagerNet/sing-box/archive/v$pkgver.tar.gz"
        "sing-box.rules")
sha256sums=('4d3da19e0819fdc12740539512dc3455ea030747c2fa04171967715fb26ff775'
            '1365536e1875043b969e2e18d7313ab7c6f7f9f63387f25506bb04362b44f206')
conflicts=("$pkgname-git" "$pkgname-beta")
depends=("glibc")
optdepends=('sing-geosite: sing-geosite database'
            'sing-geoip: sing-geoip database')

backup=("etc/$pkgname/config.json")

prepare() {
    cd "${pkgname}-${pkgver}"
    export GOPATH="${srcdir}"
    go mod download -modcacherw
}

_tags=with_gvisor,with_quic,with_dhcp,with_wireguard,with_utls,with_acme,with_clash_api,with_tailscale
build(){
    cd "${pkgname}-${pkgver}"

    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"

    go build \
        -v \
        -trimpath \
        -buildmode=pie \
        -mod=readonly \
        -modcacherw \
        -tags "$_tags" \
        -ldflags "-s -buildid= -X \"github.com/sagernet/sing-box/constant.Version=${pkgver}\" -checklinkname=0
            -linkmode external -extldflags \"${LDFLAGS}\"" \
        ./cmd/sing-box

    install -d completions
    go run ./cmd/sing-box completion bash   > completions/bash
    go run ./cmd/sing-box completion fish   > completions/fish
    go run ./cmd/sing-box completion zsh    > completions/zsh
}

package() {
    cd "$pkgname-$pkgver"

    install -Dm644 LICENSE                                 -t "$pkgdir/usr/share/licenses/$pkgname"
    install -Dm755 "$pkgname"                              -t "$pkgdir/usr/bin"
    install -Dm644 "release/config/config.json"            -t "$pkgdir/etc/$pkgname"
    install -Dm644 "release/config/$pkgname.service"       -t "$pkgdir/usr/lib/systemd/system"
    install -Dm644 "release/config/$pkgname@.service"      -t "$pkgdir/usr/lib/systemd/system"
    install -Dm644 "release/config/$pkgname.sysusers"         "$pkgdir/usr/lib/sysusers.d/$pkgname.conf"
    install -Dm644 "release/config/sing-box.rules"         -t "$pkgdir/usr/share/polkit-1/rules.d"
    install -Dm644 "release/config/sing-box-split-dns.xml"    "$pkgdir/usr/share/dbus-1/system.d/sing-box-split-dns.conf"

    install -Dm644 completions/bash "${pkgdir}/usr/share/bash-completion/completions/${pkgname}.bash"
    install -Dm644 completions/fish "${pkgdir}/usr/share/fish/vendor_completions.d/${pkgname}.fish"
    install -Dm644 completions/zsh  "${pkgdir}/usr/share/zsh/site-functions/_${pkgname}"
}
