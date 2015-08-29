
#Maintainer: xgdgsc<xgdgsc@gmail.com>

pkgname=cppreference-qt
pkgver=20150808
pkgrel=1

pkgdesc="A complete reference for the features in the C++ Standard Library, for qt help"
arch=('any')
url="http://en.cppreference.com/"
license=('CCPL:cc-by-sa')
# http://upload.cppreference.com/mwiki/images/1/15/qch_book_20150808.tar.gz
source=("http://upload.cppreference.com/mwiki/images/1/15/qch_book_$pkgver.tar.gz")
md5sums=('e4edced25239ec77e828bf432bd8c227')

package() {
    mkdir -p "$pkgdir/usr/share/doc/qt"
    cp "$srcdir"/cppreference-doc-en-cpp.qch "$pkgdir/usr/share/doc/qt"
}
