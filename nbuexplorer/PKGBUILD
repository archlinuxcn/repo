# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

pkgname=nbuexplorer
pkgver=3.3
pkgrel=3
pkgdesc='Nokia NBU, NBF, NFB, NFC and ARC backup file parser, extractor and viewer.'
arch=('any')
url='https://sourceforge.net/projects/nbuexplorer/'
license=('GPL3')
depends=('mono')
source=(
    "$pkgname::svn+https://svn.code.sf.net/p/nbuexplorer/code/trunk#revision=88"
    "$pkgname.sh"
)
makedepends=('bash>=4.0' 'subversion' 'svnwcrev')
sha256sums=('SKIP'
            '99c81f346e7c5ecbb1f880d341c775ab27358d9fad9bec76b85be8c2ed30f2d2')

prepare() {
  cd $pkgname
  sed -i 's#Subwcrev#svnwcrev#' NbuExplorer2010.csproj
}

build() {
  cd $pkgname
  xbuild /p:Configuration=Release NbuExplorer2010.sln
}

package() {
  install -Dm755 $pkgname.sh "$pkgdir/usr/bin/$pkgname"
  install -Dm644 $pkgname/bin/Release/NbuExplorer.exe "$pkgdir/usr/lib/$pkgname/NbuExplorer.exe"
  install -Dm644 $pkgname/readme.txt "$pkgdir/usr/share/doc/$pkgname/readme.txt"
  install -Dm644 $pkgname/changelog.txt "$pkgdir/usr/share/doc/$pkgname/changelog.txt"
}
