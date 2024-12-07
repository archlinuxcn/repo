# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Sherlock Holo <sherlockya@gmail.com>
# Contributor: Sean Enck <enckse@gmail.com>
# Contributor: NeoTheFox <soniczerops@gmail.com>
pkgname=python-telegram-bot
pkgver=21.9
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
sha512sums=('1d6ba998a4fe44658fabbbf811d2ffc9f8c0d75ca9c60a7dd20b7453afc1a3c5a7c1fe9455e58613fea4d5114f9b8892d41d3b886bd08471bf216e877ad7f95e')

build() {
  cd ${pkgname//-/_}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${pkgname//-/_}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
