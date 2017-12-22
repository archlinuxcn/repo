# Maintainer: Gustavo Alvarez <sl1pkn07@gmail.com>
# Contributor: Mikhail Vorozhtsov <mikhail.vorozhtsov@gmail.com>
# Contributor: Nagisa <simonas@kazlauskas.me>
# Contributor: Misc <andreas.reis@gmail.com>
# Contributor: Jeagoss <jgoliver@jeago.com>
# Contributor: Saikrishna Arcot <saiarcot895@gmail.com> and Steven Newbury <steve@snewbury.org.uk> (First Authors of VAAPI patch)

#########################
## -- Build options -- ##
#########################

_use_clang=1     # Use clang compiler (downloaded binaries from google). Results in faster build and smaller chromium.
_use_ccache=0    # Use ccache when build.
_debug_mode=0    # Build in debug mode.
_use_wayland=0   # Build Wayland NOTE: extremely experimental and don't work at this moment

##############################################
## -- Package and components information -- ##
##############################################
pkgname=chromium-dev
pkgver=65.0.3294.5
pkgrel=1
pkgdesc="The open-source project behind Google Chrome (Dev Channel)"
arch=('x86_64')
url='http://www.chromium.org'
license=('BSD')
depends=(
#          'libsrtp'
         'libxslt'
         'libxss'
         'minizip'
         'nss'
         'pciutils'
         're2'
         'snappy'
         'xdg-utils'
         'libcups'
         'libxml2'
#          'harfbuzz-icu'
#          'protobuf'
#          'libevent'
         'ffmpeg'
#          'icu'    # https://crbug.com/678661
         'gtk3'
         'openh264'
         )
makedepends=(
             'libexif'
             'gperf'
             'ninja'
             'python2-beautifulsoup4'
             'python2-html5lib'
             'python2-simplejson'
             'python2-six'
             'subversion'
             'yasm'
             'git'
             'imagemagick'
             'hwids'
             'nodejs'
             'wget'
             )
optdepends=(
            'pepper-flash: PPAPI Flash Player'
            'chromium-widevine-dev: Widevine plugin (eg: Netflix) (Dev Channel)'
            #
            'kdialog: Needed for file dialogs in KF5'
            'kwalletmanager: Needed for storing passwords in KWallet5'
            #
            'ttf-font: For some typography'
            #
            'libappindicator-gtk3: Needed for show systray icon in the panel on GTK3 Desktop based'
            )
source=( #"https://gsdview.appspot.com/chromium-browser-official/chromium-${pkgver}.tar.xz"
        "https://commondatastorage.googleapis.com/chromium-browser-official/chromium-${pkgver}.tar.xz"
        "git+https://github.com/foutrelis/chromium-launcher.git"
        'chromium-dev.svg'
        # Patch form Gentoo
        'https://raw.githubusercontent.com/gentoo/gentoo/master/www-client/chromium/files/chromium-FORTIFY_SOURCE-r2.patch'
        'chromium-gcc5-r5.patch'
        # Misc Patches
#         'chromium-intel-vaapi_r15.diff.base64::https://chromium-review.googlesource.com/changes/532294/revisions/15/patch?download'
        'chromium-intel-vaapi_r16.diff.patch'
        # Patch from crbug (chromium bugtracker) or Arch chromium package
        'chromium-widevine-r1.patch'
#         'chromium-exclude_unwind_tables.patch.base64::https://chromium-review.googlesource.com/changes/712575/revisions/1/patch?download' # https://bugs.archlinux.org/task/55914
        'chromium-exclude_unwind_tables_r2.patch.patch'
        )
