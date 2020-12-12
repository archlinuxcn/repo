# Maintainer: Yurii Kolesnykov <root@yurikoles.com>
# Previous maintainer: Christophe Robin <crobin@nekoo.com>

pkgname=minecraft
_pkgname=minecraft-launcher
pkgver=2.2.909
pkgrel=1
pkgdesc="Minecraft Launcher"
arch=(any)
license=('custom')
url="https://www.minecraft.net/"
depends=('java-runtime' 'xorg-xrandr' 'libxss' 'libx11' 'libxcb' 'alsa-lib' 'gtk2' 'gtk3' 'libxtst' 'nss')
optdepends=('flite: narrator support')
conflicts=("$_pkgname" "$_pkgname-beta")
provides=("$_pkgname" "$_pkgname-beta")
source=("minecraft-${pkgver}.deb::https://launcher.mojang.com/download/Minecraft.deb")
sha256sums=('3d50346470c64b32efe79c6026a63b5e9c64ba1806be66d79b8f7e6625271ca9')

prepare() {
    tar xpf data.tar.xz
}

package() {
    install -d "${pkgdir}/opt/$_pkgname"
    cp -a "${srcdir}/opt/${_pkgname}/"* "${pkgdir}/opt/${_pkgname}/"

    install -Dm644 "${srcdir}/usr/share/applications/${_pkgname}.desktop" \
        "${pkgdir}/usr/share/applications/${_pkgname}.desktop"

    install -Dm644 "${srcdir}/usr/share/icons/hicolor/symbolic/apps/${_pkgname}.svg" \
        "${pkgdir}/usr/share/icons/hicolor/symbolic/apps/${_pkgname}.svg"

    install -d "${pkgdir}/usr/bin"
    ln -s "/opt/${_pkgname}/${_pkgname}" "${pkgdir}/usr/bin/"
}
