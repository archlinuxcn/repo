_name=statsd
pkgname=python-statsd
pkgver=4.0.1
pkgrel=2
pkgdesc="A simple statsd client."
arch=(any)
url="https://github.com/jsocol/pystatsd"
license=('MIT')
depends=('python')
makedepends=('python-setuptools' 'python-build' 'python-installer' 'python-wheel')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/statsd-4.0.1.tar.gz")
sha256sums=('99763da81bfea8daf6b3d22d11aaccb01a8d0f52ea521daab37e758a4ca7d128')

build() {
  cd "$srcdir/statsd-4.0.1"
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/statsd-4.0.1"
  python -m installer --destdir="$pkgdir" dist/*.whl

  # make sure we don't install any world-writable or root-readable-only files
  # we shouldn't need to fix ownership as we extract tarballs as a non-root user
  # https://github.com/pypa/setuptools/issues/1328
  # https://github.com/LonamiWebs/Telethon/issues/1605
  chmod u=rwX,go=rX -R "$pkgdir"
  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"
}

