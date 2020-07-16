# Maintainer: Maxim Baz <$pkgname at maximbaz dot com>
# Contributor: Kien Dang Tran loganeast257@gmail.com
# Contributor: Samantha McVey samantham@posteo.net

# Based on extra/chromium, but with a patch to enable VA-API

# Maintainer: Evangelos Foutras <evangelos@foutrelis.com>
# Contributor: Pierre Schmitz <pierre@archlinux.de>
# Contributor: Jan "heftig" Steffens <jan.steffens@gmail.com>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>

pkgname=chromium-vaapi
pkgver=84.0.4147.89
pkgrel=1
_launcher_ver=6
_gcc_patchset=3
pkgdesc="Chromium with VA-API support to enable hardware acceleration"
arch=('x86_64')
url="https://www.chromium.org/Home"
license=('BSD')
depends=('gtk3' 'nss' 'alsa-lib' 'xdg-utils' 'libxss' 'libcups' 'libgcrypt'
         'ttf-liberation' 'systemd' 'dbus' 'libpulse' 'pciutils' 'json-glib'
         'desktop-file-utils' 'hicolor-icon-theme')
makedepends=('python' 'python2' 'gperf' 'mesa' 'ninja' 'nodejs' 'git' 'libva'
             'libpipewire02' 'clang' 'lld' 'gn' 'java-runtime-headless'
             'python2-setuptools')
optdepends=('pepper-flash: support for Flash content'
            'libpipewire02: WebRTC desktop sharing under Wayland'
            'libva: hardware-accelerated video decode [experimental]'
            'kdialog: needed for file dialogs in KDE'
            'org.freedesktop.secrets: password storage backend on GNOME / Xfce'
            'kwallet: for storing passwords in KWallet on KDE desktops')
provides=('chromium')
conflicts=('chromium')
install=chromium.install
source=(https://commondatastorage.googleapis.com/chromium-browser-official/chromium-$pkgver.tar.xz
        chromium-launcher-$_launcher_ver.tar.gz::https://github.com/foutrelis/chromium-launcher/archive/v$_launcher_ver.tar.gz
        https://github.com/stha09/chromium-patches/releases/download/chromium-${pkgver%%.*}-patchset-$_gcc_patchset/chromium-${pkgver%%.*}-patchset-$_gcc_patchset.tar.xz
        remove-NotifyError-calls-and-just-send-a-normal-message.patch
        avoid-calling-DeleteForCurrentDocument-from-destructor.patch
        force-mp3-files-to-have-a-start-time-of-zero.patch
        chromium-ffmpeg-4.3.patch
        intel-vp9-quirk.patch
        wayland-egl.patch
        nvidia-vdpau.patch
        chromium-skia-harmony.patch)
