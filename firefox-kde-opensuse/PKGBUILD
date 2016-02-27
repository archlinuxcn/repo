# Contributor: Weng Xuetian <wengxt@gmail.com>
# Maintainer: Thaodan <theodorstormgrade@gmail.com>

# enable this if you run out of memory during linking
#_lowmem=true

# enable gtk3 (warning: flash or any other plugin  crashes frequently)
_gtk3=true

# try to build with PGO
_pgo=false

_pkgname=firefox
pkgname=$_pkgname-kde-opensuse
pkgver=44.0.2
pkgrel=4
pkgdesc="Standalone web browser from mozilla.org with OpenSUSE patch, integrate better with KDE"
arch=('i686' 'x86_64')
license=('MPL' 'GPL' 'LGPL')
url="https://build.opensuse.org/package/show/mozilla:Factory/MozillaFirefox"
depends=('gtk2' 'mozilla-common' 'libxt' 'startup-notification' 'mime-types'
         'dbus-glib' 'alsa-lib' 'desktop-file-utils' 'hicolor-icon-theme'
	 'libvpx' 'icu'  'libevent' 'nss>=3.18.1' 'nspr>=4.10.6' 'hunspell'
	 'sqlite' 'libnotify' 'kmozillahelper' 'ffmpeg' )
if [ $_gtk3 ] ; then
    depends+=('gtk3')
fi

makedepends=('unzip' 'zip' 'diffutils' 'python2' 'yasm' 'mesa' 'imake'
             'xorg-server-xvfb' 'libpulse' 'inetutils')
optdepends=('networkmanager: Location detection via available WiFi networks'
	    'upower: Battery API' )
provides=("firefox=${pkgver}")
conflicts=('firefox')
install=firefox.install
_patchrev=11475705ab0f
options=('!emptydirs'  'strip' )
_patchurl=http://www.rosenauer.org/hg/mozilla/raw-file/$_patchrev
source=(https://ftp.mozilla.org/pub/mozilla.org/firefox/releases/$pkgver/source/firefox-$pkgver.source.tar.xz
        mozconfig firefox.desktop firefox-install-dir.patch vendor.js kde.js firefox-fixed-loading-icon.png
	rhbz-966424.patch
	# Firefox patchset
	$_patchurl/firefox-branded-icons.patch
	$_patchurl/firefox-kde.patch
	$_patchurl/firefox-no-default-ualocale.patch
	# Gecko/toolkit patchset
	$_patchurl/mozilla-kde.patch
	$_patchurl/mozilla-language.patch
	$_patchurl/mozilla-nongnome-proxies.patch
	unity-menubar.patch
	add_missing_pgo_rule.patch
        pgo_fix_missing_kdejs.patch
	firefox-quicktime.patch
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
_mozilla_api_key=16674381-f021-49de-8622-3021c5942aff


prepare() {
  cd $_pkgname-$pkgver

  cp "$srcdir/mozconfig" .mozconfig

  patch -Np1 -i "$srcdir/firefox-install-dir.patch"

  
  echo -n "$_google_api_key" >google-api-key
  echo "ac_add_options --with-google-api-keyfile=\"$PWD/google-api-key\"" >>.mozconfig

  echo -n "$_google_default_client_id $_google_default_client_secret" >google-oauth-api-key
  echo "ac_add_options --with-google-oauth-api-keyfile=\"$PWD/google-oauth-api-key\"" >>.mozconfig

  echo -n "$_mozilla_api_key" >mozilla-api-key
  echo "ac_add_options --with-mozilla-api-keyfile=\"$PWD/mozilla-api-key\"" >>.mozconfig
  
  # https://bugs.archlinux.org/task/41689
  patch -Np1 -i "$srcdir/rhbz-966424.patch"

  # FS#47953 - [firefox] 44.0-1 breaks mp4a audio stream playback capability 
  # https://bugzilla.mozilla.org/show_bug.cgi?id=1244523
  patch -Np1 -i "$srcdir"/firefox-quicktime.patch
  
  msg "Patching for KDE"
  patch -Np1 -i "$srcdir/mozilla-nongnome-proxies.patch"
  patch -Np1 -i "$srcdir/mozilla-kde.patch"
  patch -Np1 -i "$srcdir/mozilla-language.patch"

  patch -Np1 -i "$srcdir/firefox-kde.patch"
  patch -Np1 -i "$srcdir/firefox-no-default-ualocale.patch"
  patch -Np1 -i "$srcdir/firefox-branded-icons.patch"
  # add globalmenu support
  patch -Np1 -i "$srcdir/unity-menubar.patch"

  # add missing rule for pgo builds
  patch -Np1 -i "$srcdir"/add_missing_pgo_rule.patch

  # add missing file Makefile for pgo builds
  patch -Np1 -i "$srcdir"/pgo_fix_missing_kdejs.patch
  # enable gtk3
  if [ $_gtk3 ] ; then
     # fix gtk3 build
     sed -i 's|parent->group|gtk_window_get_group(const_cast<GtkWindow*>(parent))|g' \
	 toolkit/xre/nsKDEUtils.cpp
     echo 'ac_add_options --enable-default-toolkit=cairo-gtk3' >>.mozconfig
  fi
  # configure script misdetects the preprocessor without an optimization level
  # https://bugs.archlinux.org/task/34644
  sed -i '/ac_cpp=/s/$CPPFLAGS/& -O2/' configure

  # WebRTC build tries to execute "python" and expects Python 2
  mkdir -p "$srcdir/path"
  ln -sf /usr/bin/python2 "$srcdir/path/python"

  # Fix tab loading icon (flickers with libpng 1.6)
  # https://bugzilla.mozilla.org/show_bug.cgi?id=841734
  # TODO: Remove this; Firefox 34 might use CSS animations for the loading icon
  # https://bugzilla.mozilla.org/show_bug.cgi?id=759252
  cp "$srcdir/firefox-fixed-loading-icon.png" \
    browser/themes/linux/tabbrowser/loading.png
}

build() {

  cd $_pkgname-$pkgver

  export PATH="$srcdir/path:$PATH"
  export LDFLAGS="$LDFLAGS -Wl,-rpath,/usr/lib/firefox"
  export PYTHON="/usr/bin/python2"
  export CPPFLAGS="$CPPFLAGS -mno-avx"

  if [[ -n $_lowmem || $CARCH == i686 ]]; then
    LDFLAGS+=" -Wl,--no-keep-memory"
  fi

  if [[ -n $_pgo ]]; then
    # Do PGO
    xvfb-run -a -s "-extension GLX -screen 0 1280x1024x24" \
      make -f client.mk build MOZ_PGO=1
  else
    make -f client.mk build
  fi
}

package() {
  cd $_pkgname-$pkgver

  [[ "$CARCH" == "i686" ]] && cp "$srcdir/kde.js" obj-i686-pc-linux-gnu/dist/bin/defaults/pref
  [[ "$CARCH" == "x86_64" ]] && cp "$srcdir/kde.js" obj-x86_64-unknown-linux-gnu/dist/bin/defaults/pref

  make -f client.mk DESTDIR="$pkgdir" INSTALL_SDK= install

  install -Dm644 "$srcdir/vendor.js" "$pkgdir/usr/lib/firefox/browser/defaults/preferences/vendor.js"
  install -Dm644 "$srcdir/kde.js" "$pkgdir/usr/lib/firefox/browser/defaults/preferences/kde.js"

  for i in 16 22 24 32 48 256; do
      install -Dm644 browser/branding/official/default$i.png \
        "$pkgdir/usr/share/icons/hicolor/${i}x${i}/apps/firefox.png"
  done

  install -Dm644 browser/branding/official/content/icon64.png \
    "$pkgdir/usr/share/icons/hicolor/64x64/apps/firefox.png"
  install -Dm644 browser/branding/official/mozicon128.png \
    "$pkgdir/usr/share/icons/hicolor/128x128/apps/firefox.png"
  install -Dm644 browser/branding/official/content/about-logo.png \
    "$pkgdir/usr/share/icons/hicolor/192x192/apps/firefox.png"
  install -Dm644 browser/branding/official/content/about-logo@2x.png \
    "$pkgdir/usr/share/icons/hicolor/384x384/apps/firefox.png"

  install -Dm644 "$srcdir/firefox.desktop" "$pkgdir/usr/share/applications/firefox.desktop"

  # Use system-provided dictionaries
  rm -rf "$pkgdir"/usr/lib/firefox/{dictionaries,hyphenation}
  ln -s /usr/share/hunspell "$pkgdir/usr/lib/firefox/dictionaries"
  ln -s /usr/share/hyphen "$pkgdir/usr/lib/firefox/hyphenation"

  #workaround for now
  #https://bugzilla.mozilla.org/show_bug.cgi?id=658850
  ln -sf firefox "$pkgdir/usr/lib/firefox/firefox-bin"
}

sha256sums=('0bb28841a9268c50cbb239f759f16f55b3a624f679c68965158beaa0a83a2d9e'
            '633084aa03336088e087f39eb55b212cc97b11d27a4b288a87f75148350be4dd'
            'c202e5e18da1eeddd2e1d81cb3436813f11e44585ca7357c4c5f1bddd4bec826'
            'd86e41d87363656ee62e12543e2f5181aadcff448e406ef3218e91865ae775cd'
            '4b50e9aec03432e21b44d18c4c97b2630bace606b033f7d556c9d3e3eb0f4fa4'
            'b8cc5f35ec35fc96ac5c5a2477b36722e373dbb57eba87eb5ad1276e4df7236d'
            '68e3a5b47c6d175cc95b98b069a15205f027cab83af9e075818d38610feb6213'
            '746cb474c5a2c26fc474256e430e035e604b71b27df1003d4af85018fa263f4a'
            '0ac532cb40be8057225032a000587e1fb7936dd06607e79a69064b10d436afd5'
            '8255adfb5289505c98c2f0aa534c5e63c4750e867552f6c6f9199e03d2cc9bc8'
            '02e92f84dd31ed079be3e67509cf23d0d351e06bb690fcc091c904d906d2d690'
            '0d764c620fc2853803fca31e8b9ca1b44620ccfccceffc78f0e9af652ca80ea0'
            'feede2fb86527c4a5d90bd5458fe582da920ab02dd25ec656236d87caf8888ba'
            'e8289ea4c1f8191e1e23661312ceee2128b8e790501b9a589d0d7bfc4384553f'
            'aaf7d17559777320b7380d185fce0fd0ba455c8bc83140a005dedffcdedfc5d7'
            'f9067f62a25a7a77276e15f91cc9e7ba6576315345cfc6347b1b2e884becdb0c'
            '2797d1e61031d24ee24bf682c9447b3b9c1bca10f8e6cbd597b854af2de1ec54'
            '6b731ca36e7688aeb24685da702e0af0475e6671072fc96464fbbed49d0bbd50')
