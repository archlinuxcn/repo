# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Artem Vorotnikov <artem@vorotnikov.me>
# Contributor: Andy Weidenbaum <archbaum@gmail.com>

pkgbase=python-pytoml
pkgname=('python-pytoml' 'python2-pytoml')
_pypiname=pytoml
pkgver=0.1.14
pkgrel=1
pkgdesc="A TOML-0.4.0 parser/writer for Python."
arch=('any')
url="https://github.com/avakar/pytoml"
license=('MIT')
makedepends=('python-setuptools' 'python2-setuptools' 'unzip')
source=("https://github.com/avakar/${_pypiname}/archive/v${pkgver}.tar.gz")
sha256sums=('ced2c5d5c240fa96adf2ccbdfa071d51cc80415dd11a4ea800ff0ec987459d34')

prepare() {
  cp -r $_pypiname-$pkgver{,-py2}
}

build() {
  cd "$srcdir/$_pypiname-$pkgver"
  python setup.py build

  cd "$srcdir/$_pypiname-$pkgver-py2"
  python2 setup.py build
}

package_python-pytoml() {
  depends=('python')

  cd "$srcdir/$_pypiname-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}

package_python2-pytoml() {
  depends=('python2')

  cd "$srcdir/$_pypiname-$pkgver"
  python2 setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
