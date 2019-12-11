# Maintainer: Thaodan <theodorstormgrade@gmail.com>
# Contributor: Weng Xuetian <wengxt@gmail.com>


# enable this if you run out of memory during linking
#_lowmem=true

# build with PGO
_pgo=true

# globalmenu
# to support globalmenu a patch from ubuntu is applied
# source:
# http://bazaar.launchpad.net/~mozillateam/firefox/firefox-trunk.head
# /view/head:/debian/patches/unity-menubar.patch

# patches from gentoo:
# https://dev.gentoo.org/~anarchy/mozilla/patchsets/firefox-71.0-patches-04.tar.xz

_pkgname=firefox
pkgname=$_pkgname-kde-opensuse
pkgver=71.0
pkgrel=1
pkgdesc="Standalone web browser from mozilla.org with OpenSUSE patch, integrate better with KDE"
arch=('i686' 'x86_64')
license=('MPL' 'GPL' 'LGPL')
url="https://build.opensuse.org/package/show/mozilla:Factory/MozillaFirefox"
depends=('mozilla-common' 'libxt' 'startup-notification' 'mime-types'
         'dbus-glib' 'hicolor-icon-theme'
	 'libvpx' 'icu'  'libevent' 'nss>=3.28.3' 'nspr>=4.10.6' 'hunspell'
	 'sqlite' 'libnotify' 'kmozillahelper' 'ffmpeg' 'gtk3'
         # system av1
         'dav1d' 'aom'
         # system harfbuzz
         'harfbuzz'
         # system graphite
         'graphite'
         # system webp
         'libwebp'
         # system libevent
         'libevent'
        )

makedepends=('unzip' 'zip' 'diffutils' 'python2-setuptools' 'yasm' 'mesa' 'imake'
             'xorg-server-xvfb' 'libpulse' 'inetutils' 'autoconf2.13' 'rust'
             'cargo' 'mercurial' 'llvm' 'clang'
             'gtk2' 'nodejs' 'cbindgen' 'nasm' 'python' 'python2-psutil' 'xz')

optdepends=('networkmanager: Location detection via available WiFi networks'
            'speech-dispatcher: Text-to-Speech'
            'pulseaudio: Audio support')
provides=("firefox=${pkgver}")
conflicts=('firefox')
_patchrev=572ec48f3fe8
options=('!emptydirs')
_patchurl=http://www.rosenauer.org/hg/mozilla/raw-file/$_patchrev
_repo=https://hg.mozilla.org/mozilla-unified
source=("hg+$_repo#tag=FIREFOX_${pkgver//./_}_RELEASE"
        mozconfig
        firefox.desktop
        vendor.js
        kde.js
	# Firefox patchset
	firefox-branded-icons-$_patchrev.patch::$_patchurl/firefox-branded-icons.patch
	firefox-kde-$_patchrev.patch::$_patchurl/firefox-kde.patch
	# Gecko/toolkit patchset
	mozilla-kde-$_patchrev.patch::$_patchurl/mozilla-kde.patch
	mozilla-nongnome-proxies-$_patchrev.patch::$_patchurl/mozilla-nongnome-proxies.patch
	unity-menubar.patch
	add_missing_pgo_rule.patch
        pgo_fix_missing_kdejs.patch
        2000_system_harfbuzz_support.patch
        2001_system_graphite2_support.patch
        pgo.patch
        # use sytem av1
        7002_system_av1_support.patch
        # https://bugzilla.mozilla.org/show_bug.cgi?id=1530052
        0001-Use-remoting-name-for-GDK-application-names.patch
        # Fix building with python 3.8
        0001-Bug-1212502-Switch-mozinfo-to-using-the-distro-packa.patch.xz
        # Workaround objects no being allocated with the correct alignment
        # inside dom/indexedDB/ActorsParent.cpp
        workaround_dom_indexdb_actorsparent_allignment.patch
)

