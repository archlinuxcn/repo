# $Id$
# Maintainer : Figue <ffigue@gmail.com>
# Contributor : Ionut Biru <ibiru@archlinux.org>
# Contributor: Jakub Schmidtke <sjakub@gmail.com>

pkgname=firefox-esr60
_pkgname=firefox-esr
pkgver=60.8.0
pkgrel=1
pkgdesc="Standalone web browser from mozilla.org, Extended Support Release 60.x"
arch=(x86_64)
license=(MPL GPL LGPL)
url="https://www.mozilla.org/en-US/firefox/organizations/"
depends=(gtk3 mozilla-common libxt startup-notification mime-types dbus-glib ffmpeg
         nss hunspell ttf-font libpulse)
makedepends=(unzip zip diffutils python2 yasm mesa imake inetutils xorg-server-xvfb
             autoconf2.13 rust clang llvm jack gtk2)
optdepends=('networkmanager: Location detection via available WiFi networks'
            'libnotify: Notification integration'
            'pulseaudio: Audio support'
            'speech-dispatcher: Text-to-Speech')
provides=(firefox)
conflicts=(firefox)
options=(!emptydirs !makeflags !strip)
source=(https://ftp.mozilla.org/pub/firefox/releases/${pkgver}esr/source/firefox-${pkgver}esr.source.tar.xz
        firefox.desktop firefox-symbolic.svg
        rust_133-part0.patch 'rust_133-part1.patch::https://bugzilla.mozilla.org/attachment.cgi?id=9046663' 'rust_133-part2.patch::https://bugzilla.mozilla.org/attachment.cgi?id=9046664' deny_missing_docs.patch)
sha256sums=('c13387d944e635aebd5f1d2ce9ab77cb706a74043a240cbb7b70654519487fbe'
            '78a920ffdd44e1d51445e7255da4863604be96a4b3cd7a7cb13ecc2efae6cb39'
            'a2474b32b9b2d7e0fb53a4c89715507ad1c194bef77713d798fa39d507def9e9'
            'c10521badc262b476e844d3f3045ddf27e28d83d49b5db0d0e19431f06386e4d'
            '8b37332dd205946ea95c606103b5b0e1e8498819051ea1c1bce79f04fd88ebca'
            '08ab4293d6008524a38e20b428c750c4c55a2f7189e9a0067871ad723c1efab5'
            'cb1116c783995b8187574f84acb8365681aedaa2c76222cf060d31fedcb063c4')
validpgpkeys=('2B90598A745E992F315E22C58AB132963A06537A')

# Google API keys (see http://www.chromium.org/developers/how-tos/api-keys)
# Note: These are for Arch Linux use ONLY. For your own distribution, please
# get your own set of keys. Feel free to contact foutrelis@archlinux.org for
# more information.
_google_api_key=AIzaSyDwr302FpOSkGRpLlUpPThNTDPbXcIn_FM

# Mozilla API keys (see https://location.services.mozilla.com/api)
# Note: These are for Arch Linux use ONLY. For your own distribution, please
# get your own set of keys. Feel free to contact heftig@archlinux.org for
# more information.
_mozilla_api_key=16674381-f021-49de-8622-3021c5942aff

prepare() {
  cd firefox-${pkgver}

  # Bug 1521249 --enable-rust-simd fails to build using Rust 1.33
  # https://bugzilla.mozilla.org/show_bug.cgi?id=1521249
  patch -Np1 -i ../rust_133-part0.patch
  patch -Np1 -i ../rust_133-part1.patch || true
  patch -Np1 -i ../rust_133-part2.patch
  patch -Np1 -i ../deny_missing_docs.patch
  rm -vf third_party/rust/boxfnonce/.travis/id_rsa.enc

  echo -n "$_google_api_key" >google-api-key
  echo -n "$_mozilla_api_key" >mozilla-api-key

  cat >.mozconfig <<END
ac_add_options --enable-application=browser

ac_add_options --prefix=/usr
ac_add_options --enable-release
ac_add_options --enable-linker=gold
ac_add_options --enable-hardening
ac_add_options --enable-optimize
ac_add_options --enable-rust-simd
export CC=clang
export CXX=clang++
export AR=llvm-ar
export NM=llvm-nm
export RANLIB=llvm-ranlib


# Branding
ac_add_options --enable-official-branding
ac_add_options --enable-update-channel=release
ac_add_options --with-distribution-id=org.archlinux
export MOZILLA_OFFICIAL=1
export MOZ_APP_REMOTINGNAME=$_pkgname
export MOZ_TELEMETRY_REPORTING=1
export MOZ_ADDON_SIGNING=1
export MOZ_REQUIRE_SIGNING=1

# Keys
ac_add_options --with-google-location-service-api-keyfile=${PWD@Q}/google-api-key
ac_add_options --with-google-safebrowsing-api-keyfile=${PWD@Q}/google-api-key
ac_add_options --with-mozilla-api-keyfile=${PWD@Q}/mozilla-api-key

# System libraries
ac_add_options --with-system-nspr
ac_add_options --with-system-nss

# Features
ac_add_options --enable-alsa
ac_add_options --enable-jack
ac_add_options --enable-startup-notification
ac_add_options --enable-crashreporter
ac_add_options --disable-gconf
ac_add_options --disable-updater
END
}

build() {
  cd firefox-${pkgver}

  # Do PGO
  #xvfb-run -a -n 95 -s "-extension GLX -screen 0 1280x1024x24" \
  #  MOZ_PGO=1 ./mach build
  ./mach build
  ./mach buildsymbols
}

package() {
  cd firefox-${pkgver}
  DESTDIR="$pkgdir" ./mach install
  find . -name '*crashreporter-symbols-full.zip' -exec cp -fvt "$startdir" {} +

  _vendorjs="$pkgdir/usr/lib/firefox/browser/defaults/preferences/vendor.js"
  install -Dm644 /dev/stdin "$_vendorjs" <<END
// Use LANG environment variable to choose locale
pref("intl.locale.requested", "");

// Disable default browser checking.
pref("browser.shell.checkDefaultBrowser", false);

// Don't disable our bundled extensions in the application directory
pref("extensions.autoDisableScopes", 11);
pref("extensions.shownSelectionUI", true);

// Opt all of us into e10s, instead of just 50%
pref("browser.tabs.remote.autostart", true);
END

  _distini="$pkgdir/usr/lib/firefox/distribution/distribution.ini"
  install -Dm644 /dev/stdin "$_distini" <<END
[Global]
id=archlinux
version=1.0
about=Mozilla Firefox ESR for Arch Linux

[Preferences]
app.distributor=archlinux
app.distributor.channel=$_pkgname
app.partner.archlinux=archlinux
END

  for i in 16 22 24 32 48 64 128 256; do
    install -Dm644 browser/branding/official/default$i.png \
      "$pkgdir/usr/share/icons/hicolor/${i}x${i}/apps/$_pkgname.png"
  done
  install -Dm644 browser/branding/official/content/about-logo.png \
    "$pkgdir/usr/share/icons/hicolor/192x192/apps/$_pkgname.png"
  install -Dm644 browser/branding/official/content/about-logo@2x.png \
    "$pkgdir/usr/share/icons/hicolor/384x384/apps/$_pkgname.png"
  install -Dm644 ../firefox-symbolic.svg \
    "$pkgdir/usr/share/icons/hicolor/symbolic/apps/$_pkgname-symbolic.svg"

  install -Dm644 ../firefox.desktop \
    "$pkgdir/usr/share/applications/firefox.desktop"

  # Use system-provided dictionaries
  rm -r "$pkgdir"/usr/lib/firefox/dictionaries
  ln -Ts /usr/share/hunspell "$pkgdir/usr/lib/firefox/dictionaries"
  ln -Ts /usr/share/hyphen "$pkgdir/usr/lib/firefox/hyphenation"

  # Install a wrapper to avoid confusion about binary path
  install -Dm755 /dev/stdin "$pkgdir/usr/bin/firefox" <<END
#!/bin/sh
exec /usr/lib/firefox/firefox "\$@"
END

  # Replace duplicate binary with wrapper
  # https://bugzilla.mozilla.org/show_bug.cgi?id=658850
  ln -srf "$pkgdir/usr/bin/firefox" \
    "$pkgdir/usr/lib/firefox/firefox-bin"
}
