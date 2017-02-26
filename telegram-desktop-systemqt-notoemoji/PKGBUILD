# Maintainer: Peter Cai <peter at typeblog dot net>
#
# Thanks to hexchain <i at hexchain dot org> for the systemqt package
#
# Thanks Nicholas Guriev <guriev-ns@ya.ru> for the patches!
# https://github.com/mymedia2/tdesktop

_emoji_res_commit="62fcc728a12a4d5b41049e6aadb5e6f039c28f8d"
pkgname=telegram-desktop-systemqt-notoemoji
pkgver=1.0.14
pkgrel=1
pkgdesc='Experimental build of Telegram Desktop (using system Qt, emojis replaced with those from Noto Color Emoji)'
arch=('i686' 'x86_64')
url="https://desktop.telegram.org/"
license=('GPL3')
depends=('ffmpeg' 'hicolor-icon-theme' 'minizip' 'openal' 'qt5-base' 'qt5-imageformats')
makedepends=('cmake' 'libappindicator-gtk3' 'dee' 'git' 'gyp-git' 'libexif' 'libva' 'libwebp' 'mtdev' 'python' 'python2')
optdepends=('libappindicator-gtk3: AppIndicator tray icon')
conflicts=('telegram-desktop')
provides=('telegram-desktop')
install="telegram-desktop.install"
source=(
    "tdesktop::git+https://github.com/telegramdesktop/tdesktop.git#tag=v$pkgver"
    "telegramdesktop.desktop"
    "tg.protocol"
    "Avoid-depending-on-static-libraries.patch"
    "Fix-desktop-integration-issues.patch"
    "Flags-for-precompiled-header-and-MOC.patch"
    "Fix-rcc-path.patch"
    "Use-gtk3-headers.patch"
    "Reduce-number-of-libraries.patch"
    "CMakeLists.inj"
    "https://github.com/PeterCxy/tdesktop/raw/${_emoji_res_commit}/Telegram/Resources/art/emoji.webp"
    "https://github.com/PeterCxy/tdesktop/raw/${_emoji_res_commit}/Telegram/Resources/art/emoji_125x.webp"
    "https://github.com/PeterCxy/tdesktop/raw/${_emoji_res_commit}/Telegram/Resources/art/emoji_150x.webp"
    "https://github.com/PeterCxy/tdesktop/raw/${_emoji_res_commit}/Telegram/Resources/art/emoji_200x.webp"
    "https://github.com/PeterCxy/tdesktop/raw/${_emoji_res_commit}/Telegram/Resources/art/emoji_250x.webp"
)
sha256sums=('SKIP'
            '41c22fae6ae757936741e63aec3d0f17cafe86b2d6153cdd1d01a5581e871f17'
            'd4cdad0d091c7e47811d8a26d55bbee492e7845e968c522e86f120815477e9eb'
            '197159eca70fc4a3d55548842d3218bcd67394cb869f08825d8fc12cf7b050f8'
            '4e1938a5ddfcf8ac57bafa5f9ce80413665ac3b0ccd3c1853fe8f0835b91f468'
            '952c7590cb05354c70037745d980fa97c36e36f96a1fa7d0db29a5c6a1d8dbd1'
            'cf4dbb293afdbfd226861a00a42790a15b23bea296eccf35853d104e07ea345a'
            '5f3ac7c08df0293bed626293dbfb6040764abf28899db7681572cfb1d8bcaa6e'
            '0442af5365a31de5a8e15de8a94f5c1192775fc4460b74c4045da99e548f045a'
            '7a06af83609168a8eaec59a65252caa41dcd0ecc805225886435eb65073e9c82'
            'c6fea6d718b054aa3deb0b8b5a7f1ff330db2ab1f66962de033ad84c33622727'
            '701d15ffe711113022981b2f7da3ae2a4aa9febe260dac020a30274f8c8b538b'
            'c268159a23152b765c7af72997cd290bfbb8c1ed5219991cca28596f85596bd1'
            '410f4cf5b66bdd4f380694c983da26eefdc3e5411957db74a609072ac690d738'
            '342880dedeaaed24008430f698e252450b87527b799ebc9399f98f208c9b0953')

prepare() {
    cd "$srcdir/tdesktop"
    git apply "$srcdir/Avoid-depending-on-static-libraries.patch"
    git apply "$srcdir/Fix-desktop-integration-issues.patch"
    git apply "$srcdir/Flags-for-precompiled-header-and-MOC.patch"
    git apply "$srcdir/Fix-rcc-path.patch"
    git apply "$srcdir/Use-gtk3-headers.patch"
    git apply "$srcdir/Reduce-number-of-libraries.patch"
    cp "$srcdir/emoji.webp" "$srcdir/emoji_"{125,150,200,250}"x.webp" "$srcdir/tdesktop/Telegram/Resources/art/"
}

build() {
    cd "$srcdir/tdesktop"
    export EXTRA_CPPFLAGS="-DTDESKTOP_DISABLE_AUTOUPDATE -DTDESKTOP_DISABLE_CRASH_REPORTS -DTDESKTOP_DISABLE_REGISTER_CUSTOM_SCHEME"
    export CPPFLAGS="$CPPFLAGS $EXTRA_CPPFLAGS"
    gyp \
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
