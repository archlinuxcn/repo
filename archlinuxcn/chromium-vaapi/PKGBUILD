# Maintainer: Maxim Baz <$pkgname at maximbaz dot com>
# Contributor: Kien Dang Tran loganeast257@gmail.com
# Contributor: Samantha McVey samantham@posteo.net

# Based on extra/chromium, but with a patch to enable VA-API

# Maintainer: Evangelos Foutras <evangelos@foutrelis.com>
# Contributor: Pierre Schmitz <pierre@archlinux.de>
# Contributor: Jan "heftig" Steffens <jan.steffens@gmail.com>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>

pkgname=chromium-vaapi
pkgver=80.0.3987.149
pkgrel=1
_launcher_ver=6
pkgdesc="Chromium with VA-API support to enable hardware acceleration"
arch=('x86_64')
url="https://www.chromium.org/Home"
license=('BSD')
depends=('gtk3' 'nss' 'alsa-lib' 'xdg-utils' 'libxss' 'libcups' 'libgcrypt'
         'ttf-liberation' 'systemd' 'dbus' 'libpulse' 'pciutils' 'json-glib' 'libva'
         'desktop-file-utils' 'hicolor-icon-theme')
makedepends=('python' 'python2' 'gperf' 'yasm' 'mesa' 'ninja' 'nodejs' 'git'
             'libpipewire02' 'clang' 'lld' 'gn' 'java-runtime-headless')
optdepends=('pepper-flash: support for Flash content'
            'libpipewire02: WebRTC desktop sharing under Wayland'
            'kdialog: needed for file dialogs in KDE'
            'org.freedesktop.secrets: password storage backend on GNOME / Xfce'
            'kwallet: for storing passwords in KWallet on KDE desktops')
provides=('chromium')
conflicts=('chromium')
install=chromium.install
source=(https://commondatastorage.googleapis.com/chromium-browser-official/chromium-$pkgver.tar.xz
        chromium-launcher-$_launcher_ver.tar.gz::https://github.com/foutrelis/chromium-launcher/archive/v$_launcher_ver.tar.gz
        chromium-drirc-disable-10bpc-color-configs.conf
        vaapi-fix.patch
        vaapi-fix-wayland-init.patch
        cros-search-service-Include-cmath-for-std-pow.patch
        move-RemoteTreeNode-declaration.patch
        sync-enable-USSPasswords-by-default.patch
        fix-shim-header-generation-when-unbundling-ICU.patch
        fix-building-with-system-zlib.patch
        remove-verbose-logging-in-local-unique-font-matching.patch
        fix-building-with-unbundled-libxml.patch
        rename-Relayout-in-DesktopWindowTreeHostPlatform.patch
        rebuild-Linux-frame-button-cache-when-activation.patch
        chromium-widevine.patch
        chromium-skia-harmony.patch)
sha256sums=('50bedde7932921e375b521ceab8989be134a8d937751847e9d9287f7e0a02c1e'
            '04917e3cd4307d8e31bfb0027a5dce6d086edb10ff8a716024fbb8bb0c7dccf1'
            'babda4f5c1179825797496898d77334ac067149cac03d797ab27ac69671a7feb'
            '0ec6ee49113cc8cc5036fa008519b94137df6987bf1f9fbffb2d42d298af868a'
            'a4c022263b474ae14abd899b8e453f7d9ed9c0715b0b248b8a423aa2777095c4'
            '0a8d1af2a3734b5f99ea8462940e332db4acee7130fe436ad3e4b7ad133e5ae5'
            '21f631851cdcb347f40793485b168cb5d0da65ae26ae39ba58d624c66197d0a5'
            '08ef82476780e0864b5bf7f20eb19db320e73b9a5d4f595351e12e97dda8746f'
            'e477aa48a11ca4d53927f66a9593567fcd053325fb38af30ac3508465f1dd1f6'
            '18276e65c68a0c328601b12fefb7e8bfc632346f34b87e64944c9de8c95c5cfa'
            '5bc775c0ece84d67855f51b30eadcf96fa8163b416d2036e9f9ba19072f54dfe'
            'e530d1b39504c2ab247e16f1602359c484e9e8be4ef6d4824d68b14d29a7f60b'
            'ae3bf107834bd8eda9a3ec7899fe35fde62e6111062e5def7d24bf49b53db3db'
            '46f7fc9768730c460b27681ccf3dc2685c7e1fd22d70d3a82d9e57e3389bb014'
            '709e2fddba3c1f2ed4deb3a239fc0479bfa50c46e054e7f32db4fb1365fed070'
            '771292942c0901092a402cc60ee883877a99fb804cb54d568c8c6c94565a48e1')

