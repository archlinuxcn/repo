# Maintainer: weilinfox <sakurakaze.fox at gmail.com>

pkgname=debspawn
pkgver=0.6.4
pkgrel=5
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
sha512sums=('a60a8c98f89342368209ffdb07bd40efbe83ceedb3896972bee8984f24a792885431d127de68c05bb4e2abfaf43f764943a096e47fcf29a01bffdde7a70ce14f')

build() {
	cd "$pkgname-$pkgver"
	python -m build --wheel --skip-dependency-check --no-isolation
	# All of the tests need superuser permissions
}

package() {
	cd "$pkgname-$pkgver"
	python -m installer --destdir="$pkgdir" dist/*.whl
}

