pkgname=telegram-desktop
pkgver=1.0.14
pkgrel=1
pkgdesc='Official desktop version of Telegram messaging app.'
arch=('i686' 'x86_64')
url="https://desktop.telegram.org/"
license=('GPL3')
depends=(
    'ffmpeg'
    'icu'
    'jasper'
    'libmng'
    'libxkbcommon-x11'
    'libinput'
    'libproxy'
    'openal'
    'tslib'
    'xcb-util-wm'
    'xcb-util-keysyms'
    'xcb-util-image'
    'xcb-util-renderutil'
    'hicolor-icon-theme'
)
makedepends=(
    'git'
    'libunity'
    'libappindicator-gtk2'
    'libva'
    'mtdev'
    'libexif'
    'libwebp'
    'google-breakpad-git'
    'chrpath'
    'cmake'
    'python'
    'python2'
    
    # QT5 build dependencies
    'xcb-util-keysyms'
    'libgl'
    'fontconfig'
    'xcb-util-wm'
    'libxrender'
    'libxi'
    'sqlite'
    'xcb-util-image'
    'harfbuzz-icu'
    'tslib'
    'libinput'
    'libsm'
    'libxkbcommon-x11'
    # For qtimageformats
    'libjpeg-turbo'
    'libpng'
    'libtiff'
    'libmng'
    'libwebp'
    # For qtwayland
    'wayland'
)
qt_version=5.6.2
source=(
    "tdesktop::git+https://github.com/telegramdesktop/tdesktop.git#tag=v$pkgver"
    "https://download.qt.io/official_releases/qt/${qt_version%.*}/$qt_version/submodules/qtbase-opensource-src-$qt_version.tar.xz"
    "https://download.qt.io/official_releases/qt/${qt_version%.*}/$qt_version/submodules/qtimageformats-opensource-src-$qt_version.tar.xz"
    "https://download.qt.io/official_releases/qt/${qt_version%.*}/$qt_version/submodules/qtwayland-opensource-src-$qt_version.tar.xz"
    "git+https://chromium.googlesource.com/external/gyp"
    "telegramdesktop.desktop"
    "tg.protocol"
    "aur-fixes.diff"
)
sha256sums=(
    'SKIP'
    '2f6eae93c5d982fe0a387a01aeb3435571433e23e9d9d9246741faf51f1ee787'
    '4fb153be62dac393cbcebab65040b3b9d6edecd1ebbe5e543401b0e45bd147e4'
    '035c3199f4719627b64b7020f0f4574da2b4cb78c6981aba75f27b872d8e6c86'
    'SKIP'
    '41c22fae6ae757936741e63aec3d0f17cafe86b2d6153cdd1d01a5581e871f17'
    'd4cdad0d091c7e47811d8a26d55bbee492e7845e968c522e86f120815477e9eb'
    '7993641b29a0fe4379aa7bbd15a1fbd349b28a4894be102937716d97cafa0ee2'
)

prepare() {
    cd "$srcdir/tdesktop"
    
    mkdir -p "$srcdir/Libraries"
    
    local qt_patch_file="$srcdir/tdesktop/Telegram/Patches/qtbase_${qt_version//./_}.diff"
    local qt_src_dir="$srcdir/Libraries/qt${qt_version//./_}"
    if [ "$qt_patch_file" -nt "$qt_src_dir" ]; then
        rm -rf "$qt_src_dir"
        mkdir "$qt_src_dir"
        
        mv "$srcdir/qtbase-opensource-src-$qt_version" "$qt_src_dir/qtbase"
        mv "$srcdir/qtimageformats-opensource-src-$qt_version" "$qt_src_dir/qtimageformats"
        mv "$srcdir/qtwayland-opensource-src-$qt_version" "$qt_src_dir/qtwayland"
        
        cd "$qt_src_dir/qtbase"
        patch -p1 -i "$qt_patch_file"
    fi
    
    cd "$srcdir/gyp"
    git apply "$srcdir/tdesktop/Telegram/Patches/gyp.diff"
    sed -i 's/exec python /exec python2 /g' "$srcdir/gyp/gyp"
    
    if [ ! -h "$srcdir/Libraries/gyp" ]; then
        ln -s "$srcdir/gyp" "$srcdir/Libraries/gyp"
    fi
    
    cd "$srcdir/tdesktop"
    git apply "$srcdir/aur-fixes.diff"
}

build() {
    # Build patched Qt
    local qt_src_dir="$srcdir/Libraries/qt${qt_version//./_}"
    
    cd "$qt_src_dir/qtbase"
    ./configure \
        -prefix "$srcdir/qt" \
        -release \
        -force-debug-info \
        -opensource \
        -confirm-license \
        -system-zlib \
        -system-libpng \
        -system-libjpeg \
        -system-freetype \
        -system-harfbuzz \
        -system-pcre \
        -system-xcb \
        -system-xkbcommon-x11 \
        -no-gtkstyle \
        -static \
        -nomake examples \
        -nomake tests
        #-no-opengl
    make
    make install
    export PATH="$srcdir/qt/bin:$PATH"
    
    cd "$qt_src_dir/qtimageformats"
    qmake .
    make
    make install
    
    cd "$qt_src_dir/qtwayland"
    qmake .
    make
    make install
    
    # Build Telegram Desktop
    rm -rf "$srcdir/tdesktop/out"
    cd "$srcdir/tdesktop/Telegram/gyp"
    
    "$srcdir/Libraries/gyp/gyp" \
        -Dlinux_path_qt="$srcdir/qt" \
        -Dlinux_lib_ssl=-lssl \
        -Dlinux_lib_crypto=-lcrypto \
        -Dlinux_lib_icu="-licuuc -licutu -licui18n" \
        --depth=. --generator-output=../.. -Goutput_dir=out Telegram.gyp --format=cmake
    cd "$srcdir/tdesktop/out/Release"
    cmake .
    make
    chrpath --delete Telegram
}

package() {
    install -dm755 "$pkgdir/usr/bin"
    install -m755 "$srcdir/tdesktop/out/Release/Telegram" "$pkgdir/usr/bin/telegram-desktop"
    
    install -d "$pkgdir/usr/share/applications"
    install -m644 "$srcdir/telegramdesktop.desktop" "$pkgdir/usr/share/applications/telegramdesktop.desktop"
    
    install -d "$pkgdir/usr/share/kde4/services"
    install -m644 "$srcdir/tg.protocol" "$pkgdir/usr/share/kde4/services/tg.protocol"
    
    local icon_size icon_dir
    for icon_size in 16 32 48 64 128 256 512; do
        icon_dir="$pkgdir/usr/share/icons/hicolor/${icon_size}x${icon_size}/apps"
        
        install -d "$icon_dir"
        install -m644 "$srcdir/tdesktop/Telegram/Resources/art/icon${icon_size}.png" "$icon_dir/telegram-desktop.png"
    done
}
