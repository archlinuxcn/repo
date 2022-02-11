# Maintainer: lsf
# Contributor: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>
# Contributor: Ionut Biru <ibiru@archlinux.org>
# Contributor: Jakub Schmidtke <sjakub@gmail.com>

pkgname=librewolf
_pkgname=LibreWolf
pkgver=97.0
pkgrel=1
pkgdesc="Community-maintained fork of Firefox, focused on privacy, security and freedom."
arch=(x86_64 aarch64)
license=(MPL GPL LGPL)
url="https://librewolf-community.gitlab.io/"
depends=(gtk3 libxt mime-types dbus-glib ffmpeg nss ttf-font libpulse)
makedepends=(unzip zip diffutils yasm mesa imake inetutils xorg-server-xvfb
             autoconf2.13 rust clang llvm jack nodejs cbindgen nasm
             python-setuptools python-psutil python-zstandard git binutils lld dump_syms
             wasi-compiler-rt wasi-libc wasi-libc++ wasi-libc++abi)
optdepends=('networkmanager: Location detection via available WiFi networks'
            'libnotify: Notification integration'
            'pulseaudio: Audio support'
            'speech-dispatcher: Text-to-Speech'
            'hunspell-en_US: Spell checking, American English'
            'xdg-desktop-portal: Screensharing with Wayland')
backup=('usr/lib/librewolf/librewolf.cfg'
        'usr/lib/librewolf/distribution/policies.json')
options=(!emptydirs !makeflags !strip !lto !debug)
_arch_git=https://raw.githubusercontent.com/archlinux/svntogit-packages/packages/firefox/trunk
_common_tag="v${pkgver}-${pkgrel}"
_settings_tag='5.5'
install='librewolf.install'
source=(https://archive.mozilla.org/pub/firefox/releases/$pkgver/source/firefox-$pkgver.source.tar.xz{,.asc}
        $pkgname.desktop
        "git+https://gitlab.com/${pkgname}-community/browser/common.git#tag=${_common_tag}"
        "git+https://gitlab.com/${pkgname}-community/settings.git#tag=${_settings_tag}"
        "default192x192.png"
        )
source_aarch64=("${pkgver}-${pkgrel}_build-arm-libopus.patch::https://raw.githubusercontent.com/archlinuxarm/PKGBUILDs/master/extra/firefox/build-arm-libopus.patch")
sha256sums=('6c8a7dcb47122d033383fd62a1bcaefff0290a6c23d057898e8ff9c72749df28'
            'SKIP'
            '0b28ba4cc2538b7756cb38945230af52e8c4659b2006262da6f3352345a8bed2'
            'SKIP'
            'SKIP'
            '959c94c68cab8d5a8cff185ddf4dca92e84c18dccc6dc7c8fe11c78549cdc2f1')
sha256sums_aarch64=('2d4d91f7e35d0860225084e37ec320ca6cae669f6c9c8fe7735cdbd542e3a7c9')
validpgpkeys=('14F26682D0916CDD81E37B6D61B7B526D98F0353') # Mozilla Software Releases <release@mozilla.com>

