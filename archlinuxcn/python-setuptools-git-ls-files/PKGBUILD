# Maintainer: Caleb Maclennan <caleb@alerque.com>

pkgname=python-setuptools-git-ls-files
_pyname=${pkgname#python-}
pkgver=0.1.2
pkgrel=6
pkgdesc='A plugin for setuptools that finds all git tracked files, including submodules'
arch=(any)
url="https://github.com/anthrotype/${_pyname//-/_}"
license=(MIT)
depends=(python)
makedepends=(python-{build,installer,wheel}
             python-setuptools-scm)
_archive="${_pyname//-/_}-$pkgver"
source=("https://files.pythonhosted.org/packages/source/${_pyname::1}/$_pyname/$_archive.tar.gz")
sha256sums=('7d612087430dc912f0dca7a35c99bf791b2f86b7fa5a40c5a562192947c86efa')

build() {
	cd "$_archive"
	python -m build -wn
}

package() {
	cd "$_archive"
	python -m installer -d "$pkgdir" dist/*.whl
	install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE
}
