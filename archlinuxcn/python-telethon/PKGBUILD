_name=Telethon
pkgname=python-telethon
pkgver=1.42.0
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=(any)
url="https://github.com/LonamiWebs/Telethon"
license=('MIT')
depends=('python-pyaes' 'python-rsa')
makedepends=('python-setuptools' 'python-build' 'python-installer')
optdepends=('python-cryptg: alternative crypto library' 'python-pysocks: socks proxy support' 'python-python-socks: socks proxy support' 'python-hachoir: parse media metadata for uploading' 'python-pillow: resize photos for uploading')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/telethon-1.42.0.tar.gz")
sha256sums=('032e95511261d5ead719f75494c6c85ece2ce71816b54f3c65d6ccc371d6994d')

build() {
  cd "$srcdir/telethon-1.42.0"
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/telethon-1.42.0"
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

  # make sure we don't install any world-writable or root-readable-only files
  # we shouldn't need to fix ownership as we extract tarballs as a non-root user
  # https://github.com/pypa/setuptools/issues/1328
  # https://github.com/LonamiWebs/Telethon/issues/1605
  chmod u=rwX,go=rX -R "$pkgdir"
  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"
}

