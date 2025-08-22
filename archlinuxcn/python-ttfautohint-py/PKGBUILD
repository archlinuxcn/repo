# Maintainer: Caleb Maclennan <caleb@alerque.com>

_pyname=ttfautohint-py
pkgname=python-$_pyname
pkgver=0.6.0
pkgrel=1
pkgdesc='Python wrapper for ttfautohint, a free auto-hinter for TrueType fonts'
url="https://github.com/fonttools/$_pyname"
arch=(x86_64)
license=(MIT)
depends=(python python-setuptools)
makedepends=(python-installer)
_py=py3
_wheel="${_pyname/-/_}-$pkgver-$_py-none-manylinux2014_$CARCH.manylinux_2_17_$CARCH.whl"
source=("https://files.pythonhosted.org/packages/$_py/${_pyname::1}/$_pyname/$_wheel")
sha256sums=('7773f7bedcc71b53db1b0cd13749f6ccde888874254488d7a4b511a4c3674db9')

package() {
	python -m installer --destdir="$pkgdir" $_wheel
	python -O -m compileall "$pkgdir"
}
