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
pkgname=thunderbird-appmenu
pkgver=78.9.1
pkgrel=1
pkgdesc="Thunderbird from extra with appmenu patch"
arch=(x86_64)
license=(MPL GPL LGPL)
url="https://www.mozilla.org/thunderbird/"
depends=(
  glibc gtk3 libgdk-3.so mime-types dbus libdbus-1.so dbus-glib alsa-lib nss
  hunspell sqlite ttf-font libvpx libvpx.so zlib bzip2 botan libwebp libevent
  libjpeg-turbo libffi nspr gcc-libs libx11 libxrender libxfixes libxext
  libxcomposite libxdamage pango libpango-1.0.so cairo gdk-pixbuf2 icu
  libicui18n.so libicuuc.so freetype2 libfreetype.so fontconfig
  libfontconfig.so glib2 libglib-2.0.so pixman libpixman-1.so gnupg libnotify
)
optdepends=(
  'libotr: OTR support for active one-to-one chats'
)
makedepends=(
  unzip zip diffutils python python-setuptools yasm nasm mesa imake libpulse
  inetutils xorg-server-xvfb autoconf2.13 rust clang llvm gtk2 cbindgen nodejs
  gawk perl findutils libotr
)
provides=("thunderbird=$pkgver")
conflicts=("thunderbird")
options=(!emptydirs !makeflags)
source=(https://ftp.mozilla.org/pub/mozilla.org/thunderbird/releases/$pkgver/source/thunderbird-$pkgver.source.tar.xz{,.asc}
        thunderbird.desktop
        vendor-prefs.js
        distribution.ini
        mozconfig.cfg
        configure-fix-passing-system-bzip2-ldflags.patch
        thunderbird-78.5-rust-1.48.patch
        unity-menubar.patch)
md5sums=('SKIP'
         'SKIP'
         '10872ca39ebb8844ec753203c55bccc4'
         '7c04ba88f1078b224c7c1483b5f0fa78'
         '1ef0f094e533a68399b96dc8080c6a6e'
         '2f911c142fc7eb0b76a6af1fad0438d6'
         '2ad133b7c29d844d6e405a5005cea2f7'
         '791e650139aad8786ecae7c006c3e4b7'
         'e9e1d302d2be62192e96944610f2e14a')

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

  echo "${noextract[@]}"

  local src
  for src in "${source[@]}"; do
    src="${src%%::*}"
    src="${src##*/}"
    [[ $src = *.patch ]] || continue
    echo "Applying patch $src..."
    patch -Np1 < "../$src"
  done

  printf "%s" "$_google_api_key" >google-api-key
  printf "%s" "$_mozilla_api_key" >mozilla-api-key
  cp ../mozconfig.cfg .mozconfig
  sed "s|@PWD@|${PWD@Q}|g" -i .mozconfig
}

build() {
  cd $_pkgname-$pkgver
  if [[ -n "${SOURCE_DATE_EPOCH}" ]]; then
    export MOZ_BUILD_DATE=$(date --date "@${SOURCE_DATE_EPOCH}" "+%Y%m%d%H%M%S")
  fi
  ./mach configure
  ./mach build
# ./mach buildsymbols
}

package() {
  optdepends=('libcanberra: sound support')

  cd $_pkgname-$pkgver
  DESTDIR="$pkgdir" ./mach install

  install -Dm 644 ../vendor-prefs.js -t "$pkgdir/usr/lib/$pkgname/defaults/pref"
  install -Dm 644 ../distribution.ini -t "$pkgdir/usr/lib/$pkgname/distribution"
  install -Dm 644 ../thunderbird.desktop -t "$pkgdir/usr/share/applications"

  for i in 16 22 24 32 48 64 128 256; do
    install -Dm644 comm/mail/branding/thunderbird/default${i}.png \
      "$pkgdir/usr/share/icons/hicolor/${i}x${i}/apps/$pkgname.png"
  done
  install -Dm644 comm/mail/branding/thunderbird/TB-symbolic.svg \
    "$pkgdir/usr/share/icons/hicolor/symbolic/apps/thunderbird-symbolic.svg"

  # Use system-provided dictionaries
  ln -Ts /usr/share/hunspell "$pkgdir/usr/lib/$pkgname/dictionaries"
  ln -Ts /usr/share/hyphen "$pkgdir/usr/lib/$pkgname/hyphenation"

  # Install a wrapper to avoid confusion about binary path
  install -Dm755 /dev/stdin "$pkgdir/usr/bin/$pkgname" <<END
#!/bin/sh
exec /usr/lib/$pkgname/thunderbird "\$@"
END

  # Replace duplicate binary with wrapper
  # https://bugzilla.mozilla.org/show_bug.cgi?id=658850
  ln -srf "$pkgdir/usr/bin/$pkgname" \
    "$pkgdir/usr/lib/$pkgname/thunderbird-bin"
}