sha256sums=( #"$(curl -sL https://gsdview.appspot.com/chromium-browser-official/chromium-${pkgver}.tar.xz.hashes | grep sha256 | cut -d ' ' -f3)"
            "$(curl -sL https://commondatastorage.googleapis.com/chromium-browser-official/chromium-${pkgver}.tar.xz.hashes | grep sha256 | cut -d ' ' -f3)"
            'SKIP'
            'dd2b5c4191e468972b5ea8ddb4fa2e2fa3c2c94c79fc06645d0efc0e63ce7ee1'
            # Patch form Gentoo
            'fa3f703d599051135c5be24b81dfcb23190bb282db73121337ac76bc9638e8a5'
            '3d0d306e24b5b0c91358127a578c8a7ade8cef3eb15a769739b07a282f068de4'
            # Misc Patches
#             'cb4933db92b669696201b2866ec9b4942466a849b94b13463d8331284d09a2d1'
            'c32d71237cf9dca71c35ec54431749c837eb3a7b7dae2fb3fc88beafefa1ca97'
            # Patch from crbug (chromium bugtracker) or Arch chromium package
            '0d537830944814fe0854f834b5dc41dc5fc2428f77b2ad61d4a5e76b0fe99880'
#             'd4a99239701256edb37ef3a5504fa87ca2219349834cbf59b9fe42bf7ac496d8'
            '9478f1ec1a3c53425306cf41c2d0555c215a4f106955d9d6adfff38044530ce8'
            )
options=('!strip')
install=chromium-dev.install

################################################
## -- Don't touch anything below this line -- ##
################################################

# Google API keys (see http://www.chromium.org/developers/how-tos/api-keys)
# NOTE: These are for Arch Linux use ONLY. For your own distribution, please
# get your own set of keys. Feel free to contact foutrelis@archlinux.org for
# more information.
_google_api_key="AIzaSyDwr302FpOSkGRpLlUpPThNTDPbXcIn_FM"
_google_default_client_id="413772536636.apps.googleusercontent.com"
_google_default_client_secret="0ZChLK6AxeA3Isu96MkwqDR4"

# Build NaCL
# VULKAN!! # https://crbug.com/582558 NOTE: disabled by default
_build_nacl=1
_nacl=true
_vulkan=0
makedepends+=('ncurses5-compat-libs')

# Need you use ccache?.
if [ "${_use_ccache}" = "1" ]; then
  makedepends+=('ccache')
fi

# Are you use gnome-keyring/gnome?.
_gnome_keyring=false
if [ -e /usr/lib/libgnome-keyring.so.0 ]; then
  depends+=('libgnome-keyring')
  _gnome_keyring=true
fi

