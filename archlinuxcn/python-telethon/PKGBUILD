_name=Telethon
pkgname=python-telethon
pkgver=1.26.1
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=(any)
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python-pyaes' 'python-rsa')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/Telethon-1.26.1.tar.gz")
sha256sums=('d894f6ef2bf2cb119f6413b9f620957503785bab0999694b4bf67dea36f8ee09')

build() {
  cd "$srcdir/Telethon-1.26.1"
  python3 setup.py build
}

package() {
  cd "$srcdir/Telethon-1.26.1"
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

