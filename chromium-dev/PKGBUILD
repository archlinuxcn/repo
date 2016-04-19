# Maintainer: Gustavo Alvarez <sl1pkn07@gmail.com>
# Contributor: Mikhail Vorozhtsov <mikhail.vorozhtsov@gmail.com>
# Contributor: Nagisa <simonas@kazlauskas.me>
# Contributor: Misc <andreas.reis@gmail.com>
# Contributor: Jeagoss <jgoliver@jeago.com>

#########################
## -- Build options -- ##
#########################

_use_clang=1           # Use clang compiler (system). Results in faster build and smaller chromium.
_use_bundled_clang=1   # Use bundled clang compiler (needs build). NOTE: if use this option , '_use_clang' need set to 1
_use_ccache=0          # Use ccache when build
_use_pax=0             # Set 1 to change PaX permisions in executables NOTE: only use if use PaX environment
_use_gtk3=1            # If set 1, then build with GTK3 support, if set 0, then build with GTK2

##############################################
## -- Package and components information -- ##
##############################################
pkgname=chromium-dev
pkgver=51.0.2704.7
_launcher_ver=3
pkgrel=1
pkgdesc="The open-source project behind Google Chrome (Dev Channel)"
arch=('i686' 'x86_64')
url='http://www.chromium.org'
license=('BSD')
depends=('desktop-file-utils'
         #'icu'
         'jsoncpp'
         #'libsrtp'
         'libwebp'
         'libxslt'
         'libxss'
         'minizip'
         'perl-file-basedir'
         'nss'
         'pciutils'
         #'re2'
         'snappy'
         'speech-dispatcher'
         'speex'
         'xdg-utils'
         #'opus'
         #'protobuf'
         #'libevent'
         'libvpx'
         'ffmpeg'
         )
makedepends=('libexif'
             'elfutils'
             'gperf'
             'ninja'
             'perl-json'
             'python2-beautifulsoup4'
             'python2-html5lib'
             'python2-simplejson'
             'python2-jinja'
             'python2-ply'
             'subversion'
             'yasm'
             'git'
             'imagemagick'
             )
makedepends_x86_64=('lib32-gcc-libs' 'lib32-zlib')
optdepends=('chromium-pepper-flash-dev: PPAPI Flash Player (Dev Channel) (64bits only)'
            'chromium-widevine-dev: Widevine plugin (eg: Netflix) (Dev Channel) (64bits only)'
            #
            'kdebase-kdialog: Needed for file dialogs in KDE4/KF5'
            'kdialog-frameworks-git: Needed for file dialogs in KF5'
            #
            'kwalletmanager: Needed for storing passwords in KWallet in KF5'
            #
            'libexif: Need for read EXIF metadata'
            'ttf-font: For some typography'
            )
source=("https://commondatastorage.googleapis.com/chromium-browser-official/chromium-${pkgver}.tar.xz"
        "chromium-launcher-${_launcher_ver}.tar.gz::https://github.com/foutrelis/chromium-launcher/archive/v${_launcher_ver}.tar.gz"
        'chromium-dev.desktop'
        'chromium-dev.xml'
        'chromium-dev.svg'
        # Patch form Gentoo
        'https://raw.githubusercontent.com/gentoo/gentoo/master/www-client/chromium/files/chromium-system-ffmpeg-r2.patch'
        'https://raw.githubusercontent.com/gentoo/gentoo/master/www-client/chromium/files/chromium-snapshot-toolchain-r1.patch'
        # Misc Patches
        'enable_vaapi_on_linux-r7.diff'
        'chromium-system-jinja-r9.patch'
        'minizip.patch::http://pastebin.com/raw/QCqSDam5'
        # Patch from crbug (chromium bugtracker)
        'chromium-widevine-r0.patch' # https://crbug.com/473866
        )
