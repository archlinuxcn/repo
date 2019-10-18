# Maintainer: tjbp (archlinux@tjbp.net)
# Contributor: Thore Bödecker <me [at] foxxx0 [dot] de>
# Contributor: Evangelos Foutras <evangelos@foutrelis.com>

pkgname=php56-memcached
_pkgbase="${pkgname#php56-}"
pkgver=2.2.0
pkgrel=4
pkgdesc="php56 extension for interfacing with memcached via libmemcached library"
arch=('i686' 'x86_64')
url="https://pecl.php.net/package/memcached"
license=('PHP')
provides=("php-memcached=${pkgver}-${pkgrel}")
depends=('php56>=5.6.17-3' 'libmemcached')
checkdepends=('memcached')
backup=('etc/php56/conf.d/memcached.ini')
source=("https://pecl.php.net/get/memcached-${pkgver}.tgz")
sha512sums=('61207d3f8c11b0620dbcb20fb2ebb6d1fc10159a7e879ee91556a303c3dcdf3d2571e8dda5efcbed77ff779f5c9b226aa48800630b9e7781cd964126b848c356')

build() {
    cd "${srcdir}/${_pkgbase}-${pkgver}"

    phpize56
    ./configure \
        --config-cache \
        --sysconfdir=/etc/php56 \
        --with-php-config=/usr/bin/php-config56 \
        --localstatedir=/var
    make
}

check() {
    cd "${srcdir}/${_pkgbase}-${pkgver}"

    memcached_pids=()
    memcached -p 11211 -U 11211 >/dev/null        & memcached_pids+=($!)
    memcached -p 11212 -U 11212 >/dev/null        & memcached_pids+=($!)
    memcached -s "$PWD/memcached.sock" >/dev/null & memcached_pids+=($!)

    local ret=0
    make test NO_INTERACTION=1 REPORT_EXIT_STATUS=1 || ret=1

    kill ${memcached_pids[@]}

    return $ret
}

package() {
    cd "${srcdir}/${_pkgbase}-${pkgver}"

    make INSTALL_ROOT="$pkgdir" install

    install -d "$pkgdir/etc/php56/conf.d"
    echo ';extension=memcached.so' >"$pkgdir/etc/php56/conf.d/memcached.ini"
}
