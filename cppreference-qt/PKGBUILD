#Maintainer: xgdgsc<xgdgsc@gmail.com>
#Co-Maintainer: Mohammadreza Abdollahzadeh<morealaz at gmail dot com>

pkgname=cppreference-qt
pkgver=20161029
pkgrel=1
pkgdesc="A complete reference for the features in the C++ Standard Library, for qt help."
arch=('any')
url="http://en.cppreference.com/"
license=('CCPL:cc-by-sa')
source=("http://upload.cppreference.com/mwiki/images/2/22/qch_book_$pkgver.tar.gz")
md5sums=('1f9616de0584c73dd09c93b97f53f7ab')

package() {
    mkdir -p "$pkgdir/usr/share/doc/qt"
    cp "$srcdir"/cppreference-doc-en-cpp.qch "$pkgdir/usr/share/doc/qt"
}
