# Maintainer: Figue <ffigue at gmail>
# Contributor (Parabola): fauno <fauno@kiwwwi.com.ar>
# Thank you very much to the older contributors:
# Contributor: evr <evanroman at gmail>
# Contributor: Muhammad 'MJ' Jassim <UnbreakableMJ@gmail.com> 

pkgname=icecat
pkgver=102.7.0
pkgrel=1
_commit=7f76da3cfd5d04fa38d894f6ea6ac5f2fd0ea837
pkgdesc="GNU version of the Firefox browser."
arch=(x86_64)
url="http://www.gnu.org/software/gnuzilla/"
license=('GPL' 'MPL' 'LGPL')
depends=(gtk3 libxt mime-types dbus-glib ffmpeg nss ttf-font libpulse)
makedepends=(m4 unzip zip diffutils python-setuptools python-jsonschema yasm mesa imake inetutils
             xorg-server-xvfb autoconf2.13 rust clang llvm jack gtk2
             python nodejs python-psutil cbindgen nasm wget mercurial git lld perl-rename
             wasi-compiler-rt wasi-libc wasi-libc++ wasi-libc++abi)
optdepends=('networkmanager: Location detection via available WiFi networks'
            'libnotify: Notification integration'
            'pulseaudio: Audio support'
            'speech-dispatcher: Text-to-Speech'
            'hunspell-en_US: Spell checking, American English'
            'xdg-desktop-portal: Screensharing with Wayland')
options=(!emptydirs !makeflags !strip)

source=(https://git.savannah.gnu.org/cgit/gnuzilla.git/snapshot/gnuzilla-${_commit}.tar.gz
        icecat.desktop icecat-safe.desktop)
        #'https://raw.githubusercontent.com/canonical/firefox-snap/5622734942524846fb0eb7108918c8cd8557fde3/patches/fix-ftbfs-newer-cbindgen.patch'
        #'arc4random.patch::https://hg.mozilla.org/mozilla-central/raw-rev/970ebbe54477'
        #'arc4random_buf.patch::https://hg.mozilla.org/mozilla-central/raw-rev/a61813bd9f0a')

sha256sums=('f7adb3ab04c7a3f5ab2ec358848c2f573171825cba27e70ad009e84fff5a4164'
            'e00dbf01803cdd36fd9e1c0c018c19bb6f97e43016ea87062e6134bdc172bc7d'
            '33dd309eeb99ec730c97ba844bf6ce6c7840f7d27da19c82389cdefee8c20208')

