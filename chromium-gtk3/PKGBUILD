# Maintainer: Sergey Shatunov <me@prok.pw>
# Contributor: Evangelos Foutras <evangelos@foutrelis.com>
# Contributor: Pierre Schmitz <pierre@archlinux.de>
# Contributor: Jan "heftig" Steffens <jan.steffens@gmail.com>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>

# Possible replacements are listed in build/linux/unbundle/replace_gn_files.py
# Keys are the names in the above script; values are the dependencies in Arch
declare -rgA _system_libs=(
  [ffmpeg]=ffmpeg
  [flac]=flac
  [harfbuzz-ng]=harfbuzz-icu
  [icu]=icu
  [libjpeg]=libjpeg
  [libpng]=libpng
  [libvpx]=libvpx
  [libwebp]=libwebp
  #[libxml]=libxml2    # https://bugs.archlinux.org/task/29939
  [libxslt]=libxslt
  [re2]=re2
  [snappy]=snappy
  [yasm]=
  [zlib]=minizip
)

pkgname=chromium-gtk3
_pkgname=chromium
pkgver=56.0.2924.87
pkgrel=1
_launcher_ver=3
pkgdesc="The open-source project behind Google Chrome, an attempt at creating a safer, faster, and more stable browser (GTK3 version)"
arch=('i686' 'x86_64')
url="https://www.chromium.org/Home"
license=('BSD')
depends=('gtk3' 'libcups' 'nss' 'alsa-lib' 'xdg-utils' 'libxss' 'libexif' 'libgcrypt'
         'ttf-font' 'systemd' 'dbus' 'libpulse' 'perl' 'perl-file-basedir'
         'pciutils' 'desktop-file-utils' 'hicolor-icon-theme')
depends+=(${_system_libs[@]})
makedepends=('gtk2' 'python2' 'gperf' 'yasm' 'mesa' 'ninja' 'git')
optdepends=('kdialog: needed for file dialogs in KDE'
            'gnome-keyring: for storing passwords in GNOME keyring'
            'kwallet: for storing passwords in KWallet')
conflicts=($_pkgname)
provides=($_pkgname)
install=chromium.install
source=(https://commondatastorage.googleapis.com/chromium-browser-official/$_pkgname-$pkgver.tar.xz
        chromium-launcher-$_launcher_ver.tar.gz::https://github.com/foutrelis/chromium-launcher/archive/v$_launcher_ver.tar.gz
        chromium.desktop
        chromium-glib-2.24.patch
        chromium-system-ffmpeg-r4.patch
        chromium-widevine.patch)
sha256sums=('9aac081ffccaae6497068100477a4e6ac7086bd15ad3c3cd009b9a760b7a53e0'
            '8b01fb4efe58146279858a754d90b49e5a38c9a0b36a1f84cbb7d12f92b84c28'
            '028a748a5c275de9b8f776f97909f999a8583a4b77fd1cd600b4fc5c0c3e91e9'
            '6953651c002efe7fca8cda3143e963037ed38a0a4bc7ccb79304637c45340047'
            'e3c474dbf3822a0be50695683bd8a2c9dfc82d41c1524a20b4581883c0c88986'
            'd6fdcb922e5a7fbe15759d39ccc8ea4225821c44d98054ce0f23f9d1f00c9808')

# Google API keys (see http://www.chromium.org/developers/how-tos/api-keys)
# Note: These are for Arch Linux use ONLY. For your own distribution, please
# get your own set of keys. Feel free to contact foutrelis@archlinux.org for
# more information.
_google_api_key=AIzaSyDwr302FpOSkGRpLlUpPThNTDPbXcIn_FM
_google_default_client_id=413772536636.apps.googleusercontent.com
_google_default_client_secret=0ZChLK6AxeA3Isu96MkwqDR4

