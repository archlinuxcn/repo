
#Maintainer: xgdgsc<xgdgsc@gmail.com>

pkgname=cppreference-qt
pkgver=20151129
pkgrel=1

pkgdesc="A complete reference for the features in the C++ Standard Library, for qt help"
arch=('any')
url="http://en.cppreference.com/"
license=('CCPL:cc-by-sa')
# http://upload.cppreference.com/mwiki/images/1/15/qch_book_20150808.tar.gz
source=("http://upload.cppreference.com/mwiki/images/2/2c/qch_book_$pkgver.tar.gz")
md5sums=('da75696546d503d40db96c283ab51f7d')

package() {
    mkdir -p "$pkgdir/usr/share/doc/qt"
    cp "$srcdir"/cppreference-doc-en-cpp.qch "$pkgdir/usr/share/doc/qt"
}