prepare() {
  mkdir -p mozbuild
  cd firefox-$pkgver

  local _patches_dir="${srcdir}/common/patches"

  cat >../mozconfig <<END
ac_add_options --enable-application=browser
mk_add_options MOZ_OBJDIR=${PWD@Q}/obj

# This supposedly speeds up compilation (We test through dogfooding anyway)
ac_add_options --disable-tests
ac_add_options --disable-debug

ac_add_options --prefix=/usr
ac_add_options --enable-release
ac_add_options --enable-hardening
ac_add_options --enable-rust-simd
export CC='clang'
export CXX='clang++'

# Branding
ac_add_options --enable-update-channel=release
ac_add_options --with-app-name=${pkgname}
ac_add_options --with-app-basename=${_pkgname}
ac_add_options --with-branding=browser/branding/${pkgname}
ac_add_options --with-distribution-id=io.gitlab.${pkgname}-community
ac_add_options --with-unsigned-addon-scopes=app,system
ac_add_options --allow-addon-sideload
export MOZ_REQUIRE_SIGNING=
# export MOZ_APP_REMOTINGNAME=${pkgname//-/}

# System libraries
ac_add_options --with-system-nspr
ac_add_options --with-system-nss

# Features
ac_add_options --enable-alsa
ac_add_options --enable-jack
ac_add_options --disable-crashreporter
ac_add_options --disable-updater
ac_add_options --disable-tests

# obsoleted?
# mk_add_options MOZ_CRASHREPORTER=0

# options for ci / weaker build systems
# mk_add_options MOZ_MAKE_FLAGS="-j4"
# ac_add_options --enable-linker=gold

# wasi
ac_add_options --with-wasi-sysroot=/usr/share/wasi-sysroot
END

if [[ $CARCH == 'aarch64' ]]; then
  cat >>../mozconfig <<END
# taken from manjaro build:
ac_add_options --enable-optimize="-g0 -O2"
END

  export MOZ_DEBUG_FLAGS=" "
  export CFLAGS+=" -g0"
  export CXXFLAGS+=" -g0"
  export RUSTFLAGS="-Cdebuginfo=0"

  # we should have more than enough RAM on the CI spot instances.
  # ...or maybe not?
  export LDFLAGS+=" -Wl,--no-keep-memory"
  # patch -Np1 -i ${_patches_dir}/arm.patch # not required anymore?
  patch -Np1 -i ../${pkgver}-${pkgrel}_build-arm-libopus.patch

else

  cat >>../mozconfig <<END
# probably not needed, enabled by default?
ac_add_options --enable-optimize
END
fi

  # upstream Arch fixes
  # https://bugzilla.mozilla.org/show_bug.cgi?id=1530052
  # patch -Np1 -i ${srcdir}/0001-Use-remoting-name-for-GDK-application-names.patch

  # LibreWolf

  # Remove some pre-installed addons that might be questionable
  patch -Np1 -i ${_patches_dir}/remove_addons.patch

  # Disable (some) megabar functionality
  # Adapted from https://github.com/WesleyBranton/userChrome.css-Customizations
  patch -Np1 -i ${_patches_dir}/removed-patches/megabar.patch

  # Debian patch to enable global menubar
  # disabled for the default build, as it seems to cause issues in some configurations
  # 2022-01-21: re-enabled because it seems to not mess things up anymore nowadays?
  patch -Np1 -i ${_patches_dir}/unity-menubar.patch

  # KDE menu
  # patch -Np1 -i ${_patches_dir}/mozilla-kde.patch
  # custom patch that does not conflict with the unity patch
  patch -Np1 -i ${_patches_dir}/mozilla-kde_after_unity.patch

  # Disabling Pocket
  patch -Np1 -i ${_patches_dir}/sed-patches/disable-pocket.patch

  # remove mozilla vpn ads
  patch -Np1 -i ${_patches_dir}/mozilla-vpn-ad.patch

  # Remove Internal Plugin Certificates
  # patch -Np1 -i ${_patches_dir}/sed-patches/remove-internal-plugin-certs.patch
  # => breaks profiled builds since 90.0, it seems

  # allow SearchEngines option in non-ESR builds
  patch -Np1 -i ${_patches_dir}/sed-patches/allow-searchengines-non-esr.patch

  # remove search extensions (experimental)
  # patch -Np1 -i ${_patches_dir}/search-config.patch
  cp "${srcdir}/common/source_files/search-config.json" services/settings/dumps/main/search-config.json

  # stop some undesired requests (https://gitlab.com/librewolf-community/browser/common/-/issues/10)
  patch -Np1 -i ${_patches_dir}/sed-patches/stop-undesired-requests.patch

  # Assorted patches
  patch -Np1 -i ${_patches_dir}/context-menu.patch
  patch -Np1 -i ${_patches_dir}/urlbarprovider-interventions.patch


  # allow overriding the color scheme light/dark preference with RFP
  # deprecated, will probably be dropped soon
  # patch -Np1 -i ${_patches_dir}/allow_dark_preference_with_rfp.patch

  # change some hardcoded directory strings that could lead to unnecessarily
  # created directories
  patch -Np1 -i ${_patches_dir}/mozilla_dirs.patch

  # somewhat experimental patch to fix bus/dbus/remoting names to io.gitlab.librewolf
  # should not break things, buuuuuuuuuut we'll see.
  patch -Np1 -i ${_patches_dir}/dbus_name.patch

  # allow uBlockOrigin to run in private mode by default, without user intervention.
  patch -Np1 -i ${_patches_dir}/allow-ubo-private-mode.patch

  # add custom uBO assets (on first launch only)
  patch -Np1 -i ${_patches_dir}/custom-ubo-assets-bootstrap-location.patch

  # ui patches

  # remove references to firefox from the settings UI, change text in some of the links,
  # explain that we force en-US and suggest enabling history near the session restore checkbox.
  patch -Np1 -i ${_patches_dir}/ui-patches/pref-naming.patch

  #
  patch -Np1 -i ${_patches_dir}/ui-patches/hide-safe-browsing.patch

  # remove firefox references in the urlbar, when suggesting opened tabs.
  patch -Np1 -i ${_patches_dir}/ui-patches/remove-branding-urlbar.patch

  # remove cfr UI elements, as they are disabled and locked already.
  patch -Np1 -i ${_patches_dir}/ui-patches/remove-cfrprefs.patch

  # do not display your browser is being managed by your organization in the settings.
  patch -Np1 -i ${_patches_dir}/ui-patches/remove-organization-policy-banner.patch

  # hide "snippets" section from the home page settings, as it was already locked.
  patch -Np1 -i ${_patches_dir}/ui-patches/remove-snippets-from-home.patch

  # add warning that sanitizing exceptions are bypassed by the options in History > Clear History when LibreWolf closes > Settings
  patch -Np1 -i ${_patches_dir}/ui-patches/sanitizing-description.patch

  # pref pane
  patch -Np1 -i ${_patches_dir}/librewolf-pref-pane.patch

  # fix telemetry removal, see https://gitlab.com/librewolf-community/browser/linux/-/merge_requests/17, for example
  patch -Np1 -i ${_patches_dir}/disable-data-reporting-at-compile-time.patch

  rm -f ${srcdir}/common/source_files/mozconfig
  cp -r ${srcdir}/common/source_files/browser ./
}