# List of third-party components needed for build chromium. The rest is remove by remove_bundled_libraries srcipt in prepare().
_keeplibs=(
           'base/third_party/dmg_fp'
           'base/third_party/dynamic_annotations'
           'base/third_party/icu'
           'base/third_party/nspr'
           'base/third_party/superfasthash'
           'base/third_party/symbolize'
           'base/third_party/valgrind'
           'base/third_party/xdg_mime'
           'base/third_party/xdg_user_dirs'
           'chrome/third_party/mozilla_security_manager'
           'courgette/third_party'
           'native_client/src/third_party/dlmalloc'
           'native_client_sdk/src/libraries/third_party/newlib-extras'
           'net/third_party/mozilla_security_manager'
           'net/third_party/nss'
           'third_party/WebKit'
           'third_party/analytics'
           'third_party/angle'
           'third_party/angle/src/common/third_party/base'
           'third_party/angle/src/common/third_party/smhasher'
           'third_party/angle/src/third_party/compiler'
           'third_party/angle/src/third_party/libXNVCtrl'
           'third_party/angle/src/third_party/trace_event'
           'third_party/blink'
           'third_party/boringssl'
           'third_party/boringssl/src/third_party/fiat'
           'third_party/breakpad'
           'third_party/breakpad/breakpad/src/third_party/curl'
           'third_party/brotli'
           'third_party/cacheinvalidation'
           'third_party/catapult'
           'third_party/catapult/common/py_vulcanize/third_party/rcssmin'
           'third_party/catapult/common/py_vulcanize/third_party/rjsmin'
           'third_party/catapult/third_party/polymer'
           'third_party/catapult/tracing/third_party/d3'
           'third_party/catapult/tracing/third_party/gl-matrix'
           'third_party/catapult/tracing/third_party/jszip'
           'third_party/catapult/tracing/third_party/mannwhitneyu'
           'third_party/catapult/tracing/third_party/oboe'
           'third_party/catapult/tracing/third_party/pako'
           'third_party/ced'
           'third_party/cld_3'
           'third_party/crc32c'
           'third_party/cros_system_api'
           'third_party/devscripts'
           'third_party/dom_distiller_js'
           'third_party/fips181'
           'third_party/flatbuffers'
           'third_party/flot'
           'third_party/freetype'
           'third_party/glslang'
           'third_party/glslang-angle'
           'third_party/google_input_tools'
           'third_party/google_input_tools/third_party/closure_library'
           'third_party/google_input_tools/third_party/closure_library/third_party/closure'
           'third_party/googletest'
           'third_party/harfbuzz-ng'
           'third_party/hunspell'
           'third_party/iccjpeg'
           'third_party/inspector_protocol'
           'third_party/jinja2'
           'third_party/jstemplate'
           'third_party/khronos'
           'third_party/leveldatabase'
           'third_party/libXNVCtrl'
           'third_party/libaddressinput'
           'third_party/libaom'
           'third_party/libaom/source/libaom/third_party/x86inc'
           'third_party/libjingle'
           'third_party/libphonenumber'
           'third_party/libsecret'
           'third_party/libsrtp'
           'third_party/libudev'
           'third_party/libvpx'
           'third_party/libvpx/source/libvpx/third_party/x86inc'
           'third_party/libwebm'
           'third_party/libxml/chromium'
           'third_party/libyuv'
           'third_party/lss'
           'third_party/lzma_sdk'
           'third_party/markupsafe'
           'third_party/mesa'
           'third_party/metrics_proto'
           'third_party/modp_b64'
           'third_party/mt19937ar'
           'third_party/node'
           'third_party/node/node_modules/polymer-bundler/lib/third_party/UglifyJS2'
           'third_party/openmax_dl'
           'third_party/ots'
           'third_party/pdfium'
           'third_party/pdfium/third_party/agg23'
           'third_party/pdfium/third_party/base'
           'third_party/pdfium/third_party/build'
           'third_party/pdfium/third_party/bigint'
           'third_party/pdfium/third_party/freetype'
           'third_party/pdfium/third_party/lcms'
           'third_party/pdfium/third_party/libopenjpeg20'
           'third_party/pdfium/third_party/libpng16'
           'third_party/pdfium/third_party/libtiff'
           'third_party/ply'
           'third_party/polymer'
           'third_party/protobuf'
           'third_party/protobuf/third_party/six'
           'third_party/qcms'
           'third_party/s2cellid'
           'third_party/sfntly'
           'third_party/shaderc'
           'third_party/skia'
           'third_party/skia/third_party/gif'
           'third_party/skia/third_party/vulkan'
           'third_party/smhasher'
           'third_party/spirv-headers'
           'third_party/SPIRV-Tools'
           'third_party/spirv-tools-angle'
           'third_party/sqlite'
           'third_party/swiftshader'
           'third_party/swiftshader/third_party/llvm-subzero'
           'third_party/swiftshader/third_party/subzero'
           'third_party/tcmalloc'
           'third_party/usrsctp'
           'third_party/vulkan-validation-layers'
           'third_party/vulkan'
           'third_party/web-animations-js'
           'third_party/webdriver'
           'third_party/webrtc'
           'third_party/widevine'
           'third_party/woff2'
           'third_party/zlib/google'
           'url/third_party/mozilla'
           'v8/src/third_party/valgrind'
           'v8/src/third_party/utf8-decoder'
           'v8/third_party/inspector_protocol'

           # gyp -> gn leftovers
           'base/third_party/libevent'
           'third_party/adobe'
           'third_party/speech-dispatcher'
           'third_party/usb_ids'
           'third_party/xdg-utils'
           'third_party/yasm/run_yasm.py'
           )

