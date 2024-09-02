# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Sherlock Holo <sherlockya@gmail.com>
# Contributor: Sean Enck <enckse@gmail.com>
# Contributor: NeoTheFox <soniczerops@gmail.com>
pkgname=python-telegram-bot
pkgver=21.5
pkgrel=1
pkgdesc="A library that provides a Python interface to the Telegram Bot API"
url="https://github.com/${pkgname}/${pkgname}"
license=(LGPL-3.0-only)
arch=(any)
depends=(python-httpx)
makedepends=(python-build python-installer python-hatchling python-wheel)
# checkdepends=(python-pytest-asyncio python-pytest-timeout python-flaky python-beautifulsoup4)
optdepends=('python-cachetools: for use a variant of LRUCache'
  'python-h2: for HTTP/2 support'
  'python-apscheduler: for job queue support'
  'python-pytz: for job queue support'
  'python-cryptography: for support cryptography library'
  'python-aiolimiter: for rate limiter'
  'python-socksio: for SOCKS proxy support'
  'python-tornado: for webhooks support')
source=(${url}/releases/download/v${pkgver}/${pkgname//-/_}-${pkgver}.tar.gz)
sha512sums=('0a4b1b39ceb59e9f8c00431c454308634f0dc1ba2f0e887968af0e063895f0f393362eb79a54123b3453cdec932cc0338f546bd7c95dd298eda47a083fb3df92')

build() {
  cd ${pkgname//-/_}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${pkgname//-/_}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
