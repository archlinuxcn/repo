# Maintainer: ml <>
# Contributor: sum01 <sum01@protonmail.com>
pkgname=rocketchat-desktop
pkgver=3.1.1
_pkgname="Rocket.Chat.Electron-${pkgver}"
pkgrel=1
pkgdesc='Rocket.Chat Native Cross-Platform Desktop Application via Electron.'
arch=('i686' 'x86_64')
url='https://github.com/RocketChat/Rocket.Chat.Electron'
license=('MIT')
depends=('electron')
makedepends=('nodejs' 'node-gyp' 'python' 'yarn')
conflicts=('rocketchat-client-bin')
install=rocketchat-desktop.install
source=("${url}/archive/${pkgver}/${pkgname}-${pkgver}.tar.gz"
        rocketchat-desktop
        rocketchat-desktop.desktop)
sha256sums=('ba0f4ebee4119987ab45a304b9ee3bfc8ce14159dd9cd3dca095020e1eae8a3e'
            '18fab390ffce4f89a17d5d71a7e78fea9afa9f9d2bcdafecb4f310d4f804996f'
            '31fae4f98a61a774f84030fd43d2ef92c7633740dc5aa55967a21d0e29ea621a')

prepare() {
  cd "$_pkgname"
  yarn upgrade electron@"$(</usr/lib/electron/version)"
}

build() {
  cd "$_pkgname"
  local i686=ia32 x86_64=x64
  export NODE_ENV=production
  yarn build
  yarn run electron-builder --linux --"${!CARCH}" --dir \
    -c.electronDist=/usr/lib/electron \
    -c.electronVersion="$(</usr/lib/electron/version)"
}

package() {
  local i686=linux-ia32-unpacked x86_64=linux-unpacked
  install -Dm644 -t "${pkgdir}/usr/share/applications" "${pkgname}.desktop"
  install -Dm755 -t "${pkgdir}/usr/bin" "$pkgname"

  cd "$_pkgname"
  install -Dm644 "build/icons/512x512.png" "$pkgdir/usr/share/icons/hicolor/512x512/apps/$pkgname.png"
  install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE
  install -Dm644 "dist/${!CARCH}/resources/app.asar" "${pkgdir}/usr/lib/${pkgname}.asar"
}
