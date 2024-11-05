# Maintainer: zt <zt@zt64.dev>
# Maintainer: cookie <kyliepc@proton.me>
_pkgname=Vesktop
pkgname=vesktop
pkgdesc="A standalone Electron-based Discord app with Vencord & improved Linux support"
pkgver=1.5.3
pkgrel=4

arch=("x86_64" "aarch64")
url="https://github.com/Vencord/Vesktop"
license=('GPL-3.0-only')

depends=('alsa-lib' 'gtk3' 'nss')
makedepends=('nodejs>=18')
optdepends=(
  'libnotify: Notifications'
  'xdg-utils: Open links, files, etc'
)

provides=("vesktop")
conflicts=('vesktop-electron')

source=("$_pkgname-$pkgver.tar.gz::https://github.com/Vencord/Vesktop/archive/v${pkgver}.tar.gz" "vesktop.desktop" "vesktop.sh" "afterPack.js")

sha256sums=('615ed9275a03974a0c6486c0095cfcd0af246363a4f62ec0bdc985c763cc6334'
            'c7845033716d7fdec2ea1daf8c3575b504bc6a5c19c702e3722a0e6237ae571f'
            '4a790359a465979dbf3b5d815ed0d5f3f8a381a5ae08e1b359cee40dbd81d2ad'
            '122b17ce996318e533e6f2ab1c9b2961b39c3eba271c9b40f10c0da5dd738baa')

build() {
  cd "$srcdir/$_pkgname-$pkgver"

  # Add unpacked icon extraction script
  sed -i '/"beforePack": "scripts\/build\/sandboxFix.js",/a\ \ \ \ \ \ \ \ "afterPack": "'$srcdir'/afterPack.js",' package.json

  corepack pnpm i
  corepack pnpm build
  corepack pnpx electron-builder --dir
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"

  # Create necessary directories
  install -d "$pkgdir/usr/lib/$pkgname"
  install -d "$pkgdir/usr/bin"

  cp -R "dist/linux-unpacked/." "$pkgdir/usr/lib/$pkgname"

  install -Dm644 "../vesktop.desktop" "$pkgdir/usr/share/applications/vesktop.desktop" # Install desktop entry
  install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE" # Install license
  for _icons in 1024 512 256 128 64 48 32 16; do
    install -Dm644 "dist/.icon-set/icon_${_icons}.png" "$pkgdir/usr/share/icons/hicolor/${_icons}x${_icons}/apps/$pkgname.png"
  done # Install icons

  install -Dm755 "../vesktop.sh" "$pkgdir/usr/bin/$pkgname" # Start script
}
