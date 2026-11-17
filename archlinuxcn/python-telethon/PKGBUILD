pkgname=python-telethon
pkgver=1.46.0
pkgrel=1
pkgdesc="Full-featured Telegram client library for Python 3"
arch=(any)
url="https://telethon.dev"
license=(MIT)
depends=('python-pyaes' 'python-rsa')
makedepends=('python-hatchling' 'python-build' 'python-installer')
optdepends=('python-cryptg: alternative crypto library'
            'python-python-socks: socks proxy support'
            'python-hachoir: parse media metadata for uploading'
            'python-pillow: resize photos for uploading'
            'python-isal: faster zlib and gzip compression')
source=("https://codeberg.org/Lonami/Telethon/archive/v${pkgver}.tar.gz")
sha256sums=('e305f926e5762e9a5bb1ec2c79c9ef8176015608a5ef97bb62661a98ade894ae')

build() {
  cd "$srcdir/telethon"
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/telethon"
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

