# Maintainer: Figue <ffigue at gmail>
# Contributor (Parabola): fauno <fauno@kiwwwi.com.ar>
# Thank you very much to the older contributors:
# Contributor: evr <evanroman at gmail>
# Contributor: Muhammad 'MJ' Jassim <UnbreakableMJ@gmail.com> 

pkgname=icecat
pkgver=78.6.0
pkgrel=1
_commit=a43514623e93d4f3fe6d61f5b2f82c5ef29bf518
pkgdesc="GNU version of the Firefox browser."
arch=(x86_64)
url="http://www.gnu.org/software/gnuzilla/"
license=('GPL' 'MPL' 'LGPL')
depends=(gtk3 mozilla-common libxt startup-notification mime-types dbus-glib
         ffmpeg nss ttf-font libpulse)
makedepends=(m4 unzip zip diffutils python2-setuptools yasm mesa imake inetutils
             xorg-server-xvfb autoconf2.13 rust clang llvm jack gtk2
             python nodejs python2-psutil cbindgen nasm wget mercurial git lld)
optdepends=('networkmanager: Location detection via available WiFi networks'
            'libnotify: Notification integration'
            'pulseaudio: Audio support'
            'speech-dispatcher: Text-to-Speech'
            'hunspell-en_US: Spell checking, American English')
options=(!emptydirs !makeflags !strip)

source=(https://git.savannah.gnu.org/cgit/gnuzilla.git/snapshot/gnuzilla-${_commit}.tar.gz
        icecat.desktop icecat-safe.desktop
        "0001-Use-remoting-name-for-GDK-application-names.patch::https://raw.githubusercontent.com/archlinux/svntogit-packages/0adcedc05ce67d53268575f8801c8de872206901/firefox/trunk/0001-Use-remoting-name-for-GDK-application-names.patch"
        rust_1.48.patch.gz)

sha256sums=('d8938711584023476abb88d93bd36a7141ecdf4ac890e71ebc0666caad93775e'
            'e00dbf01803cdd36fd9e1c0c018c19bb6f97e43016ea87062e6134bdc172bc7d'
            '33dd309eeb99ec730c97ba844bf6ce6c7840f7d27da19c82389cdefee8c20208'
            'e0eaec8ddd24bbebf4956563ebc6d7a56f8dada5835975ee4d320dd3d0c9c442'
            'd32c87c4526e897d64453914da43f99366d1d0b7d71e43b4027a6cb5aa274040')

