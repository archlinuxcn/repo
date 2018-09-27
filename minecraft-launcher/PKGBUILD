# Maintainer: Petr Mrázek <petr@mojang.com>
# Maintainer: Adrien Jussak <jussak.adrien@gmail.com>
# Maintainer: Shoghi Cervantes <shoghi@mojang.com>
# Maintainer: Thomas Guimbretiere <profmobius@mojang.com>
pkgname=minecraft-launcher
pkgver=2.1.1431
pkgrel=1
pkgdesc="Official Minecraft Launcher"
arch=('x86_64')
url="https://mojang.com/"
license=('All rights reserved')
depends=('java-runtime=8' 'xorg-xrandr' 'libxss' 'alsa-lib' 'gtk2' 'gconf' 'libxtst' 'nss')
source=(
"Minecraft-$pkgver.tar.gz::https://launcher.mojang.com/download/Minecraft.tar.gz"
minecraft-launcher.desktop
minecraft-launcher.svg
)
sha256sums=(
'b0026863e8a7d41d328d831aa223fdb198a96a6bcf980969a7dc065ed29a4f06'
'e1029b0a36cef916c58262e6b41b75defd83327ec41e5b372f9861d663007857'
'35c2bcaeb09fa4b8864e9422fd66bf60847706f8b4400ec4a66ba6436b101f71'
)

build() {

  cd "$srcdir/$pkgname-$pkgver"

}

package () {

  cd "$pkgdir"

  mkdir -p "opt"
  mkdir -p "usr/bin"

  install -Dm644 "$srcdir/minecraft-launcher.svg"    "$pkgdir/usr/share/icons/hicolor/symbolic/apps/minecraft-launcher.svg"

   install -Dm644 "$srcdir/minecraft-launcher.desktop"    "$pkgdir/usr/share/applications/minecraft-launcher.desktop"

  cp -Rv "$srcdir/$pkgname-$pkgver" "$pkgdir/opt/$pkgname"
  ln -s "/opt/$pkgname/minecraft-launcher.sh" "$pkgdir/usr/bin/minecraft-launcher"

}
