
#Maintainer: xgdgsc<xgdgsc@gmail.com>

pkgname=cppreference-qt
pkgver=20141118
pkgrel=1

pkgdesc="A complete reference for the features in the C++ Standard Library, for qt help"
arch=('any')
url="http://en.cppreference.com/"
license=('CCPL:cc-by-sa')
source=("http://upload.cppreference.com/mwiki/images/2/2c/qch_book_$pkgver.tar.gz")
md5sums=('cb0da55a4363000bea7a41e27e1cb1fa')

package() {
    mkdir -p "$pkgdir/usr/share/doc/qt"
    cp "$srcdir"/cppreference-doc-en-cpp.qch "$pkgdir/usr/share/doc/qt"
}
