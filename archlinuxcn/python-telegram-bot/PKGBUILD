# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Sherlock Holo <sherlockya@gmail.com>
# Contributor: Sean Enck <enckse@gmail.com>
# Contributor: NeoTheFox <soniczerops@gmail.com>

pkgname=python-telegram-bot
pkgver=21.1.1
pkgrel=2
pkgdesc="A library that provides a Python interface to the Telegram Bot API"
url="https://github.com/${pkgname}/${pkgname}"
license=(GPL-3.0-or-later LGPL-3.0-or-later)
arch=(any)
depends=(python-httpx)
makedepends=(python-build python-installer python-setuptools python-wheel)
# checkdepends=(python-pytest-asyncio python-pytest-timeout python-flaky python-beautifulsoup4)
optdepends=('python-cryptography: for support cryptography library'
  'python-aiolimiter: for rate limiter'
  'python-tornado: for webhooks support'
  'python-cachetools: for use a variant of LRUCache'
  'python-apscheduler: for job queue support'
  'python-pytz: for job queue support')
source=(${url}/releases/download/v${pkgver}/${pkgname}-${pkgver}.tar.gz{,.asc})
validpgpkeys=('4CBA518847044E289548BD9FA2B984A9073022B2') # Hinrich Mahler (Key for signing releases of python-telegram-bot <22366557+Bibo-Joshi@users.noreply.github.com>
sha512sums=('f360f2fc0a9361cbb43a44e8ed5bddc0875707ce5b6dcacec65ab59434738007f6bcfe23137ff2650e96666870e3a52091aca92487846591e645e4acde2b759a'
            'SKIP')

build() {
  cd ${pkgname}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${pkgname}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
