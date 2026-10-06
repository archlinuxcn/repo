# Maintainer: Hu Butui <hot123tea123@gmail.com>

pkgname=cc-switch
pkgver=4.0.3
pkgrel=1
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
  'libayatana-appindicator-glib'
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
)
sha256sums=('4ff8c3dfeb53339bd86e30b7ac7e8424d0384adc46f0f4e8e88f6b1931d843bb')

prepare() {
  export RUSTUP_TOOLCHAIN=stable
  cd "${pkgname}-${pkgver}"
  cargo fetch --locked --target host-tuple --manifest-path src-tauri/Cargo.toml
}

build() {
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR="${srcdir}/target"
  # fix for static link
  unset CFLAGS CXXFLAGS LDFLAGS
  cd "${pkgname}-${pkgver}"
  pnpm install --frozen-lockfile --ignore-scripts
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
