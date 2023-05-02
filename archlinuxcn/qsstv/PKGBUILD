#Maintainer: Alexander Fasching <fasching.a91@gmail.com>
#Contributor: Andreas Schreiner <andreas.schreiner@sonnenmulde.at>
#Contributor: Bob Finch <w9ya@qrparci.net>

pkgname=qsstv
pkgver=9.5.8
_pkgver=9.5.8
pkgrel=2
pkgdesc="Radio Slow-Scan TV for qt"
url="https://github.com/ON4QZ/QSSTV"
depends=('qt5-base' 'libpulse' 'v4l-utils' 'hamlib' 'fftw' 'openjpeg2' 'alsa-lib')
source=(https://apps.manko.pro/aur/${pkgname}_${pkgver}.tar.gz
        $pkgname.desktop)

arch=('i686' 'x86_64')
license=('GPL')
sha512sums=('88e1bb62e3838d94c670397fceced7913ac4675e7fea93d78c2b2799ef172c27baad9ac7f7d119eb1130296d21b641164cdd0f53a93967305f632fa9bb3b4e6a'
            '793be2e500824966d4288fff059fe5c869ec547ff5f4e32fbec02eeae1b12d6aa4e5ba34a9ce590bb166b73086291bfa3e0c2d76fb7c03187f656e8955acef4c')

build() {
  cd "$srcdir/${pkgname}"

  # trick qmake
  # qmake-qt5 PREFIX="$pkgdir/usr/"
  qmake-qt5 PREFIX=/usr/
  make $MAKEFLAGS
}

package() {
  cd "$srcdir/${pkgname}"
  mkdir -p "$pkgdir/usr/bin/"
  make INSTALL_ROOT="$pkgdir" install

  cd $srcdir
  install -D -m644 "$pkgname.desktop" "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -D -m644 "$srcdir/${pkgname}/icons/${pkgname}.png" "$pkgdir/usr/share/pixmaps/${pkgname}.png"
}
