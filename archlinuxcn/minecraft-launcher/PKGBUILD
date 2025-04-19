# Maintainer: Phillip Schichtel <phillip@schich.tel>
# Contributor: László Várady <laszlo.varady93@gmail.com>
# Contributor: Petr Mrázek <petr@mojang.com>

pkgname=minecraft-launcher
pkgver=2.1.3
pkgrel=3
epoch=1
pkgdesc="Official Minecraft Launcher"
arch=('x86_64')
url="https://mojang.com/"
license=('custom')
depends=('gtk3' 'gcc-libs' 'zlib' 'libgpg-error')
optdepends=('flite: narrator support'
            'org.freedesktop.secrets: persistent login support'
            'orca: screen reader support')
conflicts=('minecraft-launcher-beta')
provides=('minecraft-launcher-beta')
source=("https://launcher.mojang.com/download/Minecraft.tar.gz"
        "https://launcher.mojang.com/download/minecraft-launcher.svg"
        "minecraft-launcher.sh"
        "minecraft-launcher.desktop")

sha256sums=('695269281547bbbcf47fe74633027a0e4ddc13a61060c686a7217e85d314e45e'
            '35c2bcaeb09fa4b8864e9422fd66bf60847706f8b4400ec4a66ba6436b101f71'
            '83a89378cd17c1bbee173d12d14c13edae1b29770ee8411a534c5a547c164d4b'
            '09006f33be0d4540dfb1838db00ec6c5d3a542e8c8c58c8374f4f85479222e3f')

package() {
  install -Dm755 "minecraft-launcher.sh" "$pkgdir/usr/bin/minecraft-launcher.sh"
  install -Dm644 "minecraft-launcher.svg" "$pkgdir/usr/share/icons/hicolor/symbolic/apps/minecraft-launcher.svg"
  install -Dm644 "minecraft-launcher.desktop" "$pkgdir/usr/share/applications/minecraft-launcher.desktop"
  install -Dm755 "minecraft-launcher/minecraft-launcher" "$pkgdir/usr/bin/minecraft-launcher"
}
