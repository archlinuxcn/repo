### Original Thunderbird from extra ###
# Maintainer: N Fytilis <n-fit[at]live.com>
# Contributor: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>
# Contributor: Ionut Biru <ibiru@archlinux.org>
# Contributor: Alexander Baldeck <alexander@archlinux.org>
# Contributor: Dale Blount <dale@archlinux.org>
# Contributor: Anders Bostrom <anders.bostrom@home.se>

### Appmenu patching ###
# PKGBUILD: Nikita Tarasov <nikatar@disroot.org>

_pkgname=thunderbird
pkgbase=thunderbird-appmenu
pkgname=thunderbird-appmenu
pkgver=102.0.3
pkgrel=4
pkgdesc="Thunderbird from extra with appmenu patch"
arch=(x86_64)
license=(MPL GPL LGPL)
url="https://www.mozilla.org/thunderbird/"

depends=(gtk3 libxt mime-types dbus-glib ffmpeg nss ttf-font libpulse)
makedepends=(unzip zip diffutils yasm mesa imake inetutils xorg-server-xvfb
             autoconf2.13 rust clang llvm jack nodejs cbindgen nasm
             python-setuptools python-zstandard lld dump_syms
             wasi-compiler-rt wasi-libc wasi-libc++ wasi-libc++abi)
optdepends=('networkmanager: Location detection via available WiFi networks'
            'libnotify: Notification integration'
            'pulseaudio: Audio support'
            'speech-dispatcher: Text-to-Speech'
            'hunspell-en_US: Spell checking, American English'
            'xdg-desktop-portal: Screensharing with Wayland')
options=(!emptydirs !makeflags !strip !lto !debug)

provides=("thunderbird=$pkgver")
conflicts=("thunderbird")

source=(https://ftp.mozilla.org/pub/mozilla.org/thunderbird/releases/$pkgver/source/thunderbird-$pkgver.source.tar.xz{,.asc}
        cbindgen-0.24.0.diff
        zstandard-0.18.0.diff
        unity-menubar.patch
        $_pkgname.desktop)


md5sums=('d74f2d068e97491aa498e7c8ed2f8877'
         'SKIP'
         'bb20e95b9d65d59ba39f2f7f1c853c27'
         '29ce7c26f14c9c4169d88d1b05552189'
         '63ebf05aea29545081dab2cb023e2bba'
         '10872ca39ebb8844ec753203c55bccc4')


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
_mozilla_api_key=e05d56db0a694edc8b5aaebda3f2db6a

