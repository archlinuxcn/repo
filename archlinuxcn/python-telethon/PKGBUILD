_name=Telethon
pkgname=python-telethon
pkgver=1.17.5
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=(any)
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python-pyaes' 'python-rsa')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/Telethon-1.17.5.tar.gz")
sha256sums=('958432bb3849d3e1fecfb45e211832a579fb4340a1d2b21b0d1a7d30407e39ec')

build() {
  cd "$srcdir/Telethon-1.17.5"
  python3 setup.py build
}

package() {
  cd "$srcdir/Telethon-1.17.5"
  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build

  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"
}

