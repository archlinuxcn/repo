# Maintainer: Allen Wild <allenwild93@gmail.com>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: hexchain <i@hexchain.org>

# Thanks Nicholas Guriev <guriev-ns@ya.ru> for the patches!
# https://github.com/mymedia2/tdesktop

pkgname=telegram-desktop-systemqt-notoemoji
pkgver=1.5.1
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

_emojiver=v1.1
source=(
    "tdesktop::git+https://github.com/telegramdesktop/tdesktop.git#tag=v$pkgver"
    "libtgvoip::git+https://github.com/telegramdesktop/libtgvoip"
    "variant::git+https://github.com/mapbox/variant"
    "Catch::git+https://github.com/philsquared/Catch"
    "GSL::git+https://github.com/Microsoft/GSL.git"
    "crl::git+https://github.com/telegramdesktop/crl.git"
    "xxHash::git+https://github.com/Cyan4973/xxHash.git"
    "telegram-emoji-gen-${_emojiver}.tar.xz::https://github.com/aswild/telegram-emoji-gen/archive/${_emojiver}.tar.gz"
    "build-time-optimize.patch.in"
    "tg.protocol"
    "CMakeLists.inj"
    "tdesktop.patch"
    "no-gtk2.patch"
    "libtgvoip.patch"
    "demibold.patch"
    "Use-system-wide-font.patch"
)
sha512sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '1f8a51acfe4c5262919fa441eb74af2312c3141cad84c677ef7aa45e9faf3d4c90ebb57c99a98b7cb8f2abe467d4777366523ecf2029b74e71c6bf5c09e98803'
            'fa7042f370ae4e2e14d083395743cdee25bfedc39ab5273b5d1ab12fb074757cf76dab065f2abcb44cad018920e711142fbf24a2b9cd30f517c5a5b46d6a6182'
            'b87414ceaae19185a8a5749cea1f6d9f3fc3c69b8dd729e3db8790cde00b987c3c827cd30baf0eac579d1884e34aa2f37bb90778c3c0bc9ca211d75a82891b9d'
            'b20674f61ff6378749d1f59a6a0da194d33ccc786bd783f6ed62027924a3a8a8d27c9763bf376480432d6536896b0c7eeb8c495c5b8cefff7cf5fe84da50947e'
            '7922e92d0541112e8e90dbf5b60e45d707ade38aac9d56a46491656ce37ba2386815433511775ae5c5a96fe578ed8651ada20d3b736c5e71e9231ff2b6a5abe4'
            'a8f1708616a598fea3cb94e3b63b02a7b13b55abd129a5dc02ad502529f4ebe7a673b6a350b669290fd26135358d21e2e10bf4a11d88f58f0685b7c4ab515bc5'
            'd60694dc701aa985b0e82a12c9732b945082470441c687b33167a94f94efcf253baf43bb7280ec160ba338485ee5c62de138e4804cae05f27cc5cf4298166d39'
            '6d0bac5aa4c4992b5400a9a9318f7a4e92d5eab961917cf0b05cdd251ab66a77c52ec8fbef246e8019606a7624d7b5420b87f8153e071e9724c7d2f5c94e47c0'
            'ce6be003220267bac5483caf8302b492e1581892bc36d35a61236ebf9f9d766b8bd2159557a1c36256aa85f461797a38bfaae57b12da7a72101b21c0b17ed653')

prepare() {
    cd "$srcdir/tdesktop"
    git submodule init
    git config submodule.Telegram/ThirdParty/libtgvoip.url "$srcdir/libtgvoip"
    git config submodule.Telegram/ThirdParty/variant.url "$srcdir/variant"
    git config submodule.Telegram/ThirdParty/GSL.url "$srcdir/GSL"
    git config submodule.Telegram/ThirdParty/Catch.url "$srcdir/Catch"
    git config submodule.Telegram/ThirdParty/crl.url "$srcdir/crl"
    git config submodule.Telegram/ThirdParty/xxHash.url "$srcdir/xxHash"
    git submodule update

    set -x
    patch -Np1 -i "$srcdir/tdesktop.patch"
    patch -Np1 -i "$srcdir/no-gtk2.patch"
    patch -R -Np1 -i "$srcdir/demibold.patch"
    patch -Np1 -i "$srcdir/Use-system-wide-font.patch"

    # speed up builds: disable debugging information and use parallel LTO
    sed "s/@NPROC@/$(nproc)/g" "$srcdir/build-time-optimize.patch.in" >"$srcdir/build-time-optimize.patch"
    patch -Np1 -i "$srcdir/build-time-optimize.patch"

    cd "Telegram/ThirdParty/libtgvoip"
    patch -Np1 -i "$srcdir/libtgvoip.patch"

    cp -vf "$srcdir/telegram-emoji-gen-${_emojiver#v}/telegram-noto-emoji/"*.webp "$srcdir/tdesktop/Telegram/Resources/emoji"
    set +x
}

build() {
    cd "$srcdir/tdesktop"
    export LANG=en_US.UTF-8
    export GYP_DEFINES="TDESKTOP_DISABLE_CRASH_REPORTS,TDESKTOP_DISABLE_AUTOUPDATE,TDESKTOP_DISABLE_REGISTER_CUSTOM_SCHEME,TDESKTOP_DISABLE_DESKTOP_FILE_GENERATION"
    export EXTRA_FLAGS="-Winvalid-pch"
    export CPPFLAGS="$CPPFLAGS $EXTRA_FLAGS"
    export CXXFLAGS="$CXXFLAGS $EXTRA_FLAGS"

    # Telegram requires us to set API_ID and API_HASH for some reason but they do not provide a way to receive a pair
    # See https://github.com/telegramdesktop/tdesktop/commit/65b2db216033aa08b7bc846df27843e566f08981 and
    # https://github.com/telegramdesktop/tdesktop/issues/4717
    # The official API_ID seems to be 2040 while the API_HASH is "b18441a1ff607e10a989891a5462e627".
    # We're going to use the defaults for now but might at some point use the official ones from the official binaries as noted above.

    gyp \
        -Dapi_id=17349 \
        -Dapi_hash=344583e45741c457fe1862106095a5eb \
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
