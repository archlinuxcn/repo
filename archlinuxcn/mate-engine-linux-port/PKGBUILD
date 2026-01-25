# Maintainer: Yuzu <aur at vitayuzu dot day>
pkgname=mate-engine-linux-port
pkgver=2.2.5_8
pkgrel=2
pkgdesc="Unofficial Linux port of MateEngine - A free Desktop Mate alternative with custom VRM support"
arch=('x86_64')
url="https://github.com/Marksonthegamer/Mate-Engine-Linux-Port"
license=('LicenseRef-MateEngine-Pro-License')
depends=(
    'gtk3'
    'glib2' 
    'libx11' 
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
)
optdepends=('pipewire-pulse: for dancing feature with PipeWire')
_archive="MateEngineX_${pkgver}"
_srcdir="MateEngineX"
source=("${_archive}.tar.gz::${url}/releases/download/Public-Release-${pkgver}/${_archive}.tar.gz"
        "LICENSE::https://raw.githubusercontent.com/Marksonthegamer/Mate-Engine-Linux-Port/main/LICENSE"
        "mate-engine.desktop")
sha256sums=('19c774ea0ea8af7dbad9633d917ed2d93639a598e84c606e4676b3ae4445fad9'
            '305feaea992c5c1c4c666939e04fec751e04cf37bdfeb844358600900ea0acd8'
            'bf895f958f0f7f13b31426dbd79f79f42643b9e253c1a0bb1594996f4c6cd128')

package() {
    install -dm755 "${pkgdir}/opt/${pkgname}"
    cp -r "${srcdir}/${_srcdir}"/* "${pkgdir}/opt/${pkgname}/"

    install -dm755 "${pkgdir}/usr/bin"
    ln -s "/opt/${pkgname}/launch.sh" "${pkgdir}/usr/bin/mate-engine"

    chmod +x "${pkgdir}/opt/${pkgname}/launch.sh"
    chmod +x "${pkgdir}/opt/${pkgname}/MateEngineX.x86_64"

    install -Dm644 "${srcdir}/LICENSE" \
        "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

    install -Dm644 "${srcdir}/mate-engine.desktop" \
        "${pkgdir}/usr/share/applications/mate-engine.desktop"

    install -Dm644 "${pkgdir}/opt/${pkgname}/MateEngineX_Data/Resources/UnityPlayer.png" \
        "${pkgdir}/usr/share/pixmaps/MateEngineLinux.png"
}
