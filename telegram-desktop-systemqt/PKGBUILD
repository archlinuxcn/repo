# Maintainer: hexchain <i@hexchain.org>

# Thanks Nicholas Guriev <guriev-ns@ya.ru> for the patches!
# https://github.com/mymedia2/tdesktop

pkgname=telegram-desktop-systemqt
pkgver=1.1.18
pkgrel=1
pkgdesc='Experimental build of Telegram Desktop (using system Qt)'
arch=('i686' 'x86_64')
url="https://desktop.telegram.org/"
license=('GPL3')
depends=('ffmpeg' 'hicolor-icon-theme' 'minizip' 'openal' 'qt5-base' 'qt5-imageformats')
makedepends=('cmake' 'libappindicator-gtk2' 'dee' 'git' 'gyp-git' 'libexif' 'libva' 'libwebp' 'mtdev' 'python' 'python2' 'gtk3')
optdepends=(
    'libappindicator-gtk2: AppIndicator tray icon'
    'libappindicator-gtk3: AppIndicator tray icon'
)
conflicts=('telegram-desktop')
provides=('telegram-desktop')
install="telegram-desktop.install"
source=(
    "tdesktop::git+https://github.com/telegramdesktop/tdesktop.git#tag=v$pkgver"
    "GSL::git+https://github.com/Microsoft/GSL.git"
    "libtgvoip::git+https://github.com/telegramdesktop/libtgvoip.git"
    "variant::git+https://github.com/mapbox/variant.git"
    "telegramdesktop.desktop"
    "tg.protocol"
    "CMakeLists.inj"
    "tdesktop.patch"
    "libtgvoip.patch"
)
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '41c22fae6ae757936741e63aec3d0f17cafe86b2d6153cdd1d01a5581e871f17'
            'd4cdad0d091c7e47811d8a26d55bbee492e7845e968c522e86f120815477e9eb'
            '7a06af83609168a8eaec59a65252caa41dcd0ecc805225886435eb65073e9c82'
            '6d54c8b51b2224c75c15d1e147855a6f22b96848ca3413330882ca6243dd05cb'
            '640ef297f5977de78dab17789390e628b8f7a8a495529c24da8a43693f3fae23')

prepare() {
    cd "$srcdir/tdesktop"
    git submodule init
    git config submodule.Telegram/ThirdParty/GSL.url "$srcdir/GSL"
    git config submodule.Telegram/ThirdParty/variant.url "$srcdir/variant"
    git config submodule.Telegram/ThirdParty/libtgvoip.url "$srcdir/libtgvoip"
    git submodule update
    patch -Np1 -i "$srcdir/tdesktop.patch"

    cd "Telegram/ThirdParty/libtgvoip"
    patch -Np1 -i "$srcdir/libtgvoip.patch"
}

build() {
    cd "$srcdir/tdesktop"
    export LANG=en_US.UTF-8
    export GYP_DEFINES="TDESKTOP_DISABLE_CRASH_REPORTS,TDESKTOP_DISABLE_AUTOUPDATE,TDESKTOP_DISABLE_REGISTER_CUSTOM_SCHEME"
    export EXTRA_FLAGS="-DTDESKTOP_DISABLE_AUTOUPDATE -DTDESKTOP_DISABLE_CRASH_REPORTS -DTDESKTOP_DISABLE_REGISTER_CUSTOM_SCHEME -Winvalid-pch"
    export CPPFLAGS="$CPPFLAGS $EXTRA_FLAGS"
    export CXXFLAGS="$CXXFLAGS $EXTRA_FLAGS"
    gyp \
        -Dbuild_defines=${GYP_DEFINES:1} \
        -Gconfig=Release \
        --depth=Telegram/gyp --generator-output=../.. -Goutput_dir=out Telegram/gyp/Telegram.gyp --format=cmake
    NUM=$((`wc -l < out/Release/CMakeLists.txt` - 2))
    sed -i "$NUM r ../CMakeLists.inj" out/Release/CMakeLists.txt
    cd "$srcdir/tdesktop/out/Release"
    cmake . -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_VERBOSE_MAKEFILE=ON -DCMAKE_BUILD_TYPE=None
    make
}

package() {
    install -dm755 "$pkgdir/usr/bin"
    install -m755 "$srcdir/tdesktop/out/Release/Telegram" "$pkgdir/usr/bin/telegram-desktop"

    install -d "$pkgdir/usr/share/applications"
    install -m644 "$srcdir/telegramdesktop.desktop" "$pkgdir/usr/share/applications/telegramdesktop.desktop"

    install -d "$pkgdir/usr/share/kservices5"
    install -m644 "$srcdir/tg.protocol" "$pkgdir/usr/share/kservices5/tg.protocol"

    local icon_size icon_dir
    for icon_size in 16 32 48 64 128 256 512; do
        icon_dir="$pkgdir/usr/share/icons/hicolor/${icon_size}x${icon_size}/apps"

        install -d "$icon_dir"
        install -m644 "$srcdir/tdesktop/Telegram/Resources/art/icon${icon_size}.png" "$icon_dir/telegram-desktop.png"
    done
}