prepare() {
  cd gnuzilla-${_commit}

  # Uncomment if you have issues with gpg download... WITH PROXY gpg doesn't work!!!!!!
  #sed -e 's/^verify_sources$//g' -i makeicecat

  mkdir output || rm -rf output/*  # Clean output just in case is already an old build there
  if [ -f "${SRCDEST}/firefox-${pkgver}esr.source.tar.xz" ] && [ -f "${SRCDEST}/firefox-${pkgver}esr.source.tar.xz.asc" ]; then cp -f "${SRCDEST}"/firefox-${pkgver}esr.source.tar.xz{,.asc} output/ ; fi

  # Patches to avoid download sources if you have in your $startdir
  sed -e '/rm -rf output/d' -i makeicecat
  sed -e 's/wget -N/wget -nv -Nc/g' -i makeicecat

  # Other patches
  sed '/^finalize_sourceball$/d' -i makeicecat

  # If we want to avoid all locales, we can use variable _SPEED=y to build it with only 1 locale. Use variable _LOCALE to define it
  if [[ $_SPEED =~ [y|Y] ]]; then
    msg2 "Building without all locales..."
    sed -e 's/DEVEL=0/DEVEL=1/g' -i makeicecat
    # Also you can choose your locale using external variable _LOCALE. By default in upstream script this locale is es-ES
    [ -z "$_LOCALE" ] || sed -e "s/es-ES/$_LOCALE/g" -i makeicecat && echo "$_LOCALE" > custom-shipped-locales
    rm -rf data/files-to-append/l10n/*
  fi

  patch -p1 << 'EOF'
--- a/makeicecat	2021-10-12 17:14:08.000000000 +0200
+++ b/makeicecat	2021-10-12 17:16:43.831787739 +0200
@@ -143,16 +143,23 @@
     do which ${rename_cmd} &> /dev/null && RENAME_CMD=${rename_cmd}
     done
     readonly RENAME_CMD
-    if ! ( [[ "$( ${RENAME_CMD} --version )" =~ 'File::Rename version '([0-9]+)\.([0-9]+) ]] &&
+    if ! ( [[ "$( ${RENAME_CMD} --version )" =~ ([0-9]+)\.([0-9]+) ]] &&
                (( ${BASH_REMATCH[1]} >= MIN_RENAME_VER_MAJ )) &&
                (( ${BASH_REMATCH[2]} >= MIN_RENAME_VER_MIN )) )
     then
         required_ver=${MIN_RENAME_VER_MAJ}.${MIN_RENAME_VER_MIN}
         echo -e "\nERROR: This script requires the Perl rename program (version >= ${required_ver})
  e.g.: 'rename' from the Guix 'rename' package
-       'perl-rename' from the Parabola 'perl-file-rename' package
+       'perl-rename' from the Archlinux package or 'perl-file-rename' in the Parabola project
        'prename' from the Trisquel 'rename' package"
         return 1
+    else
+        if [[ "$( ${RENAME_CMD} --version )" =~ 'File::Rename' ]]
+        then
+            RENAME_FLAVOUR=RMBARKER
+        else
+            RENAME_FLAVOUR=PEDERST
+        fi
     fi
 
     # verify that Wget is available
@@ -562,9 +569,13 @@
 
 apply_batch_branding()
 {
-    find . | tac | grep -i fennec  | ${RENAME_CMD} --nofullpath -E 's/fennec/icecatmobile/;' -E 's/Fennec/IceCatMobile/;'
-    find . | tac | grep -i firefox | ${RENAME_CMD} --nofullpath -E 's/firefox/icecat/;' -E 's/Firefox/IceCat/;'
-
+    if [ "${RENAME_FLAVOUR}" = "PEDERST" ]
+    then
+        find . | tac | grep -i firefox | ${RENAME_CMD} 's/firefox/icecat/ if -f;'
+        find . | tac | grep -i firefox | ${RENAME_CMD} 's/Firefox/IceCat/ if -f;'
+    else
+        find . | tac | grep -i firefox | ${RENAME_CMD} --nofullpath -E 's/firefox/icecat/;' -E 's/Firefox/IceCat/;'
+    fi
     echo "Running batch rebranding (this will take a while)"
     local sed_script="
 s|marketplace\\.firefox\\.com|f-droid.org/repository/browse|g;
@@ -625,7 +636,12 @@
 
     sed 's/mozilla-bin/icecat-bin/' -i build/unix/run-mozilla.sh
 
-    find . | tac | grep run-mozilla | ${RENAME_CMD} --nofullpath -E 's/mozilla/icecat/;'
+    if [ "${RENAME_FLAVOUR}" = "PEDERST" ]
+    then
+        find . | tac | grep run-mozilla | ${RENAME_CMD} 's/mozilla/icecat/ if -f;'
+    else
+        find . | tac | grep run-mozilla | ${RENAME_CMD} --nofullpath -E 's/mozilla/icecat/;'
+    fi
 
     # do not alter useragent/platform/oscpu/etc with fingerprinting countermeasure, it makes things worse
     sed '/ShouldResistFingerprinting/,/}/s/^/\/\//' -i ./netwerk/protocol/http/nsHttpHandler.cpp
EOF

  # Produce IceCat sources
  bash makeicecat
  cd output/icecat-${pkgver}

  # https://hg.mozilla.org/mozilla-central/rev/a61813bd9f0a
  #patch -Np1 -i ../../../arc4random.patch
  #patch -Np1 -i ../../../arc4random_buf.patch

  # cbindgen
  #patch -Np1 -i ../../../fix-ftbfs-newer-cbindgen.patch

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
ac_add_options --disable-bootstrap
ac_add_options --with-wasi-sysroot=/usr/share/wasi-sysroot

# Branding
ac_add_options --enable-official-branding
ac_add_options --with-distribution-id=org.gnu
ac_add_options --with-unsigned-addon-scopes=app,system
ac_add_options --allow-addon-sideload

# System libraries
ac_add_options --with-system-nspr
ac_add_options --with-system-nss

# Features
ac_add_options --enable-alsa
ac_add_options --enable-jack
ac_add_options --disable-crashreporter
ac_add_options --disable-updater
ac_add_options --disable-tests
#ac_add_options --disable-eme

ac_add_options --with-app-basename=icecat
ac_add_options --with-app-name=icecat
END
}

build() {
  cd gnuzilla-${_commit}/output/icecat-${pkgver}

  export MOZ_NOSPAM=1
  export MOZBUILD_STATE_PATH="$srcdir/mozbuild"
  export MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE=pip
  export LDFLAGS="${LDFLAGS} -lwayland-client"

  # LTO needs more open files
  ulimit -n 4096

  ./mach build

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

// Use system-provided dictionaries
pref("spellchecker.dictionary_path", "/usr/share/hunspell");

// Disable default browser checking.
pref("browser.shell.checkDefaultBrowser", false);

// Don't disable extensions in the application directory
pref("extensions.autoDisableScopes", 11);
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

# vim:set sw=2 et:
