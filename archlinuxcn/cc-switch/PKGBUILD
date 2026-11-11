# Maintainer: Hu Butui <hot123tea123@gmail.com>

pkgname=cc-switch
pkgver=4.0.29
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
sha256sums=('51885f0e63e452ff61380934c468347e46982fcbe00e5f4d7b97a5cd013f82cd')

prepare() {
  export RUSTUP_TOOLCHAIN=stable
  cd "${pkgname}-${pkgver}"
  # openssl-sys <0.9.114 / openssl <0.10.78 don't support OpenSSL 4 (Arch core
  # is 4.1 now); bump the lock beyond the pinned versions. || true keeps the
  # build working if upstream drops these transitive deps in a future release.
  cargo update --manifest-path src-tauri/Cargo.toml -p openssl-sys --precise 0.9.118 || true
  cargo update --manifest-path src-tauri/Cargo.toml -p openssl --precise 0.10.82 || true
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
