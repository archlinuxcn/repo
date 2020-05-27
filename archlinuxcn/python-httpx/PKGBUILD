_name=httpx
pkgname=python-httpx
pkgver=0.13.2
pkgrel=1
pkgdesc="The next generation HTTP client."
arch=(any)
url="https://github.com/encode/httpx"
license=('BSD')
depends=('python-urllib3' 'python-h11' 'python-h2' 'python-chardet' 'python-hstspreload' 'python-idna' 'python-rfc3986' 'python-sniffio')
makedepends=('python-setuptools')
optdepends=('python-brotlipy: decoding for "brotli" compressed responses')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/httpx-0.13.2.tar.gz")
sha256sums=('4387a6601839fb71f5aea57042e6b476f24ca118cc05c55f1e52ed8baaf0a45f')

prepare() {
  cd "$srcdir/httpx-0.13.2"
  sed -i '/certifi/d' setup.py
  sed -e '/import certifi/d' \
      -e 's|certifi.where()|"/etc/ssl/certs/ca-certificates.crt"|' \
      -i httpx/_config.py
}

build() {
  cd "$srcdir/httpx-0.13.2"
  python3 setup.py build
}

package() {
  cd "$srcdir/httpx-0.13.2"
  python3 setup.py install --root=$pkgdir --optimize=1 --skip-build

  # make sure we don't install annoying files
  local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "$pkgdir/$_site_packages/tests/"
}

