# Maintainer: Thaodan <theodorstormgrade@gmail.com>
# Contributor: Weng Xuetian <wengxt@gmail.com>


# For common issues regarding GCC and firefox see:
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=45375

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
pkgver=83.0
pkgrel=2
pkgdesc="Standalone web browser from mozilla.org with OpenSUSE patch, integrate better with KDE"
arch=('i686' 'x86_64')
license=('MPL' 'GPL' 'LGPL')
url="https://build.opensuse.org/package/show/mozilla:Factory/MozillaFirefox"
depends=('mozilla-common' 'libxt' 'mime-types'
         'dbus-glib' 'hicolor-icon-theme'
	 'libvpx' 'icu'  'libevent' 'nss>=3.28.3' 'nspr>=4.10.6' 'hunspell'
	 'sqlite' 'libnotify' 'kmozillahelper' 'ffmpeg' 'gtk3'
         # system av1
         'dav1d' 'aom'
         # system harfbuzz
         'harfbuzz'
         # system graphite
         'graphite-mozilla'
         # system webp
         'libwebp'
         # system libevent
         'libevent'
        )

makedepends=('unzip' 'zip' 'diffutils' 'yasm' 'mesa' 'imake'
             'xorg-server-xvfb' 'libpulse' 'inetutils' 'autoconf2.13'
             'cargo' 'mercurial' 'llvm' 'clang' 'rust' 'jack'
             'gtk2' 'nodejs' 'cbindgen=0.15.0' 'nasm' 'xz'
             'python' 'python-psutil' 'python-zstandard')


if [ $_pgo ] ; then
  # rhbz#1849165
  # https://bugzilla.redhat.com/show_bug.cgi?id=1849165
  # LTO/PGO needs fixes from GCC 10.2.1
  makedepends+=('gcc>=10.2.1')
fi

optdepends=('networkmanager: Location detection via available WiFi networks'
            'speech-dispatcher: Text-to-Speech'
            'pulseaudio: Audio support')
provides=("firefox=${pkgver}")
conflicts=('firefox')
_patchrev=859fecad6f780e5858788f165db72e04c17347ea
options=('!emptydirs')
_patchurl=https://raw.githubusercontent.com/openSUSE/firefox-maintenance/$_patchrev
_repo=https://hg.mozilla.org/mozilla-unified
source=("hg+$_repo#tag=FIREFOX_${pkgver//./_}_RELEASE"
        mozconfig
        firefox.desktop
        vendor.js
        kde.js
	# Firefox patchset
	firefox-branded-icons-$_patchrev.patch::$_patchurl/firefox/firefox-branded-icons.patch
	firefox-kde-$_patchrev.patch::$_patchurl/firefox/firefox-kde.patch
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
        # reenable system sqlite
        5022efe33088.patch
        # Fix MOZILLA#1516803
        # https://bugzilla.mozilla.org/show_bug.cgi?id=1516803
        mozilla-1516803.patch
        # Force disable elfhack to fix build errors
        build-disable-elfhack.patch
        # Revert patch from MOZILLA#1644409 to fix issue casused by this patch
        mozilla-1644409.patch::https://hg.mozilla.org/mozilla-central/raw-rev/795c8762b16b
        # MOZILLA#1667736
        0002-Bug-1667736-Update-packed_simd-to-compile-on-Rust-1..patch
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
  
  # Add globalmenu support
  patch -Np1 -i "$srcdir/unity-menubar.patch"
  
  patch -Np1 -i "$srcdir"/2000_system_harfbuzz_support.patch
  patch -Np1 -i "$srcdir"/2001_system_graphite2_support.patch
  patch -Np1 -i "$srcdir"/7002_system_av1_support.patch

  # Fix MOZILLA#1530052
  patch -Np1 -i "$srcdir"/0001-Use-remoting-name-for-GDK-application-names.patch

  # reenable system sqlite
  patch -R -p1 -i "$srcdir"/5022efe33088.patch

  # Fix MOZILLA#1516803
  # sandbox needs to be built with --param lto-partitions=1 when
  # GCC LTO is enabled
  patch -Np1 -i "$srcdir"/mozilla-1516803.patch

  # Force disable elfhack to fix build errors
  patch -Np1 -i "$srcdir"/build-disable-elfhack.patch


  # Revert patch from MOZILLA#1644409 to fix issue casused by this patch
  patch -R -p1 -i "$srcdir"/mozilla-1644409.patch

  # MOZILLLA#1667736
  # Update packed_simd to compile on Rust 1.48
  patch -Np1 -i "$srcdir"/0002-Bug-1667736-Update-packed_simd-to-compile-on-Rust-1..patch


  if [ $_pgo ] ; then
    # add missing rule for pgo builds
    patch -Np1 -i "$srcdir"/add_missing_pgo_rule.patch

    patch -Np1 -i "$srcdir"/pgo.patch

    # add missing file Makefile for pgo builds
    patch -Np1 -i "$srcdir"/pgo_fix_missing_kdejs.patch

    echo "ac_add_options --enable-lto" >> .mozconfig
  fi
}

build() {
  #export CXXFLAGS="${CFLAGS}"
  cd mozilla-unified
  export MOZ_SOURCE_REPO="$_repo"
  export MOZBUILD_STATE_PATH="$srcdir/mozbuild"
  export MOZ_APP_REMOTINGNAME=$pkgname
  export CARGO_HOME="$srcdir"/.cargo
  export MACH_USE_SYSTEM_PYTHON=1

  export CC=gcc
  export CXX=g++
  export AR="gcc-ar"
  export NM="gcc-nm"
  export RANLIB="gcc-ranlib"

  export MOZ_MAKE_FLAGS="$MAKEFLAGS"
  export MOZ_SMP_FLAGS="$MAKEFLAGS"
  export STRIP=/bin/true

  if [[ -n $_lowmem || $CARCH == i686 ]]; then
    LDFLAGS+=" -Xlinker --no-keep-memory"
  fi

  if [[ -n $_pgo ]]; then
    export DISPLAY=:99
    export MOZ_PGO=1

    export TMPDIR="$srcdir/tmp"
    mkdir -p "$TMPDIR"

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
         'd7bf65ba1d9f606545dcf887d23bec9f'
         'a26a061efb4def6572d5b319d657f1d6'
         '4c23d9c0a691d70919beb1dafbbecbd3'
         '05bb69d25fb3572c618e3adf1ee7b670'
         'c0f68250d27f208efcdee710207cd3e4'
         '77c039d55aa155391db518afd638a0b9'
         '93fc217bcdc9d936727a1c3446e72650'
         '0a5733b7a457a2786c2dd27626a1bf88'
         '2a23fc0920f7b2cb4f9a2a751fa060eb'
         'fe24f5ea463013bb7f1c12d12dce41b2'
         '3c383d371d7f6ede5983a40310518715'
         'd24681f9a46ae23689b2867f4ab6eaae'
         'dbb578ee6ef93f0d28584d38904fac70'
         'f867ae41a722630cc5567e2dcc51676d'
         '1e473ebbf9e5d648e498c58dd6c789e6'
         '7b479b606ce2580f786a021cc0c3c5a1'
         '129f1d0a83a9034e49c8ff62f5e0013d'
         'efcddfb6595b356b3faaf6b93313659e'
         'aa9261c4d407cf809bf8275e6f2e52c7'
         '7c42a1e4928330d82409283e9af6422c'
         'f0621d7f3d1a09d43dacf4da7871354c')
