# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>

_basename=sord
pkgname=lib32-sord
pkgver=0.16.4
pkgrel=2
pkgdesc="A lightweight C library for storing RDF data in memory (32-bit)"
arch=('x86_64')
url="https://drobilla.net/software/sord/"
license=('custom:ISC')
depends=('lib32-serd' 'sord')
makedepends=('lib32-pcre' 'waf')
source=("https://download.drobilla.net/$_basename-$pkgver.tar.bz2"{,.sig})
sha512sums=('98bb102cff5ab38d999c2f966597508076ccce54583a739810b0c28b4f3d570b2ef414605fc08361ecb11ac3184d3176f2f50c7c59c06cc50c3d522e26ed5576'
            'SKIP')
validpgpkeys=('907D226E7E13FA337F014A083672782A9BF368F3') # David Robillard

prepare() {
    cd "$_basename-$pkgver"

    # remove local call to ldconfig
    sed -i "/ldconfig/d" wscript

    # let wscript(s) find the custom waf scripts
    mkdir -pv tools
    touch __init__.py
    cp -v waflib/extras/{autoship,autowaf,lv2}.py tools/
    mkdir -pv plugins/tools/
    cp -v waflib/extras/{autoship,autowaf,lv2}.py plugins/tools/
    rm -rv waflib
    sed -e 's/waflib.extras/tools/g' \
        -e "s/load('autowaf'/load('autowaf', tooldir='tools'/g" \
        -e "s/load('lv2'/load('lv2', tooldir='tools'/g" \
        -i wscript
}

build() {
    cd "$_basename-$pkgver"

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'
    export CFLAGS="$(echo "$CFLAGS" | sed 's/ -fno-plt//')"

    waf configure --prefix=/usr \
                          --libdir=/usr/lib32 \
                          --test

    waf build
}

check() {
    cd "$_basename-$pkgver"

    waf test
}

package() {
    cd "$_basename-$pkgver"

    waf install --destdir="$pkgdir"

    install -vDm 644 COPYING -t "$pkgdir/usr/share/licenses/$pkgname"

    cd "$pkgdir/usr"

    rm -r bin include share/man
}
