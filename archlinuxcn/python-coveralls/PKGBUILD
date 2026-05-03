# Maintainer: Jax Young <jaxvanyang@gmail.com>
# Contributor: Luis Martinez <luis dot martinez at disroot dot org>
# Contributor: GI_Jack <GI_Jack@hackermail.com>

pkgname=python-coveralls
_pkg="${pkgname#python-}"
_repo="$_pkg-python"
pkgver=4.0.1
pkgrel=1
pkgdesc="Python integration with coveralls.io"
url="https://github.com/thekevjames/coveralls-python"
arch=('any')
license=('MIT')
depends=('python-coverage' 'python-docopt' 'python-requests')
optdepends=('python-yaml')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-poetry-core')
checkdepends=('git' 'python-pytest' 'python-responses')
source=("$_repo-$pkgver.tar.gz::https://github.com/TheKevJames/$_repo/archive/refs/tags/$pkgver.tar.gz")
sha256sums=('066f5e775359dda1c8e4b152f49ce6e2ea1f1e36738c08333af1bb3abc697bf5')

build() {
	cd "$_repo-$pkgver"
	python -m build --wheel --no-isolation
}

check() {
	cd "$_repo-$pkgver"
	# Coveralls tries to get itself's package metadata in code, so we have to
	# install it to import it for testing.
	rm -rf install && python -m installer --destdir=install dist/*.whl
	local python_version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
	PYTHONPATH="$PWD/install/usr/lib/python$python_version/site-packages" pytest
}

package() {
	cd "$_repo-$pkgver"
	python -m installer --destdir="$pkgdir" dist/*.whl
	local site=$(python -c 'import site; print(site.getsitepackages()[0])')
	install -d "$pkgdir/usr/share/licenses/$pkgname/"
	ln -s "$site/$_pkg-$pkgver.dist-info/LICENSE.rst" "$pkgdir/usr/share/licenses/$pkgname/"
}
