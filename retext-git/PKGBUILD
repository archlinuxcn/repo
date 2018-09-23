# Contributor: Mohammadreza Abdollahzadeh <morealaz at gmail dot com>
# former Co-maintainer: Jan Korte <j.korte@me.com>
# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=retext-git
pkgver=7.0.0.r100.g5bc778e
pkgrel=1
pkgdesc="A simple editor for Markdown and ReStructuredText markup languages."
arch=('any')
url="https://github.com/retext-project/retext"
license=('GPL3')
depends=('python-pyqt5'
         'python-markups'
         'shared-mime-info'
         'xdg-utils'
         'desktop-file-utils'
         'gconf')
makedepends=('imagemagick' 'git' 'qt5-tools')
optdepends=('python-markdown: for Markdown language support'
            'python-docutils: for reStructuredText language support'
            'python-pyenchant: for spell checking support')
provides=("${pkgname%-git}")
conflicts=("${pkgname%-git}")
source=("$pkgname::git+${url}.git"
        "retext.desktop"
        "x-retext-markdown.xml"
        "x-retext-rst.xml")
sha256sums=('SKIP'
            'a784275c951b330c2fc2ac2f5ac82b457ca09d37a0cf6e9e27e1e5716084d118'
            'b51611479d3224eec2b58264ed91ace3eccb502b7b806dae3e7a3ab4aab8c4b8'
            '6fef80cccb14813d9cc74810c397a6cd7831d1ca243536759a47c6e8b6cc977a')

pkgver() {
	cd $pkgname
	( set -o pipefail
	  git describe --long 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
	  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
	)
}

build () {
	cd $pkgname/locale
	lrelease-qt5 *.ts
}

package () {
	cd $pkgname
	python setup.py install --root="$pkgdir"

	# install icons
	for size in 16 22 24 32 48 128; do
		mkdir -p "$pkgdir"/usr/share/icons/hicolor/${size}x${size}/apps
		convert -resize $size icons/retext.png "$pkgdir"/usr/share/icons/hicolor/${size}x${size}/apps/retext.png
	done
	install -Dm644 icons/retext.svg "$pkgdir"/usr/share/icons/scalable/apps/retext.svg

	# install mime files
	install -Dm644 "$srcdir"/x-retext-markdown.xml "$pkgdir"/usr/share/mime/packages/x-retext-markdown.xml
	install -Dm644 "$srcdir"/x-retext-rst.xml "$pkgdir"/usr/share/mime/packages/x-retext-rst.xml

	# install desktop file
	install -Dm644 "$srcdir"/retext.desktop "$pkgdir"/usr/share/applications/retext.desktop
}

