# Maintainer: yesuu zhang <yesuu79@qq.com>
# Contributor: ska <skatiger@gmail.com>

pkgname=sublime-text-imfix
pkgver=2.0.2
pkgrel=2
pkgdesc='sophisticated text editor for code, html and prose. Fcitx input method support'
arch=('i686' 'x86_64')
url='http://www.sublimetext.com/2'
license=('custom')
depends=('libpng' 'gtk2' 'xdg-utils' 'desktop-file-utils')
makedepends=('gcc')
conflicts=('sublime-text')
install='sublime-text.install'
source=(
	'sublime-text.desktop'
	'subl'
	'sublime_imfix.c'
)
source_i686=("http://c758482.r82.cf2.rackcdn.com/Sublime%20Text%20${pkgver}.tar.bz2")
source_x86_64=("http://c758482.r82.cf2.rackcdn.com/Sublime%20Text%20${pkgver}%20x64.tar.bz2")

sha256sums=(
	'3f11bf8cb814b68ed81b535dd13cc86bb28c71010d74141bfa06137782fd2f7d'
	'd3453ef5f1722be562baea8a4afce0b11aa5d6228292c8e2f1a621ebad28a4f1'
	'8ac4d949f65785736f6a67de9c23cb25b22495313a5b5de95f199cf84568524f'
)
sha256sums_i686=('07338e041cfb348938fa8069f0aad3b5b43c319b7ec564ffff1489796f2dcf08')
sha256sums_x86_64=('01baed30d66432e30002a309ff0393967be1daba5cce653e43bba6bd6c38ab84')

package () {
	cd "${srcdir}"

	gcc -shared -o libsublime-imfix.so sublime_imfix.c `pkg-config --libs --cflags gtk+-2.0` -fPIC

	install -Dm644 sublime-text.desktop "${pkgdir}/usr/share/applications/sublime-text.desktop"

	install -dm755 "${pkgdir}/opt"
	cp --preserve=mode -r "Sublime Text 2" "${pkgdir}/opt/sublime-text"

	cp --preserve=mode -r libsublime-imfix.so "${pkgdir}/opt/sublime-text/libsublime-imfix.so"

	for res in 128x128 16x16 256x256 32x32 48x48; do
		install -dm755 "${pkgdir}/usr/share/icons/hicolor/${res}/apps"
		ln -s "/opt/sublime-text/Icon/${res}/sublime_text.png" "${pkgdir}/usr/share/icons/hicolor/${res}/apps/sublime_text.png"
	done

	install -Dm755 subl "${pkgdir}/usr/bin/subl"
}
