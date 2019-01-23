# Maintainer: Joffrey <j-off@live.fr>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>

pkgname=seafile-server
pkgver=6.3.4
pkgrel=2
pkgdesc='Seafile server core'
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url='https://github.com/haiwen/seafile-server'
license=('AGPL3')
depends=(
    "ccnet-server>=$pkgver"
    'fuse2'
    'libevhtp-seafile'
    'libarchive'
)
makedepends=('vala')
conflicts=('seafile')
changelog='ChangeLog'
source=(
    "$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver-server.tar.gz"
    'fix_pids-folder-out-of-seafile-data.diff'
    'fix_seafile-admin.diff'
    'fix_mysql_support.diff'
    'seafile-server@.service'
)
sha256sums=(
    '1ba4c641bad8d7592fd2592827e81470c88b8e802707d2b1e6d551c16d0da100'
    'd725bda36aedd424d426d7ce62e19c7036ccfc6a5759df12f139656ba15e425c'
    '51a7f13b8c3dfcb3f510c68c9791bf6ace1a0b332ba26fdf55c850409bf387fa'
    'd625d1ac5fc666386a53059b1d31bce0e63c79b69c11bfb769f6390afb629611'
    'da31d1b61031cbacc42e1ab708c67c83dba933ff391b07677dabab7ab79729f4'
)

prepare() {
    cd "$srcdir/$pkgname-$pkgver-server"
    # Remove scripts for tests and others OS
    rm -rf "./scripts/"{build,upgrade/win32,*.bat,*.md} "./integration-tests"

    # Apply patchs
    sed -i "s|(DESTDIR)@prefix@|@prefix@|" "./lib/libseafile.pc.in"
    for diff in "$srcdir"/*.diff; do patch -p1 -i "$diff"; done

    # Fix python path
    shebang='#!/usr/bin/env python'; pyenv='PYTHON=python[.0-9]+' 
    grep -s -l -r    "$shebang" | xargs sed -i -E "1 s|$shebang|${shebang}2|"
    grep -s -l -r -E "$pyenv"   | xargs sed -i -E "s|$pyenv|PYTHON=python2|g"
}

build() {
    cd "$srcdir/$pkgname-$pkgver-server"
    ./autogen.sh
    ./configure \
        --enable-fuse \
        --enable-python \
        --prefix=/usr \
        PYTHON='/usr/bin/python2'
    make
}

package() {
    cd "$srcdir/$pkgname-$pkgver-server"
    make DESTDIR="$pkgdir" install

    # Prepare directories layout for deploying
    mkdir -p "$pkgdir/usr/share/$pkgname/runtime"
    cp -r -p "./scripts" "$pkgdir/usr/share/$pkgname/scripts"

    mv "$pkgdir/usr/share/$pkgname/scripts/seahub.conf" \
       "$pkgdir/usr/share/$pkgname/runtime/"
    mv "$pkgdir/usr/share/$pkgname/scripts/upgrade" \
       "$pkgdir/usr/share/$pkgname/"

    install -Dm644 \
        "$srcdir/seafile-server@.service" \
        "$pkgdir/usr/lib/systemd/system/seafile-server@.service"
}
