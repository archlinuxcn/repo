# Maintainer: arjan5 <aur@anymore.nl>

_pkgname=ntfy
pkgname=${_pkgname}sh-bin
pkgver=2.6.2
pkgrel=1
pkgdesc="Send push notifications to your phone or desktop using PUT/POST"
arch=('x86_64' 'aarch64' 'armv7h')
url="https://github.com/binwiederhier/ntfy"
license=('GPL2')
depends=()
makedepends=()
provides=("${_pkgname}")
conflicts=("${_pkgname}")
backup=('etc/ntfy/server.yml' 'etc/ntfy/client.yml')

source_x86_64=("${url}/releases/download/v${pkgver}/${_pkgname}_${pkgver}_linux_amd64.tar.gz"
               "${_pkgname}.sysusers")
source_aarch64=("${url}/releases/download/v${pkgver}/${_pkgname}_${pkgver}_linux_arm64.tar.gz"
               "${_pkgname}.sysusers")
source_armv7h=("${url}/releases/download/v${pkgver}/${_pkgname}_${pkgver}_linux_armv7.tar.gz"
               "${_pkgname}.sysusers")

sha256sums_x86_64=('c8a23c5ecb4fd58549bb18524fd3990f032f17e5adef97dcea0633b40d700816'
                   '0799a140256072b350b56c1b2db5fc21c94c6992277d6d1364c28ddf7058cc8f')
sha256sums_aarch64=('fc5b20d587798567a419934196ede635ccdac04fbac94d6de06ffc0efb1d5a59'
                   '0799a140256072b350b56c1b2db5fc21c94c6992277d6d1364c28ddf7058cc8f')
sha256sums_armv7h=('72f2477de6e325bd91ed18edf8e4229bfa68ded2d6089d7b0202c3ea0a67d815'
                   '0799a140256072b350b56c1b2db5fc21c94c6992277d6d1364c28ddf7058cc8f')

package() {
    case "${CARCH}" in
        "x86_64")
            cd "${srcdir}/${_pkgname}_${pkgver}_linux_amd64/"
            ;;
        "aarch64")
            cd "${srcdir}/${_pkgname}_${pkgver}_linux_arm64/"
            ;;
        "armv7h")
            cd "${srcdir}/${_pkgname}_${pkgver}_linux_armv7/"
            ;;
    esac
    install -Dm755 "${_pkgname}" "${pkgdir}/usr/bin/${_pkgname}"
    install -Dm644 "client/${_pkgname}-client.service" "${pkgdir}/usr/lib/systemd/system/${_pkgname}-client.service"
    install -Dm644 "client/client.yml" "${pkgdir}/etc/ntfy/client.yml"
    install -Dm644 "server/${_pkgname}.service" "${pkgdir}/usr/lib/systemd/system/${_pkgname}.service"
    install -Dm644 "server/server.yml" "${pkgdir}/etc/ntfy/server.yml"
    install -Dm644 "README.md" "${pkgdir}/usr/share/doc/${pkgname}/README.md"
    install -Dm644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -Dm644 "../${_pkgname}.sysusers" "${pkgdir}/usr/lib/sysusers.d/${_pkgname}.conf"
}

