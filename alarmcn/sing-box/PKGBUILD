# Maintainer: everyx <lunt.luo#gmail.com>

pkgname=sing-box
pkgver=1.13.0
pkgrel=1

pkgdesc='The universal proxy platform.'
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64')
url='https://sing-box.sagernet.org/'
license=("LicenseRef-${pkgname}")

makedepends=('go')
source=("$pkgname-$pkgver.tar.gz::https://github.com/SagerNet/sing-box/archive/v$pkgver.tar.gz")
sha256sums=('6ddc71596dc937873c5aba15a4f2b395c5434265efdc1bd21f4c03d8c5b7f641')
conflicts=("$pkgname-git" "$pkgname-beta")
depends=("glibc")
optdepends=('libcronet.so: NaiveProxy outbound support'
            'sing-geosite-rule-set: geosite rule sets'
            'sing-geoip-rule-set: geoip rule sets')

backup=("etc/$pkgname/config.json")

prepare() {
    cd "${pkgname}-${pkgver}"
    export GOPATH="${srcdir}"
    go mod download -modcacherw
}

_tags=with_gvisor,with_quic,with_dhcp,with_wireguard,with_utls,with_acme,with_clash_api,with_tailscale,with_ccm,with_ocm,badlinkname,tfogo_checklinkname0,with_naive_outbound,with_purego
build(){
    cd "${pkgname}-${pkgver}"

    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"

    go build -v \
        -trimpath \
        -buildmode=pie \
        -mod=readonly \
        -modcacherw \
        -tags "$_tags" \
        -ldflags "-linkmode external -extldflags \"${LDFLAGS}\"
            -s -buildid= -X \"github.com/sagernet/sing-box/constant.Version=${pkgver}\"
            -X internal/godebug.defaultGODEBUG=multipathtcp=0 -checklinkname=0" \
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
    install -Dm644 "release/config/sing-box.rules"         -t "$pkgdir/usr/share/polkit-1/rules.d"
    install -Dm644 "release/config/sing-box.service"       -t "$pkgdir/usr/lib/systemd/system"
    install -Dm644 "release/config/sing-box.sysusers"         "$pkgdir/usr/lib/sysusers.d/sing-box.conf"
    install -Dm644 "release/config/sing-box@.service"      -t "$pkgdir/usr/lib/systemd/system"
    install -Dm644 "release/config/sing-box-split-dns.xml"    "$pkgdir/usr/share/dbus-1/system.d/sing-box-split-dns.conf"

    install -Dm644 completions/bash "${pkgdir}/usr/share/bash-completion/completions/${pkgname}.bash"
    install -Dm644 completions/fish "${pkgdir}/usr/share/fish/vendor_completions.d/${pkgname}.fish"
    install -Dm644 completions/zsh  "${pkgdir}/usr/share/zsh/site-functions/_${pkgname}"
}
