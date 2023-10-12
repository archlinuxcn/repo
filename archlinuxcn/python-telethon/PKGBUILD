_name=Telethon
pkgname=python-telethon
pkgver=1.31.0
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=(any)
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python-pyaes' 'python-rsa')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/Telethon-1.31.0.tar.gz")
sha256sums=('8c2a2e0398e329323bd6d2a6c1d3964f85e882d557144b77edb8ff969916ff5b')

build() {
  cd "$srcdir/Telethon-1.31.0"
  python3 setup.py build
}

package() {
  cd "$srcdir/Telethon-1.31.0"
  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build

  # make sure we don't install any world-writable or root-readable-only files
  # we shouldn't need to fix ownership as we extract tarballs as a non-root user
  # https://github.com/pypa/setuptools/issues/1328
  # https://github.com/LonamiWebs/Telethon/issues/1605
  chmod u=rwX,go=rX -R "$pkgdir"
  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"
}

