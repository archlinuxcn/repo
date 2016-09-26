# Contributor: Weng Xuetian <wengxt@gmail.com>
# Maintainer: Thaodan <theodorstormgrade@gmail.com>


# enable this if you run out of memory during linking
#_lowmem=true

# enable gtk3 (warning: flash or any other plugin  crashes frequently)
_gtk3=true

# try to build with PGO
# currently broken
#_pgo=false

_pkgname=firefox
pkgname=$_pkgname-kde-opensuse
pkgver=49.0.1
pkgrel=1
pkgdesc="Standalone web browser from mozilla.org with OpenSUSE patch, integrate better with KDE"
arch=('i686' 'x86_64')
license=('MPL' 'GPL' 'LGPL')
url="https://build.opensuse.org/package/show/mozilla:Factory/MozillaFirefox"
depends=('gtk2' 'mozilla-common' 'libxt' 'startup-notification' 'mime-types'
         'dbus-glib' 'alsa-lib' 'hicolor-icon-theme'
	 'libvpx' 'icu'  'libevent' 'nss>=3.18.1' 'nspr>=4.10.6' 'hunspell'
	 'sqlite' 'libnotify' 'kmozillahelper' 'ffmpeg' )
if [ $_gtk3 ] ; then
    depends+=('gtk3')
fi

makedepends=('unzip' 'zip' 'diffutils' 'python2' 'yasm' 'mesa' 'imake'
             'xorg-server-xvfb' 'libpulse' 'inetutils' 'autoconf2.13' 'rust')
optdepends=('networkmanager: Location detection via available WiFi networks'
	    'upower: Battery API' )
provides=("firefox=${pkgver}")
conflicts=('firefox')
_patchrev=9fc2ebe6d7f1
options=('!emptydirs'  'strip' )
_patchurl=http://www.rosenauer.org/hg/mozilla/raw-file/$_patchrev
source=(https://ftp.mozilla.org/pub/mozilla.org/firefox/releases/$pkgver/source/firefox-$pkgver.source.tar.xz
        mozconfig firefox.desktop firefox-install-dir.patch vendor.js kde.js firefox-fixed-loading-icon.png
	# Firefox patchset
	$_patchurl/firefox-branded-icons.patch
	$_patchurl/firefox-kde.patch
	$_patchurl/firefox-no-default-ualocale.patch
	# Gecko/toolkit patchset
	$_patchurl/mozilla-kde.patch
	$_patchurl/mozilla-language.patch
	$_patchurl/mozilla-nongnome-proxies.patch
        $_patchurl/mozilla-flex_buffer_overrun.patch
	unity-menubar.patch
	add_missing_pgo_rule.patch
        pgo_fix_missing_kdejs.patch
        rb39193.patch
        fix_mozalloc.patch
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
  
  msg "Patching for KDE"
  patch -Np1 -i "$srcdir/mozilla-nongnome-proxies.patch"
  patch -Np1 -i "$srcdir/mozilla-kde.patch"
  patch -Np1 -i "$srcdir/mozilla-language.patch"

  patch -Np1 -i "$srcdir/firefox-kde.patch"
  patch -Np1 -i "$srcdir/firefox-no-default-ualocale.patch"
  patch -Np1 -i "$srcdir/firefox-branded-icons.patch"
  # add globalmenu support
  #patch -Np1 -i "$srcdir/unity-menubar.patch"

  # add missing rule for pgo builds
  patch -Np1 -i "$srcdir"/add_missing_pgo_rule.patch

  # add missing file Makefile for pgo builds
  patch -Np1 -i "$srcdir"/pgo_fix_missing_kdejs.patch

  # configure script misdetects the preprocessor without an optimization level
  # https://bugs.archlinux.org/task/34644
  # sed -i '/ac_cpp=/s/$CPPFLAGS/& -O2/' configure

  # CVE-2016-6354 (bmo#1292534)
  patch -Np1 -i "$srcdir"/mozilla-flex_buffer_overrun.patch
  
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
  export PYTHON="/usr/bin/python2"
  
  # _FORTIFY_SOURCE causes configure failures
  CPPFLAGS+=" -O2"

  # GCC 6
  CFLAGS+=" -fPIC -fno-delete-null-pointer-checks -fno-lifetime-dse -fno-schedule-insns2"
  CXXFLAGS+=" -fPIC -fno-delete-null-pointer-checks -fno-lifetime-dse -fno-schedule-insns2"

  # Hardening
  LDFLAGS+=" -Wl,-z,now"

  if [[ -n $_lowmem || $CARCH == i686 ]]; then
    LDFLAGS+=" -Xlinker --no-keep-memory"
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
  [[ "$CARCH" == "x86_64" ]] && cp "$srcdir/kde.js" obj-x86_64-pc-linux-gnu/dist/bin/defaults/pref

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
md5sums=('3ce01741b9eab6a2988b970127330dcd'
         '169f583544e9efaf1f80f8548b57a8cc'
         '14e0f6237a79b85e60256f4808163160'
         'dbf14588e85812ee769bd735823a0146'
         '0d053487907de4376d67d8f499c5502b'
         '05bb69d25fb3572c618e3adf1ee7b670'
         '6e335a517c68488941340ee1c23f97b0'
         '3b3eb8c2747429887e4a03537932eac5'
         'edb29c1ac737a2a2ecdfd499bd30237a'
         '1fad9a988826d69fe712ea973e43f6da'
         '7b8cf4883062938956f202d04af47411'
         '903307f923a459189a5a6062ff9df38c'
         '0c684360f1df4536512d51873c1d243d'
         '01af53dc830d00fe522c545bcc0ec4b9'
         'eb6771472c8c5f67331256c7f5a692da'
         'fe24f5ea463013bb7f1c12d12dce41b2'
         '3fa8bd22d97248de529780f5797178af'
         '43550e772f110a338d5a42914ee2c3a6'
         '0c1ed789c06297659137a2ed2ef769f7')
