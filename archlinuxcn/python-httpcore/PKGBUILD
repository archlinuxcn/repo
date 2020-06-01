_name=httpcore
pkgname=python-httpcore
pkgver=0.9.1
pkgrel=2
pkgdesc="A minimal low-level HTTP client."
arch=(any)
url="https://github.com/encode/httpcore"
license=('BSD')
depends=('python-h11' 'python-h2' 'python-sniffio')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/httpcore-0.9.1.tar.gz")
sha256sums=('ecc5949310d9dae4de64648a4ce529f86df1f232ce23dcfefe737c24d21dfbe9')

build() {
  cd "$srcdir/httpcore-0.9.1"
  python3 setup.py build
}

package() {
  cd "$srcdir/httpcore-0.9.1"
  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build

  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"
}

