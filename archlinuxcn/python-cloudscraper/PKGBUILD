# Maintainer: Mufeed Ali <lastweakness@tuta.io>
# Based on the git package by Manuel Palenzuela

pkgname=python-cloudscraper
_author=VeNoMouS
_gitname=cloudscraper
pkgver=1.2.48
pkgrel=1
pkgdesc='A Python module to bypass Cloudflare anti-bot page. (Release version)'
url='https://pypi.org/project/cloudscraper'
arch=('any')
license=('MIT')
depends=(
  python
  python-requests
  python-js2py
  python-requests-toolbelt
)
optdepends=('nodejs: use Node.js Javascript Interpreter/Engine')
makedepends=('git' 'python-setuptools')
provides=('python-cloudscraper')

source=("$_gitname-$pkgver.tar.gz::https://files.pythonhosted.org/packages/9a/2c/2139cdd276f54d0dbf6397950e65b53f617082cde7832c47b4afea327e4d/$_gitname-$pkgver.tar.gz")
sha256sums=('bb6be1c2d12720c9fcde80f1965a2250444821f64a900e5bddf9aef2c1fa5d62')

package() {
  cd "$_gitname-$pkgver"
  python setup.py install --root=$pkgdir
}
