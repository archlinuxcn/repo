# Maintainer: Hao Long <imlonghao@archlinuxcn.org>

_name=rich
pkgname=python-rich
pkgver=2.1.0
pkgrel=1
pkgdesc="Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal"
arch=(any)
url="https://github.com/willmcgugan/rich"
license=('MIT')
depends=('python-colorama'
         'python-pprintpp'
         'python-pygments'
         'python-typing_extensions'
         'python-commonmark')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('e39a43f4e61ac922cea11d8b335913232bda21fa0f5481dc3701a6d31f2d2569')

build() {
  cd "$srcdir/$_name-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_name-$pkgver"
  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build

  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"

  install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}