prepare() {
  cd gnuzilla-${_commit}

  # Uncomment if you have issues with gpg download... WITH PROXY gpg doesn't work!!!!!!
  #sed -e 's/^gpg2 --keyserver.*//g' -i makeicecat

  mkdir output || rm -rf output/*  # Clean output just in case is already an old build there
  if [ -f "${startdir}/firefox-${pkgver}esr.source.tar.xz" ]; then cp -f "${startdir}/firefox-${pkgver}esr.source.tar.xz" output/ ; fi

  # Patches to avoid download sources if you have in your $startdir
  sed -e '/rm -rf output/d' -i makeicecat
  sed -e 's/wget -N/wget -nv -Nc/g' -i makeicecat

  # Other patches
  sed -e 's/^gpg2 /gpg /g' -i makeicecat
  sed -e 's/^gpg.*list-keys.*//g' -i makeicecat
  sed -e 's/^tar cfj icecat-/#tar cfj icecat-/g' -i makeicecat

  # rename patches
  patch --ignore-whitespace << 'EOF'
--- makeicecat	2020-09-21 23:59:38.942240104 +0200
+++ makeicecat.new	2020-09-22 00:06:29.240253121 +0200
@@ -270,9 +270,12 @@
 ###############################################################################
 
 # Replace Firefox branding
-find . | tac | grep -i fennec  | prename --nofullpath -E 's/fennec/icecatmobile/;' -E 's/Fennec/IceCatMobile/;'
-find . | tac | grep -i firefox | prename --nofullpath -E 's/firefox/icecat/;' -E 's/Firefox/IceCat/;'
-find services/fxaccounts/rust-bridge | tac | prename --nofullpath -E 's/icecat-accounts/firefox-accounts/;' -E 's/IceCatAccounts/FirefoxAccounts/;'
+find . -iname "*fennec*" | tac | xargs -i rename -v 'fennec' 'icecatmobile' "{}" || true
+find . -iname "*fennec*" | tac | xargs -i rename -v 'Fennec' 'IceCatMobile' "{}" || true
+find . -iname "*firefox*" | tac | xargs -i rename -v 'firefox' 'icecat' "{}" || true
+find . -iname "*firefox*" | tac | xargs -i rename -v 'Firefox' 'IceCat' "{}" || true
+find services/fxaccounts/rust-bridge -iname "*icecat-accounts*" | tac | xargs -i rename -v 'icecat-accounts' 'firefox-accounts' "{}" || true
+find services/fxaccounts/rust-bridge -iname "*icecat-accounts*" | tac | xargs -i rename -v 'IceCatAccounts' 'FirefoxAccounts' "{}" || true
 
 echo "Running batch rebranding"
 SEDSCRIPT="
@@ -337,7 +337,7 @@
 
 sed 's/mozilla-bin/icecat-bin/' -i build/unix/run-mozilla.sh
 
-find . | tac | grep run-mozilla | prename --nofullpath -E 's/mozilla/icecat/;'
+find . -iname "*run-mozilla*" | tac | xargs -i rename -v 'mozilla' 'icecat' "{}" || true
 
 # do not alter useragent/platform/oscpu/etc with fingerprinting countermeasure, it makes things worse
 sed '/ShouldResistFingerprinting/,/}/s/^/\/\//' -i ./netwerk/protocol/http/nsHttpHandler.cpp
EOF

  # If we want to avoid all locales, we can use variable _SPEED=y to avoid them
  if [[ $_SPEED =~ [y|Y] ]]; then
    msg2 "Building without all locales..."
    #sed -e '/#\[ \$line = \"es-ES\" \]/,${s//\[ \$line = \"es-ES\" \]/;b};$q1' -e '/\[ \$line = \"en-US\" \]/d' -i makeicecat
    sed -e 's;\$SOURCEDIR/browser/locales/shipped-locales;\.\./custom-shipped-locales;g' -i makeicecat
    echo es-ES > custom-shipped-locales
    rm -rf data/files-to-append/l10n/*
  fi

  # Produce IceCat sources
  bash makeicecat
  cd output/icecat-${pkgver}

  # https://bugzilla.mozilla.org/show_bug.cgi?id=1530052
  patch -Np1 -i ../../../0001-Use-remoting-name-for-GDK-application-names.patch

  # https://bugzilla.mozilla.org/show_bug.cgi?id=1667736
  patch -Np1 -i ../../../rust_1.48.patch

  # Patch to move files directly to /usr/lib/icecat. No more symlinks.
  sed -e 's;$(libdir)/$(MOZ_APP_NAME)-$(MOZ_APP_VERSION);$(libdir)/$(MOZ_APP_NAME);g' -i config/baseconfig.mk
  sed -e 's;$(libdir)/$(MOZ_APP_NAME)-devel-$(MOZ_APP_VERSION);$(libdir)/$(MOZ_APP_NAME)-devel;g' -i config/baseconfig.mk

  printf '%b' "  \e[1;36m->\e[0m\033[1m Starting build...\n"
  
  cat >./mozconfig <<END
ac_add_options --enable-application=browser

ac_add_options --prefix=/usr
ac_add_options --enable-release
ac_add_options --enable-hardening
ac_add_options --enable-optimize
ac_add_options --enable-rust-simd
ac_add_options --enable-linker=lld
ac_add_options --disable-elf-hack
export CC='clang --target=x86_64-unknown-linux-gnu'
export CXX='clang++ --target=x86_64-unknown-linux-gnu'
export AR=llvm-ar
export NM=llvm-nm
export RANLIB=llvm-ranlib

# Branding
ac_add_options --enable-official-branding
ac_add_options --with-distribution-id=org.gnu
ac_add_options --with-unsigned-addon-scopes=app,system

# System libraries
ac_add_options --with-system-nspr
ac_add_options --with-system-nss

# Features
ac_add_options --enable-alsa
ac_add_options --enable-jack
ac_add_options --disable-crashreporter
ac_add_options --disable-updater
ac_add_options --disable-tests
ac_add_options --disable-eme

ac_add_options --with-app-basename=icecat
ac_add_options --with-app-name=icecat
END
}

build() {
  cd gnuzilla-${_commit}/output/icecat-${pkgver}

  # LTO needs more open files
  ulimit -n 4096

  # -fno-plt with cross-LTO causes obscure LLVM errors
  # LLVM ERROR: Function Import: link error
  #CFLAGS="${CFLAGS/-fno-plt/}"
  #CXXFLAGS="${CXXFLAGS/-fno-plt/}"

  xvfb-run -a -n 97 -s "-screen 0 1600x1200x24" ./mach build
  ./mach buildsymbols

}

package () {
  cd gnuzilla-${_commit}/output/icecat-${pkgver}

  # Remove cose.manifest and cose.sig cause march install fails
  find obj-x86_64-pc-linux-gnu/dist/bin/browser/extensions -name cose.manifest -delete
  find obj-x86_64-pc-linux-gnu/dist/bin/browser/extensions -name cose.sig -delete

  DESTDIR="$pkgdir" ./mach install

  local _vendorjs="$pkgdir/usr/lib/${pkgname}/browser/defaults/preferences/vendor.js"
  install -Dvm644 /dev/stdin "$_vendorjs" <<END
// Use LANG environment variable to choose locale
pref("intl.locale.requested", "");

// Disable default browser checking.
pref("browser.shell.checkDefaultBrowser", false);

// Opt all of us into e10s, instead of just 50%
pref("browser.tabs.remote.autostart", true);
END

  local distini="$pkgdir/usr/lib/$pkgname/distribution/distribution.ini"
  install -Dvm644 /dev/stdin "$distini" <<END
[Global]
id=archlinux
version=1.0
about=GNU IceCat for Arch Linux

[Preferences]
app.distributor=archlinux
app.distributor.channel=$pkgname
app.partner.archlinux=archlinux
END

  printf '%b' "  \e[1;36m->\e[0m\033[1m Finishing...\n"
  install -m755 -d ${pkgdir}/usr/share/applications
  install -m755 -d ${pkgdir}/usr/share/pixmaps

  for i in 16 32 48; do
      install -Dm644 browser/branding/official/default${i}.png \
      "$pkgdir/usr/share/icons/hicolor/${i}x${i}/apps/icecat.png"
  done
  install -Dm644 browser/branding/official/default48.png ${pkgdir}/usr/share/pixmaps/icecat.png
  install -Dm644 ${srcdir}/icecat.desktop ${pkgdir}/usr/share/applications/
  install -Dm644 ${srcdir}/icecat-safe.desktop ${pkgdir}/usr/share/applications/
}
