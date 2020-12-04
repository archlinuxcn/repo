_name=aiosocks
pkgname=python-aiosocks
pkgver=0.2.6
pkgrel=4
pkgdesc="SOCKS proxy client for asyncio and aiohttp"
arch=('any')
url="https://github.com/nibrag/aiosocks"
license=('Apache 2')
depends=('python' 'python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/aiosocks-0.2.6.tar.gz")
sha256sums=('94dfb2c3ff2fc646c88629e29872599cc93d9137c2eace68dc89079e6a221277')

build() {
  cd "$srcdir/aiosocks-0.2.6"
  python3 setup.py build
}

package() {
  cd "$srcdir/aiosocks-0.2.6"
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

