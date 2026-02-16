# Maintainer: Yuzu <aur at vitayuzu dot day>
pkgname=mateengine
pkgver=3.2.0_2
pkgrel=2
pkgdesc="Unofficial Linux port of MateEngine - A free Desktop Mate alternative with custom VRM support"
arch=('x86_64')
url="https://github.com/Marksonthegamer/Mate-Engine-Linux-Port"
license=('LicenseRef-MateEngine-Pro-License')
replaces=('mate-engine-linux-port')
depends=(
    'gtk3'
    'glib2' 
    'libx11' 
    'libxcursor'
    'libxext' 
    'libxrender'
    'libxdamage' 
    'libayatana-appindicator'
    'libayatana-appindicator'
    'libdecor'
    'vulkan-icd-loader'
    'libpulse'
    'pango'
    'cargo'
    'wayland'
    'bash'
    'glibc'
    'gcc-libs'
    'zlib'
    'dbus'
    'glxinfo'
)
optdepends=('pipewire-pulse: for dancing feature with PipeWire'
            'xdpyinfo: for transparent background if glxinfo does not works')
_archive="MateEngineX_${pkgver}"
_srcdir="MateEngineX"
source=("${_archive}.tar.gz::${url}/releases/download/Public-Release-X${pkgver}/${_archive}.tar.gz"
        "LICENSE::https://raw.githubusercontent.com/Marksonthegamer/Mate-Engine-Linux-Port/main/LICENSE"
        "mateengine.desktop")
sha256sums=('2a07e6a2dc8fe6b06b29afc3eb705906579bc570b2a3b38081e0eee23fc45280'
            '305feaea992c5c1c4c666939e04fec751e04cf37bdfeb844358600900ea0acd8'
            '063cf3a5c67b290ff7fcc99443a8b67f573331be0fad9f1ba4d80a053506d023')

package() {
    install -dm755 "${pkgdir}/opt/${pkgname}"
    cp -r "${srcdir}/${_srcdir}"/* "${pkgdir}/opt/${pkgname}/"

    install -dm755 "${pkgdir}/usr/bin"
    ln -s "/opt/${pkgname}/launch.sh" "${pkgdir}/usr/bin/${pkgname}"

    chmod +x "${pkgdir}/opt/${pkgname}/launch.sh"
    chmod +x "${pkgdir}/opt/${pkgname}/MateEngineX.x86_64"

    install -Dm644 "${srcdir}/LICENSE" \
        "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

    install -Dm644 "${srcdir}/${pkgname}.desktop" \
        "${pkgdir}/usr/share/applications/${pkgname}.desktop"

    install -Dm644 "${pkgdir}/opt/${pkgname}/MateEngineX_Data/Resources/UnityPlayer.png" \
        "${pkgdir}/usr/share/pixmaps/${pkgname}.png"
}