# Google API keys (see http://www.chromium.org/developers/how-tos/api-keys)
# Note: These are for Arch Linux use ONLY. For your own distribution, please
# get your own set of keys. Feel free to contact foutrelis@archlinux.org for
# more information.
_google_api_key=AIzaSyDwr302FpOSkGRpLlUpPThNTDPbXcIn_FM
_google_default_client_id=413772536636.apps.googleusercontent.com
_google_default_client_secret=0ZChLK6AxeA3Isu96MkwqDR4


# Mozilla API keys (see https://location.services.mozilla.com/api)
# Note: These are for Arch Linux use ONLY. For your own distribution, please
# get your own set of keys. Feel free to contact heftig@archlinux.org for
# more information.
_mozilla_api_key=e05d56db0a694edc8b5aaebda3f2db6a

prepare() {
  cd mozilla-unified

  cp "$srcdir/mozconfig" .mozconfig

  echo -n "$_google_api_key" >google-api-key
  echo "ac_add_options --with-google-location-service-api-keyfile=\"$PWD/google-api-key\"" >>.mozconfig

  echo -n "$_google_default_client_id $_google_default_client_secret" >google-oauth-api-key
  echo "ac_add_options --with-google-safebrowsing-api-keyfile=\"$PWD/google-oauth-api-key\"" >>.mozconfig

  echo -n "$_mozilla_api_key" >mozilla-api-key
  echo "ac_add_options --with-mozilla-api-keyfile=\"$PWD/mozilla-api-key\"" >>.mozconfig
  
  msg "Patching for KDE"
  patch -Np1 -i "$srcdir/mozilla-nongnome-proxies-$_patchrev.patch"
  patch -Np1 -i "$srcdir/mozilla-kde-$_patchrev.patch"

  patch -Np1 -i "$srcdir/firefox-kde-$_patchrev.patch"
  patch -Np1 -i "$srcdir/firefox-branded-icons-$_patchrev.patch"
  
  # add globalmenu support
  patch -Np1 -i "$srcdir/unity-menubar.patch"
  
  patch -Np1 -i "$srcdir"/2000_system_harfbuzz_support.patch
  patch -Np1 -i "$srcdir"/2001_system_graphite2_support.patch
  patch -Np1 -i "$srcdir"/7002_system_av1_support.patch

  # https://bugzilla.mozilla.org/show_bug.cgi?id=1530052
  patch -Np1 -i "$srcdir"/0001-Use-remoting-name-for-GDK-application-names.patch

  # Fix building with python 3.8
  xzcat "$srcdir"/\
0001-Bug-1212502-Switch-mozinfo-to-using-the-distro-packa.patch.xz  | \
    patch -Np1

  # Workaround objects no being allocated with the correct alignment
  # inside dom/indexedDB/ActorsParent.cpp
  patch -Np1 -i "$srcdir"/workaround_dom_indexdb_actorsparent_allignment.patch
  
  if [[ $_pgo ]] ; then
    # add missing rule for pgo builds
    patch -Np1 -i "$srcdir"/add_missing_pgo_rule.patch

    patch -Np1 -i "$srcdir"/pgo.patch

    # add missing file Makefile for pgo builds
    patch -Np1 -i "$srcdir"/pgo_fix_missing_kdejs.patch

    echo "ac_add_options --enable-lto" >> .mozconfig
    echo "ac_add_options --disable-elf-hack" >> .mozconfig
  fi
}

build() {
  #export CXXFLAGS="${CFLAGS}"
  cd mozilla-unified
  export MOZ_SOURCE_REPO="$_repo"
  export MOZBUILD_STATE_PATH="$srcdir/mozbuild"
  export MOZ_APP_REMOTINGNAME=$pkgname
  export CARGO_HOME="$srcdir"/.cargo

  export CC=gcc
  export CXX=g++
  export AR="gcc-ar"
  export NM="gcc-nm"
  export RANLIB="gcc-ranlib"

  export MOZ_MAKE_FLAGS="$MAKEFLAGS"
  export STRIP=/bin/true

  if [[ -n $_lowmem || $CARCH == i686 ]]; then
    LDFLAGS+=" -Xlinker --no-keep-memory"
  fi

  if [[ -n $_pgo ]]; then
    export DISPLAY=:99
    export MOZ_PGO=1
    
    xvfb-run \
      -a \
      -s "-extension GLX -screen 0 1280x1024x24" \
      ./mach build
  else
    ./mach build
  fi
  ./mach buildsymbols
}

