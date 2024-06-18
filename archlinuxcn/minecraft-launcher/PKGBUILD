# Maintainer: Phillip Schichtel <phillip@schich.tel>
# Contributor: László Várady <laszlo.varady93@gmail.com>
# Contributor: Petr Mrázek <petr@mojang.com>

pkgname=minecraft-launcher
pkgver=1.0.1221
pkgrel=3
epoch=1
pkgdesc="Official Minecraft Launcher"
arch=('x86_64')
url="https://mojang.com/"
license=('custom')
depends=('gtk3' 'gcc-libs' 'zlib' 'libgpg-error')
optdepends=('flite: narrator support'
            'org.freedesktop.secrets: persistent login support')
conflicts=('minecraft-launcher-beta')
provides=('minecraft-launcher-beta')
source=("https://launcher.mojang.com/download/linux/x86_64/minecraft-launcher_${pkgver}.tar.gz"
        "minecraft-launcher.desktop"
        "https://launcher.mojang.com/download/minecraft-launcher.svg")

sha256sums=('cd9f0b44fc9cec42829cb2e71145ee599f3d34c7715b55963514d0a8d36214ab'
            '431040831069a1ea867cb7c6f708e3c8f5788fb3d3e41d068f8afbef60cfafbd'
            '35c2bcaeb09fa4b8864e9422fd66bf60847706f8b4400ec4a66ba6436b101f71')

package() {
  install -Dm644 "minecraft-launcher.svg" "$pkgdir/usr/share/icons/hicolor/symbolic/apps/minecraft-launcher.svg"
  install -Dm644 "minecraft-launcher.desktop" "$pkgdir/usr/share/applications/minecraft-launcher.desktop"
  install -Dm755 "minecraft-launcher/minecraft-launcher" "$pkgdir/usr/bin/minecraft-launcher"
}
