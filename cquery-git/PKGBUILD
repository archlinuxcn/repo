# Maintainer: Vic Luo <vicluo96 at gmail.com>
# Contributor: Litao Lu <lulitao1997 at gmail.com>

pkgname=cquery-git
_pkgname=cquery
pkgver=1942.3ac1ff24
pkgrel=2
pkgdesc='Low-latency vscode language server for large C++ code-bases, powered by libclang.'
arch=('x86_64')
url='https://github.com/cquery-project/cquery/'
license=('MIT')
depends=('clang')
makedepends=('cmake' 'git')

source=('git+https://github.com/cquery-project/cquery.git')
md5sums=(
    'SKIP'
)

pkgver() {
    cd $_pkgname
    printf "%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
    cd $_pkgname
    git submodule update --init --recursive
}

build() {
    cd $_pkgname
    mkdir -p build
    cd build
    cmake -DSYSTEM_CLANG=ON -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release ..
    make -j$(nproc)
}

package() {
    cd $_pkgname/build
    make DESTDIR="$pkgdir/" install
}
