# Maintainer: Andreas Bilke <andreas@bilke>

pkgname=pdfpc
pkgver=4.0.0
pkgrel=1
pkgdesc='A presenter console with multi-monitor support for PDF files'
arch=('i686' 'x86_64')
url='https://pdfpc.github.io/'
license=('GPL')
depends=('gtk3' 'poppler-glib' 'libgee' 'gstreamer' 'gst-plugins-base')
optdepends=('gst-plugins-good: more codecs for video playback support')
makedepends=('cmake' 'vala')
conflicts=('pdfpc-git')
source=(https://github.com/pdfpc/pdfpc/releases/download/v$pkgver/$pkgname-v$pkgver.tar.gz)
md5sums=('a5c2115618f3b5571019892c086a6610')
sha1sums=('4c54b585d14749ceedfede1ebda5e232a52c455c')
sha256sums=('c091c554f4e3ed8735df40055253459c47b09590775a6f9b5b6abf1b42647a62')

build() {
    cd "$srcdir/$pkgname-v$pkgver"
    cmake  -DCMAKE_INSTALL_PREFIX="/usr/" -DSYSCONFDIR="/etc" .
    make
}

package() {
    cd "$srcdir/$pkgname-v$pkgver"
    make DESTDIR="$pkgdir/" install
}

# vim:set ts=4 sw=4 et:
