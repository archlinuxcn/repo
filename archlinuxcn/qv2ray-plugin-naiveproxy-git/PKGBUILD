# Maintainer: DuckSoft <realducksoft at gmail dot com>

pkgname=qv2ray-plugin-naiveproxy-git
_pkgname=qv2ray-plugin-naiveproxy
pkgver=20200612.r12.d924872
pkgrel=1
pkgdesc="Qv2ray Plugin: NaiveProxy (for Qv2ray v2.6.0-rc2+ only)"
arch=('x86_64')
url='https://github.com/Qv2ray/QvPlugin-NaiveProxy'
license=('GPL3')
# _virtualdepends=('qv2ray-plugin-host=2')
depends=('qt5-base>5.11.0' 'qv2ray-dev-git')
makedepends=('git' 'make' 'qt5-tools' 'which' 'gcc' 'cmake' 'ninja' 'libffi')
optdepends=('naiveproxy')
provides=('qv2ray-plugin-naiveproxy')
groups=('qv2ray-plugin')
conflicts=('qv2ray-plugin-naiveproxy')
source=("$_pkgname::git+${url}")
sha512sums=('SKIP')
pkgver() {
    cd "$srcdir"/"$_pkgname"
    local date=$(git log -1 --format="%cd" --date=short | sed s/-//g)
    local count=$(git rev-list --count HEAD)
    local commit=$(git rev-parse --short HEAD)
    echo "$date.r${count}.$commit"
}
prepare() {
    cd "$srcdir"/"$_pkgname"
    git submodule update --init
}
build() {
    cd "$srcdir"/"$_pkgname"
    mkdir -p build && cd build
    cmake .. \
        -DCMAKE_BUILD_TYPE=Release \
        -GNinja
    ninja
}
package() {
    cd "$srcdir"/"$_pkgname"/build
    install -Dm644 -t "$pkgdir"/usr/share/qv2ray/plugins/ libQvPlugin-NaiveProxy.so
    # NOTE: This virtual dependency will be introduced after Qv2ray stablize its interface.
    #     depends+=(${_virtualdepends[@]})
} 
