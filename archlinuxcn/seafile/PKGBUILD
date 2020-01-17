# Maintainer: Joffrey <j-off@live.fr>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>

pkgname=seafile
pkgver=7.0.5
pkgrel=1
pkgdesc='An online file storage and collaboration tool'
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/$pkgname"
license=('GPL2')
depends=(
    'ccnet-server'
    'libsearpc'
    'libevent'
    'fuse'
    'python2'
    'python2-future'
    'sqlite'
)
makedepends=(
    'vala'
    'intltool'
)
conflicts=('seafile-server')
source=(
    "seafile-$pkgver.tar.gz::$url/archive/v${pkgver}.tar.gz"
    "seaf-cli@.service"
)
sha256sums=(
    '19b353279e20f84af94b08c62b948748bda8cd69eeb980c9fc124ea9a9a5f825'
    'c37510109c1de64c774896df39aece240c056b54414d2119fca01860211156ba'
)
provides=('seafile-client-cli')

prepare() {
    cd "$srcdir/seafile-$pkgver"
    sed -i 's|(DESTDIR)@prefix@|@prefix@|' './lib/libseafile.pc.in'

    # Fix all script's python 2 requirement
    shebang='#!/usr/bin/env python'
    grep -s -l -r "$shebang" | xargs sed -i "1 s|$shebang|${shebang}2|"
}

build() {
    cd "$srcdir/seafile-$pkgver"
    ./autogen.sh
    ./configure \
        --enable-console \
        --prefix=/usr \
        PYTHON=/usr/bin/python2
    make
}

package() {
    cd "$srcdir/seafile-$pkgver"
    make DESTDIR="$pkgdir" install

    install -Dm644 \
        "$srcdir/seaf-cli@.service" \
        "$pkgdir/usr/lib/systemd/system/seaf-cli@.service"
}
