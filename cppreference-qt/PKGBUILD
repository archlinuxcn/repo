#Maintainer: xgdgsc<xgdgsc@gmail.com>
#Co-Maintainer: Mohammadreza Abdollahzadeh<morealaz at gmail dot com>

pkgname=cppreference-qt
pkgver=20170214
pkgrel=1
pkgdesc="A complete reference for the features in the C++ Standard Library, for qt help."
arch=('any')
url="http://en.cppreference.com/"
license=('CCPL:cc-by-sa')
source=("http://upload.cppreference.com/mwiki/images/1/1d/qch_book_$pkgver.tar.gz")
md5sums=('f36940c9cb9471e9303c72db1e900575')

package() {
    mkdir -p "$pkgdir/usr/share/doc/qt"
    cp "$srcdir"/cppreference-doc-en-cpp.qch "$pkgdir/usr/share/doc/qt"
}