# Possible replacements are listed in build/linux/unbundle/replace_gn_files.py
# Keys are the names in the above script; values are the dependencies in Arch
declare -gA _system_libs=(
  [ffmpeg]=ffmpeg
  [flac]=flac
  [fontconfig]=fontconfig
  [freetype]=freetype2
  [harfbuzz-ng]=harfbuzz
  [icu]=icu
  [libdrm]=
  [libjpeg]=libjpeg
  #[libpng]=libpng    # https://crbug.com/752403#c10
  [libvpx]=libvpx
  [libwebp]=libwebp
  [libxml]=libxml2
  [libxslt]=libxslt
  [opus]=opus
  [re2]=re2
  [snappy]=snappy
  [yasm]=
  [zlib]=minizip
)
_unwanted_bundled_libs=(
  ${!_system_libs[@]}
  ${_system_libs[libjpeg]+libjpeg_turbo}
)
depends+=(${_system_libs[@]})

# Google API keys (see https://www.chromium.org/developers/how-tos/api-keys)
# Note: These are for Arch Linux use ONLY. For your own distribution, please
# get your own set of keys.
_google_api_key=AIzaSyDwr302FpOSkGRpLlUpPThNTDPbXcIn_FM
_google_default_client_id=413772536636.apps.googleusercontent.com
_google_default_client_secret=0ZChLK6AxeA3Isu96MkwqDR4

