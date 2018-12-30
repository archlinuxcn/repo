# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

pkgname=python-nvchecker-toolbelt
pkgver=0.2
pkgrel=2
pkgdesc='Utilities around nvchecker'
arch=(any)
url='https://gitlab.com/yan12125/nvchecker-toolbelt'
license=('GPL3')
makedepends=('git' 'python-setuptools-scm')
depends=('nvchecker')
source=("git+https://gitlab.com/yan12125/nvchecker-toolbelt?signed#tag=$pkgver")
sha256sums=('SKIP')
validpgpkeys=('481C4474AF1572165AE4C6AF3FDDD575826C5C30')  # Chih-Hsuan Yen <yan12125@gmail.com>

build() {
  cd nvchecker-toolbelt
  python setup.py build
}

package() {
  cd nvchecker-toolbelt
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