# Set build flags.
_flags=(
        'is_debug=false'
        'enable_widevine=true'
        'enable_hangout_services_extension=false'
        "ffmpeg_branding=\"ChromeOS\""
        'proprietary_codecs=true'
        "google_api_key=\"${_google_api_key}\""
        "google_default_client_id=\"${_google_default_client_id}\""
        "google_default_client_secret=\"${_google_default_client_secret}\""
        'fieldtrial_testing_like_official_build=false'
        'use_gtk3=true'
        'use_gconf=false'
        "use_gio=false"
        "use_gnome_keyring=${_gnome_keyring}"
        'link_pulseaudio=true'
        'use_sysroot=false'
        'use_gold=false'
        'linux_use_bundled_binutils=false'
        'fatal_linker_warnings=false'
        'treat_warnings_as_errors=false'
        "enable_nacl=${_nacl}"
        "enable_nacl_nonsfi=${_nacl}"
        'use_custom_libcxx=false'
        )

if [ "$_wayland" = "1" ]; then
  _flags+=(
           'use_ozone=true'
           'use_xkbcommon=true'
           'enable_package_mash_services=true'
           'enable_vulkan_wayland_client=true'
           )
fi
if [ "$_vulkan" = "1" ]; then
  _flags+=('enable_vulkan=true')
fi

# Enable VAAPI, see https://chromium-review.googlesource.com/532294
_flags+=('use_vaapi=true')
optdepends+=(
             'libva-vdpau-driver-chromium: HW video acceleration for NVIDIA users'
             'libva-mesa-driver: HW video acceleration for Nouveau, R600 and RadeonSI users'
             'libva-intel-driver: HW video acceleration for Intel G45 and HD users'
            )

# Set the bundled/external components.
# TODO: need ported to GN as GYP doing before. see status page: https://crbug.com/551343
_use_system=(
             'ffmpeg'
             'flac'
#              'freetype'    # https://bugs.chromium.org/p/pdfium/issues/detail?id=733
#              'harfbuzz-ng' # freetype and harfbuzz needs update at same time, or both or none. disable due freetype bug. link avobe
#              'icu'         # https://crbug.com/678661
             'libdrm'
#              'libevent'    # Get segfaults and other problems https://bugs.gentoo.org/593458
             'libjpeg'
             'libpng'
#              'libvpx'      # Needs update
             'libwebp'
             'libxml'
             'libxslt'
             'openh264'
             'opus'
             're2'
             'snappy'
             'yasm'
             'zlib'
             )

# Use system harfbuzz
_flags+=('use_system_harfbuzz=true')

# Conditionals.
# Build Debug mode?.
if [ "${_debug_mode}" = "1" ]; then
  _keeplibs+=('native_client/src/third_party/valgrind')
  _flags+=(
           'symbol_level=1'
           'remove_webcore_debug_symbols=false'
           )
elif [ "${_debug_mode}" = "0" ]; then
  _flags+=(
           'remove_webcore_debug_symbols=true'
           'exclude_unwind_tables=true'
           )
fi

# https://crbug.com/678661
if [ "${_build_nacl}" = "1" ]; then
  _keeplibs+=('third_party/icu') # https://crbug.com/678661
elif [ "${_build_nacl}" = "0" ]; then
  depends+=('icu')
  _use_system+=('icu')
fi

################################################

