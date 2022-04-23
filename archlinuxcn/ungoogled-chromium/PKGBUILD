# Maintainer: Seppia <seppia@seppio.fish>
# Maintainer: JustKidding <jk@vin.ovh>
 
# Based on aur/chromium-vaapi, with ungoogled-chromium patches

# Maintainer: Evangelos Foutras <evangelos@foutrelis.com>
# Contributor: Pierre Schmitz <pierre@archlinux.de>
# Contributor: Jan "heftig" Steffens <jan.steffens@gmail.com>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>

pkgname=ungoogled-chromium
pkgver=100.0.4896.127
pkgrel=2
_launcher_ver=8
_gcc_patchset=4
pkgdesc="A lightweight approach to removing Google web service dependency"
arch=('x86_64')
url="https://github.com/Eloston/ungoogled-chromium"
license=('BSD')
depends=('gtk3' 'nss' 'alsa-lib' 'xdg-utils' 'libxss' 'libcups' 'libgcrypt'
         'ttf-liberation' 'systemd' 'dbus' 'libpulse' 'pciutils' 'libva'
         'desktop-file-utils' 'hicolor-icon-theme')
makedepends=('python' 'gn' 'ninja' 'clang' 'lld' 'gperf' 'nodejs' 'pipewire'
             'java-runtime-headless')
optdepends=('pipewire: WebRTC desktop sharing under Wayland'
            'kdialog: support for native dialogs in Plasma'
            'org.freedesktop.secrets: password storage backend on GNOME / Xfce'
            'kwallet: support for storing passwords in KWallet on Plasma')
options=('debug' '!lto') # Chromium adds its own flags for ThinLTO
source=(https://commondatastorage.googleapis.com/chromium-browser-official/chromium-$pkgver.tar.xz
        https://github.com/foutrelis/chromium-launcher/archive/v$_launcher_ver/chromium-launcher-$_launcher_ver.tar.gz
        https://github.com/stha09/chromium-patches/releases/download/chromium-${pkgver%%.*}-patchset-$_gcc_patchset/chromium-${pkgver%%.*}-patchset-$_gcc_patchset.tar.xz
        webcodecs-stop-using-AudioOpusEncoder.patch
        webrtc-check-existence-of-cursor-metadata.patch
        enable-GlobalMediaControlsCastStartStop.patch
        sql-make-VirtualCursor-standard-layout-type.patch
        use-oauth2-client-switches-as-default.patch)
sha256sums=('4710e3453c972c91e68a21f6b0b76ba73d4d617f299a5208615ed6e41b1af84d'
            '213e50f48b67feb4441078d50b0fd431df34323be15be97c55302d3fdac4483a'
            'a6120e7d4eb5e131b87b6ab3b922e0c6cd78e15501e54cfb2019875173688d80'
            '064daaa2b9d95b96ec04d8ddebf4af441f92263d123365b58fe73966866080af'
            '88b2c8d9c6c1917f6632453f18aad7a3fd94d605eecb6c77ae2394ac5856ba95'
            '779fb13f2494209d3a7f1f23a823e59b9dded601866d3ab095937a1a04e19ac6'
            'b94b2e88f63cfb7087486508b8139599c89f96d7a4181c61fec4b4e250ca327a'
            'e393174d7695d0bafed69e868c5fbfecf07aa6969f3b64596d0bae8b067e1711')
provides=('chromium')
conflicts=('chromium')
source=(${source[@]}
        $pkgname-$pkgver-1.tar.gz::https://github.com/Eloston/ungoogled-chromium/archive/$pkgver-1.tar.gz
        chromium-drirc-disable-10bpc-color-configs.conf
        wayland-egl.patch)
sha256sums=(${sha256sums[@]}
            '855e12e68ee767571f9032e1465ba4acd97f500fe8cf0cf67ce15f2bd9573154'
            'babda4f5c1179825797496898d77334ac067149cac03d797ab27ac69671a7feb'
            '34d08ea93cb4762cb33c7cffe931358008af32265fc720f2762f0179c3973574')

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
  #[libvpx]=libvpx
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