sha256sums=('17970d998c125b40765141f2cd346d1674f05dbd4a28fdcf31f9e3540890c679'
            '04917e3cd4307d8e31bfb0027a5dce6d086edb10ff8a716024fbb8bb0c7dccf1'
            'f77088dd59b170b767ba91c6b410abb778ff2e68553433b24124d398fa4d3ce7'
            '3b10917f646f88ae988ca18be9cbef82025abb6a6e5cb00b77a11077192ce32c'
            '4e41cb637e96bcef98c119ed052ba1aeab45fca5b89d65955583dab002de783e'
            'abc3fad113408332c3b187b083bf33eba59eb5c87fa3ce859023984b5804623c'
            '5390304b5f544868985ce00a3ec082d4ece2dacb1c73cdb35dd4facfea12449a'
            'a25fc6fccb84fd0a58a799661cd9c4ffeb2731fa49268f43aa7108f1542c5af6'
            '34d08ea93cb4762cb33c7cffe931358008af32265fc720f2762f0179c3973574'
            '8095bf73afbca7c2b07306c5b4dd8f79b66e1053fa4e58b07f71ef938be603f1'
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
  [libpng]=libpng
  [libvpx]=libvpx
  [libwebp]=libwebp
  [libxml]=libxml2
  [libxslt]=libxslt
  [opus]=opus
  [re2]=re2
  [snappy]=snappy
  [zlib]=minizip
)
_unwanted_bundled_libs=(
  $(printf "%s\n" ${!_system_libs[@]} | sed 's/^libjpeg$/&_turbo/')
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

  # https://chromium-review.googlesource.com/c/chromium/src/+/2223010
  patch -Np1 -i ../remove-NotifyError-calls-and-just-send-a-normal-message.patch

  # https://chromium-review.googlesource.com/c/chromium/src/+/2224737
  patch -Np1 -i ../avoid-calling-DeleteForCurrentDocument-from-destructor.patch

  # https://chromium-review.googlesource.com/c/chromium/src/+/2268221
  patch -Np1 -i ../force-mp3-files-to-have-a-start-time-of-zero.patch

  # Fixes for building with libstdc++ instead of libc++
  patch -Np1 -i ../patches/chromium-84-AXObject-stl-iterator.patch
  patch -Np1 -i ../patches/chromium-84-ListContainerHelper-include-cstring.patch
  patch -Np1 -i ../patches/chromium-84-crashpad-include-cstring.patch
  patch -Np1 -i ../patches/chromium-84-gcc-10-include-stddef.patch
  patch -Np1 -i ../patches/chromium-84-gcc-10-webrtc-include-stddef.patch
  patch -Np1 -i ../patches/chromium-84-gcc-DCHECK_EQ-unique_ptr.patch
  patch -Np1 -i ../patches/chromium-84-std-vector-const.patch

  # https://crbug.com/1095962
  patch -Np1 -i ../chromium-ffmpeg-4.3.patch

  # https://crbug.com/skia/6663#c10
  patch -Np0 -i ../chromium-skia-harmony.patch

  # Intel KabyLake/GeminiLake VP9 quirk
  patch -Np1 -i ../intel-vp9-quirk.patch
  # Wayland/EGL regression (crbug #1071528 #1071550)
  patch -Np1 -i ../wayland-egl.patch
  # NVIDIA vdpau-wrapper
  patch -Np1 -i ../nvidia-vdpau.patch

  # Force script incompatible with Python 3 to use /usr/bin/python2
  sed -i '1s|python$|&2|' third_party/dom_distiller_js/protoc_plugins/*.py

  # Make xcbgen available to ui/gfx/x/gen_xproto.py running under Python 2
  ln -s /usr/lib/python3.*/site-packages/xcbgen "$srcdir/"

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
      \! -path "third_party/harfbuzz-ng/utils/hb_scoped.h" \
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

  # ui/gfx/x/gen_xproto.py needs xcbgen
  export PYTHONPATH=$srcdir

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

  install -Dm644 chrome/installer/linux/common/desktop.template \
    "$pkgdir/usr/share/applications/chromium.desktop"
  install -Dm644 chrome/app/resources/manpage.1.in \
    "$pkgdir/usr/share/man/man1/chromium.1"
  sed -i \
    -e 's/@@MENUNAME@@/Chromium/g' \
    -e 's/@@PACKAGE@@/chromium/g' \
    -e 's/@@USR_BIN_SYMLINK_NAME@@/chromium/g' \
    "$pkgdir/usr/share/applications/chromium.desktop" \
    "$pkgdir/usr/share/man/man1/chromium.1"

  install -Dm644 chrome/installer/linux/common/chromium-browser/chromium-browser.appdata.xml \
    "$pkgdir/usr/share/metainfo/chromium.appdata.xml"
  sed -ni \
    -e 's/chromium-browser\.desktop/chromium.desktop/' \
    -e '/<update_contact>/d' \
    -e '/<p>/N;/<p>\n.*\(We invite\|Chromium supports Vorbis\)/,/<\/p>/d' \
    -e '/^<?xml/,$p' \
    "$pkgdir/usr/share/metainfo/chromium.appdata.xml"

  local toplevel_files=(
    chrome_100_percent.pak
    chrome_200_percent.pak
    resources.pak
    v8_context_snapshot.bin
    chromedriver
  )

  if [[ -z ${_system_libs[icu]+set} ]]; then
    toplevel_files+=(icudtl.dat)
  fi

  cp "${toplevel_files[@]/#/out/Release/}" "$pkgdir/usr/lib/chromium/"
  install -Dm644 -t "$pkgdir/usr/lib/chromium/locales" out/Release/locales/*.pak

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
