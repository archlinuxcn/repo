# Maintainer: Peter Cai <peter at typeblog dot net>
#
# Thanks to hexchain <i at hexchain dot org> for the systemqt package
#
# Thanks Nicholas Guriev <guriev-ns@ya.ru> for the patches!
# https://github.com/mymedia2/tdesktop

_emoji_res_commit="db4c66e311a160b3f849d6c76890932c50701bf8"
pkgname=telegram-desktop-systemqt-notoemoji
pkgver=1.1.10
pkgrel=1
pkgdesc='Experimental build of Telegram Desktop (using system Qt, emojis replaced with those from Noto Color Emoji)'
arch=('i686' 'x86_64')
url="https://desktop.telegram.org/"
license=('GPL3')
depends=('ffmpeg' 'hicolor-icon-theme' 'minizip' 'openal' 'qt5-base' 'qt5-imageformats')
makedepends=('cmake' 'libappindicator-gtk2' 'dee' 'git' 'gtk3' 'gyp-git' 'libexif' 'libva' 'libwebp' 'mtdev' 'python' 'python2')
optdepends=(
    'libappindicator-gtk3: AppIndicator tray icon'
    'libappindicator-gtk2: AppIndicator tray icon'
)
conflicts=('telegram-desktop')
provides=('telegram-desktop')
install="telegram-desktop.install"
_variant_ver="1.1.3"
_GSL_commit="16a6a41690325433976d843e13ec676d6f9ab091"
_libtgvoip_commit="ccf715b626246990bf57068102bc04014f4ac385"
source=(
    "tdesktop::git+https://github.com/telegramdesktop/tdesktop.git#tag=v$pkgver"
    "GSL::git+https://github.com/Microsoft/GSL.git#commit=${_GSL_commit}"
    "variant::git+https://github.com/mapbox/variant#tag=v${_variant_ver}"
    "libtgvoip::git+https://github.com/telegramdesktop/libtgvoip.git#commit=${_libtgvoip_commit}"
    "telegramdesktop.desktop"
    "tg.protocol"
    "CMakeLists.inj"
    "tdesktop.patch"
    "libtgvoip.patch"
    "emoji.webp_${_emoji_res_commit}::https://github.com/PeterCxy/tdesktop/raw/${_emoji_res_commit}/Telegram/Resources/art/emoji.webp"
    "emoji_125x.webp_${_emoji_res_commit}::https://github.com/PeterCxy/tdesktop/raw/${_emoji_res_commit}/Telegram/Resources/art/emoji_125x.webp"
    "emoji_150x.webp_${_emoji_res_commit}::https://github.com/PeterCxy/tdesktop/raw/${_emoji_res_commit}/Telegram/Resources/art/emoji_150x.webp"
    "emoji_200x.webp_${_emoji_res_commit}::https://github.com/PeterCxy/tdesktop/raw/${_emoji_res_commit}/Telegram/Resources/art/emoji_200x.webp"
    "emoji_250x.webp_${_emoji_res_commit}::https://github.com/PeterCxy/tdesktop/raw/${_emoji_res_commit}/Telegram/Resources/art/emoji_250x.webp"
)
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '41c22fae6ae757936741e63aec3d0f17cafe86b2d6153cdd1d01a5581e871f17'
            'd4cdad0d091c7e47811d8a26d55bbee492e7845e968c522e86f120815477e9eb'
            '7a06af83609168a8eaec59a65252caa41dcd0ecc805225886435eb65073e9c82'
            '0aa02c2dc2cb4a32519de43a9f188d924b9a3458fdd941e733a17d54ec3db8ed'
            '3d72e09b9054ff75785a85c9f24ee82d48a2b9bf0ce8515156717b20157a45b3'
            'fccd084805b4621e3614d2a0584bb78a0ad44f502a79b4a4534e901881677555'
            '668a2371c3dae8e95187f0c9f8fec9b0e535157482747d2f9c6034c6b9eefa16'
            'd84537063ccf42904ab35ea2624263419f7d17671d24b17d02d02020d9af8be2'
            '876e085cee23f988b86398fb8bd104e3d7ad1aa45accd75e1d1d1653f2b32663'
            '37add3f2536dc027705c202446deb0c5351c3c7ade27336b2c054917acf4d15f')

prepare() {
    cd "$srcdir/tdesktop"
    git submodule init
    git config submodule.Telegram/ThirdParty/GSL.url "$srcdir/GSL"
    git config submodule.Telegram/ThirdParty/variant.url "$srcdir/variant"
    git config submodule.Telegram/ThirdParty/libtgvoip.url "$srcdir/libtgvoip"
    git submodule update
    patch -Np1 -i "$srcdir/tdesktop.patch"
    pushd "Telegram/ThirdParty/libtgvoip"
    patch -Np1 -i "$srcdir/libtgvoip.patch"
    popd
    for x in "" "_125x" "_150x" "_200x" "_250x"; do
        cp "$srcdir/emoji$x.webp_${_emoji_res_commit}" "$srcdir/tdesktop/Telegram/Resources/art/emoji$x.webp"
    done
}

build() {
    export LANG=en_US.UTF-8
    export GYP_DEFINES="TDESKTOP_DISABLE_CRASH_REPORTS,TDESKTOP_DISABLE_AUTOUPDATE,TDESKTOP_DISABLE_REGISTER_CUSTOM_SCHEME"
    cd "$srcdir/tdesktop"
    export EXTRA_CPPFLAGS="-DTDESKTOP_DISABLE_AUTOUPDATE -DTDESKTOP_DISABLE_CRASH_REPORTS -DTDESKTOP_DISABLE_REGISTER_CUSTOM_SCHEME"
    export CPPFLAGS="$CPPFLAGS $EXTRA_CPPFLAGS"
    export CXXFLAGS="$CXXFLAGS $EXTRA_CPPFLAGS"
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
