# Maintainer: merrkry <jeffpotvin930@gmail.com>

pkgname=sing-box-alpha
_pkgname=sing-box
pkgver=1.11.0beta.1
_pkgver=$(echo "$pkgver" | sed 's/\([0-9]\+\.[0-9]\+.[0-9]\+\)\(alpha\|beta\|rc\)/\1-\2/')
pkgrel=1
epoch=1

pkgdesc='The universal proxy platform.'
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64')
url='https://sing-box.sagernet.org/'
license=('custom:GPL-3.0-or-later WITH name use or association addition')

makedepends=('go')

source=("$_pkgname-$_pkgver.tar.gz::https://github.com/SagerNet/sing-box/archive/v$_pkgver.tar.gz"
        "sing-box.rules")
sha256sums=('5406b8c5896ec6cddf1a8f2c64a7ac3f638ede92bfd43ab92570b4ccced6de38'
            '1365536e1875043b969e2e18d7313ab7c6f7f9f63387f25506bb04362b44f206')

provides=("$_pkgname")
conflicts=("$_pkgname")

optdepends=('sing-geosite: sing-geosite database (deprecated)'
            'sing-geoip: sing-geoip database (deprecated)')

backup=("etc/$_pkgname/config.json")

_tags=with_gvisor,with_quic,with_wireguard,with_utls,with_reality_server,with_clash_api,with_ech,with_acme,with_dhcp
build(){
    cd "$_pkgname-$_pkgver"

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
            -X \"github.com/sagernet/sing-box/constant.Version=$_pkgver\"
            -s -w -buildid= -linkmode=external" \
        ./cmd/sing-box

    sed -i "/^\[Service\]$/a StateDirectory=$_pkgname"    release/config/$_pkgname.service
    sed -i "/^\[Service\]$/a StateDirectory=$_pkgname-%i" release/config/$_pkgname@.service
    sed -i "/^\[Service\]$/a User=$_pkgname"              release/config/$_pkgname*.service

    echo "u $_pkgname - \"Sing-box Service\" - -" > "release/config/$_pkgname.sysusers"

    install -d completions
    go run ./cmd/sing-box completion bash   > completions/bash
    go run ./cmd/sing-box completion fish   > completions/fish
    go run ./cmd/sing-box completion zsh    > completions/zsh
}

package() {
    cd "$_pkgname-$_pkgver"

    install -Dm644 LICENSE                            -t "$pkgdir/usr/share/licenses/$_pkgname"
    install -Dm755 "$_pkgname"                         -t "$pkgdir/usr/bin"
    install -Dm644 "release/config/config.json"       -t "$pkgdir/etc/$_pkgname"
    install -Dm644 "release/config/$_pkgname.service"  -t "$pkgdir/usr/lib/systemd/system"
    install -Dm644 "release/config/$_pkgname@.service" -t "$pkgdir/usr/lib/systemd/system"
    install -Dm644 "release/config/$_pkgname.sysusers"    "$pkgdir/usr/lib/sysusers.d/$_pkgname.conf"
    install -Dm644 "${srcdir}/sing-box.rules"            "$pkgdir/usr/share/polkit-1/rules.d/sing-box.rules"

    install -Dm644 completions/bash "${pkgdir}/usr/share/bash-completion/completions/${_pkgname}.bash"
    install -Dm644 completions/fish "${pkgdir}/usr/share/fish/vendor_completions.d/${_pkgname}.fish"
    install -Dm644 completions/zsh  "${pkgdir}/usr/share/zsh/site-functions/_${_pkgname}"
}
