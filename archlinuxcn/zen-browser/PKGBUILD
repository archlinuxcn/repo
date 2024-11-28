# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgbase=zen-browser
pkgname=()
pkgver=1.0.1_a.21
_zen_version=${pkgver//_/-}
_firefox_version=133.0
pkgrel=1
pkgdesc='Experience tranquillity while browsing the web without people tracking you'
url='https://zen-browser.app/'
arch=('x86_64')
license=(MPL-2.0)
depends=(alsa-lib
         at-spi2-core
         bash
         cairo
         dbus
         ffmpeg
         fontconfig
         freetype2
         gcc-libs
         gdk-pixbuf2
         glib2
         glibc
         gtk3
         hicolor-icon-theme
         libpulse
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
         ttf-font)
makedepends=(git
             pnpm
             rsync
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
             python
             rust
             unzip
             wasi-compiler-rt
             wasi-libc
             wasi-libc++
             wasi-libc++abi
             xorg-server-xvfb
             yasm
             zip)
optdepends=('hunspell-en_US: Spell checking, American English'
            'libnotify: Notification integration'
            'networkmanager: Location detection via available WiFi networks'
            'speech-dispatcher: Text-to-Speech'
            'xdg-desktop-portal: Screensharing with Wayland')
options=(!emptydirs
         !lto
         !makeflags
         !debug)

_repo='https://github.com/zen-browser/desktop'
source=("git+$_repo.git#tag=$_zen_version"
        "git+https://github.com/mozilla-l10n/firefox-l10n"
        "https://archive.mozilla.org/pub/firefox/releases/${_firefox_version}/source/firefox-${_firefox_version}.source.tar.xz"
        desktop.patch
        download-language-packs.patch
        do-not-auto-disable-extensions-in-system-directories.patch)
sha256sums=('14582f3323e4a687c257a47ee4d208c0566a22dfa1665d62ff44e8704629fba6'
            'SKIP'
            '492b2c9a3b6d215e38ce490624e8b2b9473419accdeaddb24ba00bc6adc3cc60'
            'fb8a1373a1e9f1b8b1443f75368b647f370735e5b95da82bab106000ef71fa76'
            'f2a917dea2c5cbd702da69c0c8648047f2f28ae77c5807350f4cb4d2dd5fe4fb'
            '8c1dec4e17516ecc737cb4fd37a215a59a4a3dea49770290125973038d987e01')
noextract=("firefox-${_firefox_version}.source.tar.xz")

_zen_variant=(generic specific)
_languages=(zh-CN zh-TW ja)

for _variant in "${_zen_variant[@]}"; do
  _pkgname=$pkgbase-$_variant
  pkgname+=("$_pkgname")
  
  _pkgdesc="$pkgdesc"
  if test "$_variant" = "specific"; then
    _pkgdesc="${pkgdesc} (optimized for modern devices)"
  fi

  eval "package_$_pkgname() {
  provides=('$pkgbase=$pkgver')
  conflicts=('$pkgbase')
  pkgdesc='$_pkgdesc'

  _package_zen '$_variant'
}"
done

for _lang in "${_languages[@]}"; do
  _pkgname=$pkgbase-i18n-${_lang,,}
  pkgname+=("$_pkgname")

  eval "package_$_pkgname() {
  arch=(any)
  depends=('$pkgbase>=$pkgver')
  optdepends=()
  pkgdesc='Language pack for Zen Browser ($_lang)'

  _package_i18n '$_lang'
}"
done


# Google API keys (see http://www.chromium.org/developers/how-tos/api-keys)
# Note: These are for Arch Linux use ONLY. For your own distribution, please
# get your own set of keys. Feel free to contact foutrelis@archlinux.org for
# more information.
_google_api_key=AIzaSyDwr302FpOSkGRpLlUpPThNTDPbXcIn_FM

