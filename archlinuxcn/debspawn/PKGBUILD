# Maintainer: weilinfox <sakurakaze.fox at gmail.com>

pkgname=debspawn
pkgver=0.6.5
pkgrel=1
pkgdesc='Debspawn is a tool to build Debian packages in an isolated environment, using systemd-nspawn containers'
arch=('any')
url="https://github.com/lkhq/debspawn"
license=('LGPL-3.0-only')
depends=(
  'debootstrap'
  'dpkg'
  'python'
  'python-tomlkit'
  'zstd'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-setuptools'
  'python-wheel'
)
source=("https://github.com/lkhq/debspawn/archive/refs/tags/v$pkgver.tar.gz")
sha512sums=('03dbc3681ded6ccd5d31a4632a8aec34a75baee039a6a683872e21eda40b4a88507b44fa5f695f1228389356f5e490c22dde72e65d9b643c17bfb814cc5d7dcf')

build() {
	cd "$pkgname-$pkgver"
	python -m build --wheel --skip-dependency-check --no-isolation
	# All of the tests need superuser permissions
}

package() {
	cd "$pkgname-$pkgver"
	python -m installer --destdir="$pkgdir" dist/*.whl
}

