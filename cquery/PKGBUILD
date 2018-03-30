# Maintainer: Shengyu Zhang <la@archlinuxcn.org>

pkgname=cquery
pkgver=v20180302
__pkgver=${pkgver:1}
pkgrel=6
pkgdesc='Low-latency vscode language server for large C++ code-bases, powered by libclang.'
arch=('x86_64')
url='https://github.com/cquery-project/cquery/'
license=('MIT')
depends=('clang')
makedepends=('git' 'python' 'llvm')
conflicts=('cquery-git')
source=("https://github.com/cquery-project/$pkgname/archive/$pkgver.tar.gz"
        'git+https://github.com/miloyip/rapidjson'
        'git+https://github.com/onqtam/doctest'
        'git+https://github.com/greg7mdp/sparsepp'
        'git+https://github.com/emilk/loguru'
        'git+https://github.com/msgpack/msgpack-c'
        )
sha256sums=('273b317f6ad13f29db1e5e14ff7103e8946e6208ab246166ce1afc6f3381d65e'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

prepare() {
    cd $pkgname-$__pkgver
    cp -r $srcdir/rapidjson third_party
    cp -r $srcdir/doctest third_party
    cp -r $srcdir/sparsepp third_party
    cp -r $srcdir/loguru third_party
    cp -r $srcdir/msgpack-c third_party
}

build() {
    cd $pkgname-$__pkgver
    # --variant=custom will not add extra CXXFLAGS
    python waf configure --variant=custom --prefix="$pkgdir/usr" --llvm-config=/usr/bin/llvm-config
    python waf build --variant=custom
}

check() {
    cd $pkgname-$__pkgver
    # yes | build/custom/bin/cquery --test-unit --test-index --clang-sanity-check
    yes | build/custom/bin/cquery --test-unit --clang-sanity-check
}

package() {
    cd $pkgname-$__pkgver
    python waf install --variant=custom
}
