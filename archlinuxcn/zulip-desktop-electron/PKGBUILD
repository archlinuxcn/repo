# Maintainer: poscat
# Contributor: Martin Reboredo <yakoyoku@gmail.com>
# Contributor: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: aspen <aspen@aspenuwu.me>
pkgname=zulip-desktop-electron
pkgver=5.12.0
pkgrel=2
_electronversion=34
pkgdesc="Real-time team chat based on the email threading model"
arch=('x86_64')
url="https://zulip.com"
license=('Apache')
depends=("electron$_electronversion" 'libxkbfile' 'libxss')
makedepends=('nodejs>=12.10.0' 'npm')
provides=("${pkgname%-*}")
conflicts=("${pkgname%-*}")
source=(
  "${pkgname%-*}-$pkgver.tar.gz::https://github.com/zulip/zulip-desktop/archive/v$pkgver.tar.gz"
  "Zulip.desktop"
  "${pkgname%-*}.sh.in")
sha256sums=(
  '65deb781e00e2857ad459ea98574c569e15a0fd7c3c41d6dc11ed4e7c5b12666'
  '8f3440dc9195c6763de16f8b13409a5c130bdf417015e7e27bb64fdb227f4f10'
  '70ed0f08158c6ea8ef99dbbe360861e2c63911c2fadc74c0154bd6567abc8979')

build() {
  cd "${pkgname%-*}-$pkgver"
  electronDist="/usr/lib/electron$_electronversion"
  electronVer="$(sed s/^v// $electronDist/version)"
  export ELECTRON_SKIP_BINARY_DOWNLOAD=1
  HOME="$srcdir/.electron-gyp" npm install --cache "$srcdir/npm-cache"
  npm run pack -- --linux --x64 \
    -c.electronDist=$electronDist -c.electronVersion=$electronVer
}

package() {
  cd "${pkgname%-*}-$pkgver"
  sed "s/@@VERSION@@/$_electronversion/" "$srcdir/${pkgname%-*}.sh.in" >"${pkgname%-*}.sh"
  install -Dm644 dist/linux-unpacked/resources/app.asar -t "$pkgdir/usr/lib/${pkgname%-*}/resources/"
  install -Dm755 "${pkgname%-*}.sh" "$pkgdir/usr/bin/zulip"
  install -Dm644 "$srcdir/Zulip.desktop" -t "$pkgdir/usr/share/applications/"

  install -Dm644 build/icon-macos.png \
    "$pkgdir/usr/share/icons/hicolor/512x512/apps/zulip.png"
  install -Dm644 build/icon-macos.svg \
    "$pkgdir/usr/share/icons/hicolor/scalable/apps/zulip.svg"
}
