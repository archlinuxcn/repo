# Maintainer: Ian MacKay <immackay0@gmail.com>

_pkgname='github-desktop'
pkgname="${_pkgname}-bin"
pkgver=2.6.1
_pkgver="${pkgver}-linux2"
gitname="release-${_pkgver}"
pkgrel=2
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
    a43c188f8fd326499b5c1d4099239f658ebac8e9a21001481407cccafcd5f208
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