build() {
  cd firefox-$pkgver

  export MOZ_NOSPAM=1
  export MOZBUILD_STATE_PATH="$srcdir/mozbuild"
  export MACH_USE_SYSTEM_PYTHON=1

  # LTO needs more open files
  ulimit -n 4096

  # -fno-plt with cross-LTO causes obscure LLVM errors
  # LLVM ERROR: Function Import: link error
  # CFLAGS="${CFLAGS/-fno-plt/}"
  # CXXFLAGS="${CXXFLAGS/-fno-plt/}"

  # Do 3-tier PGO
  echo "Building instrumented browser..."

if [[ $CARCH == 'aarch64' ]]; then

  cat >.mozconfig ../mozconfig - <<END
ac_add_options --enable-profile-generate
END

else

  cat >.mozconfig ../mozconfig - <<END
ac_add_options --enable-profile-generate=cross
END

fi

  ./mach build

  echo "Profiling instrumented browser..."
  ./mach package
  LLVM_PROFDATA=llvm-profdata \
    JARLOG_FILE="$PWD/jarlog" \
    xvfb-run -s "-screen 0 1920x1080x24 -nolisten local" \
    ./mach python build/pgo/profileserver.py

  stat -c "Profile data found (%s bytes)" merged.profdata
  test -s merged.profdata

  stat -c "Jar log found (%s bytes)" jarlog
  test -s jarlog

  echo "Removing instrumented browser..."
  ./mach clobber

  echo "Building optimized browser..."

if [[ $CARCH == 'aarch64' ]]; then

  cat >.mozconfig ../mozconfig - <<END
ac_add_options --enable-lto
ac_add_options --enable-profile-use
ac_add_options --with-pgo-profile-path=${PWD@Q}/merged.profdata
ac_add_options --with-pgo-jarlog=${PWD@Q}/jarlog
ac_add_options --enable-linker=lld
END

else

  cat >.mozconfig ../mozconfig - <<END
ac_add_options --enable-lto=cross
ac_add_options --enable-profile-use=cross
ac_add_options --with-pgo-profile-path=${PWD@Q}/merged.profdata
ac_add_options --with-pgo-jarlog=${PWD@Q}/jarlog
ac_add_options --enable-linker=lld
ac_add_options --disable-elf-hack
ac_add_options --disable-bootstrap
END

fi

  ./mach build

  echo "Building symbol archive..."
  ./mach buildsymbols
}

