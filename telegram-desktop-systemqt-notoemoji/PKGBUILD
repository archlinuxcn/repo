# Maintainer: Allen Wild <allenwild93@gmail.com>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: hexchain <i@hexchain.org>

# Thanks Nicholas Guriev <guriev-ns@ya.ru> for the patches!
# https://github.com/mymedia2/tdesktop

pkgname=telegram-desktop-systemqt-notoemoji
pkgver=1.3.9
pkgrel=2
pkgdesc='Official Telegram Desktop client (with noto emoji)'
arch=('x86_64')
url="https://desktop.telegram.org/"
license=('GPL3')
depends=('ffmpeg' 'hicolor-icon-theme' 'minizip' 'openal' 'qt5-base' 'qt5-imageformats' 'openssl')
makedepends=('cmake' 'git' 'gyp' 'range-v3' 'python' 'libappindicator-gtk3')
optdepends=('libnotify: desktop notifications')
conflicts=('telegram-desktop')
provides=('telegram-desktop')

_emojiver="v1"
source=(
    "tdesktop::git+https://github.com/telegramdesktop/tdesktop.git#tag=v$pkgver"
    "GSL::git+https://github.com/Microsoft/GSL.git"
    "libtgvoip::git+https://github.com/telegramdesktop/libtgvoip.git"
    "variant::git+https://github.com/mapbox/variant.git"
    "Catch::git+https://github.com/philsquared/Catch"
    "https://s3.amazonaws.com/aur-telegram-desktop-notoemoji/noto-emoji-${_emojiver}.tar.xz"
    "tg.protocol"
    "CMakeLists.inj"
    "tdesktop.patch"
    "no-gtk2.patch"
    "build-time-optimize.patch.in"
    "libtgvoip.patch"
    "libtgvoip-2.patch"
)
sha512sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '376a4860e37b0f60892f362e954f976a563c632579167003b4aacbb24b6fea6aabb4e6952baf6d1a546b961936935cc49cf0e0ce9570320245b6bb326cb149e5'
            'b87414ceaae19185a8a5749cea1f6d9f3fc3c69b8dd729e3db8790cde00b987c3c827cd30baf0eac579d1884e34aa2f37bb90778c3c0bc9ca211d75a82891b9d'
            'ccbfca942e9fc5ce94a7e9c74429f3463886a35d887aad39ea74a95a2bfc664e5d6641bf1c46e1cf9b786c8aaa21449ac6bbbbc52c84dea550add80d8ea060d4'
            '37eda4cd7c88f8b55f7bc6786dd23af691060c9040b8e5d65dda07ab234397af23c3f699abe2bfec8919f501ce45b8f1d25180f5077480b1ca966308c62f8ecb'
            'c05351aa9f6503daa6ef8b01adb73c7e71fd01377d833f47f826e184d78dd79628ce7c686ae23a40b7468adcd5af0af9ebce4783113957b6126892aca83c7712'
            'fa7042f370ae4e2e14d083395743cdee25bfedc39ab5273b5d1ab12fb074757cf76dab065f2abcb44cad018920e711142fbf24a2b9cd30f517c5a5b46d6a6182'
            'd60694dc701aa985b0e82a12c9732b945082470441c687b33167a94f94efcf253baf43bb7280ec160ba338485ee5c62de138e4804cae05f27cc5cf4298166d39'
            '251f43bcdfd688a4c7dda082e981569c6cd6332289652576cfdc9f6376eee6e28195ec4a60bcfa002c6358d0f3cbdf215b7d390bbcce2ed560abfc9c606566b5')

prepare() {
    cd "$srcdir/tdesktop"
    git submodule init
    git config submodule.Telegram/ThirdParty/GSL.url "$srcdir/GSL"
    git config submodule.Telegram/ThirdParty/variant.url "$srcdir/variant"
    git config submodule.Telegram/ThirdParty/libtgvoip.url "$srcdir/libtgvoip"
    git config submodule.Telegram/ThirdParty/Catch.url "$srcdir/Catch"
    git submodule update
    patch -Np1 -i "$srcdir/tdesktop.patch"
    patch -Np1 -i "$srcdir/no-gtk2.patch"

    # speed up builds: disable debugging information and use parallel LTO
    sed "s/@NPROC@/$(nproc)/g" "$srcdir/build-time-optimize.patch.in" >"$srcdir/build-time-optimize.patch"
    patch -Np1 -i "$srcdir/build-time-optimize.patch"

    cd "Telegram/ThirdParty/libtgvoip"
    patch -Np1 -i "$srcdir/libtgvoip.patch"
    # patch -Np1 -i "$srcdir/libtgvoip-2.patch"

    for x in "" "_125x" "_150x" "_200x" "_250x"; do
        cp -vf "$srcdir/noto-emoji-${_emojiver}/emoji$x.webp" "$srcdir/tdesktop/Telegram/Resources/art/emoji$x.webp"
    done
}

build() {
    cd "$srcdir/tdesktop"
    export LANG=en_US.UTF-8
    export GYP_DEFINES="TDESKTOP_DISABLE_CRASH_REPORTS,TDESKTOP_DISABLE_AUTOUPDATE,TDESKTOP_DISABLE_REGISTER_CUSTOM_SCHEME,TDESKTOP_DISABLE_UNITY_INTEGRATION"
    export EXTRA_FLAGS="-Winvalid-pch"
    export CPPFLAGS="$CPPFLAGS $EXTRA_FLAGS"
    export CXXFLAGS="$CXXFLAGS $EXTRA_FLAGS"
    gyp \
        -Dbuild_defines=${GYP_DEFINES} \
        -Gconfig=Release \
        --depth=Telegram/gyp --generator-output=../.. -Goutput_dir=out Telegram/gyp/Telegram.gyp --format=cmake
    NUM=$((`wc -l < out/Release/CMakeLists.txt` - 2))
    sed -i "$NUM r ../CMakeLists.inj" out/Release/CMakeLists.txt
    cd "$srcdir/tdesktop/out/Release"
    cmake . -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release
    make
}

package() {
    install -dm755 "$pkgdir/usr/bin"
    install -m755 "$srcdir/tdesktop/out/Release/Telegram" "$pkgdir/usr/bin/telegram-desktop"

    install -d "$pkgdir/usr/share/applications"
    install -m644 "$srcdir/tdesktop/lib/xdg/telegramdesktop.desktop" "$pkgdir/usr/share/applications/telegramdesktop.desktop"

    install -d "$pkgdir/usr/share/kservices5"
    install -m644 "$srcdir/tg.protocol" "$pkgdir/usr/share/kservices5/tg.protocol"

    local icon_size icon_dir
    for icon_size in 16 32 48 64 128 256 512; do
        icon_dir="$pkgdir/usr/share/icons/hicolor/${icon_size}x${icon_size}/apps"

        install -d "$icon_dir"
        install -m644 "$srcdir/tdesktop/Telegram/Resources/art/icon${icon_size}.png" "$icon_dir/telegram.png"
    done
}
