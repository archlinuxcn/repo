_name=aioimaplib
pkgname=python-aioimaplib
pkgver=2.0.3
pkgrel=1
pkgdesc="Python asyncio IMAP4rev1 client library"
arch=(any)
url=""
license=(GPL-3.0-only)
depends=('python' 'python-setuptools')
makedepends=('python-poetry-core' 'python-build' 'python-installer')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/aioimaplib-2.0.3.tar.gz")
sha256sums=('0a7c3e558af754a7ca8b5927be07c4ab6a0b7cd963174ca4290f6b0d51d4616b')

build() {
  cd "$srcdir/aioimaplib-2.0.3"
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/aioimaplib-2.0.3"
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