_OBJ_DIR=obj
prepare() {
  cd desktop

  msg2 "init repo submodules"
  git submodule update --init --recursive --depth 1

  # Apply patches
  msg2 "apply patches"
  git apply -3 "$srcdir"/*.patch
  # use the --enable-jack option to keep in sync with the official repository of Firefox
  sed -i 's/--enable-pulseaudio/--enable-jack/g' "$srcdir"/desktop/configs/linux/mozconfig

  msg2 "prepare dependencies"
  pnpm config set store-dir "$srcdir"/pnpm-store
  pnpm --silent install --frozen-lockfile

  msg2 "prepare surfer build environment"
  pnpm surfer ci --brand alpha --display-version "$_zen_version"
  # setup Firefox source
  install -Dvm644 "$srcdir/firefox-${_firefox_version}.source.tar.xz" -t "./.surfer/engine"
  pnpm surfer download > /dev/null
  # Import patches into the firefox
  pnpm surfer import > /dev/null

  msg2 "prepare firefox l10n"
  rm -rf "$srcdir/desktop/l10n/firefox-l10n"
  cp -r "$srcdir/firefox-l10n" "$srcdir/desktop/l10n/"
  sh scripts/download-language-packs.sh > /dev/null

  msg2 "prepare custom mozconfig"
  echo -n "$_google_api_key" >google-api-key
  cat > mozconfig <<END
# # sccache
# mk_add_options 'export RUSTC_WRAPPER=sccache'
# mk_add_options 'export CCACHE_CPP2=yes'
# ac_add_options --with-ccache=sccache

# ac_add_options --enable-application=browser
# Incompatible with surfer, disable this configuration
mk_add_options MOZ_OBJDIR=${srcdir}/$_OBJ_DIR

ac_add_options --prefix=/usr
# ac_add_options --enable-release
# ac_add_options --enable-hardening
# ac_add_options --enable-optimize
# ac_add_options --enable-rust-simd
# ac_add_options --enable-linker=lld
# ac_add_options --disable-install-strip
# ac_add_options --disable-elf-hack
# It seems to be overwritten by surfer internal mozconfg, let's keep it for now
ac_add_options --disable-bootstrap
ac_add_options --with-wasi-sysroot=/usr/share/wasi-sysroot

# Branding
# ac_add_options --enable-official-branding
# ac_add_options --enable-update-channel=release
# ac_add_options --with-distribution-id=org.archlinux
# ac_add_options --with-unsigned-addon-scopes=app,system
ac_add_options --allow-addon-sideload
# export MOZILLA_OFFICIAL=1
export MOZ_APP_REMOTINGNAME=$pkgbase

# Keys
ac_add_options --with-google-location-service-api-keyfile=${PWD@Q}/google-api-key
ac_add_options --with-google-safebrowsing-api-keyfile=${PWD@Q}/google-api-key

# System libraries
ac_add_options --with-system-nspr
ac_add_options --with-system-nss

# Features
# ac_add_options --enable-alsa
# ac_add_options --enable-jack
# ac_add_options --enable-crashreporter
ac_add_options --disable-updater
# ac_add_options --disable-tests
END
}

_mach() {
  "$srcdir/desktop/engine/mach" "$@" > /dev/null
}

_build() {
  export MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE=pip
  export MOZBUILD_STATE_PATH="$srcdir/mozbuild"
  MOZ_BUILD_DATE="$(date -u${SOURCE_DATE_EPOCH:+d @$SOURCE_DATE_EPOCH} +%Y%m%d%H%M%S)"
  export MOZ_BUILD_DATE
  # export MOZ_BUILD_PRIORITY=normal
  export MOZ_NOSPAM=1

  # malloc_usable_size is used in various parts of the codebase
  CFLAGS="${CFLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"
  CXXFLAGS="${CXXFLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"

  # Breaks compilation since https://bugzilla.mozilla.org/show_bug.cgi?id=1896066
  CFLAGS="${CFLAGS/-fexceptions/}"
  CXXFLAGS="${CXXFLAGS/-fexceptions/}"

  # LTO needs more open files
  ulimit -n 4096

  local _variant=$1
  if test "$_variant" = "generic"; then
    export SURFER_COMPAT=true
  else
    export SURFER_COMPAT=false
  fi

  # Run PGO Build
  msg2 "build zen browser: $_variant"
  (
    cd "$srcdir/desktop"
    ZEN_RELEASE=1 LLVM_PROFDATA=llvm-profdata \
      dbus-run-session \
        xvfb-run -s "-screen 0 1920x1080x24 -nolisten local" \
          pnpm surfer build --skip-patch-check
  )

  # Build langpacks
  if test "$_variant" = "${_zen_variant[0]}"; then
    msg2 "build langpacks: ${_languages[*]}"
    echo $_firefox_version > "$srcdir/desktop/engine/browser/config/version.txt"
    for _lang in "${_languages[@]}"; do
      _mach build "merge-$_lang"
      _mach build "langpack-$_lang"
    done
  fi
}

_package_zen() {
  _build "$1"

  # package variant
  msg2 "install to pkgdir"
  DESTDIR="$pkgdir" _mach install

  local _appdir="$pkgdir/usr/lib/$pkgbase"

  msg2 "zen -> $pkgbase"
  rm -rf "$_appdir"
  mv "$pkgdir"/usr/lib/zen "$_appdir"

  # Replace duplicate binary
  # https://bugzilla.mozilla.org/show_bug.cgi?id=658850
  msg2 "replace duplicate zen binary"
  ln -srvf "$_appdir"/zen "$_appdir/zen-bin"
  ln -srvf "$_appdir"/zen "$pkgdir"/usr/bin/zen

  msg2 "install distribution config files from Zen Browser"
  install -Dvm644 "$srcdir"/desktop/AppDir/distribution/*.json -t "$_appdir/distribution"

  msg2 "install vendor.js"
  local _vendorjs="$_appdir/browser/defaults/preferences/vendor.js"
  install -Dvm644 /dev/stdin "$_vendorjs" <<END
// Use LANG environment variable to choose locale
pref("intl.locale.requested", "");

// Use system-provided dictionaries
pref("spellchecker.dictionary_path", "/usr/share/hunspell");

// Don't disable extensions in the application directory
pref("extensions.autoDisableScopes", 11);

// TODO: Enable GNOME Shell search provider
// pref("browser.gnome-search-provider.enabled", true);
END

  msg2 "install distribution.ini"
  local _distini="$_appdir/distribution/distribution.ini"
  install -Dvm644 /dev/stdin "$_distini" <<END
[Global]
id=archlinux
version=1.0
about=Zen Browser for Arch Linux

[Preferences]
app.distributor=archlinux
app.distributor.channel=$pkgbase
app.partner.archlinux=archlinux
END

  msg2 "install icons"
  for i in 16 32 48 64 128; do
    install -d "$pkgdir/usr/share/icons/hicolor/${i}x${i}/apps"
    ln -srvf \
      "$_appdir/browser/chrome/icons/default/default${i}.png" \
      "$pkgdir/usr/share/icons/hicolor/${i}x${i}/apps/$pkgbase.png"
  done
  install -Dm0644 "$srcdir"/desktop/docs/assets/zen-black.svg "$pkgdir/usr/share/icons/hicolor/scalable/apps/$pkgbase.svg"
  install -Dvm644 "$srcdir"/desktop/docs/assets/zen-black.svg "$pkgdir/usr/share/icons/hicolor/symbolic/apps/$pkgbase-symbolic.svg"

  msg2 "install desktop file"
  install -Dvm644 "$srcdir"/desktop/AppDir/*.desktop "$pkgdir/usr/share/applications/$pkgbase.desktop"

  msg2 "use system certificates"
  local _nssckbi="$_appdir/libnssckbi.so"
  if test -e "$_nssckbi"; then
    ln -srvf "$pkgdir/usr/lib/libnssckbi.so" "$_nssckbi"
  fi

  # TODO: Enable GNOME Shell search provider
#   local sprovider="$pkgdir/usr/share/gnome-shell/search-providers/$pkgbase.search-provider.ini"
#   install -Dvm644 /dev/stdin "$sprovider" <<END
# [Shell Search Provider]
# DesktopId=$pkgbase.desktop
# BusName=org.mozilla.${pkgname//-/_}.SearchProvider
# ObjectPath=/org/mozilla/${pkgname//-/_}/SearchProvider
# Version=2
# END
}

_package_i18n() {
  msg2 "install langpack $1"
  install -Dvm644 \
    "$srcdir/$_OBJ_DIR/dist/linux-$CARCH/xpi/zen-$_firefox_version.$1.langpack.xpi" \
    "$pkgdir/usr/lib/$pkgbase/browser/extensions/langpack-$1@firefox.mozilla.org.xpi"
}
