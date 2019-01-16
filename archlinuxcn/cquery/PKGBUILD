# Maintainer: Shengyu Zhang <la@archlinuxcn.org>

pkgname=cquery
pkgver=v20180718
__pkgver=${pkgver:1}
pkgrel=8
pkgdesc='cquery is a highly-scalable, low-latency language server for C/C++/Objective-C.'
arch=('x86_64')
url='https://github.com/cquery-project/cquery/'
license=('MIT')
depends=('clang>=6.0.0')
makedepends=('git' 'cmake>=3.1')
conflicts=('cquery-git')
source=("https://github.com/cquery-project/$pkgname/archive/$pkgver.tar.gz"
        'git+https://github.com/miloyip/rapidjson#commit=daabb88'
        'git+https://github.com/onqtam/doctest#commit=b40b7e7'
        'git+https://github.com/greg7mdp/sparsepp#commit=1ca7189'
        'git+https://github.com/emilk/loguru#commit=6bf94c5'
        'git+https://github.com/msgpack/msgpack-c#commit=208595b'
        'git+https://github.com/zeux/pugixml#commit=24a7064'
        )
sha256sums=('72361e5e6f7a4a6b5ae27d555354efb4b012d20798b50ddd19cfd81bdf56cc1c'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

prepare() {
    cd $pkgname-$__pkgver
    cp -r -u $srcdir/rapidjson third_party
    cp -r -u $srcdir/doctest third_party
    cp -r -u $srcdir/sparsepp third_party
    cp -r -u $srcdir/loguru third_party
    cp -r -u $srcdir/msgpack-c third_party
    cp -r -u $srcdir/pugixml third_party
}
build() {
    mkdir -p $pkgname-$__pkgver/build
    cd $pkgname-$__pkgver/build
    cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DSYSTEM_CLANG=ON ..
		cmake --build .
}
package() {
    cd $pkgname-$__pkgver/build
    make DESTDIR="$pkgdir" install
}
