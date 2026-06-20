# Maintainer: NourEddine Y.
# Contributor: Oskar Gerlciz Kowalczuk
# Contributor: StaticNullException <aurcontact@teto.party>

pkgname=zen-browser
pkgver=1.21.1b
pkgrel=3
pkgdesc='Firefox-based web browser built from upstream release source snapshot'
url='https://zen-browser.app'
arch=('x86_64')
license=('MPL-2.0')
depends=(
  alsa-lib
  at-spi2-core
  bash
  cairo
  dbus
  ffmpeg
  fontconfig
  freetype2
  gdk-pixbuf2
  glib2
  glibc
  gtk3
  hicolor-icon-theme
  libgcc
  libpulse
  libstdc++
  libx11
  libxcb
  libxcomposite
  libxdamage
  libxext
  libxfixes
  libxrandr
  libxss
  libxt
  mime-types
  nspr
  nss
  pango
  ttf-font
)
makedepends=(
  cbindgen
  clang
  diffutils
  imake
  jack
  lld
  llvm
  mesa
  nasm
  nodejs
  onnxruntime
  python
  rust
  unzip
  wasi-compiler-rt
  wasi-libc
  wasi-libc++
  wasi-libc++abi
  xorg-server-xvfb
  yasm
  zip
)
optdepends=(
  'libnotify: Notification integration'
  'networkmanager: Location detection via available WiFi networks'
  'onnxruntime: Local machine learning features such as smart tab groups'
  'speech-dispatcher: Text-to-Speech'
  'xdg-desktop-portal: Screensharing with Wayland'
)
conflicts=('zen-browser-bin')
options=(
  !emptydirs
  !lto
  !makeflags
)

_srcroot='zen-source'
# Keep versioned GitHub release URLs here. Do not switch this to /latest/ in an
# AUR package; use .nvchecker.toml or update-zen-browser-release.sh to refresh
# pkgver and checksums deterministically.
source=(
  "$_srcroot-$pkgver.tar.zst::https://github.com/zen-browser/desktop/releases/download/$pkgver/zen.source.tar.zst"
  "$pkgname.desktop"
  '0002-Patch-glsl-optimizer-to-build-with-glibc-2.43.patch'
  '0004-Use-wasm32-wasip1-target.patch'
  '0005-Fix-cbindgen-BudgetType_VALUES-COUNT-issue.patch'
)
sha256sums=('e218d89839fa601931939c48f3cd811a80dd053cb5e33ef659573873262106ab'
            'af16fec9a88cbfffee34a6a4eb5b3074931477fcefee252840d77cf146568851'
            'c7d6572fe1ac76f6adbfb10102f284fd55690396ac0a275a5cfea9a2efa22b58'
            '28b086f5492d8e6731fe0dfe34a2e4c6d4d502a9eefa15a31e44b5788cf4df89'
            '0a44b78d761a279786ba2801091fb75bffeb0d9ae93c41738d2f64464d40e4d3')
noextract=("$_srcroot-$pkgver.tar.zst")

prepare() {
  rm -rf "$srcdir/$_srcroot"
  mkdir -p "$srcdir/$_srcroot" "$srcdir/mozbuild"
  bsdtar -xf "$srcdir/$_srcroot-$pkgver.tar.zst" -C "$srcdir/$_srcroot"

  cd "$srcdir/$_srcroot"

  patch -Np1 -i "$srcdir/0002-Patch-glsl-optimizer-to-build-with-glibc-2.43.patch"
  patch -Np1 -i "$srcdir/0004-Use-wasm32-wasip1-target.patch"
  patch -Np1 -i "$srcdir/0005-Fix-cbindgen-BudgetType_VALUES-COUNT-issue.patch"

  cat >"$srcdir/mozconfig" <<EOF
ac_add_options --enable-application=browser
mk_add_options MOZ_OBJDIR=${PWD@Q}/obj

ac_add_options --prefix=/usr
ac_add_options --enable-release
ac_add_options --enable-hardening
ac_add_options --enable-optimize
# encoding_rs simd-accel opts out of Rust's stable compatibility story and
# has started breaking with newer stable compilers in release snapshots.
ac_add_options --enable-linker=lld
ac_add_options --disable-install-strip
ac_add_options --disable-bootstrap
ac_add_options --with-wasi-sysroot=/usr/share/wasi-sysroot

# Branding
ac_add_options --enable-official-branding
ac_add_options --enable-update-channel=release
ac_add_options --with-distribution-id=org.archlinux
ac_add_options --with-unsigned-addon-scopes=app,system
ac_add_options --allow-addon-sideload
export MOZILLA_OFFICIAL=1
export MOZ_APP_REMOTINGNAME=zen-browser

# System libraries
ac_add_options --with-system-nspr
ac_add_options --with-system-nss

# Features
ac_add_options --enable-alsa
ac_add_options --enable-jack
ac_add_options --enable-crashreporter
ac_add_options --disable-updater
ac_add_options --disable-tests
EOF
}

