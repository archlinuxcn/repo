# Maintainer: Boohbah <boohbah at gmail.com>
# Contributor: mathieui <mathieui[at]mathieui.net>
# Contributor: rayanamukami <matthewchoi_123 at hotmail.com>

pkgname=oneko
pkgrel=6
pkgver=1.2.5
_pkgver="1.2.sakura.5"
pkgdesc="A cat that chases around your cursor"
arch=('x86_64' 'i686')
url="http://www.daidouji.com/oneko/"
license=('Public Domain')
depends=('libx11' 'libxext')
makedepends=('imake' 'make' 'desktop-file-utils')
source=(
    "http://www.daidouji.com/$pkgname/distfiles/$pkgname-$_pkgver.tar.gz"
    "gcc2024.patch"
    "gcc2025.patch"
)
md5sums=('456b318fa6e61431bf4f0a42b110014a'
         'f6ebbd81cab895f8909fbd26832cfba7'
         '145b0a52bd79f29fa965f57e4092e0b9')

prepare() {
    cd "$srcdir/$pkgname-$_pkgver/"
    patch -Np1 -i ../gcc2024.patch
    patch -Np1 -i ../gcc2025.patch
}

build() {
    cd "$srcdir/$pkgname-$_pkgver/"
    xmkmf -a
    make
}

package() {
    cd "$srcdir/$pkgname-$_pkgver/"
    _mandir="$pkgdir/usr/share/man"

    mkdir -p "$_mandir/man1/"
    mkdir -p "$_mandir/jp/man1/"
    mkdir -p "$pkgdir/usr/bin"

    make DESTDIR=$pkgdir install

    cp oneko.man "$_mandir/man1/oneko.1"
    cp oneko.man.jp "$_mandir/jp/man1/oneko.1"
    echo -e '#!/bin/sh'"\nxsetroot -cursor_name top_left_arrow || xsetroot -cursor_name left_ptr " > "$pkgdir/usr/bin/oneko-restore-cursor"
    chmod +x "$pkgdir/usr/bin/oneko-restore-cursor"
}
