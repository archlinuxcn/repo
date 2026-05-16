# Maintainer: Hu Butui <hot123tea123@gmail.com>

pkgname=cc-switch
pkgver=3.15.0
pkgrel=2
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
sha256sums=('fc5fa3941dff278d61dd2e48c5c005508fb31beedc506e37a9306be024ef651b'
            '9686d576fd9dd596edf805507e0f8752abd3fa8a6ca85664afcd1582188b04e7'
            '333ef252456975051f0163c9b8bcf37fadec3a43bc05f192cb4ec87b2761b3f6')

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
