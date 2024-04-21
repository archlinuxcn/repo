# Maintainer: Alesar1
# Contributor: solopasha <daron439 at gmail dot com>
# Contributor: KspLite <ksplite@outlook.com>
# Contributor: Daniil Kovalev <daniil@kovalev.website>
pkgname=64gram-desktop
_pkgname=64Gram
pkgver=1.1.19
pkgrel=1
epoch=1
pkgdesc='Unofficial desktop version of Telegram messaging app'
arch=('x86_64')
url="https://github.com/TDesktop-x64/tdesktop"
license=('GPL3')
depends=('hunspell' 'ffmpeg' 'hicolor-icon-theme' 'lz4' 'minizip' 'openal'
         'qt6-imageformats' 'qt6-svg' 'qt6-wayland' 'xxhash'
         'rnnoise' 'pipewire' 'libxtst' 'libxrandr' 'abseil-cpp' 'libdispatch'
         'openssl' 'protobuf' 'glib2' 'libsigc++-3.0'
         'libxcomposite' 'libvpx' 'libxdamage' 'kcoreaddons' 'jemalloc')
makedepends=('cmake' 'git' 'ninja' 'python' 'range-v3' 'tl-expected' 'microsoft-gsl' 'meson'
             'extra-cmake-modules' 'wayland-protocols' 'plasma-wayland-protocols' 'libtg_owt'
             'gobject-introspection' 'boost' 'fmt' 'mm-common' 'perl-xml-parser' 'python-packaging' 'dos2unix')
optdepends=('webkit2gtk: embedded browser features'
            'xdg-desktop-portal: desktop integration')

source=("https://github.com/TDesktop-x64/tdesktop/releases/download/v${pkgver}/${_pkgname}-${pkgver}-full.tar.gz"
        "block-sponsored_messages.patch"
        "fix-lzma-link.patch"
        "io.github.tdesktop_x64.TDesktop.desktop")

noextract=("${_pkgname}-${pkgver}-full.tar.gz")

sha512sums=('6c9c53de1456014c7476ae5c1d0d078674da6eac06f2ac7eadf9015965c2ae07cc724906e7b5393ec823baffdf8ce7718c0c36a187d1d2ee29c73a859a0af62a'
            '0e0f0dcb99ed6c7566e7a75404e39e16c27658eb5999e041a82aa975447ce8719ce6703cc36efc039e16a3ff3721f4a7c76df24f0ead9aa48ce5e23001142072'
            'd813a5ac6ff2208b693ecf494d7bf036087e223662f9f34aaaeafea0afe0fe798e867b9610f7221ea80319865502c20b61310d5a31634b888793873d63322463'
            'ea027bc2d40c74507adf32380444207210a8c31cdba57f3f468d23d8e9c7376647cc8c713f188660f9b1dacd9041227aafd5a27c7889f47ea3985712b6b74b8b')

prepare() {
    LANG=C.UTF-8 bsdtar -xf ${_pkgname}-${pkgver}-full.tar.gz
    cd $_pkgname-$pkgver-full
    patch -Np1 --binary -i ../block-sponsored_messages.patch
    patch -p1 --binary < ../fix-lzma-link.patch
    find "${srcdir}"/ -type f -exec dos2unix {} \;
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
    mv "$pkgdir/usr/bin/telegram-desktop" "$pkgdir/usr/bin/64gram-desktop"
    install -Dm644 "$srcdir/io.github.tdesktop_x64.TDesktop.desktop" -t "$pkgdir/usr/share/applications"
    find "$pkgdir" -type f -name "telegram.png" -exec rename telegram.png 64gram.png {} \;
    mv "$pkgdir/usr/share/icons/hicolor/symbolic/apps/telegram-symbolic.svg" "$pkgdir/usr/share/icons/hicolor/symbolic/apps/64gram-symbolic.svg"
    mkdir -p "$pkgdir/usr/share/64Gram/externalupdater.d"
    echo "/usr/bin/64gram-desktop" >"$pkgdir/usr/share/64Gram/externalupdater.d/telegram-desktop.conf"
}