prepare() {
  cd "$srcdir/$_pkgname-$pkgver"

  # Enable support for the Widevine CDM plugin
  # libwidevinecdm.so is not included, but can be copied over from Chrome
  # (Version string doesn't seem to matter so let's go with "Pinkie Pie")
  sed "s/@WIDEVINE_VERSION@/Pinkie Pie/" ../chromium-widevine.patch |
    patch -Np1

  # Fixes from Gentoo
  patch -Np1 -i ../chromium-system-ffmpeg-r4.patch
  patch -Np1 -i ../chromium-glib-2.24.patch

  # Work around bug in blink in which GCC 6 optimizes away null pointer checks
  # https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=833524
  # https://gcc.gnu.org/bugzilla/show_bug.cgi?id=68853#c2
  sed -i '/config("compiler")/ a cflags_cc = [ "-fno-delete-null-pointer-checks" ]' \
    build/config/linux/BUILD.gn

  # Use Python 2
  find . -name '*.py' -exec sed -i -r 's|/usr/bin/python$|&2|g' {} +

  # There are still a lot of relative calls which need a workaround
  mkdir -p "$srcdir/python2-path"
  ln -sf /usr/bin/python2 "$srcdir/python2-path/python"

  # Remove bundled libraries for which we will use the system copies; this
  # *should* do what the remove_bundled_libraries.py script does, with the
  # added benefit of not having to list all the remaining libraries
  local _lib
  for _lib in ${!_system_libs[@]} ${_system_libs[libjpeg]+libjpeg_turbo}; do
    find -type f -path "*third_party/$_lib/*" \
      \! -path "*third_party/$_lib/chromium/*" \
      \! -path "*third_party/$_lib/google/*" \
      \! -path "*base/third_party/icu/*" \
      \! -regex '.*\.\(gn\|gni\|isolate\|py\)' \
      -delete
  done

  python2 build/linux/unbundle/replace_gn_files.py \
    --system-libraries "${!_system_libs[@]}"

  python2 third_party/libaddressinput/chromium/tools/update-strings.py
}

build() {
  make -C "$srcdir/chromium-launcher-$_launcher_ver" PREFIX=/usr GTK=3

  cd "$srcdir/$_pkgname-$pkgver"

  export PATH="$srcdir/python2-path:$PATH"
  export TMPDIR="$srcdir/temp"
  mkdir -p "$TMPDIR"

  local _flags=(
    'is_clang=false'
    'clang_use_chrome_plugins=false'
    'symbol_level=0'
    'is_debug=false'
    'fatal_linker_warnings=false'
    'treat_warnings_as_errors=false'
    'fieldtrial_testing_like_official_build=true'
    'remove_webcore_debug_symbols=true'
    'ffmpeg_branding="Chrome"'
    'proprietary_codecs=true'
    'link_pulseaudio=true'
    'linux_use_bundled_binutils=false'
    'use_cups=true'
    'use_gconf=false'
    'use_gnome_keyring=false'
    'use_gold=false'
    'use_gtk3=true'
    'use_kerberos=true'
    'use_pulseaudio=true'
    'use_sysroot=false'
    'enable_hangout_services_extension=true'
    'enable_widevine=true'
    'enable_nacl=false'
    'enable_nacl_nonsfi=false'
    "google_api_key=\"${_google_api_key}\""
    "google_default_client_id=\"${_google_default_client_id}\""
    "google_default_client_secret=\"${_google_default_client_secret}\""
  )

  python2 tools/gn/bootstrap/bootstrap.py --gn-gen-args "${_flags[*]}"
  out/Release/gn gen out/Release --args="${_flags[*]}" \
    --script-executable=/usr/bin/python2

  ninja -C out/Release chrome chrome_sandbox chromedriver widevinecdmadapter
}

package() {
  cd "$srcdir/chromium-launcher-$_launcher_ver"

  make PREFIX=/usr DESTDIR="$pkgdir" install-strip
  install -Dm644 LICENSE \
    "$pkgdir/usr/share/licenses/chromium/LICENSE.launcher"

  cd "$srcdir/$_pkgname-$pkgver"

  install -D out/Release/chrome "$pkgdir/usr/lib/chromium/chromium"
  install -Dm644 out/Release/chrome.1 "$pkgdir/usr/share/man/man1/chromium.1"
  install -Dm644 "$srcdir/chromium.desktop" \
    "$pkgdir/usr/share/applications/chromium.desktop"

  install -Dm4755 out/Release/chrome_sandbox \
    "$pkgdir/usr/lib/chromium/chrome-sandbox"

  cp -a out/Release/{*.pak,*.bin,chromedriver,libwidevinecdmadapter.so} \
    out/Release/locales \
    out/Release/gen/content/content_resources.pak \
    "$pkgdir/usr/lib/chromium/"

  ln -s /usr/lib/chromium/chromedriver "$pkgdir/usr/bin/chromedriver"

  for size in 22 24 48 64 128 256; do
    install -Dm644 "chrome/app/theme/chromium/product_logo_$size.png" \
      "$pkgdir/usr/share/icons/hicolor/${size}x${size}/apps/chromium.png"
  done

  for size in 16 32; do
    install -Dm644 "chrome/app/theme/default_100_percent/chromium/product_logo_$size.png" \
      "$pkgdir/usr/share/icons/hicolor/${size}x${size}/apps/chromium.png"
  done

  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set ts=2 sw=2 et:
