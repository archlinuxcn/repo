# Maintainer: Kevin MacMartin <prurigro at gmail dot com>

_pkgname=treesheets
pkgname=$_pkgname-git
pkgver=r274.6d1b992
pkgrel=1
pkgdesc='The ultimate replacement for spreadsheets, mind mappers, outliners, PIMs, text editors and small databases'
url='http://treesheets.com'
license=('zlib')
depends=('wxgtk')
makedepends=('cmake' 'git')
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h')

source=(
  "git://github.com/aardappel/$_pkgname.git"
  'myframe.patch'
)

sha512sums=(
  'SKIP'
  '7ea8b6947c334adebba774bcdd4db27670206a216de0c023c2b69aa3ad3b621165733a36f03f2e23bab1e7721982a24c29c4446754ba79c11c5735961ad04816'
)

pkgver() {
  cd $_pkgname
  printf 'r%s.%s' "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  cd $_pkgname
  patch -p1 < ../myframe.patch
  find TS/images -type f ! -iname '*.png' -a ! -iname '*.svg' -delete
}

build() {
  cd $_pkgname
  cmake -DCMAKE_BUILD_TYPE=Release
  make
}

package() {
  cd $_pkgname
  install -Dm644 ZLIB_LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

  cd TS
  install -dm755 "$pkgdir/usr/share/applications"
  sed 's|Icon=images/|Icon=|' $_pkgname.desktop > "$pkgdir/usr/share/applications/$_pkgname.desktop"
  install -Dm644 images/$_pkgname.svg "$pkgdir/usr/share/pixmaps/$_pkgname.svg"
  install -Dm755 $_pkgname "$pkgdir/usr/bin/$_pkgname"

  install -dm755 "$pkgdir/usr/share/$_pkgname"
  cp -R scripts "$pkgdir/usr/share/$_pkgname/scripts"
  cp -R examples "$pkgdir/usr/share/$_pkgname/examples"
  cp -R images "$pkgdir/usr/share/$_pkgname/images"
  cp -R docs "$pkgdir/usr/share/$_pkgname/docs"

  cd "$pkgdir/usr/share/$_pkgname/examples"
  ln -s tutorial.cts tutorial-en.cts
}
