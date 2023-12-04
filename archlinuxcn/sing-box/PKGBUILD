# Maintainer: everyx <lunt.luo#gmail.com>

pkgname=sing-box
pkgver=1.7.2
pkgrel=1

pkgdesc='The universal proxy platform.'
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64')
url='https://sing-box.sagernet.org/'
license=('GPL3 with name use or association addition')

makedepends=('go')

source=("$pkgname-$pkgver.tar.gz::https://github.com/SagerNet/sing-box/archive/v$pkgver.tar.gz")
sha256sums=('74bbe97b0f8df19c1196deda4ad53edc75c57259f51f88391d66071a315829d7')

conflicts=("$pkgname-git" "$pkgname-beta")
optdepends=('sing-geosite: sing-geosite database'
            'sing-geoip: sing-geoip database')

backup=("etc/$pkgname/config.json")

_tags=with_gvisor,with_quic,with_wireguard,with_utls,with_reality_server,with_clash_api,with_ech
build(){
    cd "$pkgname-$pkgver"

    export CGO_CPPFLAGS="$CPPFLAGS"
    export CGO_CFLAGS="$CFLAGS"
    export CGO_CXXFLAGS="$CXXFLAGS"
    export CGO_LDFLAGS="$LDFLAGS"

    go build \
        -v \
        -trimpath \
        -buildmode=pie \
        -mod=readonly \
        -modcacherw \
        -tags "$_tags" \
        -ldflags "
            -X \"github.com/sagernet/sing-box/constant.Version=$pkgver\"
            -s -w -buildid= -linkmode=external" \
        ./cmd/sing-box

    sed -i "/^\[Service\]$/a StateDirectory=$pkgname"    release/config/$pkgname.service
    sed -i "/^\[Service\]$/a StateDirectory=$pkgname-%i" release/config/$pkgname@.service
    sed -i "/^\[Service\]$/a User=$pkgname"              release/config/$pkgname*.service

    echo "u $pkgname - \"Sing-box Service\" - -" > "release/config/$pkgname.sysusers"

    install -d completions
    go run ./cmd/sing-box completion bash   > completions/bash
    go run ./cmd/sing-box completion fish   > completions/fish
    go run ./cmd/sing-box completion zsh    > completions/zsh
}

package() {
    cd "$pkgname-$pkgver"

    install -Dm644 LICENSE                            -t "$pkgdir/usr/share/licenses/$pkgname"
    install -Dm755 "$pkgname"                         -t "$pkgdir/usr/bin"
    install -Dm644 "release/config/config.json"       -t "$pkgdir/etc/$pkgname"
    install -Dm644 "release/config/$pkgname.service"  -t "$pkgdir/usr/lib/systemd/system"
    install -Dm644 "release/config/$pkgname@.service" -t "$pkgdir/usr/lib/systemd/system"
    install -Dm644 "release/config/$pkgname.sysusers"    "$pkgdir/usr/lib/sysusers.d/$pkgname.conf"

    install -Dm644 completions/bash "${pkgdir}/usr/share/bash-completion/completions/${pkgname}.bash"
    install -Dm644 completions/fish "${pkgdir}/usr/share/fish/vendor_completions.d/${pkgname}.fish"
    install -Dm644 completions/zsh  "${pkgdir}/usr/share/zsh/site-functions/_${pkgname}"
}
