# Maintainer: Hao Long <imlonghao@archlinuxcn.org>

_name=rich
pkgname=python-rich
pkgver=2.3.1
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
sha256sums=('0bf16dc14184aeea22c5c6895c4c7061cd49ee87cd9110cb62b0cfd492b30758')

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

