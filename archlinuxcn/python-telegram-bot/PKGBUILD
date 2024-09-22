# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Sherlock Holo <sherlockya@gmail.com>
# Contributor: Sean Enck <enckse@gmail.com>
# Contributor: NeoTheFox <soniczerops@gmail.com>
pkgname=python-telegram-bot
pkgver=21.6
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
sha512sums=('ded73d3166ccabab52961f91b3599841931c40b51e3aeda05603deb1a0aec9a30cab8c31ae1dd92c85c5f90a23bd5e84dc8b063941446f28f748033f7c5f13f1')

build() {
  cd ${pkgname//-/_}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${pkgname//-/_}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
