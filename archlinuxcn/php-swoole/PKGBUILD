# Maintainer: William Tang <galaxyking0419@gmail.com>
# Contributor: Bruce Zhang
# Contributor: lilac <lilac@build.archlinuxcn.org>
# Contributor: 吕海涛 <aur@lvht.net>

_extname=swoole
pkgname=php-$_extname
pkgver=5.0.2
pkgrel=1
pkgdesc="Coroutine-based concurrency library for PHP"
arch=('x86_64')
url="https://github.com/swoole/swoole-src"
license=('Apache')
depends=('php')
makedepends=('autoconf' 'gcc' 'make')

source=("https://github.com/swoole/swoole-src/archive/refs/tags/v$pkgver.tar.gz" "$_extname.ini")
sha256sums=('14d442d5e945fe67a3e912d332175b2386a50c38a674c4559d2d0211db23362e'
            '58d1d032fe130fee8666238d14013e51c75683d7b806c61d1ada3bb8470adb44')

build() {
    cd $_extname-src-$pkgver
    phpize
    ./configure --enable-swoole-curl
    make
}

package() {
    mkdir -p "$pkgdir"/etc/php/conf.d \
        "$pkgdir"/usr/include/php/ext \
        "$pkgdir"/usr/lib/php/modules \
        "$pkgdir"/usr/share/licenses/$pkgname

    cp $_extname.ini "$pkgdir"/etc/php/conf.d/

    cd $_extname-src-$pkgver
    cp -a include "$pkgdir"/usr/include/php/ext/$_extname
    mv .libs/$_extname.so "$pkgdir"/usr/lib/php/modules/
    cp LICENSE "$pkgdir"/usr/share/licenses/$pkgname/
}