build() {
  cd "$srcdir/$_srcroot"

  export MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE=pip
  export MOZBUILD_STATE_PATH="$srcdir/mozbuild"
  export MOZ_BUILD_DATE="$(date -u${SOURCE_DATE_EPOCH:+d @$SOURCE_DATE_EPOCH} +%Y%m%d%H%M%S)"
  export MOZ_NOSPAM=1

  CFLAGS="${CFLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"
  CXXFLAGS="${CXXFLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"
  CFLAGS="${CFLAGS/-fexceptions/}"
  CXXFLAGS="${CXXFLAGS/-fexceptions/}"

  ulimit -n 4096

  echo 'Building instrumented browser...'
  cat >.mozconfig "$srcdir/mozconfig" - <<'EOF'
ac_add_options --enable-profile-generate=cross
EOF
  ./mach build --priority normal

  echo 'Profiling instrumented browser...'
  ./mach package
  LLVM_PROFDATA=llvm-profdata JARLOG_FILE="$PWD/jarlog" \
    dbus-run-session \
    xvfb-run -s '-screen 0 1920x1080x24 -nolisten local' \
    ./mach python build/pgo/profileserver.py

  test -s merged.profdata
  test -s jarlog

  echo 'Removing instrumented browser...'
  ./mach clobber objdir

  echo 'Building optimized browser...'
  cat >.mozconfig "$srcdir/mozconfig" - <<EOF
ac_add_options --enable-lto=cross,full
ac_add_options --enable-profile-use=cross
ac_add_options --with-pgo-profile-path=${PWD@Q}/merged.profdata
ac_add_options --with-pgo-jarlog=${PWD@Q}/jarlog
EOF
  ./mach build --priority normal
}

package() {
  cd "$srcdir/$_srcroot"

  DESTDIR="$pkgdir" ./mach install

  local _launcher='zen-browser'
  local _appdir="$pkgdir/usr/lib/$_launcher"
  local _size

  if [[ -d "$pkgdir/usr/lib/firefox" && ! -d "$_appdir" ]]; then
    mv "$pkgdir/usr/lib/firefox" "$_appdir"
    ln -sf firefox "$_appdir/zen"
  fi

  install -Dm755 /dev/stdin "$pkgdir/usr/bin/$_launcher" <<'EOF'
#!/bin/sh
exec /usr/lib/zen-browser/zen "$@"
EOF
  ln -s "$_launcher" "$pkgdir/usr/bin/zen"

  ln -srv "$pkgdir/usr/lib/libonnxruntime.so" -t "$_appdir"

  install -Dm644 "$srcdir/$pkgname.desktop" \
    "$pkgdir/usr/share/applications/$pkgname.desktop"

  for _size in 16 32 48 64 128; do
    install -Dm644 \
      "$_appdir/browser/chrome/icons/default/default${_size}.png" \
      "$pkgdir/usr/share/icons/hicolor/${_size}x${_size}/apps/$_launcher.png"
  done

  install -Dm644 /dev/stdin \
    "$_appdir/browser/defaults/preferences/vendor.js" <<'EOF'
// Use LANG environment variable to choose locale.
pref("intl.locale.requested", "");

// Use system-provided dictionaries.
pref("spellchecker.dictionary_path", "/usr/share/hunspell");

// Avoid first-run default browser noise on managed systems.
pref("browser.shell.checkDefaultBrowser", false);

// Don't disable extensions shipped in application directories.
pref("extensions.autoDisableScopes", 11);
EOF

  install -Dm644 /dev/stdin "$_appdir/distribution/distribution.ini" <<EOF
[Global]
id=archlinux
version=1.0
about=Zen Browser for Arch Linux

[Preferences]
app.distributor=archlinux
app.distributor.channel=$_launcher
app.partner.archlinux=archlinux
EOF

  install -Dm644 /dev/stdin "$_appdir/distribution/policies.json" <<'EOF'
{
  "policies": {
    "DisableAppUpdate": true
  }
}
EOF

  rm -f \
    "$_appdir/updater" \
    "$_appdir/updater.ini" \
    "$_appdir/update-settings.ini"

  if [[ -e "$_appdir/libnssckbi.so" ]]; then
    ln -sf ../libnssckbi.so "$_appdir/libnssckbi.so"
  fi
}
