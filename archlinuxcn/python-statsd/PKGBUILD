_name=statsd
pkgname=python-statsd
pkgver=4.0.0
pkgrel=1
pkgdesc="A simple statsd client."
arch=(any)
url=""
license=('MIT')
depends=('python')
makedepends=('python-setuptools' 'python-setuptools' 'python-build' 'python-installer' 'python-wheel')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/statsd-4.0.0.tar.gz")
sha256sums=('e767eb2b8c705ca4c0a55b96fe47f80ce15ba98c7a851dd2ad00504d29cb2e3c')

build() {
  cd "$srcdir/statsd-4.0.0"
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/statsd-4.0.0"
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