package() {
  cd firefox-$pkgver
  DESTDIR="$pkgdir" ./mach install

  local vendorjs="$pkgdir/usr/lib/$pkgname/browser/defaults/preferences/vendor.js"

  install -Dvm644 /dev/stdin "$vendorjs" <<END
// Use system-provided dictionaries
pref("spellchecker.dictionary_path", "/usr/share/hunspell");

// Don't disable extensions in the application directory
// done in librewolf.cfg
// pref("extensions.autoDisableScopes", 11);
END

  # cd ${srcdir}/settings
  # git checkout ${_settings_commit}
  cd ${srcdir}/firefox-$pkgver
  cp -r ${srcdir}/settings/* ${pkgdir}/usr/lib/${pkgname}/

  local distini="$pkgdir/usr/lib/$pkgname/distribution/distribution.ini"
  install -Dvm644 /dev/stdin "$distini" <<END
[Global]
id=io.gitlab.${pkgname}-community
version=1.0
about=LibreWolf

[Preferences]
app.distributor="LibreWolf Community"
app.distributor.channel=$pkgname
app.partner.librewolf=$pkgname
END

  for i in 16 32 48 64 128; do
    install -Dvm644 browser/branding/${pkgname}/default$i.png \
      "$pkgdir/usr/share/icons/hicolor/${i}x${i}/apps/$pkgname.png"
  done
  # install -Dvm644 browser/branding/librewolf/content/about-logo.png \
    # "$pkgdir/usr/share/icons/hicolor/192x192/apps/$pkgname.png"
  install -Dvm644 ${srcdir}/default192x192.png \
    "$pkgdir/usr/share/icons/hicolor/192x192/apps/$pkgname.png"

  # arch upstream provides a separate svg for this. we don't have that, so let's re-use 16.png
  install -Dvm644 browser/branding/${pkgname}/default16.png \
    "$pkgdir/usr/share/icons/hicolor/symbolic/apps/$pkgname-symbolic.png"

  install -Dvm644 ../$pkgname.desktop \
    "$pkgdir/usr/share/applications/$pkgname.desktop"

  # Install a wrapper to avoid confusion about binary path
  install -Dvm755 /dev/stdin "$pkgdir/usr/bin/$pkgname" <<END
#!/bin/sh
exec /usr/lib/$pkgname/librewolf "\$@"
END

  # Replace duplicate binary with wrapper
  # https://bugzilla.mozilla.org/show_bug.cgi?id=658850
  ln -srfv "$pkgdir/usr/bin/$pkgname" "$pkgdir/usr/lib/$pkgname/librewolf-bin"
  # Use system certificates
  local nssckbi="$pkgdir/usr/lib/$pkgname/libnssckbi.so"
  if [[ -e $nssckbi ]]; then
    ln -srfv "$pkgdir/usr/lib/libnssckbi.so" "$nssckbi"
  fi
}
