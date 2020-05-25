# Maintainer: Fabius
# Contributor: Adria Arrufat <swiftscythe @t gmail d@t com>
# Contributor: Gordin <9ordin @t gmail d@t com>

pkgname=screenkey
pkgver=1.0
pkgrel=1
pkgdesc="A screencast tool to display your keys inspired by Screenflick"
arch=('any')
url="https://gitlab.com/screenkey/screenkey"
license=('GPL3')
depends=('python' 'python-gobject' 'gtk3' 'python-cairo' 'libx11')
makedepends=('python-setuptools' 'python-distutils-extra')
optdepends=('slop' 'ttf-font-awesome' 'libappindicator-gtk3')
source=("https://gitlab.com/$pkgname/$pkgname/-/archive/v$pkgver/$pkgname-v$pkgver.tar.gz")
sha256sums=('e4d841ed599c73b71b99f7e06482995addc2e626215be0a12d4e3ca66cdee3c2')

build() {
  cd "$srcdir/$pkgname-v$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$pkgname-v$pkgver"
  python3 setup.py install --skip-build --optimize=1 --root="$pkgdir/"
}
