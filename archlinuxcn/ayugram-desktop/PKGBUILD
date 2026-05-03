# Use environment variable MAKEPKG_AYUGRAM_API_ID and MAKEPKG_AYUGRAM_API_HASH to override default values

pkgname=ayugram-desktop
pkgver=6.7.8
pkgrel=3
pkgdesc="Desktop Telegram client with good customization and Ghost mode."
arch=("x86_64" "aarch64")
url="https://github.com/AyuGram/AyuGramDesktop"
license=("GPL-3.0-or-later WITH OpenSSL-exception")
depends=('abseil-cpp'
         'ada'
         'ffmpeg'
         'glib2'
         'glibc'
         'hicolor-icon-theme'
         'hunspell'
         'kcoreaddons'
         'libavif'
         'libdispatch'
         'libgcc'
         'libheif'
         'libjpeg-turbo'
         'libjxl'
         'libpipewire'
         'libstdc++'
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
         'pipewire'
         'protobuf'
         'qt6-base'
         'qt6-imageformats'
         'qt6-svg'
         'qt6-wayland'
         'rnnoise'
         'xxhash'
         'zlib')
makedepends=('boost'
             'boost-libs'
             'cmake'
             'glib2-devel'
             'gobject-introspection'
             'gperf'
             'libtg_owt'
             'microsoft-gsl'
             'ninja'
             'python'
             'range-v3'
             'tl-expected')
optdepends=('geoclue: geoinformation support'
            'crow-translate: translation provider'
            'webkit2gtk-4.1: embedded browser features provided by webkit2gtk-4.1'
            'webkitgtk-6.0: embedded browser features provided by webkitgtk-6.0 (Wayland only)'
            'xdg-desktop-portal: desktop integration')
_tdlib_commit=51743dfd01dff6179e2d8f7095729caa4e2222e9
source=("AyuGram-$pkgver-full.tar.gz::https://github.com/AyuGram/AyuGramDesktop/releases/download/v$pkgver/AyuGramDesktop-$pkgver-full.tar.gz"
        "td-$_tdlib_commit.tar.gz::https://github.com/tdlib/td/archive/$_tdlib_commit.tar.gz"
        "0001-force-minizip-includes.diff"
        "0002-fix-missing-cstdint.diff")

sha256sums=('c8de66c5568dfc3e4e309275cc858e84a61f781fe93ed967290c31b70c770b00'
            'f2c6b92533ba41a024b9fdb86d346c8bfc876d5961738ad463effbd844d61405'
            '1ff58d023daa8882e952d2322c7b119e31f98ddecea32473bd8079d93295e7b6'
            '566920c751e0f599411ff914649ffbf1f19e26a0ead368d9c4a18cbf760406e1')

prepare() {
    cd "$srcdir/AyuGramDesktop-$pkgver-full"
    # minizip seems setting its include directory to /usr/include in pkg-config script...
    patch -Np1 -d Telegram/lib_base -i "$srcdir/0001-force-minizip-includes.diff"
    # uint8_t, uint_64_t, etc.
    patch -Np1 -d Telegram/ThirdParty/tgcalls -i "$srcdir/0002-fix-missing-cstdint.diff"
}
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
    cmake -B build -S "AyuGramDesktop-$pkgver-full" -G Ninja \
        -DCMAKE_INSTALL_PREFIX="/usr" \
        -DCMAKE_BUILD_TYPE=Release \
        -DTDESKTOP_API_ID="${MAKEPKG_AYUGRAM_API_ID:-2040}" \
        -DTDESKTOP_API_HASH="${MAKEPKG_AYUGRAM_API_HASH:-b18441a1ff607e10a989891a5462e627}" \
        -DDESKTOP_APP_DISABLE_AUTOUPDATE=True \
        -Dtde2e_DIR="$PWD/td-$_tdlib_commit/install/lib/cmake/tde2e"
    cmake --build build
}
package() {
    DESTDIR="$pkgdir" cmake --install build
}