prepare() {
  mkdir mozbuild
  cd thunderbird-$pkgver

  # Unbreak build with cbindgen 0.24.0
  patch -Np1 -i ../cbindgen-0.24.0.diff

  # Unbreak build with python-zstandard 0.18.0
  patch -Np1 -i ../zstandard-0.18.0.diff
  patch -Np1 -i ../unity-menubar.patch

  echo -n "$_google_api_key" >google-api-key
  echo -n "$_mozilla_api_key" >mozilla-api-key

  cat >../mozconfig <<END
ac_add_options --enable-application=comm/mail
mk_add_options MOZ_OBJDIR=${PWD@Q}/obj

ac_add_options --prefix=/usr
ac_add_options --enable-release
ac_add_options --enable-hardening
ac_add_options --enable-optimize
ac_add_options --enable-rust-simd
ac_add_options --enable-linker=lld
ac_add_options --disable-elf-hack
ac_add_options --disable-bootstrap
ac_add_options --with-wasi-sysroot=/usr/share/wasi-sysroot

# Branding
ac_add_options --enable-official-branding
ac_add_options --enable-update-channel=release
ac_add_options --with-distribution-id=org.archlinux
ac_add_options --with-unsigned-addon-scopes=app,system
ac_add_options --allow-addon-sideload
export MOZILLA_OFFICIAL=1
export MOZ_APP_REMOTINGNAME=${_pkgname//-/}

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
ac_add_options --enable-crashreporter
ac_add_options --disable-updater
ac_add_options --disable-tests
END

  for i in tools/fuzzing/smoke/grizzly_requirements.txt build/psutil_requirements.txt build/psutil_requirements.in python/sites/mach.txt
  do sed 's/5.8.0/5.9.1/g' -i $i
  done
}

build() {
  cd thunderbird-$pkgver

  export MOZ_NOSPAM=1
  export MOZBUILD_STATE_PATH="$srcdir/mozbuild"
#  export MOZ_ENABLE_FULL_SYMBOLS=1
  export MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE=system

  # LTO needs more open files
  ulimit -n 4096

  # Do 3-tier PGO
  echo "Building instrumented browser..."
  cat >.mozconfig ../mozconfig - <<END
END
  ./mach build
}

package() {
  cd thunderbird-$pkgver
  DESTDIR="$pkgdir" ./mach install

#  local vendorjs="$pkgdir/usr/lib/$pkgname/browser/defaults/preferences/vendor.js"
#  install -Dvm644 /dev/stdin "$vendorjs" <<END
#// Use LANG environment variable to choose locale
#pref("intl.locale.requested", "");
#
#// Use system-provided dictionaries
#pref("spellchecker.dictionary_path", "/usr/share/hunspell");
#
#// Disable default browser checking.
#pref("browser.shell.checkDefaultBrowser", false);
#
#// Don't disable extensions in the application directory
#pref("extensions.autoDisableScopes", 11);
#END

  local distini="$pkgdir/usr/lib/$_pkgname/distribution/distribution.ini"
  install -Dvm644 /dev/stdin "$distini" <<END
[Global]
id=archlinux
version=1.0
about=Mozilla thunderbird for Arch Linux

[Preferences]
app.distributor=archlinux
app.distributor.channel=$_pkgname
app.partner.archlinux=archlinux
END

#  local i theme=official
#  for i in 16 22 24 32 48 64 128 256; do
#    install -Dvm644 browser/branding/$theme/default$i.png \
#      "$pkgdir/usr/share/icons/hicolor/${i}x${i}/apps/$pkgname.png"
#  done
#  install -Dvm644 browser/branding/$theme/content/about-logo.png \
#    "$pkgdir/usr/share/icons/hicolor/192x192/apps/$pkgname.png"
#  install -Dvm644 browser/branding/$theme/content/about-logo@2x.png \
#    "$pkgdir/usr/share/icons/hicolor/384x384/apps/$pkgname.png"
#  install -Dvm644 browser/branding/$theme/content/about-logo.svg \
#    "$pkgdir/usr/share/icons/hicolor/scalable/apps/$pkgname.svg"
#
#  install -Dvm644 ../$pkgname.desktop \
#    "$pkgdir/usr/share/applications/$pkgname.desktop"

  # Install a wrapper to avoid confusion about binary path
  install -Dvm755 /dev/stdin "$pkgdir/usr/bin/$_pkgname" <<END
#!/bin/sh
exec /usr/lib/$_pkgname/thunderbird "\$@"
END

  # Replace duplicate binary with wrapper
  # https://bugzilla.mozilla.org/show_bug.cgi?id=658850
  ln -srfv "$pkgdir/usr/bin/$_pkgname" "$pkgdir/usr/lib/$_pkgname/thunderbird-bin"

  # Use system certificates
  local nssckbi="$pkgdir/usr/lib/$_pkgname/libnssckbi.so"
  if [[ -e $nssckbi ]]; then
    ln -srfv "$pkgdir/usr/lib/libnssckbi.so" "$nssckbi"
  fi

#  export SOCORRO_SYMBOL_UPLOAD_TOKEN_FILE="$startdir/.crash-stats-api.token"
#  if [[ -f $SOCORRO_SYMBOL_UPLOAD_TOKEN_FILE ]]; then
#    make -C obj uploadsymbols
#  else
#    cp -fvt "$startdir" obj/dist/*crashreporter-symbols-full.tar.zst
#  fi
}

# vim:set sw=2 et:
