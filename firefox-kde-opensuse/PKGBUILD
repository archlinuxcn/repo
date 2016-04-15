# Contributor: Weng Xuetian <wengxt@gmail.com>
# Maintainer: Thaodan <theodorstormgrade@gmail.com>


# enable this if you run out of memory during linking
#_lowmem=true

# enable gtk3 (warning: flash or any other plugin  crashes frequently)
_gtk3=true

# try to build with PGO
_pgo=true

_pkgname=firefox
pkgname=$_pkgname-kde-opensuse
pkgver=45.0.2
pkgrel=1
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
_patchrev=3ccb278a9ceb
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
	unity-menubar.patch
	add_missing_pgo_rule.patch
        pgo_fix_missing_kdejs.patch
)

if [ $_gtk3 ] ; then
    source+=($_patchurl/mozilla-gtk3_20.patch)
fi
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
  patch -Np1 -i "$srcdir/unity-menubar.patch"

  # add missing rule for pgo builds
  patch -Np1 -i "$srcdir"/add_missing_pgo_rule.patch

  # add missing file Makefile for pgo builds
  patch -Np1 -i "$srcdir"/pgo_fix_missing_kdejs.patch
  # enable gtk3
  if [ $_gtk3 ] ; then
     # fix gtk3 build
   #  sed -i 's|parent->group|gtk_window_get_group(const_cast<GtkWindow*>(parent))|g' \
#	 toolkit/xre/nsKDEUtils.cpp
      echo 'ac_add_options --enable-default-toolkit=cairo-gtk3' >>.mozconfig
          patch -Np1 -i "$srcdir"/mozilla-gtk3_20.patch
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
md5sums=('deda5fcd4a41fc63cb8c14102cb8c561'
         '3bf79ce63bd0b0c11a9403ecc251c583'
         '9b02198df96be08f2a0a323ac2e6c2a2'
         'dbf14588e85812ee769bd735823a0146'
         '0d053487907de4376d67d8f499c5502b'
         '05bb69d25fb3572c618e3adf1ee7b670'
         '6e335a517c68488941340ee1c23f97b0'
         '98a1b2c0b2450d5c0737dbe8f1e571e0'
         '3a56df3cc8441da9e3ebd4dbfd184be3'
         '648958ae7db60bc16dca3f847ee9791b'
         'e98c962df7a52395459ec8b1a81ce33d'
         '903307f923a459189a5a6062ff9df38c'
         '0c684360f1df4536512d51873c1d243d'
         '06192dd34d7f6078353d4da5725d1d57'
         'fe24f5ea463013bb7f1c12d12dce41b2'
         '3fa8bd22d97248de529780f5797178af'
         'aace13105ee6e53f49c5c43d4eb582bf')
