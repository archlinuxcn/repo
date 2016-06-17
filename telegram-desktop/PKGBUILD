pkgname=telegram-desktop
pkgver=0.9.51
pkgrel=1
_qtver=5.6.0
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
)
source=(
    "tdesktop::git+https://github.com/telegramdesktop/tdesktop.git#tag=v$pkgver"
    "http://download.qt.io/official_releases/qt/${_qtver%.*}/$_qtver/submodules/qtbase-opensource-src-$_qtver.tar.xz"
    "http://download.qt.io/official_releases/qt/${_qtver%.*}/$_qtver/submodules/qtimageformats-opensource-src-$_qtver.tar.xz"
    "breakpad::git+https://chromium.googlesource.com/breakpad/breakpad"
    "breakpad-lss::git+https://chromium.googlesource.com/linux-syscall-support"
    "telegramdesktop.desktop"
    "tg.protocol"
)
sha256sums=(
    'SKIP'
    '6efa8a5c559e92b2e526d48034e858023d5fd3c39115ac1bfd3bb65834dbd67a'
    '2c854275a689a513ba24f4266cc6017d76875336671c2c8801b4b7289081bada'
    'SKIP'
    'SKIP'
    'adb111ad10872e2858c8ccdd8645a1566736dec8d48deb50a9a7c0fbcae5cfb0'
    'd4cdad0d091c7e47811d8a26d55bbee492e7845e968c522e86f120815477e9eb'
)

prepare() {
    cd "$srcdir/tdesktop"
    
    mkdir -p "$srcdir/Libraries"
    
    local qt_patch_file="$srcdir/tdesktop/Telegram/Patches/qtbase_${_qtver//./_}.diff"
    local qt_src_dir="$srcdir/Libraries/qt${_qtver//./_}"
    if [ "$qt_patch_file" -nt "$qt_src_dir" ]; then
        rm -rf "$qt_src_dir"
        mkdir "$qt_src_dir"
        
        mv "$srcdir/qtbase-opensource-src-$_qtver" "$qt_src_dir/qtbase"
        mv "$srcdir/qtimageformats-opensource-src-$_qtver" "$qt_src_dir/qtimageformats"
        
        cd "$qt_src_dir/qtbase"
        patch -p1 -i "$qt_patch_file"
    fi
    
    if [ ! -h "$srcdir/Libraries/breakpad" ]; then
        ln -s "$srcdir/breakpad" "$srcdir/Libraries/breakpad"
        ln -s "$srcdir/breakpad-lss" "$srcdir/Libraries/breakpad/src/third_party/lss"
    fi
    
    sed -i 's/CUSTOM_API_ID//g' "$srcdir/tdesktop/Telegram/Telegram.pro"
    sed -i 's,LIBS += /usr/local/lib/libxkbcommon.a,,g' "$srcdir/tdesktop/Telegram/Telegram.pro"
    sed -i 's,LIBS += /usr/local/lib/libz.a,LIBS += -lz,g' "$srcdir/tdesktop/Telegram/Telegram.pro"
    sed -i 's/c++11/c++14/g' "$srcdir/tdesktop/Telegram/Telegram.pro"
    
    (
        echo "DEFINES += TDESKTOP_DISABLE_AUTOUPDATE"
        echo "DEFINES += TDESKTOP_DISABLE_REGISTER_CUSTOM_SCHEME"
        echo 'INCLUDEPATH += "/usr/lib/glib-2.0/include"'
        echo 'INCLUDEPATH += "/usr/lib/gtk-2.0/include"'
        echo 'INCLUDEPATH += "/usr/include/opus"'
        echo 'LIBS += -lcrypto -lssl'
    ) >> "$srcdir/tdesktop/Telegram/Telegram.pro"
}

build() {
    # Build patched Qt
    local qt_src_dir="$srcdir/Libraries/qt${_qtver//./_}"
    
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
        -no-opengl \
        -static \
        -nomake examples \
        -nomake tests
    make
    make install
    export PATH="$srcdir/qt/bin:$PATH"
    
    cd "$qt_src_dir/qtimageformats"
    qmake .
    make
    make install
    
    # Build breakpad
    cd "$srcdir/Libraries/breakpad"
    ./configure
    make
    
    # Build codegen_style
    mkdir -p "$srcdir/tdesktop/Linux/obj/codegen_style/Debug"
    cd "$srcdir/tdesktop/Linux/obj/codegen_style/Debug"
    qmake CONFIG+=debug "../../../../Telegram/build/qmake/codegen_style/codegen_style.pro"
    make
    
    # Build codegen_numbers
    mkdir -p "$srcdir/tdesktop/Linux/obj/codegen_numbers/Debug"
    cd "$srcdir/tdesktop/Linux/obj/codegen_numbers/Debug"
    qmake CONFIG+=debug "../../../../Telegram/build/qmake/codegen_numbers/codegen_numbers.pro"
    make
    
    # Build MetaLang
    mkdir -p "$srcdir/tdesktop/Linux/DebugIntermediateLang"
    cd "$srcdir/tdesktop/Linux/DebugIntermediateLang"
    qmake CONFIG+=debug "../../Telegram/MetaLang.pro"
    make
    
    # Build Telegram Desktop
    mkdir -p "$srcdir/tdesktop/Linux/ReleaseIntermediate"
    cd "$srcdir/tdesktop/Linux/ReleaseIntermediate"
    
    ./../codegen/Debug/codegen_style \
        "-I./../../Telegram/Resources" \
        "-I./../../Telegram/SourceFiles" \
        "-o./../../Telegram/GeneratedFiles/styles" \
        all_files.style --rebuild
    
    ./../codegen/Debug/codegen_numbers \
        "-o./../../Telegram/GeneratedFiles" \
        "./../../Telegram/Resources/numbers.txt"
    
    ./../DebugLang/MetaLang \
        -lang_in ./../../Telegram/Resources/langs/lang.strings \
        -lang_out ./../../Telegram/GeneratedFiles/lang_auto
    
    qmake CONFIG+=release QT_TDESKTOP_PATH="$srcdir/qt" "../../Telegram/Telegram.pro"
    make
}

package() {
    install -dm755 "$pkgdir/usr/bin"
    install -m755 "$srcdir/tdesktop/Linux/Release/Telegram" "$pkgdir/usr/bin/telegram-desktop"
    
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
