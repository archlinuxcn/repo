# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Sherlock Holo <sherlockya@gmail.com>
# Contributor: Sean Enck <enckse@gmail.com>
# Contributor: NeoTheFox <soniczerops@gmail.com>
pkgname=python-telegram-bot
pkgver=22.0
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
sha512sums=('9acc9e36f868a99da285ca170260ebf8db6c4532dcad8c1d3553b10679bf7cb7e013e7049da0f7df85a6533bd78e3977bb8e6a7afe6098c4c18f899dfd74be76')

build() {
  cd ${pkgname//-/_}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${pkgname//-/_}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
