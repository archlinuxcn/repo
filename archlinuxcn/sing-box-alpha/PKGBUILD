# Maintainer: merrkry <merrkry@tsubasa.moe>

pkgname=sing-box-alpha
_pkgname=sing-box
pkgver=1.13.0alpha.15
_pkgver=$(echo "${pkgver}" | sed 's/\([0-9]\+\.[0-9]\+.[0-9]\+\)\(alpha\|beta\|rc\)/\1-\2/')
pkgrel=1
epoch=1

pkgdesc='The universal proxy platform.'
arch=('x86_64' 'aarch64')
url='https://sing-box.sagernet.org/'
license=('custom:GPL-3.0-or-later WITH name use or association addition')

depends=('glibc')
makedepends=('go')

source=("${_pkgname}-${_pkgver}.tar.gz::https://github.com/SagerNet/sing-box/archive/v${_pkgver}.tar.gz")
sha256sums=('f428b71d7ddc3caa45b833ccd77a62843622db9a02a2f28c11d10b7dadd771eb')

provides=("${_pkgname}")
conflicts=("${_pkgname}")

backup=("etc/${_pkgname}/config.json")

_tags=with_gvisor,with_quic,with_wireguard,with_utls,with_clash_api,with_acme,with_dhcp,with_tailscale
build() {
    cd "${_pkgname}-${_pkgver}"

    export CGO_CPPFLAGS="${CPPFLAGS}"
    export CGO_CFLAGS="${CFLAGS}"
    export CGO_CXXFLAGS="${CXXFLAGS}"
    export CGO_LDFLAGS="${LDFLAGS}"
    export CGO_ENABLED=1

    ldflags=(
        "-X"
        "github.com/sagernet/sing-box/constant.Version=${_pkgver}"
        "-s"
        "-w"
        "-buildid="
        "-linkmode=external"
        "-checklinkname=0"
    )
    ldflags_string=$(printf "%s " "${ldflags[@]}")
    # echo "ldflags: ${ldflags_string}"

    go build \
        -v \
        -trimpath \
        -buildmode=pie \
        -mod=readonly \
        -modcacherw \
        -tags "${_tags}" \
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
