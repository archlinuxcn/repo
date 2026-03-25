# Maintainer: merrkry <merrkry@tsubasa.moe>

pkgname=sing-box-alpha
_pkgname=sing-box
pkgver=1.14.0alpha.6
_pkgver=$(echo "${pkgver}" | sed 's/\([0-9]\+\.[0-9]\+.[0-9]\+\)\(alpha\|beta\|rc\)/\1-\2/')
pkgrel=1
epoch=1

pkgdesc='The universal proxy platform.'
arch=('x86_64' 'aarch64')
url='https://sing-box.sagernet.org/'
license=('custom:GPL-3.0-or-later WITH name use or association addition')

depends=('glibc')
makedepends=('go' 'clang' 'lld')

source=("${_pkgname}-${_pkgver}.tar.gz::https://github.com/SagerNet/sing-box/archive/v${_pkgver}.tar.gz")
sha256sums=('9b39b46483b8742813cfd4d0bf513a7ed70836acd64fbb116ed455fa6fc0c2fd')

provides=("${_pkgname}")
conflicts=("${_pkgname}")

backup=("etc/${_pkgname}/config.json")

build() {
    cd "${_pkgname}-${_pkgver}"

    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS} -fuse-ld=lld"
    export CGO_ENABLED=1
    export CC=clang
    export CXX=clang++

    local TAGS=$(cat release/DEFAULT_BUILD_TAGS)
    local LDFLAGS_SHARED=$(cat release/LDFLAGS)

    ldflags=(
        "-X"
        "github.com/sagernet/sing-box/constant.Version=${_pkgver}"
        "-s"
        "-w"
        "-buildid="
        "-linkmode=external"
        "${LDFLAGS_SHARED}"
    )
    ldflags_string="${ldflags[*]}"

    go build \
        -v \
        -trimpath \
        -buildmode=pie \
        -mod=readonly \
        -modcacherw \
        -tags "${TAGS}" \
        -ldflags "${ldflags_string}" \
        ./cmd/sing-box

    install -d completions
    "./${_pkgname}" completion bash >completions/bash
    "./${_pkgname}" completion fish >completions/fish
    "./${_pkgname}" completion zsh >completions/zsh
}

package() {
    cd "${_pkgname}-${_pkgver}"

    install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${_pkgname}"
    install -Dm755 "${_pkgname}" -t "${pkgdir}/usr/bin"
    install -Dm644 "release/config/config.json" -t "${pkgdir}/etc/${_pkgname}"
    install -Dm644 "release/config/${_pkgname}.service" -t "${pkgdir}/usr/lib/systemd/system"
    install -Dm644 "release/config/${_pkgname}@.service" -t "${pkgdir}/usr/lib/systemd/system"
    install -Dm644 "release/config/${_pkgname}.sysusers" "${pkgdir}/usr/lib/sysusers.d/${_pkgname}.conf"
    install -Dm644 "release/config/${_pkgname}.rules" -t "${pkgdir}/usr/share/polkit-1/rules.d"
    install -Dm644 "release/config/${_pkgname}-split-dns.xml" "${pkgdir}/usr/share/dbus-1/system.d/${_pkgname}-split-dns.conf"

    install -Dm644 completions/bash "${pkgdir}/usr/share/bash-completion/completions/${_pkgname}.bash"
    install -Dm644 completions/fish "${pkgdir}/usr/share/fish/vendor_completions.d/${_pkgname}.fish"
    install -Dm644 completions/zsh "${pkgdir}/usr/share/zsh/site-functions/_${_pkgname}"
}