prepare() {
  # Use custom toolchain.
  _flags+=(
           "custom_toolchain=\"//build/toolchain/linux/unbundle:default\""
           "host_toolchain=\"//build/toolchain/linux/unbundle:default\""
           )

  # Set Python2 path.
  mkdir -p python-path
  ln -sf /usr/bin/python2 "${srcdir}/python-path/python"
  export PATH="${srcdir}/python-path:$PATH"

  cd "${srcdir}/chromium-${pkgver}"

  # Use chromium-dev as branch name.
  sed -e 's|filename = "chromium-browser"|filename = "chromium-dev"|' \
      -e 's|confdir = "chromium|&-dev|' \
      -i chrome/BUILD.gn
  sed -e 's|config_dir.Append("chromium|&-dev|' \
      -i chrome/common/chrome_paths_linux.cc
  sed -e 's|/etc/chromium|&-dev|' \
      -e 's|/usr/share/chromium|&-dev|' \
      -i chrome/common/chrome_paths.cc
  sed -e 's|/etc/chromium|&-dev|' \
      -i components/policy/tools/template_writers/writer_configuration.py

  msg2 "Patching the sources"
  # Patch sources from Gentoo.
  patch -p1 -i "${srcdir}/chromium-FORTIFY_SOURCE-r2.patch"

  # Fix build with gcc 7(?)
  patch -p1 -i "${srcdir}/chromium-gcc5-r5.patch"

  # Pats to chromium dev's about why always they forget add/remove missing build rules
  # Done this time :D

  # Misc Patches:

  # https://crbug.com/710701
  _chrome_build_hash=$(curl -s "https://chromium.googlesource.com/chromium/src.git/+/${pkgver}?format=TEXT" | base64 -d | grep -Po '^parent \K[0-9a-f]{40}$')
  if [[ -z $_chrome_build_hash ]]; then
    error "Unable to fetch Chrome build hash."
    return 1
  fi
  echo "LASTCHANGE=$_chrome_build_hash-" > build/util/LASTCHANGE

  if [ "${_vulkan}" = "1" ]; then
    export VULKAN_SDK="/usr"
    sed 's|base/||' -i cc/output/vulkan_renderer.h
    sed 's|/x86_64-linux-gnu||' -i gpu/vulkan/BUILD.gn
  fi

  # Apply VAAPI patch
  # base64 -d "${srcdir}/chromium-intel-vaapi_r15.diff.base64" | patch -p1 -i -
  #patch -p1 -i "${srcdir}/chromium-intel-vaapi_r16.diff.patch"
  # needs generate gpu_lists_version.h by hand (?) # taked from DEPS files
  python2 build/util/lastchange.py -m GPU_LISTS_VERSION --revision-id-only --header gpu/config/gpu_lists_version.h

  # Patch from crbug (chromium bugtracker) or Arch chromium package

  # https://crbug.com/473866
  patch -p0 -i "${srcdir}/chromium-widevine-r1.patch"
  sed 's|@WIDEVINE_VERSION@|The Cake Is a Lie|g' -i third_party/widevine/cdm/stub/widevine_cdm_version.h

  # https://bugs.archlinux.org/task/55914
  #base64 -d "${srcdir}/chromium-exclude_unwind_tables.patch.base64" | patch -p1 -i -
  patch -p1 -i "${srcdir}/chromium-exclude_unwind_tables_r2.patch.patch"

  # Setup nodejs dependency
  mkdir -p third_party/node/linux/node-linux-x64/bin/
  ln -sf /usr/bin/node third_party/node/linux/node-linux-x64/bin/node

  # Try to fix libpng errors.
  msg2 "Attempt for fix libpng errors"
  for _path in 'chrome/app/theme' 'chrome/renderer' 'ui'; do
    pushd "${_path}" &> /dev/null
    export IFS=$'\n'
    for i in $(find . -name '*.png' -type f); do
      mogrify "${i}" &> /dev/null
    done
    export IFS=' '
    popd &> /dev/null
  done

  # Remove most bundled libraries. Some are still needed.
  msg2 "Removing unnecessary components to save space."
  python2 build/linux/unbundle/remove_bundled_libraries.py ${_keeplibs[@]} --do-remove

  msg2 "Make sure use Python2"
  find -name '*.py' | xargs sed -e 's|env python|&2|g' -e 's|bin/python|&2|g' -i

  msg2 "Changing bundle libraries to system ones."
  python2 build/linux/unbundle/replace_gn_files.py --system-libraries ${_use_system[@]}

  # Use the file at run time instead of effectively compiling it in.
  sed 's|//third_party/usb_ids/usb.ids|/usr/share/hwdata/usb.ids|g' -i device/usb/BUILD.gn

  if [ "${_build_nacl}" = "1" ]; then
    msg2 "Setup NaCl/PNaCl SDK: Download and install NaCl/PNaCl toolchains"
    python2 build/download_nacl_toolchains.py --packages nacl_x86_newlib,pnacl_newlib,pnacl_translator sync --extract
    # Download clang from google. need for build NaCl. also is used by build the project in x86_64 systems when use clang
    python2 tools/clang/scripts/update.py
  fi

  # Setup compilers.
  if [ "${_use_ccache}" = "1" ]; then
    export CCACHE_CPP2=yes
    export CCACHE_SLOPPINESS=time_macros
    _ccache=ccache
    _ccache_flags='-Qunused-arguments'
  fi

  _set_gcc() {
    _compiler=GCC
    _flags+=(
             'is_clang=false'
             'clang_use_chrome_plugins=false'
             )
    _c_compiler=gcc
    _cpp_compiler=g++
    CFLAGS+=' -fno-delete-null-pointer-checks'
    CXXFLAGS+=' -fno-delete-null-pointer-checks'
  }

  if [ "${_use_clang}" = "0" ]; then
    _set_gcc
  elif [ "${_use_clang}" = "1" ]; then
    _compiler=Clang
    _flags+=(
             'is_clang=true'
             'clang_use_chrome_plugins=true'
            )
    _clang_path="${srcdir}/chromium-${pkgver}/third_party/llvm-build/Release+Asserts/bin"
    _c_compiler="${_clang_path}/clang"
    _cpp_compiler="${_clang_path}/clang++"
    export CXXFLAGS="${CXXFLAGS//-fno-plt/}"
    export CFLAGS="${CFLAGS//-fno-plt/}"
    CFLAGS+=' -Wno-unknown-warning-option'
    CXXFLAGS+=' -Wno-unknown-warning-option'
  fi

  # Export compilers
  msg2 "Setup ${_compiler} compiler${_compiler_msg}"
  export AR=ar
  export NM=nm
  export CC="${_ccache} ${_c_compiler} ${_ccache_flags}"
  export CXX="${_ccache} ${_cpp_compiler} ${_ccache_flags}"
}

