# Maintainer: Caleb Maclennan <caleb@alerque.com>

_pyname=ttfautohint-py
pkgname=python-$_pyname
pkgver=0.5.1
pkgrel=1
pkgdesc='Python wrapper for ttfautohint, a free auto-hinter for TrueType fonts'
url="https://github.com/fonttools/$_pyname"
arch=(x86_64)
license=(MIT)
depends=(python)
makedepends=(python-pip)
_py=py2.py3
_wheel="${_pyname/-/_}-$pkgver-$_py-none-manylinux_2_17_$CARCH.manylinux2014_$CARCH.whl"
source=("https://files.pythonhosted.org/packages/$_py/${_pyname::1}/$_pyname/$_wheel")
sha256sums=('5c65fe2fd3ee16d68201169c72413e70130d9f9d0b92589f9122d9f72a98d093')

package() {
	export PIP_CONFIG_FILE=/dev/null
	pip install --isolated --root="$pkgdir" --ignore-installed --no-deps $_wheel
	python -O -m compileall "$pkgdir"
}
