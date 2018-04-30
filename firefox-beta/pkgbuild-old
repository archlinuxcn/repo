# $Id$
# Maintainer: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>
# Contributor: Ionut Biru <ibiru@archlinux.org>
# Contributor: Jakub Schmidtke <sjakub@gmail.com>

pkgname=firefox-beta
name=firefox-beta
pkgver=58.0.16
pkgrel=4
ver=58.0b16
pkgdesc="Standalone web browser from mozilla.org, with telemetry, webrtc and signing disabled"
arch=(i686 x86_64)
license=(MPL GPL LGPL)
url="https://www.mozilla.org/firefox/"
depends=(gtk3 gtk2 mozilla-common libxt startup-notification mime-types dbus-glib ffmpeg
         nss hunspell sqlite ttf-font libpulse)
makedepends=(unzip zip diffutils python2 yasm mesa imake gconf inetutils xorg-server-xvfb
             autoconf2.13 rust mercurial clang llvm jack)
optdepends=('networkmanager: Location detection via available WiFi networks'
            'libnotify: Notification integration'
            'pulseaudio: Audio support'
            'speech-dispatcher: Text-to-Speech')
options=(!emptydirs !makeflags !strip)
source=("https://archive.mozilla.org/pub/firefox/releases/$ver/source/firefox-$ver.source.tar.xz"
        https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/$name.desktop 
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/firefox-symbolic.svg 
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/firefox-install-dir.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/1000_gentoo_install_dir.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/1001_add_gentoo_preferences.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/1002_drop_build_id.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/1003_gentoo_specific_pgo.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/1004_fix_hardened_pie_detection.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/1005_fix_fortify_sources.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/2001_system_harfbuzz.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/2002_system_graphite2.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/2003_musl_fix_gettid_inclusion.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/2004_nICEr-implicit-decls.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/6001_add_missing_header_for_basename.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/6002_add_alternate_name_for_private_siginfo_struct_member.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/6003_fix_syscall_wrappers_on_musl.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/6004_musl_drop_alloc_hooks.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/6005_musl_memory_report.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/6006_musl_pthread_setname.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/6007_musl_fix_tools.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/firefox-52-disable-data-sharing-infobar.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/firefox-52-disable-location.services.mozilla.com.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/firefox-52-disable-telemetry.patch
https://raw.githubusercontent.com/bn0785ac/firefox-beta/master/id.patch
)

sha256sums=('ebb8b570f5760078508101b281f1c6f0cda2e218d32bfea03b49bd0549cbb785'
            'd6b4c91a7fe77f9a335b44b943e120ce44511e46bbb16ae305cc82b4c3db66cd'
            'a2474b32b9b2d7e0fb53a4c89715507ad1c194bef77713d798fa39d507def9e9'
            'd86e41d87363656ee62e12543e2f5181aadcff448e406ef3218e91865ae775cd'
            'f337793c7ba07d2e2d4df9a8adf8e47da3ed61f2ef77330c673a521361614b44'
            '3a3ebfc60dc7f307faad86bbd4b19ddf3831c79e5ac48a6e844ee4f11700c493'
            '9595a3be842a1bb40076d70ffec2b09dc8b9d9318b7cbf226229dda6f3aad26d'
            '765d9670345a02cadd56b7f6e9c931961ec79632187ab88a304cd6313c00deab'
            'f112c7b500c281d429669f92b39efa9990bdee2b178b9474150adf0c0d403652'
            '34cf4e33dc1ff6bd4416ec91ea27cdd8b4149be37c97c1c38910193a38abd232'
            '9fb4323d9afc43486ba26d6b0233583c9a8735f18f60c368125385be8cd22bd9'
            '9c24e722d560ad62ee6672577742674d1479f955bb2ae5b7ef5b91eff0dde408'
            '33ed936b143342969d2cf86d7724fe86954724ad6a65ce6a3fc6df662e7df865'
            '10956f70de73d726ee8e6e71ace291cf842f78b3b91faa3f8868ac36c11c7387'
            '6f51f713abe4f6c5955b38d10d4ba266a4cee538719e0b7681fecec56b916d39'
            '0c8a66e4a787edf48d4c4b88cafa3e284dea6f9f523b5a370ad3a52fdf39a797'
            '45d5f114fe589fc789dc7c981cfe5aea29a90fd60aa00b4a59a356440343c793'
            '878f1f071f8cd1259bd00674bfa02df49a7eb1a84da94ed7919cc900a7b3999f'
            'b74b1a880065e4b6598206265fca5376165190291ddf2df51671eed7aaadfb19'
            '9d918abce2abaa8633a56b5509f088fb0524c5b0134a062c6f00175f6f23329e'
            '2b4a1780670ceb6e2022153f3c35f82e4c40d19ac67dbeaf47f53bd5be6fedbb'
            'bdad68eafe110b9f94a0e025635e32a6ab53e2f9adcd594c8dd2e3225f6453ab'
            '8d9afa1f940a9dac689ead40a57990d1491f34a1787b2222f8f5b5e485d54103'
            '24019d3d7e6b169087d4515db9d3a179239d1e4fe726f0906f6f26877c726040'
            'd86e41d87363656ee62e12543e2f5181aadcff448e406ef3218e91865ae775cd'
            'ef2647ee1b82d46f3bd4b503e3e0ea7350360e898ab1272b82d6892b75eba5f6')


# Google API keys (see http://www.chromium.org/developers/how-tos/api-keys)
# Note: These are for Arch Linux use ONLY. For your own distribution, please
# get your own set of keys. Feel free to contact foutrelis@archlinux.org for
# more information.