prepare() {
  cd "$srcdir/chromium-$pkgver"

  # Allow building against system libraries in official builds
  sed -i 's/OFFICIAL_BUILD/GOOGLE_CHROME_BUILD/' \
    tools/generate_shim_headers/generate_shim_headers.py

  # https://crbug.com/893950
  sed -i -e 's/\<xmlMalloc\>/malloc/' -e 's/\<xmlFree\>/free/' \
    third_party/blink/renderer/core/xml/*.cc \
    third_party/blink/renderer/core/xml/parser/xml_document_parser.cc \
    third_party/libxml/chromium/*.cc

  # Fix VA-API on Intel and Nvidia
  patch -Np1 -i ../vaapi-fix.patch
  patch -Np1 -i ../vaapi-fix-wayland-init.patch

  # https://crbug.com/957519
  patch -Np1 -i ../cros-search-service-Include-cmath-for-std-pow.patch
  patch -Np1 -i ../move-RemoteTreeNode-declaration.patch

  # https://crbug.com/1027929
  patch -Np1 -i ../sync-enable-USSPasswords-by-default.patch

  # https://crbug.com/989153
  patch -Np1 -i ../fix-shim-header-generation-when-unbundling-ICU.patch

  # https://crbug.com/977964
  patch -Np1 -i ../fix-building-with-system-zlib.patch

  # https://crbug.com/1005508
  patch -Np1 -i ../remove-verbose-logging-in-local-unique-font-matching.patch

  # https://crbug.com/1043042
  patch -Np1 -i ../fix-building-with-unbundled-libxml.patch

  # https://crbug.com/1049258
  patch -Np1 -i ../rename-Relayout-in-DesktopWindowTreeHostPlatform.patch
  patch -Np1 -i ../rebuild-Linux-frame-button-cache-when-activation.patch

  # Load bundled Widevine CDM if available (see chromium-widevine in the AUR)
  # M79 is supposed to download it as a component but it doesn't seem to work
  patch -Np1 -i ../chromium-widevine.patch

  # https://crbug.com/skia/6663#c10
  patch -Np0 -i ../chromium-skia-harmony.patch

  # Force script incompatible with Python 3 to use /usr/bin/python2
  sed -i '1s|python$|&2|' third_party/dom_distiller_js/protoc_plugins/*.py

  mkdir -p third_party/node/linux/node-linux-x64/bin
  ln -s /usr/bin/node third_party/node/linux/node-linux-x64/bin/

  # Remove bundled libraries for which we will use the system copies; this
  # *should* do what the remove_bundled_libraries.py script does, with the
  # added benefit of not having to list all the remaining libraries
  local _lib
  for _lib in ${_unwanted_bundled_libs[@]}; do
    find "third_party/$_lib" -type f \
      \! -path "third_party/$_lib/chromium/*" \
      \! -path "third_party/$_lib/google/*" \
      \! -path 'third_party/yasm/run_yasm.py' \
      \! -regex '.*\.\(gn\|gni\|isolate\)' \
      -delete
  done

  python2 build/linux/unbundle/replace_gn_files.py \
    --system-libraries "${!_system_libs[@]}"
}

build() {
  make -C chromium-launcher-$_launcher_ver

  cd "$srcdir/chromium-$pkgver"

  if check_buildoption ccache y; then
    # Avoid falling back to preprocessor mode when sources contain time macros
    export CCACHE_SLOPPINESS=time_macros
  fi

  export CC=clang
  export CXX=clang++
  export AR=ar
  export NM=nm

  local _flags=(
    'custom_toolchain="//build/toolchain/linux/unbundle:default"'
    'host_toolchain="//build/toolchain/linux/unbundle:default"'
    'clang_use_chrome_plugins=false'
    'is_official_build=true' # implies is_cfi=true on x86_64
    'treat_warnings_as_errors=false'
    'fieldtrial_testing_like_official_build=true'
    'ffmpeg_branding="Chrome"'
    'proprietary_codecs=true'
    'rtc_use_pipewire=true'
    'link_pulseaudio=true'
    'use_gnome_keyring=false'
    'use_sysroot=false'
    'linux_use_bundled_binutils=false'
    'use_custom_libcxx=false'
    'enable_hangout_services_extension=true'
    'enable_widevine=true'
    'use_vaapi=true'
    'enable_nacl=false'
    'enable_swiftshader=false'
    "google_api_key=\"${_google_api_key}\""
    "google_default_client_id=\"${_google_default_client_id}\""
    "google_default_client_secret=\"${_google_default_client_secret}\""
  )

  if [[ -n ${_system_libs[icu]+set} ]]; then
    _flags+=('icu_use_data_file=false')
  fi

  if check_option strip y; then
    _flags+=('symbol_level=0')
  fi

  # Facilitate deterministic builds (taken from build/config/compiler/BUILD.gn)
  CFLAGS+='   -Wno-builtin-macro-redefined'
  CXXFLAGS+=' -Wno-builtin-macro-redefined'
  CPPFLAGS+=' -D__DATE__=  -D__TIME__=  -D__TIMESTAMP__='

  # Do not warn about unknown warning options
  CFLAGS+='   -Wno-unknown-warning-option'
  CXXFLAGS+=' -Wno-unknown-warning-option'

  gn gen out/Release --args="${_flags[*]}" --script-executable=/usr/bin/python2
  ninja -C out/Release chrome chrome_sandbox chromedriver
}

package() {
  cd chromium-launcher-$_launcher_ver
  make PREFIX=/usr DESTDIR="$pkgdir" install
  install -Dm644 LICENSE \
    "$pkgdir/usr/share/licenses/chromium/LICENSE.launcher"

  cd "$srcdir/chromium-$pkgver"

  install -D out/Release/chrome "$pkgdir/usr/lib/chromium/chromium"
  install -Dm4755 out/Release/chrome_sandbox "$pkgdir/usr/lib/chromium/chrome-sandbox"
  ln -s /usr/lib/chromium/chromedriver "$pkgdir/usr/bin/chromedriver"

  install -Dm644 ../chromium-drirc-disable-10bpc-color-configs.conf \
    "$pkgdir/usr/share/drirc.d/10-$pkgname.conf"

  install -Dm644 chrome/installer/linux/common/desktop.template \
    "$pkgdir/usr/share/applications/chromium.desktop"
  install -Dm644 chrome/app/resources/manpage.1.in \
    "$pkgdir/usr/share/man/man1/chromium.1"
  sed -i \
    -e "s/@@MENUNAME@@/Chromium/g" \
    -e "s/@@PACKAGE@@/chromium/g" \
    -e "s/@@USR_BIN_SYMLINK_NAME@@/chromium/g" \
    "$pkgdir/usr/share/applications/chromium.desktop" \
    "$pkgdir/usr/share/man/man1/chromium.1"

  cp \
    out/Release/{chrome_{100,200}_percent,resources}.pak \
    out/Release/{*.bin,chromedriver} \
    "$pkgdir/usr/lib/chromium/"
  install -Dm644 -t "$pkgdir/usr/lib/chromium/locales" out/Release/locales/*.pak

  if [[ -z ${_system_libs[icu]+set} ]]; then
    cp out/Release/icudtl.dat "$pkgdir/usr/lib/chromium/"
  fi

  for size in 24 48 64 128 256; do
    install -Dm644 "chrome/app/theme/chromium/product_logo_$size.png" \
      "$pkgdir/usr/share/icons/hicolor/${size}x${size}/apps/chromium.png"
  done

  for size in 16 32; do
    install -Dm644 "chrome/app/theme/default_100_percent/chromium/product_logo_$size.png" \
      "$pkgdir/usr/share/icons/hicolor/${size}x${size}/apps/chromium.png"
  done

  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/chromium/LICENSE"
}

# vim:set ts=2 sw=2 et:
