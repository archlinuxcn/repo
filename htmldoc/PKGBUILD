# Maintainer: James An <james@jamesan.ca>
# Contributor: Mariusz Libera <mariusz.libera@gmail.com>
# Contributor: mortdeus <mortdeus@gocos2d.org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: tobias <tobias@archlinux.org>
# Contributor: Simon Rutishauser <simon.rutishauser@gmx.ch>

pkgname=htmldoc
pkgver=1.8.28
pkgrel=1
pkgdesc="Produce PDF or Postscript from HTML documents including TOCs and Indices"
arch=('i686' 'x86_64')
url="http://www.htmldoc.org"
license=('GPL2')
depends=('libxpm' 'fltk' 'libjpeg' 'openssl' 'shared-mime-info')
conflicts=('htmldoc-svn')
changelog=Changelog
install=$pkgname.install
source=(
    "http://www.msweet.org/files/project1/htmldoc-${pkgver}-source.tar.gz"
    'errno.patch'
)
md5sums=('1c2f379e4535734ececd59d6629b4d2d'
         '2f48488fd485f2583e02b519d6cef553')

prepare() {
    cd "$pkgname-$pkgver"

    # replace obsolete libgnutls-config with pkg-config
    grep -rIl 'libgnutls-config --libs' | while read file ; do sed -i 's/libgnutls-config --libs/pkg-config --libs gnutls/' $file ; done

    # apply patches
    for patch in ../*.patch ; do
        patch -Np1 -i $patch
    done

    # fix desktop file
    echo "MimeType=application/vnd.htmldoc-book;" >> desktop/htmldoc.desktop
    sed -i 's/X-Red-Hat.*$//' desktop/htmldoc.desktop
    sed -i 's/htmldoc.png/htmldoc/' desktop/htmldoc.desktop
}

build() {
    cd "$pkgname-$pkgver"

    ./configure \
        prefix="$pkgdir/usr" \

    make
}

package() {
    cd "$pkgname-$pkgver"

    make install

    # documentation
    install -d "$pkgdir/usr/share/doc/htmldoc"
    for f in CHANGES.txt README.txt; do
        install -Dm644 $f \
            "$pkgdir/usr/share/doc/htmldoc/$f"
    done

    # desktop file
    install -Dm644 desktop/htmldoc.desktop \
        "$pkgdir/usr/share/applications/htmldoc.desktop"

    # icons
    for s in 16 24 32 48 64 96 128; do
        install -Dm644 desktop/htmldoc-${s}.png \
            "$pkgdir/usr/share/icons/hicolor/${s}x${s}/apps/htmldoc.png"
    done

    # mime
    install -Dm644 desktop/htmldoc.xml \
        "$pkgdir/usr/share/mime/packages/htmldoc.xml"
}
