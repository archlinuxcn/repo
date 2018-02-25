# Maintainer: Shengyu Zhang <la@archlinuxcn.org>

pkgname=cquery
pkgver=v20180215
__pkgver=${pkgver:1}
pkgrel=2
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
sha256sums=('1651672e2e5f9707778ab2b9a0b719596c7cb8bf77f374994abc23baa532148d'
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
    sed -e "s/, '-Werror'//g" -i ./wscript
}

build() {
    cd $pkgname-$__pkgver
    # --variant=custom will not add extra CXXFLAGS
    python waf configure --variant=custom --prefix="$pkgdir/usr" --llvm-config=/usr/bin/llvm-config
    python waf build --variant=custom
}

check() {
    cd $pkgname-$__pkgver
    yes | build/custom/bin/cquery --test-unit --test-index --clang-sanity-check
}

package() {
    cd $pkgname-$__pkgver
    python waf install --variant=custom
}