build() {

  msg2 "Build the Launcher"
  make -C "chromium-launcher" \
     CHROMIUM_SUFFIX="-dev" \

  cd "chromium-${pkgver}"

  msg2 "Starting building Chromium..."
  # Configure the builder.
  python2 tools/gn/bootstrap/bootstrap.py -v -s --no-clean
  out/Release/gn gen out/Release -v --args="${_flags[*]}" --script-executable=/usr/bin/python2

  # Build all with ninja.
  LC_ALL=C ninja -C out/Release -v pdf chrome chrome_sandbox chromedriver widevinecdmadapter clearkeycdm
}

package() {
  # Install launcher.
  make -C "chromium-launcher" \
    PREFIX=/usr \
    CHROMIUM_SUFFIX="-dev" \
    DESTDIR="${pkgdir}" \
    install
  install -Dm644 "chromium-launcher/LICENSE" "${pkgdir}/usr/share/licenses/chromium-dev/LICENSE.launcher"

  pushd "chromium-${pkgver}/out/Release" &> /dev/null

  # Set info
  source "${srcdir}/chromium-${pkgver}/chrome/installer/linux/common/installer.include"
  PACKAGE=chromium-dev
  PROGNAME=chromium-dev
  MENUNAME="Chromium-dev Web Browser"
  USR_BIN_SYMLINK_NAME=chromium-dev

  # Build with debug needs a tons of space. remove this save that space, but break the rebuild process.
  if [ "${_debug_mode}" = "1" ]; then
    rm -fr "chromium-${pkgver}/third_party"
  fi

  # Install binaries.
  install -Dm755 chrome "${pkgdir}/usr/lib/chromium-dev/chromium-dev"
  install -Dm4755 chrome_sandbox "${pkgdir}/usr/lib/chromium-dev/chrome-sandbox"
  install -Dm755 chromedriver "${pkgdir}/usr/lib/chromium-dev/chromedriver"
  ln -sf /usr/lib/chromium-dev/chromedriver "${pkgdir}/usr/bin/chromedriver-dev"

  # Install libs.
  _libs=(
         'libclearkeycdm.so'
         'libEGL.so'
         'libGLESv2.so'
         'libVkLayer_core_validation.so'
         'libVkLayer_object_tracker.so'
         'libVkLayer_parameter_validation.so'
         'libVkLayer_swapchain.so'
         'libVkLayer_threading.so'
         'libVkLayer_unique_objects.so'
         'libwidevinecdmadapter.so'
         'swiftshader/libEGL.so'
         'swiftshader/libGLESv2.so'
         #
         'natives_blob.bin'
         'snapshot_blob.bin'
         'v8_context_snapshot.bin'
         )
  for i in "${_libs[@]}"; do
    install -Dm755 "${i}" "${pkgdir}/usr/lib/chromium-dev/${i}"
  done

  # Install Resources.
  _resources=(
              'chrome_100_percent.pak'
              'chrome_200_percent.pak'
              'headless_lib.pak'
              'keyboard_resources.pak'
              'mus_app_resources_100.pak'
              'mus_app_resources_200.pak'
              'mus_app_resources_strings.pak'
              'resources.pak'
              'views_mus_resources.pak'
              )
  for i in "${_resources[@]}"; do
    install -Dm644 "${i}" "${pkgdir}/usr/lib/chromium-dev/${i}"
  done
  find resources -type f -name "*" -exec install -Dm644 '{}' "${pkgdir}/usr/lib/chromium-dev/{}" \;

  # Install .desktop and manpages
  process_template "${srcdir}/chromium-${pkgver}/chrome/app/resources/manpage.1.in" chromium-dev.1
  install -Dm644 chromium-dev.1 "${pkgdir}/usr/share/man/man1/chromium-dev.1"
  process_template "${srcdir}/chromium-${pkgver}/chrome/installer/linux/common/desktop.template" chromium-dev.desktop
  install -Dm644 chromium-dev.desktop "${pkgdir}/usr/share/applications/chromium-dev.desktop"

  # Install locales.
  find locales -type f -name "*.pak" -exec install -Dm644 '{}' "${pkgdir}/usr/lib/chromium-dev/{}" \;

  # Install icons.
  for _size in 16 22 24 32 48 128 256; do
    case "${_size}" in
      16|32) _branding="${srcdir}/chromium-${pkgver}/chrome/app/theme/default_100_percent/chromium" ;;
      *) _branding="${srcdir}/chromium-${pkgver}/chrome/app/theme/chromium" ;;
    esac
    install -Dm644 "${_branding}/product_logo_${_size}.png" "${pkgdir}/usr/share/icons/hicolor/${_size}x${_size}/apps/chromium-dev.png"
  done
  install -Dm644 "${srcdir}/chromium-dev.svg" "${pkgdir}/usr/share/icons/hicolor/scalable/apps/chromium-dev.svg"

  # Install NaCL stuff if is detected.
  if [ "${_build_nacl}" = "1" ]; then
    _nacl_libs=(
                'nacl_helper'
                'nacl_helper_bootstrap'
                'nacl_helper_nonsfi'
                'nacl_irt_x86_64.nexe'
                'icudtl.dat'
                )
    for i in "${_nacl_libs[@]}"; do
      install -Dm755 "${i}" "${pkgdir}/usr/lib/chromium-dev/${i}"
    done
  fi

  popd &> /dev/null

  # Install License
  install -Dm644 "chromium-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/chromium-dev/LICENSE"

  if [ "${_debug_mode}" = "0" ]; then
    # Manually strip binaries so that 'nacl_irt_*.nexe' is left intact.
    if [ "${_build_nacl}" = "1" ]; then
      strip $STRIP_BINARIES "${pkgdir}/usr/lib/chromium-dev/"nacl_helper{,_bootstrap,_nonsfi}
    fi
    strip $STRIP_BINARIES "${pkgdir}/usr/lib/chromium-dev/"{chromium-dev,chrome-sandbox,chromedriver}
    strip $STRIP_SHARED "${pkgdir}/usr/lib/chromium-dev/"lib*.so
    strip $STRIP_SHARED "${pkgdir}/usr/lib/chromium-dev/swiftshader/"lib*.so
  fi

  # Try to fix libpng errors. (second attemp)
  for _path in "${pkgdir}/usr/lib/chromium-dev/resources/inspector/Images"; do
    pushd "${_path}" &> /dev/null
    export IFS=$'\n'
    for i in $(find . -name '*.png' -type f); do
      mogrify "${i}" &> /dev/null
    done
    export IFS=' '
    popd &> /dev/null
  done
}