package() {
  cd mozilla-unified

  [[ "$CARCH" == "i686" ]] && cp "$srcdir/kde.js" obj-i686-pc-linux-gnu/dist/bin/defaults/pref
  [[ "$CARCH" == "x86_64" ]] && cp "$srcdir/kde.js" obj-x86_64-pc-linux-gnu/dist/bin/defaults/pref

  DESTDIR="$pkgdir" ./mach install

  install -Dm644 "$srcdir/vendor.js" "$pkgdir/usr/lib/firefox/browser/defaults/preferences/vendor.js"
  install -Dm644 "$srcdir/kde.js" "$pkgdir/usr/lib/firefox/browser/defaults/preferences/kde.js"

  _distini="$pkgdir/usr/lib/firefox/distribution/distribution.ini"
  install -Dm644 /dev/stdin "$_distini" <<END
[Global]
id=archlinux
version=1.0
about=Mozilla Firefox for Arch Linux

[Preferences]
app.distributor=archlinux
app.distributor.channel=$pkgname
app.partner.archlinux=archlinux
END

  for i in 16 22 24 32 48 64 128 256; do
      install -Dm644 browser/branding/official/default$i.png \
        "$pkgdir/usr/share/icons/hicolor/${i}x${i}/apps/firefox.png"
  done

  install -Dm644 browser/branding/official/content/about-logo.png \
    "$pkgdir/usr/share/icons/hicolor/192x192/apps/firefox.png"
  install -Dm644 browser/branding/official/content/about-logo@2x.png \
    "$pkgdir/usr/share/icons/hicolor/384x384/apps/firefox.png"

  install -Dm644 "$srcdir/firefox.desktop" "$pkgdir/usr/share/applications/firefox.desktop"

  # Use system certificates
  local nssckbi="$pkgdir/usr/lib/$pkgname/libnssckbi.so"
  if [[ -e $nssckbi ]]; then
    ln -srfv "$pkgdir/usr/lib/libnssckbi.so" "$nssckbi"
  fi

  #workaround for now
  #https://bugzilla.mozilla.org/show_bug.cgi?id=658850
  ln -sf firefox "$pkgdir/usr/lib/firefox/firefox-bin"
}
md5sums=('SKIP'
         'f758e064e1463b90878790124f398197'
         'a26a061efb4def6572d5b319d657f1d6'
         '4c23d9c0a691d70919beb1dafbbecbd3'
         '05bb69d25fb3572c618e3adf1ee7b670'
         'ad055db454c9263623fdbc857e8290fe'
         '0756f1b090f9c3371df957257907b0c7'
         'bc1f7445de31cd5ff20f00d0f9bc8e57'
         'e083ae314eaa9355aa2d4aa75a7fc277'
         '35fd9214a0af395543346f4dd074f92b'
         'fe24f5ea463013bb7f1c12d12dce41b2'
         '3fa8bd22d97248de529780f5797178af'
         '28c2eff56d3d95da6e9ba444fc60e90b'
         '8d0c0ebc805e4e52a3cb2c0dc64ea2de'
         'f867ae41a722630cc5567e2dcc51676d'
         'd87270bfe02ea30e2fde3fcae5daf18d'
         '0ffabb81dd8a5fe98bb8afe47d6541d3'
         '3016656551d00f4f22dc2eaccc71ee14'
         'f4a8a7f7480c74556ffb8fea3c5fe51a')
