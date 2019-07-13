# Maintainer: robertfoster
# Contributor: kurych
# Contributor: redfish
# Contributor: atommixz
# Contributor: denn
# Contributor: post-factum
# Contributor: wrdcrrtmnstr
# Contributor: r4sas

pkgname=i2pd
pkgver=2.27.0
pkgrel=1
pkgdesc="Simplified C++ implementation of I2P client"
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/PurpleI2P/$pkgname"
license=('BSD')
depends=('boost-libs' 'miniupnpc' 'openssl' 'zlib')
makedepends=('boost' 'cmake')
source=(https://github.com/PurpleI2P/${pkgname}/archive/${pkgver}.tar.gz)
install=$pkgname.install
backup=(etc/$pkgname/$pkgname.conf
etc/$pkgname/tunnels.conf)
conflicts=("$pkgname-git")

build() {
    cd "$srcdir/$pkgname-$pkgver"
    cd build

    BUILD_FLAGS='-DCMAKE_CXX_FLAGS="-w" -DCMAKE_INSTALL_PREFIX=/usr
    -DWITH_UPNP=ON -DWITH_PCH=OFF -DCMAKE_BUILD_TYPE=Release'

    if [ "$CARCH" == "x86_64" ] || [ "$CARCH" == "i686" ]
    then
        if grep -q -m1 -o aes /proc/cpuinfo
        then
            BUILD_FLAGS="${BUILD_FLAGS} -DWITH_AESNI=ON"
        fi

        if grep -q -m1 -o avx /proc/cpuinfo
        then
            BUILD_FLAGS="${BUILD_FLAGS} -DWITH_AVX=ON"
        fi
    fi

    cmake . $BUILD_FLAGS
    make
}

package(){
    _conf_dest=etc/${pkgname}
    _home_dest=var/lib/${pkgname}
    _share_dest=usr/share

    cd $srcdir/$pkgname-$pkgver

    cd build
    make DESTDIR=$pkgdir install
    install -Dm0644 ../contrib/debian/$pkgname.service $pkgdir/usr/lib/systemd/system/$pkgname.service
    install -Dm0644 ../contrib/debian/$pkgname.tmpfile $pkgdir/usr/lib/tmpfiles.d/$pkgname.conf

    install -Dm0644 $srcdir/$pkgname-$pkgver/contrib/$pkgname.conf $pkgdir/${_conf_dest}/$pkgname.conf
    install -Dm0644 $srcdir/$pkgname-$pkgver/contrib/tunnels.conf $pkgdir/${_conf_dest}/tunnels.conf
    install -Dm0644 $srcdir/$pkgname-$pkgver/contrib/subscriptions.txt $pkgdir/${_conf_dest}/subscriptions.txt

    install -d -m0750 $pkgdir/${_home_dest}
    ln -s /${_conf_dest}/$pkgname.conf $pkgdir/${_home_dest}/$pkgname.conf
    ln -s /${_conf_dest}/tunnels.conf $pkgdir/${_home_dest}/tunnels.conf
    ln -s /${_conf_dest}/subscriptions.txt $pkgdir/${_home_dest}/subscriptions.txt

    cd $srcdir/$pkgname-$pkgver/contrib
    _dest="$pkgdir/${_share_dest}/${pkgname}"
    find ./certificates -type d -exec install -d {} ${_dest}/{} \;
    find ./certificates -type f -exec install -Dm644 {} ${_dest}/{} \;
    ln -s /${_share_dest}/${pkgname}/certificates $pkgdir/${_home_dest}/certificates

    # license
    install -Dm644 $srcdir/$pkgname-$pkgver/LICENSE "$pkgdir/${_share_dest}/licenses/${pkgname}/LICENSE"

    # docs
    _dest="$pkgdir/${_share_dest}/doc/${pkgname}"
    install -Dm644 $srcdir/$pkgname-$pkgver/README.md "${_dest}/README.md"

    # remove src folder and LICENSE
    rm -r $pkgdir/usr/{src,LICENSE}

    #man
    install -Dm644 $srcdir/$pkgname-$pkgver/debian/$pkgname.1 "$pkgdir/${_share_dest}/man/man1/$pkgname.1"
    chmod -R o= $pkgdir/${_home_dest}
}

md5sums=('ebf5acc5b0ee17b0387aa6a0714be997')