sha1sums=( #"$(curl -sL https://gsdview.appspot.com/chromium-browser-official/?marker=chromium-${pkgver}.tar.x | awk -v FS='<td>"' -v RS='"</td>' '$0=$2' | head -n1)"
          "$(curl -sL "https://commondatastorage.googleapis.com/chromium-browser-official/chromium-${pkgver}.tar.xz.hashes" | grep sha1 | cut -d " " -f3)"
          'd18f8d96e80be9c31d994cc6362d7d8041c53319'
          '0acc45b901418f270d0b2068502e39c407c74ea4'
          '2b98c549332e7337307ce287e150930cfc1dfa5f'
          '336976cb66bf8df71fc7f2e92aa723891b6efb53'
          # Patch form Gentoo
          #'c24d14029714d2295f3220a7173a5a7362f578a2'
          '450cd81653499eb50f0f7df1b0d4d1c1620365a5'
          '7b9c1a7e0e581413dbebb0e894f68ce2f2ba0e6a'
          # Misc Patches
          'a1bf7f2f23544ef9612513c9271cb98963075dae'
          '1063521b4e3bf1bb25b666ef7423968886fe055c'
          'bc90b327b05dbecaa88da43211ae0a4ed0c6c57f'
          # Patch from crbug (chromium bugtracker)
          'fa9ff0ff9049784b4a1ec37292530ae61aece610'
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

# 32 or 64 bits?
if [ "${CARCH}" = "i686" ]; then
  _target_arch=ia32
  _build_pnacl=0
  _pnacl_arch=32
elif  [ "${CARCH}" = "x86_64" ]; then
  _target_arch=x64
  _build_pnacl=1
  _pnacl_arch=64
fi

# If use PaX environment, need 'paxctl'
if [ "${_use_pax}" = "1" ]; then
  makedepends+=('paxctl')
fi

# Need you use clang?
if [ "${_use_clang}" = "1" ]; then
  makedepends+=('clang')
fi
if [ "${_use_bundled_clang}" = "1" ]; then
  makedepends+=('cmake'
                'ocaml'
                'libffi'
                'chrpath'
                )
fi

# Build with GTK3?
if [ "${_use_gtk3}" = "1" ]; then
  depends+=('gtk3')
  _launcher_gtk='GTK=3'
  optdepends+=('libappindicator-gtk3: Needed for show systray icon in the panel in plasma-next (KF5)')
elif [ "${_use_gtk3}" = "0" ]; then
  depends+=('gtk2')
  optdepends+=('libappindicator-gtk2: Needed for show systray icon in the panel in plasma-next (KF5)')
fi

# Need you use ccache?
if [ "${_use_ccache}" = "1" ]; then
  makedepends+=('ccache')
fi

# Are we in Gnome?
_use_gnome=0
if [ -f /usr/lib/libgconf-2.so ]; then
  depends+=('gconf')
  _use_gnome=1
fi

# Are you use gnome-keyring?
_use_gnome_keyring=0
if [ -f /usr/lib/libgnome-keyring.so ]; then
  depends+=('libgnome-keyring'
            'gnome-keyring')
  _use_gnome_keyring=1
fi

# Are you use Pulseaudio?
_use_pulseaudio=0
if [ -x /usr/lib/libpulse.so ]; then
  depends+=('libpulse')
  _use_pulseaudio=1
fi


# List of third-party components needed for build chromium. The rest is remove by remove_bundled_libraries srcipt in prepare()
_necesary=('base/third_party/dmg_fp'
           'base/third_party/dynamic_annotations'
           'base/third_party/icu'
           'base/third_party/libevent'
           'base/third_party/nspr'
           'base/third_party/superfasthash'
           'base/third_party/symbolize'
           'base/third_party/valgrind'
           'base/third_party/xdg_mime'
           'base/third_party/xdg_user_dirs'
           'breakpad/src/third_party/curl'
           'chrome/third_party/mozilla_security_manager'
           'courgette/third_party'
           'crypto/third_party/nss'
           'native_client/src/third_party/dlmalloc'
           'native_client_sdk/src/libraries/third_party/newlib-extras'
           'net/third_party/mozilla_security_manager'
           'net/third_party/nss'
           'third_party/WebKit'
           'third_party/analytics'
           'third_party/angle'
           'third_party/angle/src/third_party/compiler'
           'third_party/angle/src/third_party/murmurhash'
           'third_party/angle/src/third_party/trace_event'
           'third_party/angle/src/third_party/libXNVCtrl'
           'third_party/brotli'
           'third_party/boringssl'
           'third_party/cacheinvalidation'
           'third_party/catapult'
           'third_party/catapult/third_party/py_vulcanize'
           'third_party/catapult/third_party/py_vulcanize/third_party/rcssmin'
           'third_party/catapult/third_party/py_vulcanize/third_party/rjsmin'
           'third_party/catapult/tracing/third_party/components/polymer'
           'third_party/catapult/tracing/third_party/d3'
           'third_party/catapult/tracing/third_party/gl-matrix'
           'third_party/catapult/tracing/third_party/jszip'
           'third_party/cld_2'
           'third_party/cros_system_api'
           'third_party/cython/python_flags.py'
           'third_party/devscripts'
           'third_party/dom_distiller_js'
           'third_party/dom_distiller_js/dist/proto_gen/third_party/dom_distiller_js'
           'third_party/ffmpeg' # http://crbug.com/588423
           'third_party/fips181'
           'third_party/flot'
           'third_party/google_input_tools'
           'third_party/google_input_tools/third_party/closure_library'
           'third_party/google_input_tools/third_party/closure_library/third_party/closure'
           'third_party/hunspell'
           'third_party/iccjpeg'
           'third_party/icu' # https://crbug.com/584920 and https://crbug.com/592268
           'third_party/jstemplate'
           'third_party/khronos'
           'third_party/leveldatabase'
           'third_party/libaddressinput'
           'third_party/libjingle'
           'third_party/libphonenumber'
           'third_party/libpng'
           'third_party/libsecret'
           'third_party/libsrtp'
           'third_party/libudev'
           'third_party/libusb'
           'third_party/libva'
           'third_party/libxml/chromium'
           'third_party/libwebm'
           'third_party/libXNVCtrl'
           'third_party/libyuv'
           'third_party/lss'
           'third_party/lzma_sdk'
           'third_party/mesa'
           'third_party/modp_b64'
           'third_party/mt19937ar'
           'third_party/openh264' # http://crbug.com/588423 (?)
           'third_party/openmax_dl'
           'third_party/opus'
           'third_party/ots'
           'third_party/pdfium'
           'third_party/pdfium/third_party/agg23'
           'third_party/pdfium/third_party/base'
           'third_party/pdfium/third_party/bigint'
           'third_party/pdfium/third_party/freetype'
           'third_party/pdfium/third_party/lcms2-2.6'
           'third_party/pdfium/third_party/libjpeg'
           'third_party/pdfium/third_party/libopenjpeg20'
           'third_party/pdfium/third_party/zlib_v128'
           'third_party/polymer'
           'third_party/protobuf'
           'third_party/qcms'
           'third_party/re2'
           'third_party/sfntly'
           'third_party/skia'
           'third_party/smhasher'
           'third_party/sqlite'
           'third_party/tcmalloc'
           'third_party/usrsctp'
           'third_party/web-animations-js'
           'third_party/webdriver'
           'third_party/webrtc'
           'third_party/widevine'
           'third_party/woff2'
           'third_party/x86inc'
           'third_party/zlib/google'
           'url/third_party/mozilla'
           'v8/src/third_party/fdlibm'
           'v8/src/third_party/valgrind'
           )

# Set build flags
# NOTE
# -Denable_sql_database=0                    | http://crbug.com/22208
# -Dlogging_like_official_build=1            | Save space by removing DLOG and DCHECK messages (about 6% reduction).
# -Dlinux_use_gold_flags=0                   | Never use bundled gold binary. Disable gold linker flags for now.
# -Dusb_ids_path=/usr/share/hwdata/usb.ids   | Use the file at run time instead of effectively compiling it in.
# -Denable_hotwording=0                      | http://crbug.com/491435
# -Dicu_use_data_file_flag=1                 | set to 0 when fix https://crbug.com/592268

_flags=("-Dclang=${_use_clang}"
        '-Ddisable_glibc=1'
        '-Ddisable_fatal_linker_warnings=1'
        '-Denable_sql_database=0'
        '-Denable_hidpi=1'
        '-Denable_touch_ui=1'
        '-Denable_webrtc=1'
        '-Denable_widevine=1'
        '-Denable_pepper_cdms=1'
        '-Denable_hotwording=0'
        '-Denable_hangout_services_extension=1'
        '-Dffmpeg_branding=ChromeOS'
        "-Dgoogle_api_key=${_google_api_key}"
        "-Dgoogle_default_client_id=${_google_default_client_id}"
        "-Dgoogle_default_client_secret=${_google_default_client_secret}"
        '-Dicu_use_data_file_flag=1'
        '-Dlibspeechd_h_prefix=speech-dispatcher/'
        "-Dlinux_link_gnome_keyring=${_use_gnome_keyring}"
        "-Dlinux_link_gsettings=${_use_gnome}"
        '-Dlinux_link_kerberos=1'
        '-Dlinux_link_libbrlapi=1'
        '-Dlinux_link_libpci=1'
        '-Dlinux_link_libspeechd=1'
        "-Dlinux_link_pulseaudio=${_use_pulseaudio}"
        '-Dlinux_strip_binary=1'
        '-Dlinux_use_bundled_binutils=0'
        '-Dlinux_use_bundled_gold=0'
        '-Dlinux_use_gold_flags=0'
        '-Dlogging_like_official_build=1'
        '-Dno_strict_aliasing=1'
        '-Dproprietary_codecs=1'
        '-Dpython_ver=2.7'
        '-Dremove_webcore_debug_symbols=1'
        "-Dtarget_arch=${_target_arch}"
        '-Dusb_ids_path=/usr/share/hwdata/usb.ids'
        "-Duse_gconf=${_use_gnome}"
        "-Duse_gio=${_use_gnome}"
        "-Duse_gnome_keyring=${_use_gnome_keyring}"
        "-Duse_gtk3=${_use_gtk3}"
        "-Duse_pulseaudio=${_use_pulseaudio}"
        '-Duse_sysroot=0'
        '-Duse_ash=0'
        '-Duse_ozone=0'
        '-Duse_xkbcommon=1'
        '-Dchromeos=0'
        '-Dwerror='
        )

# Set pnacl flags
if [ "${_build_pnacl}" = "0" ]; then
  _flags+=('-Ddisable_nacl=1'
           '-Ddisable_pnacl=1'
           )
fi

# Set clang flags
if [ "${_use_clang}" = "1" ]; then
  if [ "${_use_bundled_clang}" = "0" ]; then
    _flags+=('-Dclang_use_chrome_plugins=0'
             '-Dhost_clang=0'
             )
  elif [ "${_use_bundled_clang}" = "1" ]; then
    _flags+=('-Dclang_use_chrome_plugins=1'
             '-Dhost_clang=1'
             )
  fi
fi

# Set the bundled/external components
# TODO
# -Duse_system_hunspell=1    | Upstream changes needed
# -Duse_system_libusb=1      | https://crbug.com/266149
# -Duse_system_opus=1        | https://code.google.com/p/webrtc/issues/detail?id=3077
# -Duse_system_sqlite=1      | https://crbug.com/22208
# -Duse_system_ssl=1         | https://crbug.com/58087
# -Duse_system_libsrtp=1     | https://crbug.com/501318
# -Duse_system_re2=1         | https://bugs.gentoo.org/show_bug.cgi?id=571156
# -Duse_system_protobuf=1    | https://bugs.gentoo.org/show_bug.cgi?id=525560
# -Duse_system_icu=1         | https://crbug.com/584920 and https://crbug.com/592268
# -Duse_system_libpng=1      | https://crbug.com/595429
# NOTE
# -Duse_system_openssl=0     | Set to 1 if use BoringSSL instead of SSL
# -Duse_system_libevent=0    | Need older version (<2.x.x)
# -Duse_system_v8=0          | Possible broken in API/ABI if use a differen version
# -Duse_system_libxnvctrl=0  | Because not exist in Arch (and not all users use nvidia blob drivers)
_use_system=('-Duse_system_expat=1'
             '-Duse_system_ffmpeg=1'
             '-Duse_system_flac=1'
             '-Duse_system_fontconfig=1'
             '-Duse_system_harfbuzz=1'
             '-Duse_system_icu=0'
             '-Duse_system_jsoncpp=1'
             '-Duse_system_libevent=0'
             '-Duse_system_libexif=1'
             '-Duse_system_libjpeg=1'
             '-Duse_system_libpng=0'
             '-Duse_system_libsrtp=0'
             '-Duse_system_libusb=0'
             '-Duse_system_libvpx=1'
             '-Duse_system_libwebp=1'
             '-Duse_system_libxml=1'
             '-Duse_system_libxnvctrl=0'
             '-Duse_system_libxslt=1'
             '-Duse_system_minizip=1'
             '-Duse_system_nspr=1'
             '-Duse_system_openssl=0'
             '-Duse_system_opus=0'
             '-Duse_system_protobuf=0'
             '-Duse_system_re2=0'
             '-Duse_system_snappy=1'
             '-Duse_system_speex=1'
             '-Duse_system_sqlite=0'
             '-Duse_system_ssl=0'
             '-Duse_system_v8=0'
             '-Duse_system_yasm=1'
             '-Duse_system_xdg_utils=1'
             '-Duse_system_zlib=1'
             )

################################################

prepare() {

  # Set Python2 path
  mkdir -p python-path
  ln -s /usr/bin/python2 "${srcdir}/python-path/python"
  export PATH="${srcdir}/python-path:$PATH"

  cd "chromium-${pkgver}"

  # Fix to save configuration in ~/.config/chromium-dev
  sed -e "s|'filename': 'chromium-browser'|'filename': 'chromium-dev'|" \
      -e "s|'confdir': 'chromium'|'confdir': 'chromium-dev'|" \
      -i chrome/chrome_exe.gypi
  sed -e 's|config_dir.Append("chromium")|config_dir.Append("chromium-dev")|' \
      -e 's|config_dir.Append("chrome-frame")|config_dir.Append("chrome-frame-dev")|' \
      -i chrome/common/chrome_paths_linux.cc

  msg2 "Patching the sources"
  # Patch sources from Gentoo
  patch -p1 -i "${srcdir}/chromium-system-ffmpeg-r2.patch"
  patch -p0 -i "${srcdir}/chromium-snapshot-toolchain-r1.patch"

  # Misc Patches:
  patch -p1 -i "${srcdir}/enable_vaapi_on_linux-r7.diff"
  patch -p0 -i "${srcdir}/chromium-system-jinja-r9.patch"
  patch -p1 -i "${srcdir}/minizip.patch"

  # Patch from crbug (chromium bugtracker)
  # https://crbug.com/473866
  patch -p0 -i "${srcdir}/chromium-widevine-r0.patch"
  sed 's|@WIDEVINE_VERSION@|The Cake Is a Lie|g' -i "third_party/widevine/cdm/stub/widevine_cdm_version.h"

  ##
  # Fix libpng errors
  pushd chrome/app/theme &> /dev/null
  export IFS=$'\n'
  for i in $(find . -name '*.png' -type f); do
    mogrify "${i}" &> /dev/null
  done
  export IFS=' '
  popd &> /dev/null

  # Make it possible to remove third_party/adobe
  echo > "${srcdir}/flapper_version.h"
  _flags+=("-Dflapper_version_h_file=${srcdir}/flapper_version.h")

  # Remove most bundled libraries. Some are still needed.
  msg2 "Removing unnecessary components to save space"
  python2 build/linux/unbundle/remove_bundled_libraries.py ${_necesary[@]} --do-remove
  rm -fr native_client/toolchain
  rm -fr build/linux/debian*

  if [ "${_build_pnacl}" = "1" ]; then
    msg2 "Setup NaCl/PNaCl SDK: Download and install NaCl/PNaCl toolchains"
    python2 build/download_nacl_toolchains.py --packages nacl_x86_newlib,pnacl_newlib,pnacl_translator sync --extract
  fi

  msg2 "Make sure use Python2"
  find . -name '*.py' -exec sed -r 's|/usr/bin/python$|&2|g' -i {} +
  find . -name '*.py' -exec sed -r 's|/usr/bin/env python$|&2|g' -i {} +

  touch chrome/test/data/webui/i18n_process_css_test.html
}

build() {

  msg2 "Build the Launcher"
  make -C "chromium-launcher-${_launcher_ver}" CHROMIUM_SUFFIX="-dev" PREFIX=/usr ${_launcher_gtk}

  cd "chromium-${pkgver}"

  # Set ccache environment
  if [ "${_use_ccache}" = "1" ]; then
    msg2 "Setup ccache"
    export CCACHE_CPP2=yes
    export CCACHE_SLOPPINESS=time_macros
  fi

  # Use system/bundled Clang? or GCC?
  _bundled_clang_path="${srcdir}/chromium-${pkgver}/third_party/llvm-build/Release+Asserts/bin"

  if [ "${_use_clang}" = "0" ]; then
    msg2 "Setup for use system GCC"
    if [ "${_use_ccache}" = "0" ]; then
      export CC="gcc -Wall"
      export CXX="g++ -Wall"
    elif [ "${_use_ccache}" = "1" ]; then
      export CC="ccache gcc -Wall"
      export CXX="ccache g++ -Wall"
    fi
  elif [ "${_use_clang}" = "1" ]; then
    if [ "${_use_bundled_clang}" = "0" ]; then
      msg2 "Setup for use system Clang"
      if [ "${_use_ccache}" = "0" ]; then
        export CC="clang -Qunused-arguments"
        export CXX="clang++ -Qunused-arguments"
      elif [ "${_use_ccache}" = "1" ]; then
        export CC="ccache clang -Qunused-arguments"
        export CXX="ccache clang++ -Qunused-arguments"
      fi
      export CXXFLAGS="${CXXFLAGS} -Wno-unknown-warning-option"
    elif [ "${_use_bundled_clang}" = "1" ]; then
      msg2 "Setup and build bundled Clang"
      python2 tools/clang/scripts/update.py --force-local-build --without-android --gcc-toolchain=/usr
      if [ "${_use_ccache}" = "0" ]; then
        export CC="${_bundled_clang_path}/clang -Qunused-arguments"
        export CXX="${_bundled_clang_path}/clang++ -Qunused-arguments"
      elif [ "${_use_ccache}" = "1" ]; then
        export CC="ccache ${_bundled_clang_path}/clang -Qunused-arguments"
        export CXX="ccache ${_bundled_clang_path}/clang++ -Qunused-arguments"
      fi
    fi
  fi

  # Changing bundle libraries to system ones
  python2 build/linux/unbundle/replace_gyp_files.py ${_use_system[@]}

  # update libaddressinput strings
  python2 third_party/libaddressinput/chromium/tools/update-strings.py

  # CFLAGS are passed through -Drelease_extra_cflags=
  export -n CFLAGS CXXFLAGS

  msg2 "Starting building Chromium..."
  # Configure the builder
  python2 build/gyp_chromium --depth=. -Drelease_extra_cflags="$CFLAGS" ${_flags[@]} ${_use_system[@]}

  # Build mksnapshot and pax-mark it.
  if [ "${_use_pax}" = "1" ]; then
    ninja -C out/Release -v "mksnapshot"
    paxctl -cm "out/Release/mksnapshot"
  fi

  # Build all with ninja
  LC_ALL=C ninja -C out/Release -v pdf chrome chrome_sandbox chromedriver widevinecdmadapter clearkeycdm

  # Pax-mark again
  if [ "${_use_pax}" = "1" ]; then
    paxctl -cm out/Release/chrome
  fi
}

package() {
  # Install launcher
  make -C "chromium-launcher-${_launcher_ver}" CHROMIUM_SUFFIX="-dev" PREFIX=/usr DESTDIR="${pkgdir}" install-strip
  install -Dm644 "chromium-launcher-${_launcher_ver}/LICENSE" "${pkgdir}/usr/share/licenses/chromium-dev/LICENSE.launcher"

  pushd "chromium-${pkgver}/out/Release" &> /dev/null

  # Install binaries
  install -Dm755 chrome "${pkgdir}/usr/lib/chromium-dev/chromium-dev"
  install -Dm644 chrome.1 "${pkgdir}/usr/share/man/man1/chromium-dev.1"
  install -Dm4755 chrome_sandbox "${pkgdir}/usr/lib/chromium-dev/chrome-sandbox"
  install -Dm755 chromedriver "${pkgdir}/usr/lib/chromium-dev/chromedriver"
  ln -s /usr/lib/chromium-dev/chromedriver "${pkgdir}/usr/bin/chromedriver-dev"

  # Install libs
  for i in libwidevinecdmadapter libclearkeycdm; do
    install -Dm755 "${i}.so" "${pkgdir}/usr/lib/chromium-dev/${i}.so"
  done
  install -Dm644 icudtl.dat "${pkgdir}/usr/lib/chromium-dev/icudtl.dat" # https://crbug.com/584920 and https://crbug.com/592268
  install -Dm644 natives_blob.bin "${pkgdir}/usr/lib/chromium-dev/natives_blob.bin"
  install -Dm644 snapshot_blob.bin "${pkgdir}/usr/lib/chromium-dev/snapshot_blob.bin"

  # Install Resources
  for i in content_resources keyboard_resources resources chrome_100_percent chrome_200_percent chrome_material_100_percent chrome_material_200_percent; do
    install -Dm644 "${i}.pak" "${pkgdir}/usr/lib/chromium-dev/${i}.pak"
  done

  # Install locales
  find pseudo_locales -type f -name "*.pak" -exec install -Dm644 '{}' "${pkgdir}/usr/lib/chromium-dev/{}" \;
  find locales -type f -name "*.pak" -exec install -Dm644 '{}' "${pkgdir}/usr/lib/chromium-dev/{}" \;
  find resources -type f -name "*" -exec install -Dm644 '{}' "${pkgdir}/usr/lib/chromium-dev/{}" \;
  (cd "${pkgdir}/usr/lib/chromium-dev"; ln -s locales remote_locales)

  # Install icons
  for _size in 16 22 24 32 48 128 256; do
    case "${_size}" in
      16|32) _branding="${srcdir}/chromium-${pkgver}/chrome/app/theme/default_100_percent/chromium" ;;
      *) _branding="${srcdir}/chromium-${pkgver}/chrome/app/theme/chromium" ;;
    esac
    install -Dm644 "${_branding}/product_logo_${_size}.png" "${pkgdir}/usr/share/icons/hicolor/${_size}x${_size}/apps/chromium-dev.png"
  done

  # Install pNaCL/NaCL stuff if is detected
  if [ "${_build_pnacl}" = "1" ]; then
    install -Dm755 nacl_helper "${pkgdir}/usr/lib/chromium-dev/nacl_helper"
    install -Dm755 nacl_helper_bootstrap "${pkgdir}/usr/lib/chromium-dev/nacl_helper_bootstrap"
    install -Dm755 nacl_helper_nonsfi "${pkgdir}/usr/lib/chromium-dev/nacl_helper_nonsfi"
    install -Dm755 "nacl_irt_x86_${_pnacl_arch}.nexe" "${pkgdir}/usr/lib/chromium-dev/nacl_irt_x86_${_pnacl_arch}.nexe"
    (cd pnacl; for i in $(find -type f); do install -Dm755 "${i}" "${pkgdir}/usr/lib/chromium-dev/pnacl/${i}"; done)
  fi

  popd &> /dev/null

  # Install some external files
  install -Dm644 chromium-dev.desktop "${pkgdir}/usr/share/applications/chromium-dev.desktop"
  install -Dm644 chromium-dev.svg "${pkgdir}/usr/share/icons/hicolor/scalable/apps/chromium-dev.svg"
  install -Dm644 "chromium-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/chromium-dev/LICENSE"

  # install gnome stuff if is detected
  if [ "${_use_gnome}" = "1" ]; then
    install -Dm644 chromium-dev.xml "${pkgdir}/usr/share/gnome-control-center/default-apps/chromium-dev.xml"
  fi

  # Manually strip binaries so that 'nacl_irt_*.nexe' is left intact
  if [ "${_build_pnacl}" = "1" ]; then
    strip $STRIP_BINARIES "${pkgdir}/usr/lib/chromium-dev/"nacl_helper{,_bootstrap,_nonsfi}
  fi
  strip $STRIP_BINARIES "${pkgdir}/usr/lib/chromium-dev/"{chromium-dev,chrome-sandbox,chromedriver}
  strip $STRIP_SHARED "${pkgdir}/usr/lib/chromium-dev/"lib{widevinecdmadapter,clearkeycdm}.so
}