# Mozilla API keys (see https://location.services.mozilla.com/api)
# Note: These are for Arch Linux use ONLY. For your own distribution, please
# get your own set of keys. Feel free to contact heftig@archlinux.org for
# more information.


prepare() {
  mkdir path
  ln -s /usr/bin/python2 path/python

  cd firefox-$ver
  patch -Np1 -i ../id.patch



patch -Np1 -i ../firefox-52-disable-data-sharing-infobar.patch
patch -Np1 -i ../firefox-52-disable-location.services.mozilla.com.patch
patch -Np1 -i ../firefox-52-disable-telemetry.patch



  cat >.mozconfig <<END
ac_add_options --enable-application=browser

ac_add_options --prefix=/usr
ac_add_options --enable-release
ac_add_options --enable-gold
ac_add_options --enable-pie
ac_add_options --enable-optimize="-O2"
ac_add_options --disable-stylo

# Branding
ac_add_options --enable-official-branding
ac_add_options --enable-update-channel=release
ac_add_options --with-distribution-id=org.archlinux
export MOZILLA_OFFICIAL=1
export MOZ_TELEMETRY_REPORTING=0
export MOZ_ADDON_SIGNING=1
export MOZ_REQUIRE_SIGNING=0

# Keys
# System libraries
ac_add_options --with-system-zlib
ac_add_options --with-system-bz2
ac_add_options --enable-system-hunspell
ac_add_options --enable-system-sqlite
ac_add_options --enable-system-ffi
ac_add_options --disable-gamepad
ac_add_options --disable-necko-wifi 
ac_add_options --disable-webspeech
ac_add_options --disable-webrtc

# Features
ac_add_options --enable-alsa
ac_add_options --enable-jack
ac_add_options --enable-startup-notification
ac_add_options --enable-crashreporter
ac_add_options --disable-updater

ac_add_options --disable-debug
ac_add_options --disable-debug-symbols
ac_add_options --disable-tests
ac_add_options --disable-parental-controls
ac_add_options --disable-accessibility


# faster build 
ac_add_options --disable-tests

# please put 1.25 times your number of threads

mk_add_options MOZ_MAKE_FLAGS="-j10"

END
}

build() {
  cd firefox-$ver

  # _FORTIFY_SOURCE causes configure failures
  CPPFLAGS+=" -O2"

  export PATH="$srcdir/path:$PATH"
  export MOZ_SOURCE_REPO="$_repo"

  # Do PGO
  #xvfb-run -a -n 95 -s "-extension GLX -screen 0 1280x1024x24" \
  #  MOZ_PGO=1 ./mach build
  ./mach build
  ./mach buildsymbols
}

package() {
  cd firefox-$ver
  DESTDIR="$pkgdir" ./mach install
  find . -name '*crashreporter-symbols-full.zip' -exec cp -fvt "$startdir" {} +

  _vendorjs="$pkgdir/usr/lib/$name/browser/defaults/preferences/vendor.js"
  install -Dm644 /dev/stdin "$_vendorjs" <<END
// Use LANG environment variable to choose locale
pref("intl.locale.matchOS", true);

// Disable default browser checking.
pref("browser.shell.checkDefaultBrowser", false);

// Don't disable our bundled extensions in the application directory
pref("extensions.autoDisableScopes", 11);
pref("extensions.shownSelectionUI", true);

// Opt all of us into e10s, instead of just 50%
pref("browser.tabs.remote.autostart", true);
END

  _distini="$pkgdir/usr/lib/$name/distribution/distribution.ini"
  install -Dm644 /dev/stdin "$_distini" <<END
[Global]
id=archlinux
version=1.0
about=Mozilla Firefox for Arch Linux

[Preferences]
app.distributor=archlinux
app.distributor.channel=$name
app.partner.archlinux=archlinux
END

  for i in 16 22 24 32 48 256; do
    install -Dm644 browser/branding/official/default$i.png \
      "$pkgdir/usr/share/icons/hicolor/${i}x${i}/apps/$name.png"
  done
  install -Dm644 browser/branding/official/content/icon64.png \
    "$pkgdir/usr/share/icons/hicolor/64x64/apps/$name.png"
  install -Dm644 browser/branding/official/mozicon128.png \
    "$pkgdir/usr/share/icons/hicolor/128x128/apps/$name.png"
  install -Dm644 browser/branding/official/content/about-logo.png \
    "$pkgdir/usr/share/icons/hicolor/192x192/apps/$name.png"
  install -Dm644 browser/branding/official/content/about-logo@2x.png \
    "$pkgdir/usr/share/icons/hicolor/384x384/apps/$name.png"
  install -Dm644 ../firefox-symbolic.svg \
    "$pkgdir/usr/share/icons/hicolor/symbolic/apps/$name-symbolic.svg"

  install -Dm644 ../$name.desktop \
    "$pkgdir/usr/share/applications/$name.desktop"

  # Use system-provided dictionaries


  # Install a wrapper to avoid confusion about binary path

  # Replace duplicate binary with wrapper
  # https://bugzilla.mozilla.org/show_bug.cgi?id=658850


  # Use system certificates
  ln -srf "$pkgdir/usr/lib/libnssckbi.so" \
    "$pkgdir/usr/lib/$name/libnssckbi.so"



msg2 'renaming'

  ln -s "/usr/lib/firefox-beta/firefox/firefox-bin"  "$pkgdir/usr/bin/firefox-beta"


rm "$pkgdir/usr/bin/firefox"
}
