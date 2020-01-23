# Maintainer: Shatur95 <genaloner@gmail.com>
# Co-Maintainer: Mark Wagie <mark.wagie@tutanota.com>

pkgname=bibata-cursor-theme
pkgver=0.4.2
pkgrel=1
pkgdesc="Material Based Cursor Theme"
arch=('any')
url="https://github.com/KaizIqbal/Bibata_Cursor"
license=('GPL3')
makedepends=('python-pillow' 'inkscape' 'xorg-xcursorgen')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('d00f91ebefa34d5c7d578c78a17825238fcb90540de0dbf4cf3ffb587e1ae976')

_variants=(Bibata_Amber Bibata_Classic Bibata_Ice Bibata_Oil)

build() {
  cd "$srcdir/Bibata_Cursor-$pkgver"
  
  for variant in ${_variants[*]}
  do
    echo "Building $variant..."
    python render-cursors.py ./src/$variant/source-cursors.svg -o -a --name $variant
    ./tweak.sh $variant
    ./x11-make.sh $variant
    cp src/$variant/*.theme $variant/out/X11/$variant
  done
}

package() {
  cd "$srcdir/Bibata_Cursor-$pkgver"
  
  install -d "$pkgdir/usr/share/icons"
  for variant in ${_variants[*]}
  do
    cp -a $variant/out/X11/$variant "$pkgdir/usr/share/icons"
  done
}
