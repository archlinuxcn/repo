# Use environment variable MAKEPKG_AYUGRAM_API_ID and MAKEPKG_AYUGRAM_API_HASH to override default values

pkgname=ayugram-desktop
pkgver=7.2.9
pkgrel=1
pkgdesc="Desktop Telegram client with good customization and Ghost mode."
arch=("x86_64" "aarch64")
url="https://github.com/AyuGram/AyuGramDesktop"
license=("GPL-3.0-or-later WITH OpenSSL-exception")
depends=('abseil-cpp'
         'ada'
         'cmark-gfm'
         'ffmpeg'
         'glib2'
         'glibc'
         'hicolor-icon-theme'
         'hunspell'
         'kcoreaddons'
         'libavif'
         'libfido2'
         'libgcc'
         'libheif'
         'libjpeg-turbo'
         'libjxl'
         'libpipewire'
         'libsrtp'
         'libstdc++'
         'libvpx'
         'libxcb'
         'libxcomposite'
         'libxdamage'
         'libxext'
         'libxfixes'
         'libxkbcommon'
         'libxrandr'
         'libxtst'
         'lz4'
         'minizip'
         'openal'
         'openh264'
         'openssl'
         'opus'
         'pipewire'
         'qt6-base'
         'qt6-declarative'
         'qt6-imageformats'
         'qt6-svg'
         'qt6-wayland'
         'rnnoise'
         'tlottie'
         'xxhash'
         'zlib')
makedepends=('boost'
             'boost-libs'
             'cmake'
             'glib2-devel'
             'gobject-introspection'
             'qt6-shadertools'
             'gperf'
             'libtg_owt'
             'microsoft-gsl'
             'ninja'
             'python'
             'range-v3'
             'tl-expected'
             'vulkan-headers')
optdepends=('geoclue: geoinformation support'
            'crow-translate: translation provider'
            'webkit2gtk-4.1: embedded browser features provided by webkit2gtk-4.1 (gtk3)'
            'webkitgtk-6.0: embedded browser features provided by webkitgtk-6.0 (gtk4)'
            'xdg-desktop-portal: desktop integration')
_tdlib_commit=bc9c263e2bfee06aaab41e82db51a103376030bc
source=("AyuGram-$pkgver-full.tar.gz::https://github.com/AyuGram/AyuGramDesktop/releases/download/v$pkgver/AyuGramDesktop-$pkgver-full.tar.gz"
        "td-$_tdlib_commit.tar.gz::https://github.com/tdlib/td/archive/$_tdlib_commit.tar.gz")

sha256sums=('ead2665a32f38277e76d3041a5b780100afa0d87b7b1440c1278c5229936a842'
            'b4eb7ed255cbdce826211c9b8f84b05982dce0f02879b833e50020c3bff49576')

build() {
    cmake -B td-$_tdlib_commit/build -S td-$_tdlib_commit \
        -DCMAKE_BUILD_TYPE=None \
        -DCMAKE_INSTALL_PREFIX="$PWD/td-$_tdlib_commit/install" \
        -Wno-dev \
        -DTD_E2E_ONLY=ON
    cmake --build td-$_tdlib_commit/build
    cmake --install td-$_tdlib_commit/build  
    # https://github.com/AyuGram/AyuGramDesktop/blob/dev/docs/building-linux.md#building-the-project
    # for API_ID and API_HASH
    CFLAGS=${CFLAGS//-flto=auto/-flto=1}
    CXXFLAGS=${CXXFLAGS//-flto=auto/-flto=1}
    cmake -B build -S "AyuGramDesktop-$pkgver-full" -G Ninja \
        -DCMAKE_INSTALL_PREFIX="/usr" \
        -DCMAKE_BUILD_TYPE=None \
        -DTDESKTOP_API_ID="${MAKEPKG_AYUGRAM_API_ID:-2040}" \
        -DTDESKTOP_API_HASH="${MAKEPKG_AYUGRAM_API_HASH:-b18441a1ff607e10a989891a5462e627}" \
        -DDESKTOP_APP_DISABLE_AUTOUPDATE=True \
        -Dtde2e_DIR="$PWD/td-$_tdlib_commit/install/lib/cmake/tde2e"
    cmake --build build --parallel 6
}
package() {
    DESTDIR="$pkgdir" cmake --install build
}
