# Maintainer: solopasha <daron439 at gmail dot com>
# Contributor: KspLite <ksplite@outlook.com>
pkgname=64gram-desktop
_pkgname=64Gram
pkgver=1.0.39
pkgrel=2
epoch=1
pkgdesc='Unofficial desktop version of Telegram messaging app'
arch=('x86_64')
url="https://github.com/TDesktop-x64/tdesktop"
license=('GPL3')
depends=('hunspell' 'ffmpeg4.4' 'hicolor-icon-theme' 'lz4' 'minizip' 'openal' 'ttf-opensans'
         'qt6-imageformats' 'qt6-svg' 'qt6-wayland' 'qt6-5compat' 'xxhash' 'glibmm'
         'rnnoise' 'pipewire' 'libxtst' 'libxrandr' 'jemalloc' 'abseil-cpp' 'libdispatch')
makedepends=('cmake' 'git' 'ninja' 'python' 'range-v3' 'tl-expected' 'microsoft-gsl' 'meson'
             'extra-cmake-modules' 'wayland-protocols' 'plasma-wayland-protocols' 'libtg_owt')
optdepends=('webkit2gtk: embedded browser features'
            'xdg-desktop-portal: desktop integration')
source=("https://github.com/TDesktop-x64/tdesktop/releases/download/v${pkgver}/${_pkgname}-${pkgver}-full.tar.gz"
        "block-sponsored_messages.patch"
        "fix-tgcalls-cstdint.patch")
sha512sums=('0cace8576fe4a2f802aad218bbbf73d6fb6470a0f20bba4f8db1773a15434f71995b2eaad2089dce255dc59d56f40b12f8ee6a9855a909d3cf0443ceced04074'
            'c662524ca4f4a8df021ee94696d84896ed9a271df321933942806dda4544ea25f51a650ec8b4fc72f9a2219ea54cbfaf37b9604124f7263c86f74f1d647587ae'
            '7b66b1dc928c9107a5f47ba8782eec0f811fe5988449afcb24e1e15cbc7c4c3e284d0480e272a4ba7a15d4acc374cae72ba3caa382cc9e67dd23c7ed6bad0e8c')
conflicts=("telegram-desktop" "tdesktop-x64")
replaces=("tdesktop-x64")
prepare() {
    cd $_pkgname-$pkgver-full
    sed -i '/option(DESKTOP_APP_DISABLE_AUTOUPDATE/s/^# //' cmake/variables.cmake
    patch -Np1 --binary -i ../block-sponsored_messages.patch
    patch -Np1 --binary -i "$srcdir"/fix-tgcalls-cstdint.patch -d Telegram/ThirdParty/tgcalls
}

build() {
    cd $_pkgname-$pkgver-full
    export PKG_CONFIG_PATH='/usr/lib/ffmpeg4.4/pkgconfig'
    cmake . \
        -B build \
        -G Ninja \
        -DCMAKE_INSTALL_PREFIX="/usr" \
        -DCMAKE_BUILD_TYPE=Release \
        -DDESKTOP_APP_DISABLE_AUTOUPDATE=ON \
        -DTDESKTOP_API_TEST=ON
    sed -i '/LINK_LIBRARIES/s/$/ \/usr\/lib\/liblzma.so/' build/build.ninja
    ninja -C build
}

package() {
    cd $_pkgname-$pkgver-full
    DESTDIR=$pkgdir ninja -C build install
}
