# Maintainer: Mario Finelli <mario at finel dot li>
# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Arthur Titeica <arthur dot titeica at gmail dot com>

pkgname=ttfautohint
pkgver=1.8.4
pkgrel=3
pkgdesc="Provides automated hinting process for web fonts"
arch=(i686 x86_64)
url="http://www.freetype.org/$pkgname"
license=(FTL GPL-2.0-only)
depends=(freetype2
         gcc-libs
         glibc
         harfbuzz
         qt5-base)
source=(https://download.savannah.gnu.org/releases/freetype/$pkgname-$pkgver.tar.gz{,.sig})
sha256sums=('8a876117fa6ebfd2ffe1b3682a9a98c802c0f47189f57d3db4b99774206832e1'
            'SKIP')
validpgpkeys=('58E0C111E39F5408C5D3EC76C1A60EACE707FDA5')

build() {
  cd "$pkgname-$pkgver"
  ./configure \
    --prefix=/usr \
    --without-doc \
    --with-qt=/usr/lib/qt
  make
}

check() {
  cd "$pkgname-$pkgver"
  make -k check
}

package() {
  cd "$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname/" COPYING FTL.TXT
  install -Dm644 -t "$pkgdir/usr/share/doc/$pkgname/" "doc/$pkgname.pdf"
  install -Dm644 -t "$pkgdir/usr/share/man/man1/" "frontend/$pkgname"{,GUI}.1
}

# vim: set ts=2 sw=2 et:
