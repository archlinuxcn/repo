# Maintainer: William Tang <galaxyking0419@gmail.com>
# Contributor: Bruce Zhang
# Contributor: lilac <lilac@build.archlinuxcn.org>
# Contributor: 吕海涛 <aur@lvht.net>

_extname=swoole
pkgname=php-$_extname
pkgver=5.1.2
pkgrel=1
pkgdesc='Coroutine-based concurrency library for PHP'
arch=('x86_64')
url='https://github.com/swoole/swoole-src'
license=('Apache-2.0')
depends=('php-pgsql')
makedepends=('autoconf' 'gcc' 'make')

source=("https://github.com/swoole/swoole-src/archive/refs/tags/v$pkgver.tar.gz" "$_extname.ini")
sha256sums=('89d88ef2f7dfca96d4ff74febc62ec78ccbf92996176107cf30d538b30dee1ba'
            '970534465ebbbf9be58ec8dba5399f7b9473c432cb5b42098125b4bcf1fdef85')

build() {
    cd $_extname-src-$pkgver
    phpize
    ./configure --enable-swoole-curl --enable-swoole-pgsql
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
