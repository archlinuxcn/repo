pkgname=telegram-desktop
pkgver=0.9.42
pkgrel=1
_qtver=5.5.1
pkgdesc='Official desktop version of Telegram messaging app.'
arch=('i686' 'x86_64')
url="https://desktop.telegram.org/"
license=('GPL3')
depends=('ffmpeg' 'icu' 'jasper' 'libexif' 'libmng' 'libwebp' 'libxkbcommon-x11'
	 'libinput' 'libproxy' 'mtdev' 'openal' 'libva' 'desktop-file-utils'
	 'gtk-update-icon-cache')
makedepends=('git' 'libunity' 'libappindicator-gtk2')
source=("tdesktop::git+https://github.com/telegramdesktop/tdesktop.git#tag=v$pkgver"
	"http://download.qt.io/official_releases/qt/${_qtver%.*}/$_qtver/single/qt-everywhere-opensource-src-$_qtver.tar.xz"
	"breakpad::git+https://chromium.googlesource.com/breakpad/breakpad"
	"breakpad-lss::git+https://chromium.googlesource.com/linux-syscall-support"
	"telegramdesktop.desktop"
	"tg.protocol")
sha256sums=('SKIP'
	    '6f028e63d4992be2b4a5526f2ef3bfa2fe28c5c757554b11d9e8d86189652518'
	    'SKIP'
	    'SKIP'
	    'adb111ad10872e2858c8ccdd8645a1566736dec8d48deb50a9a7c0fbcae5cfb0'
	    'd4cdad0d091c7e47811d8a26d55bbee492e7845e968c522e86f120815477e9eb')
install="$pkgname.install"


prepare() {
	cd "$srcdir/tdesktop"
	
	mkdir -p "$srcdir/Libraries"
	
	local qt_patch_file="$srcdir/tdesktop/Telegram/_qtbase_${_qtver//./_}_patch.diff"
	if [ "$qt_patch_file" -nt "$srcdir/Libraries/QtStatic" ]; then
		rm -rf "$srcdir/Libraries/QtStatic"
		mv "$srcdir/qt-everywhere-opensource-src-$_qtver" "$srcdir/Libraries/QtStatic"
		cd "$srcdir/Libraries/QtStatic/qtbase"
		patch -p1 -i "$qt_patch_file"
	fi
	
	if [ ! -h "$srcdir/Libraries/breakpad" ]; then
		ln -s "$srcdir/breakpad" "$srcdir/Libraries/breakpad"
		ln -s "$srcdir/breakpad-lss" "$srcdir/Libraries/breakpad/src/third_party/lss"
	fi
	
	sed -i 's/CUSTOM_API_ID//g' "$srcdir/tdesktop/Telegram/Telegram.pro"
	sed -i 's,LIBS += /usr/local/lib/libxkbcommon.a,,g' "$srcdir/tdesktop/Telegram/Telegram.pro"
	sed -i 's,LIBS += /usr/local/lib/libz.a,LIBS += -lz,g' "$srcdir/tdesktop/Telegram/Telegram.pro"
	
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
	cd "$srcdir/Libraries/QtStatic"
	./configure -prefix "$srcdir/qt" -release -opensource -confirm-license -qt-zlib \
	            -qt-libpng -qt-libjpeg -qt-freetype -qt-harfbuzz -qt-pcre -qt-xcb \
	            -qt-xkbcommon-x11 -no-opengl -static -nomake examples -nomake tests
	make module-qtbase module-qtimageformats
	make module-qtbase-install_subtargets module-qtimageformats-install_subtargets
	
	export PATH="$srcdir/qt/bin:$PATH"
	
	# Build breakpad
	cd "$srcdir/Libraries/breakpad"
	./configure
	make
	
	# Build MetaStyle
	mkdir -p "$srcdir/tdesktop/Linux/DebugIntermediateStyle"
	cd "$srcdir/tdesktop/Linux/DebugIntermediateStyle"
	qmake CONFIG+=debug "../../Telegram/MetaStyle.pro"
	make
	
	# Build MetaLang
	mkdir -p "$srcdir/tdesktop/Linux/DebugIntermediateLang"
	cd "$srcdir/tdesktop/Linux/DebugIntermediateLang"
	qmake CONFIG+=debug "../../Telegram/MetaLang.pro"
	make
	
	# Build Telegram Desktop
	mkdir -p "$srcdir/tdesktop/Linux/ReleaseIntermediate"
	cd "$srcdir/tdesktop/Linux/ReleaseIntermediate"
	
	qmake CONFIG+=release "../../Telegram/Telegram.pro"
	local pattern="^PRE_TARGETDEPS +="
	grep "$pattern" "$srcdir/tdesktop/Telegram/Telegram.pro" | sed "s/$pattern//g" | xargs make
	
	qmake CONFIG+=release "../../Telegram/Telegram.pro"
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
