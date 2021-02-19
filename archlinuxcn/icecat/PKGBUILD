# Maintainer: Figue <ffigue at gmail>
# Contributor (Parabola): fauno <fauno@kiwwwi.com.ar>
# Thank you very much to the older contributors:
# Contributor: evr <evanroman at gmail>
# Contributor: Muhammad 'MJ' Jassim <UnbreakableMJ@gmail.com> 

pkgname=icecat
pkgver=78.7.1
pkgrel=1
_commit=bb1c105f4416c2973f394680c2d579918a1da77a
pkgdesc="GNU version of the Firefox browser."
arch=(x86_64)
url="http://www.gnu.org/software/gnuzilla/"
license=('GPL' 'MPL' 'LGPL')
depends=(gtk3 mozilla-common libxt mime-types dbus-glib ffmpeg nss ttf-font libpulse)
makedepends=(m4 unzip zip diffutils python2-setuptools yasm mesa imake inetutils
             xorg-server-xvfb autoconf2.13 rust clang llvm jack gtk2
             python nodejs python2-psutil cbindgen nasm wget mercurial git lld perl-file-rename)
optdepends=('networkmanager: Location detection via available WiFi networks'
            'libnotify: Notification integration'
            'pulseaudio: Audio support'
            'speech-dispatcher: Text-to-Speech'
            'hunspell-en_US: Spell checking, American English')
options=(!emptydirs !makeflags !strip)

source=(https://git.savannah.gnu.org/cgit/gnuzilla.git/snapshot/gnuzilla-${_commit}.tar.gz
        icecat.desktop icecat-safe.desktop
        "0001-Use-remoting-name-for-GDK-application-names.patch::https://raw.githubusercontent.com/archlinux/svntogit-packages/0adcedc05ce67d53268575f8801c8de872206901/firefox/trunk/0001-Use-remoting-name-for-GDK-application-names.patch"
        rust_1.48.patch.gz rust_1.50.patch)

sha256sums=('f8fc6889a0d6c7ebec076d90f7fe4804abb6efb03fc086e5d526b325cb1c5c37'
            'e00dbf01803cdd36fd9e1c0c018c19bb6f97e43016ea87062e6134bdc172bc7d'
            '33dd309eeb99ec730c97ba844bf6ce6c7840f7d27da19c82389cdefee8c20208'
            'e0eaec8ddd24bbebf4956563ebc6d7a56f8dada5835975ee4d320dd3d0c9c442'
            'd32c87c4526e897d64453914da43f99366d1d0b7d71e43b4027a6cb5aa274040'
            '12b677de5181466634aff6e68b9a189b21a1b3a7ea1dbf666462602320442c02')

prepare() {
  cd gnuzilla-${_commit}

  # Uncomment if you have issues with gpg download... WITH PROXY gpg doesn't work!!!!!!
  #sed -e 's/^verify_sources$//g' -i makeicecat

  mkdir output || rm -rf output/*  # Clean output just in case is already an old build there
  if [ -f "${startdir}/firefox-${pkgver}esr.source.tar.xz" ] && [ -f "${startdir}/firefox-${pkgver}esr.source.tar.xz.asc" ]; then cp -f "${startdir}"/firefox-${pkgver}esr.source.tar.xz{,.asc} output/ ; fi

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

  # Produce IceCat sources
  bash makeicecat
  cd output/icecat-${pkgver}

  # https://bugzilla.mozilla.org/show_bug.cgi?id=1530052
  patch -Np1 -i ../../../0001-Use-remoting-name-for-GDK-application-names.patch

  # https://bugzilla.mozilla.org/show_bug.cgi?id=1667736
  patch -Np1 -i ../../../rust_1.48.patch

  # https://bugzilla.mozilla.org/show_bug.cgi?id=1684261
  patch -Np1 -i ../../../rust_1.50.patch

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
