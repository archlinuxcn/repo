### Original Thunderbird from extra ###
# Maintainer: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>
# Contributor: Ionut Biru <ibiru@archlinux.org>
# Contributor: Alexander Baldeck <alexander@archlinux.org>
# Contributor: Dale Blount <dale@archlinux.org>
# Contributor: Anders Bostrom <anders.bostrom@home.se>

### Appmenu patching ###
# PKGBUILD: Nikita Tarasov <nikatar@disroot.org>

_pkgname=thunderbird
pkgname=thunderbird-appmenu
pkgver=68.6.0
pkgrel=1
pkgdesc="Thunderbird from extra with appmenu patch"
arch=(x86_64)
license=(MPL GPL LGPL)
url="https://www.mozilla.org/thunderbird/"
depends=(gtk3 mozilla-common libxt startup-notification mime-types dbus-glib alsa-lib
         nss hunspell sqlite ttf-font icu)  # libvpx
makedepends=(unzip zip diffutils python python2 yasm nasm mesa imake libpulse inetutils xorg-server-xvfb
             autoconf2.13 rust clang llvm gtk2 cbindgen nodejs)
optdepends=('libcanberra: sound support')
provides=("thunderbird=$pkgver")
conflicts=("thunderbird")
options=(!emptydirs !makeflags)
source=(https://ftp.mozilla.org/pub/mozilla.org/thunderbird/releases/$pkgver/source/thunderbird-$pkgver.source.tar.xz{,.asc}
        $_pkgname.desktop
        unity-menubar.patch)
sha512sums=('3502cc42b594eebf3511219ae8e7fb8a13594534abfe7a40ec32e5a3f60343cfab7c652b161a5f33af46bd5e6f096e3abd4a407c8b307ce4693089b471a42c3e'
            'SKIP'
            'fa28ec547f87658cf72d160e9c2a7867d3e8a9b8c76ffa29d1098fddfc9331f65cc6dbf24c15da28c5d1b4ffa587d14d529d5da522a8805b073ad89986a552c9'
            'f3aa468974780016de60fa61a61f7e67a2cc51b4f888b223d16b9afaa42e82100c3b3d7f9491dfd0de3c5667ad4ac0fc58b96d81ef448ccf6e924cdc49066ad5')
validpgpkeys=(14F26682D0916CDD81E37B6D61B7B526D98F0353) # Mozilla Software Releases <release@mozilla.com>

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
  cd $_pkgname-$pkgver

  # Actual appmenu patch from ubuntu repos
  patch -Np1 -i ../unity-menubar.patch

  echo -n "$_google_api_key" >google-api-key
  echo -n "$_mozilla_api_key" >mozilla-api-key

  cat >.mozconfig <<END
ac_add_options --enable-application=comm/mail
ac_add_options --enable-calendar

ac_add_options --prefix=/usr
ac_add_options --enable-release
ac_add_options --enable-linker=gold
ac_add_options --enable-hardening
ac_add_options --enable-optimize
# https://bugzilla.mozilla.org/show_bug.cgi?id=1521249
#ac_add_options --enable-rust-simd
# https://bugzilla.mozilla.org/show_bug.cgi?id=1423822
ac_add_options --disable-elf-hack

# Branding
ac_add_options --enable-official-branding
ac_add_options --enable-update-channel=release
ac_add_options --with-distribution-id=org.archlinux

# Keys
ac_add_options --with-google-location-service-api-keyfile=${PWD@Q}/google-api-key
ac_add_options --with-google-safebrowsing-api-keyfile=${PWD@Q}/google-api-key
ac_add_options --with-mozilla-api-keyfile=${PWD@Q}/mozilla-api-key

# System libraries
ac_add_options --with-system-zlib
ac_add_options --with-system-bz2
ac_add_options --with-system-icu
ac_add_options --with-system-jpeg
# ac_add_options --with-system-libvpx
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --enable-system-sqlite
ac_add_options --enable-system-ffi

# Features
ac_add_options --enable-alsa
ac_add_options --disable-jack
ac_add_options --enable-startup-notification
ac_add_options --disable-crashreporter
ac_add_options --disable-updater
ac_add_options --disable-gconf
END
}

build() {
  cd $_pkgname-$pkgver
  ./mach configure
  ./mach build
  ./mach buildsymbols
}

package() {
  cd $_pkgname-$pkgver
  DESTDIR="$pkgdir" ./mach install

  _vendorjs="$pkgdir/usr/lib/$_pkgname/defaults/preferences/vendor.js"
  install -Dm644 /dev/stdin "$_vendorjs" <<END
// Use LANG environment variable to choose locale
pref("intl.locale.requested", "");

// Use system-provided dictionaries
pref("spellchecker.dictionary_path", "/usr/share/hunspell");

// Disable default mailer checking.
pref("mail.shell.checkDefaultMail", false);

// Don't disable our bundled extensions in the application directory
pref("extensions.autoDisableScopes", 11);
pref("extensions.shownSelectionUI", true);
END

  _distini="$pkgdir/usr/lib/$_pkgname/distribution/distribution.ini"
  install -Dm644 /dev/stdin "$_distini" <<END
[Global]
id=archlinux
version=1.0
about=Mozilla Thunderbird for Arch Linux

[Preferences]
app.distributor=archlinux
app.distributor.channel=$_pkgname
END

  for i in 16 22 24 32 48 64 128 256; do
    install -Dm644 comm/mail/branding/thunderbird/default${i}.png \
      "$pkgdir/usr/share/icons/hicolor/${i}x${i}/apps/$_pkgname.png"
  done
  install -Dm644 comm/mail/branding/thunderbird/TB-symbolic.svg \
    "$pkgdir/usr/share/icons/hicolor/symbolic/apps/thunderbird-symbolic.svg"

  install -Dm644 ../$_pkgname.desktop \
    "$pkgdir/usr/share/applications/$_pkgname.desktop"

  # Use system-provided dictionaries
  ln -Ts /usr/share/hunspell "$pkgdir/usr/lib/$_pkgname/dictionaries"
  ln -Ts /usr/share/hyphen "$pkgdir/usr/lib/$_pkgname/hyphenation"

  # Install a wrapper to avoid confusion about binary path
  install -Dm755 /dev/stdin "$pkgdir/usr/bin/$_pkgname" <<END
#!/bin/sh
exec /usr/lib/$_pkgname/thunderbird "\$@"
END

  # Replace duplicate binary with wrapper
  # https://bugzilla.mozilla.org/show_bug.cgi?id=658850
  ln -srf "$pkgdir/usr/bin/$_pkgname" \
    "$pkgdir/usr/lib/$_pkgname/thunderbird-bin"
}
