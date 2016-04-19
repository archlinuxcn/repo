# Maintainer: Sebastian Jug <seb@stianj.ug>
# Contributor: John Reese <jreese@noswap.com>
# Upstream URL: https://github.com/atom/atom
#
# For improvements/fixes to this package, please send a pull request:
# https://github.com/sjug/atom-editor

pkgname=atom-editor
pkgver=1.7.2
pkgrel=1
pkgdesc='Chrome-based text editor from Github'
arch=('x86_64' 'i686')
url='https://github.com/atom/atom'
license=('MIT')
depends=('alsa-lib' 'desktop-file-utils' 'gconf' 'gtk2' 'libgnome-keyring' 'libnotify' 'libxtst' 'nodejs' 'nss' 'python2')
optdepends=('gvfs: file deletion support')
makedepends=('git' 'npm')
conflicts=('atom-editor-bin' 'atom-editor-git')
install=atom.install
source=("https://github.com/atom/atom/archive/v${pkgver}.tar.gz"
        'package.patch')
sha256sums=('f6784b4f681706faf1e2a8369c06df4289646b1a547032e6b0b8b0e93e848113'
            'ab27ab817f67043e98298d525efb6a417dea07f4012b6dfb7cf6a538f9b50bab')

prepare() {
  cd "atom-$pkgver"
  
  patch -Np0 -i "$srcdir/package.patch"

  sed -i -e "/exception-reporting/d" \
      -e "/metrics/d" package.json

  sed -e "s/<%= description %>/$pkgdesc/" \
    -e "s|<%= appName %>|Atom|"\
    -e "s|<%= installDir %>/share/<%= appFileName %>|/usr/bin|"\
    -e "s|<%= iconPath %>|atom|"\
    resources/linux/atom.desktop.in > resources/linux/Atom.desktop
}

build() {
  cd "$srcdir/atom-$pkgver"

  export PYTHON=python2
  script/build --build-dir "$srcdir/atom-build"
}

package() {
  cd "$srcdir/atom-$pkgver"

  script/grunt install --build-dir "$srcdir/atom-build" --install-dir "$pkgdir/usr"

  install -Dm644 resources/linux/Atom.desktop "$pkgdir/usr/share/applications/atom.desktop"
  install -Dm644 resources/app-icons/stable/png/1024.png "$pkgdir/usr/share/pixmaps/atom.png"
  install -Dm644 LICENSE.md "$pkgdir/usr/share/licenses/$pkgname/LICENSE.md"
}