prepare() {
  cd "$srcdir/chromium-$pkgver"

  # Allow building against system libraries in official builds
  sed -i 's/OFFICIAL_BUILD/GOOGLE_CHROME_BUILD/' \
    tools/generate_shim_headers/generate_shim_headers.py

  # https://crbug.com/893950
  sed -i -e 's/\<xmlMalloc\>/malloc/' -e 's/\<xmlFree\>/free/' \
    third_party/blink/renderer/core/xml/*.cc \
    third_party/blink/renderer/core/xml/parser/xml_document_parser.cc \
    third_party/libxml/chromium/*.cc \
    third_party/maldoca/src/maldoca/ole/oss_utils.h

  # Use the --oauth2-client-id= and --oauth2-client-secret= switches for
  # setting GOOGLE_DEFAULT_CLIENT_ID and GOOGLE_DEFAULT_CLIENT_SECRET at
  # runtime -- this allows signing into Chromium without baked-in values
  patch -Np1 -i ../use-oauth2-client-switches-as-default.patch

  # Upstream fixes
  patch -Np1 -i ../webcodecs-stop-using-AudioOpusEncoder.patch
  patch -Np1 -d third_party/webrtc <../webrtc-check-existence-of-cursor-metadata.patch

  # Revert kGlobalMediaControlsCastStartStop enabled by default
  # https://crbug.com/1314342
  patch -Rp1 -F3 -i ../enable-GlobalMediaControlsCastStartStop.patch

  # https://chromium-review.googlesource.com/c/chromium/src/+/2862724
  patch -Np1 -i ../sql-make-VirtualCursor-standard-layout-type.patch

  # Fixes for building with libstdc++ instead of libc++
  #patch -Np1 -i ../patches/

  # Wayland/EGL regression (crbug #1071528 #1071550)
  patch -Np1 -i ../wayland-egl.patch

  # Ungoogled Chromium changes
  _ungoogled_repo="$srcdir/$pkgname-$pkgver-1"
  _utils="${_ungoogled_repo}/utils"
  python "$_utils/prune_binaries.py" ./ "$_ungoogled_repo/pruning.list"
  python "$_utils/patches.py" apply ./ "$_ungoogled_repo/patches"
  python "$_utils/domain_substitution.py" apply -r "$_ungoogled_repo/domain_regex.list" \
    -f "$_ungoogled_repo/domain_substitution.list" -c domainsubcache.tar.gz ./

  # Link to system tools required by the build
  mkdir -p third_party/node/linux/node-linux-x64/bin
  ln -s /usr/bin/node third_party/node/linux/node-linux-x64/bin/
  ln -s /usr/bin/java third_party/jdk/current/bin/

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

  ./build/linux/unbundle/replace_gn_files.py \
    --system-libraries "${!_system_libs[@]}"
}

build() {
  make -C chromium-launcher-$_launcher_ver

  cd "$srcdir/chromium-$pkgver"

  export CC=clang
  export CXX=clang++
  export AR=ar
  export NM=nm

  local _flags=(
    'custom_toolchain="//build/toolchain/linux/unbundle:default"'
    'host_toolchain="//build/toolchain/linux/unbundle:default"'
    'is_official_build=true' # implies is_cfi=true on x86_64
    'symbol_level=0' # sufficient for backtraces on x86(_64)
    'disable_fieldtrial_testing_config=true'
    'blink_enable_generated_code_formatting=false'
    'ffmpeg_branding="Chrome"'
    'proprietary_codecs=true'
    'rtc_use_pipewire=true'
    'link_pulseaudio=true'
    'use_gnome_keyring=false'
    'use_sysroot=false'
    'use_custom_libcxx=false'
    'enable_widevine=true'
  )

  if [[ -n ${_system_libs[icu]+set} ]]; then
    _flags+=('icu_use_data_file=false')
  fi

  # Append ungoogled chromium flags to _flags array
  _ungoogled_repo="$srcdir/$pkgname-$pkgver-1"
  readarray -t -O ${#_flags[@]} _flags < "${_ungoogled_repo}/flags.gn"

  # Facilitate deterministic builds (taken from build/config/compiler/BUILD.gn)
  CFLAGS+='   -Wno-builtin-macro-redefined'
  CXXFLAGS+=' -Wno-builtin-macro-redefined'
  CPPFLAGS+=' -D__DATE__=  -D__TIME__=  -D__TIMESTAMP__='

  # Do not warn about unknown warning options
  CFLAGS+='   -Wno-unknown-warning-option'
  CXXFLAGS+=' -Wno-unknown-warning-option'

  # Let Chromium set its own symbol level
  CFLAGS=${CFLAGS/-g }
  CXXFLAGS=${CXXFLAGS/-g }

  # https://github.com/ungoogled-software/ungoogled-chromium-archlinux/issues/123
  CFLAGS=${CFLAGS/-fexceptions}
  CFLAGS=${CFLAGS/-fcf-protection}
  CXXFLAGS=${CXXFLAGS/-fexceptions}
  CXXFLAGS=${CXXFLAGS/-fcf-protection}

  # This appears to cause random segfaults when combined with ThinLTO
  # https://bugs.archlinux.org/task/73518
  CFLAGS=${CFLAGS/-fstack-clash-protection}
  CXXFLAGS=${CXXFLAGS/-fstack-clash-protection}

  # https://crbug.com/957519#c122
  CXXFLAGS=${CXXFLAGS/-Wp,-D_GLIBCXX_ASSERTIONS}

  gn gen out/Release --args="${_flags[*]}"
  ninja -C out/Release chrome chrome_sandbox chromedriver
}

package() {
  cd chromium-launcher-$_launcher_ver
  make PREFIX=/usr DESTDIR="$pkgdir" install
  install -Dm644 LICENSE \
    "$pkgdir/usr/share/licenses/chromium/LICENSE.launcher"

  cd "$srcdir/chromium-$pkgver"

  install -D out/Release/chrome "$pkgdir/usr/lib/chromium/chromium"
  install -D out/Release/chromedriver "$pkgdir/usr/bin/chromedriver"
  install -Dm4755 out/Release/chrome_sandbox "$pkgdir/usr/lib/chromium/chrome-sandbox"

  install -Dm644 ../chromium-drirc-disable-10bpc-color-configs.conf \
    "$pkgdir/usr/share/drirc.d/10-$pkgname.conf"

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
    chrome_crashpad_handler
    resources.pak
    v8_context_snapshot.bin

    # ANGLE
    libEGL.so
    libGLESv2.so

    # SwiftShader ICD
    libvk_swiftshader.so
    vk_swiftshader_icd.json
  )

  if [[ -z ${_system_libs[icu]+set} ]]; then
    toplevel_files+=(icudtl.dat)
  fi

  cp "${toplevel_files[@]/#/out/Release/}" "$pkgdir/usr/lib/chromium/"
  install -Dm644 -t "$pkgdir/usr/lib/chromium/locales" out/Release/locales/*.pak
  install -Dm755 -t "$pkgdir/usr/lib/chromium/swiftshader" out/Release/swiftshader/*.so

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
