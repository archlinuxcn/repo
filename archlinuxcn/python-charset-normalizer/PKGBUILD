_name=charset-normalizer
pkgname=python-charset-normalizer
pkgver=2.0.4
pkgrel=1
pkgdesc="The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet."
arch=(any)
url="https://github.com/ousret/charset_normalizer"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/charset-normalizer-2.0.4.tar.gz")
sha256sums=('f23667ebe1084be45f6ae0538e4a5a865206544097e4e8bbcacf42cd02a348f3')

build() {
  cd "$srcdir/charset-normalizer-2.0.4"
  python3 setup.py build
}

package() {
  cd "$srcdir/charset-normalizer-2.0.4"
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

