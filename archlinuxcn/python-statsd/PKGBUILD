_name=statsd
pkgname=python-statsd
pkgver=3.3.0
pkgrel=4
pkgdesc="A simple statsd client."
arch=(any)
url="https://github.com/jsocol/pystatsd"
license=('MIT')
depends=('python' 'python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/statsd-3.3.0.tar.gz")
sha256sums=('e3e6db4c246f7c59003e51c9720a51a7f39a396541cb9b147ff4b14d15b5dd1f')

build() {
  cd "$srcdir/statsd-3.3.0"
  python3 setup.py build
}

package() {
  cd "$srcdir/statsd-3.3.0"
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

