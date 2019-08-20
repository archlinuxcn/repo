# Maintainer: Joffrey <j-off@live.fr>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>

pkgname=seafile-server
pkgver=7.0.4
pkgrel=1
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
source=(
    "$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver-server.tar.gz"
    'fix_seafile-controller_paths.diff'
    'fix_seafile-admin.diff'
    'fix_mysql_support.diff'
    'seafile-server@.service'
)
sha256sums=(
    'a17c8b5bdfc82ac893160ff6255b16882f748e3b3dbf6f72dee17d40b895f783'
    '8069df2e84e5142a030c4598e410eeece1aaed2fdce3b8abe82b4752d257ffb9'
    '51a7f13b8c3dfcb3f510c68c9791bf6ace1a0b332ba26fdf55c850409bf387fa'
    '4596350a73025b63ad8189488bff896c09a4b1e2855e25ee5bbc111d25b7cfe7'
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
