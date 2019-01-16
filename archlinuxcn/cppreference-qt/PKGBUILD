#Maintainer: xgdgsc<xgdgsc@gmail.com>
#Co-Maintainer: Mohammadreza Abdollahzadeh<morealaz at gmail dot com>

pkgname=cppreference-qt
pkgver=20181028
pkgrel=1
pkgdesc="A complete reference for the features in the C++ Standard Library, for qt help."
arch=('any')
url="http://en.cppreference.com/"
license=('CCPL:cc-by-sa')
source=("http://upload.cppreference.com/mwiki/images/b/b1/qch_book_$pkgver.tar.xz")
md5sums=('84293c04d80ef46a2c64c9547ae9668b')

package() {
    mkdir -p "$pkgdir/usr/share/doc/qt"
    cp "$srcdir"/cppreference-doc-en-cpp.qch "$pkgdir/usr/share/doc/qt"
}
