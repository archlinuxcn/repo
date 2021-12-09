# Maintainer: lilydjwg <lilydjwg@gmail.com>
pkgname=multimc-bin
pkgver=0.6.14
pkgrel=1
pkgdesc="a custom launcher for Minecraft that allows you to easily manage multiple installations of Minecraft at once"
arch=('x86_64')
url="https://multimc.org/"
license=('Apache')
depends=('zlib' 'qt5-base' 'java-runtime')
conflicts=('multimc' 'multimc5' 'multimc5-git')
provides=('multimc' 'multimc5' 'multimc5-git')
source=("$pkgname-$pkgver.tar.gz::https://files.multimc.org/downloads/mmc-stable-lin64.tar.gz"
        multimc.desktop
        icon.svg # from upstream deb file
        multimc.sh)
sha256sums=('b99051b70903c7229877c9c2bc2ccaf1c20bb2510a5e4082d0113331bd321023'
            'a4d277f1e34f411301f4a2a32a8d35edfc57b8d43e728e930f1fa204e3dd8a20'
            'a78ab75d753c20e998992723f96814351dce0817d7dbf6ceb88bb1d4f1f51bd6'
            '776449fd26926f076cb42b925cec7708e295790981762a9a547c61c52e72bb71')

package() {
  mkdir -p "$pkgdir/opt"
  mkdir -p "$pkgdir/usr/bin"

  cp -R "$srcdir/MultiMC/bin" "$pkgdir/opt/multimc"

  install -Dm644 "$srcdir/multimc.desktop" "$pkgdir/usr/share/applications/multimc.desktop"
  install -Dm644 "$srcdir/icon.svg" "$pkgdir/usr/share/icons/hicolor/scalable/apps/multimc.svg"
  install -Dm755 "$srcdir/multimc.sh" "$pkgdir/usr/bin/multimc"
}
