_name=httpx
pkgname=python-httpx
pkgver=0.12.1
pkgrel=1
pkgdesc="The next generation HTTP client."
arch=(any)
url="https://github.com/encode/httpx"
license=(BSD)
depends=('python-urllib3' 'python-h11' 'python-h2' 'python-chardet' 'python-hstspreload' 'python-idna' 'python-rfc3986' 'python-sniffio')
makedepends=('python-setuptools')
optdepends=('python-brotlipy: decoding for "brotli" compressed responses')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('405b4749f597b1f45cae5bffc17b23dc251cce30a0c4c8126f1007b9e728a615')

prepare() {
  cd "$srcdir/$_name-$pkgver"
  sed -i '/certifi/d' setup.py
  sed -e '/import certifi/d' \
      -e 's|certifi.where()|"/etc/ssl/certs/ca-certificates.crt"|' \
      -i httpx/_config.py
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

