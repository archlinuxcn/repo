#Maintainer: xgdgsc<xgdgsc@gmail.com>
#Co-Maintainer: Mohammadreza Abdollahzadeh<morealaz at gmail dot com>

pkgname=cppreference-qt
pkgver=20190607
pkgrel=1
pkgdesc="A complete reference for the features in the C++ Standard Library, for qt help."
arch=('any')
url="http://en.cppreference.com/"
license=('CCPL:cc-by-sa')
source=("http://upload.cppreference.com/mwiki/images/5/5a/qch_book_$pkgver.tar.xz")
md5sums=('09f2c6eb8f99d4023445fda4bf757be3')

package() {
    mkdir -p "$pkgdir/usr/share/doc/qt"
    cp "$srcdir"/cppreference-doc-en-cpp.qch "$pkgdir/usr/share/doc/qt"
}
