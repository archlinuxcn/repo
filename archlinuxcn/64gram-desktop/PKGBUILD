# Maintainer: solopasha <daron439 at gmail dot com>
# Contributor: KspLite <ksplite@outlook.com>
pkgname=64gram-desktop
_pkgname=64Gram
pkgver=1.0.62
pkgrel=1
epoch=1
pkgdesc='Unofficial desktop version of Telegram messaging app'
arch=('x86_64')
url="https://github.com/TDesktop-x64/tdesktop"
license=('GPL3')
depends=('hunspell' 'ffmpeg' 'hicolor-icon-theme' 'lz4' 'minizip' 'openal'
         'qt6-imageformats' 'qt6-svg' 'qt6-wayland' 'qt6-5compat' 'xxhash' 'glibmm-2.68'
         'rnnoise' 'pipewire' 'libxtst' 'libxrandr' 'jemalloc' 'abseil-cpp' 'libdispatch' 'openssl-1.1' 'protobuf')
makedepends=('cmake' 'git' 'ninja' 'python' 'range-v3' 'tl-expected' 'microsoft-gsl' 'meson'
             'extra-cmake-modules' 'wayland-protocols' 'plasma-wayland-protocols' 'libtg_owt' 'qt6-tools')
optdepends=('webkit2gtk: embedded browser features'
            'xdg-desktop-portal: desktop integration')
provides=(telegram-desktop)
conflicts=(telegram-desktop)
source=("https://github.com/TDesktop-x64/tdesktop/releases/download/v${pkgver}/${_pkgname}-${pkgver}-full.tar.gz"
        "block-sponsored_messages.patch")
sha512sums=('93980b16b7041999f4ac539c691a27bac2fdc04e785504c664b8ccdd707961d388b6b6cf3376f7d9416a5739180d8a33d9b87c89298f84da43426c612c29008b'
            'c662524ca4f4a8df021ee94696d84896ed9a271df321933942806dda4544ea25f51a650ec8b4fc72f9a2219ea54cbfaf37b9604124f7263c86f74f1d647587ae')
prepare() {
    cd $_pkgname-$pkgver-full
    rm -rf Telegram/ThirdParty/libtgvoip/webrtc_dsp/absl
    patch -Np1 --binary -i ../block-sponsored_messages.patch
}

build() {
    cd "${srcdir}/$_pkgname-$pkgver-full"
    cmake \
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
    install -Dm644 /dev/null "$pkgdir/etc/tdesktop/externalupdater"
}
