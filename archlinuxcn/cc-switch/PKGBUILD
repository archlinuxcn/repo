# Maintainer: Hu Butui <hot123tea123@gmail.com>

pkgname=cc-switch
pkgver=3.14.1
pkgrel=7
pkgdesc='All-in-One assistant tool for Claude Code, Codex, OpenCode, openclaw & Gemini CLI'
arch=('x86_64')
url='https://github.com/farion1231/cc-switch'
license=('MIT')
depends=(
  'cairo'
  'gdk-pixbuf2'
  'glib2'
  'gtk3'
  'hicolor-icon-theme'
  'libayatana-appindicator'
  'libsoup3'
  'openssl'
  'pango'
  'webkit2gtk-4.1'
)
makedepends=(
  'cargo-tauri'
  'nodejs'
  'pnpm'
  'rust'
  'xdg-utils'
)
source=(
  "${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
  "0001-feat-universal-provider-Auto-sync-after-adding.patch"
  "0002-feat-universal-provider-Add-one-click-sync-all-providers.patch"
)
sha256sums=('e06791b370b5c8782d3ed46a4d3137ac6beb82b55318ceba609bc82f73a5c30d'
            'b62e6c6c077ce39b3b23274302215ff7714501ef0056ca1c9522b7dd6ff51bb2'
            '252cea0ad0e11f93a2d1b963a1be9a95ebe8704c9dbffe3c8c07c749db2e9b5d')

prepare() {
  export RUSTUP_TOOLCHAIN=stable
  cd "${pkgname}-${pkgver}"
  patch -p1 -i "${srcdir}/0001-feat-universal-provider-Auto-sync-after-adding.patch"
  patch -p1 -i "${srcdir}/0002-feat-universal-provider-Add-one-click-sync-all-providers.patch"
  cargo fetch --locked --target host-tuple --manifest-path src-tauri/Cargo.toml
}

build() {
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR="${srcdir}/target"
  # fix for static link
  unset CFLAGS CXXFLAGS LDFLAGS
  cd "${pkgname}-${pkgver}"
  pnpm install --frozen-lockfile
  pnpm tauri build --no-bundle
}

package() {
  install -Dm755 "${srcdir}/target/release/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  cd "${pkgname}-${pkgver}"
  install -Dm644 src-tauri/icons/128x128.png "${pkgdir}/usr/share/icons/hicolor/128x128/apps/com.ccswitch.desktop.png"
  install -Dm644 src-tauri/icons/128x128@2x.png "${pkgdir}/usr/share/icons/hicolor/256x256@2/apps/com.ccswitch.desktop.png"
  install -Dm644 src-tauri/icons/32x32.png "${pkgdir}/usr/share/icons/hicolor/32x32/apps/com.ccswitch.desktop.png"
  install -Dm644 flatpak/com.ccswitch.desktop.desktop "${pkgdir}/usr/share/applications/com.ccswitch.desktop.desktop"
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
# vim:set ts=2 sw=2 et:
