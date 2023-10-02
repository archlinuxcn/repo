# Maintainer: Alesar1
# Contributor: solopasha <daron439 at gmail dot com>
# Contributor: KspLite <ksplite@outlook.com>
# Contributor: Daniil Kovalev <daniil@kovalev.website>
pkgname=64gram-desktop
_pkgname=64Gram
pkgver=1.0.98
pkgrel=1
epoch=1
pkgdesc='Unofficial desktop version of Telegram messaging app'
arch=('x86_64')
url="https://github.com/TDesktop-x64/tdesktop"
license=('GPL3')
depends=('hunspell' 'ffmpeg' 'hicolor-icon-theme' 'lz4' 'minizip' 'openal' 'ttf-opensans'
         'qt6-imageformats' 'qt6-svg' 'qt6-wayland' 'xxhash'
         'rnnoise' 'pipewire' 'libxtst' 'libxrandr' 'jemalloc' 'abseil-cpp' 'libdispatch'
         'openssl' 'protobuf' 'glib2' 'boost-libs' 'libsigc++-3.0' 'cppgir' 'glibmm-2.68')
makedepends=('cmake' 'git' 'ninja' 'python' 'range-v3' 'tl-expected' 'microsoft-gsl' 'meson'
             'extra-cmake-modules' 'wayland-protocols' 'plasma-wayland-protocols' 'libtg_owt'
             'gobject-introspection' 'boost' 'fmt' 'mm-common' 'perl-xml-parser' 'p7zip')
optdepends=('webkit2gtk: embedded browser features'
            'xdg-desktop-portal: desktop integration')
provides=(telegram-desktop)
conflicts=(telegram-desktop)
source=("https://github.com/TDesktop-x64/tdesktop/releases/download/v${pkgver}/${_pkgname}-${pkgver}-full.tar.gz"
        "block-sponsored_messages.patch"
        "fix-lzma-link.patch")
noextract=("${_pkgname}-${pkgver}-full.tar.gz")
sha512sums=('8a70a2d820c5f8b6ed444ac3a4a9736df2dda3ff4692d99d6f96ea2df7f4c3877349ce6d0a6a69fc4e2f0652856309eb5599e4afc210ef31caf09d9990b157ed'
            'c662524ca4f4a8df021ee94696d84896ed9a271df321933942806dda4544ea25f51a650ec8b4fc72f9a2219ea54cbfaf37b9604124f7263c86f74f1d647587ae'
            'd813a5ac6ff2208b693ecf494d7bf036087e223662f9f34aaaeafea0afe0fe798e867b9610f7221ea80319865502c20b61310d5a31634b888793873d63322463')

prepare() {
    7za x ${_pkgname}-${pkgver}-full.tar.gz
    tar -xvf ${_pkgname}-${pkgver}-full.tar
    cd $_pkgname-$pkgver-full
    patch -Np1 --binary -i ../block-sponsored_messages.patch
    patch -p1 --binary < ../fix-lzma-link.patch
}

build() {
    CXXFLAGS+=' -ffat-lto-objects'

    cmake \
        -B build \
        -S $_pkgname-$pkgver-full \
        -G Ninja \
        -DCMAKE_VERBOSE_MAKEFILE=ON \
        -DCMAKE_INSTALL_PREFIX="/usr" \
        -DCMAKE_BUILD_TYPE=Release \
        -DDESKTOP_APP_DISABLE_AUTOUPDATE=ON \
        -DTDESKTOP_API_TEST=ON
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -Dm644 /dev/null "$pkgdir/etc/tdesktop/externalupdater"
}
