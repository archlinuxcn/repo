# Maintainer: Ian MacKay <immackay0@gmail.com>

_pkgname='github-desktop'
pkgname="${_pkgname}-bin"
pkgver=2.7.1
_pkgver="${pkgver}-linux1"
gitname="release-${_pkgver}"
pkgrel=1
pkgdesc="GUI for managing Git and GitHub."
arch=('x86_64')
url="https://desktop.github.com"
license=('MIT')
depends=('gnome-keyring' 'libsecret' 'git' 'curl' 'libxss' 'gconf' 'nss' 'nspr' 'unzip')
optdepends=('hub: CLI interface for GitHub.')
provides=(${_pkgname})
conflicts=(${_pkgname})
source=(
    https://github.com/shiftkey/desktop/releases/download/${gitname}/GitHubDesktop-linux-${_pkgver}.deb
    ${_pkgname}.desktop
)
sha256sums=(
    84dae08a6bc7d0035dc0029e3ad2299eed2c50ea94974c1944ee1ac4f98a8920
    932e4c456e8c6db03d27172cf0daa37806bf025bb560d8b3d758c0997d1a618c
)
package() {
    tar xf data.tar.xz -C "${pkgdir}"
    install -d "${pkgdir}/opt/${_pkgname}"
    mv "${pkgdir}/usr/lib/github-desktop" "${pkgdir}/opt/"
    rm "${pkgdir}/usr/share/applications/github-desktop.desktop"
    install -Dm644 "${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
    printf "#!/bin/sh\n\n/opt/${_pkgname}/github-desktop \"\$@\"\n" | install -Dm755 /dev/stdin "${pkgdir}/usr/bin/${_pkgname}"
}
