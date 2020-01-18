_name=httpx
pkgname=python-httpx
pkgver=0.11.1
pkgrel=1
pkgdesc="The next generation HTTP client."
arch=(any)
url="https://github.com/encode/httpx"
license=(BSD)
depends=('python-urllib3' 'python-h11' 'python-h2' 'python-chardet' 'python-hstspreload' 'python-idna' 'python-rfc3986' 'python-sniffio')
makedepends=('python-setuptools')
optdepends=('python-brotlipy: decoding for "brotli" compressed responses')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('7d2bfb726eeed717953d15dddb22da9c2fcf48a4d70ba1456aa0a7faeda33cf7')

prepare() {
  cd "$srcdir/$_name-$pkgver"
  sed -i '/certifi/d' setup.py
  sed -e '/import certifi/d' \
      -e 's|certifi.where()|"/etc/ssl/certs/ca-certificates.crt"|' \
      -i httpx/config.py
}

build() {
  cd "$srcdir/$_name-$pkgver"
  python3 setup.py build
}

package() {
  cd "$srcdir/$_name-$pkgver"
  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build

  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"
}

