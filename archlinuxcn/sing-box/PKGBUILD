# Maintainer: everyx <lunt.luo#gmail.com>

pkgname=sing-box
pkgver=1.13.7
pkgrel=1

pkgdesc='The universal proxy platform.'
arch=('i686' 'pentium4' 'x86_64' 'arm' 'armv7h' 'armv6h' 'aarch64')
url='https://sing-box.sagernet.org/'
license=("LicenseRef-${pkgname}")

makedepends=('go' 'clang' 'lld')
source=("$pkgname-$pkgver.tar.gz::https://github.com/SagerNet/sing-box/archive/v$pkgver.tar.gz")
sha256sums=('cbd2f1dc0ae3d2a9418d8a1faea9adf864c7a73a52e0f4598e1dfbaa9f182073')
conflicts=("$pkgname-git" "$pkgname-beta")
depends=("glibc")
optdepends=('sing-geosite-rule-set: GeoSite rule sets'
            'sing-geoip-rule-set: GeoIP rule sets')

backup=("etc/$pkgname/config.json")

prepare() {
    cd "${pkgname}-${pkgver}"
    export GOPATH="${srcdir}"
    go mod download -modcacherw
}

build(){
    cd "${pkgname}-${pkgver}"

    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS} -fuse-ld=lld"
    export CGO_ENABLED=1
    export CC=clang
    export CXX=clang++

    local TAGS=$(cat release/DEFAULT_BUILD_TAGS)
    local LDFLAGS_SHARED=$(cat release/LDFLAGS)

    go build -v \
        -trimpath \
        -buildmode=pie \
        -mod=readonly \
        -modcacherw \
        -tags "$TAGS" \
        -ldflags "-linkmode external -X github.com/sagernet/sing-box/constant.Version=${pkgver} ${LDFLAGS_SHARED} -s -buildid=" \
        ./cmd/sing-box

    install -d completions
    ./"$pkgname" completion bash > completions/bash
    ./"$pkgname" completion fish > completions/fish
    ./"$pkgname" completion zsh  > completions/zsh
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
