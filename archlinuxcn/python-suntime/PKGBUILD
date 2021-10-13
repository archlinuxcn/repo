# Maintainer: Blazej Sewera <blazejok1[at]wp.pl>

pkgname=python-suntime
_module="suntime"
pkgver=1.2.5
pkgrel=1
pkgdesc="Simple sunset and sunrise time calculation python library"
url="https://github.com/SatAgro/suntime"
depends=("python" "python-six" "python-dateutil")
makedepends=("python-setuptools")
license=("LGPL3")
arch=("any")
source=("https://files.pythonhosted.org/packages/source/${_module::1}/$_module/$_module-$pkgver.tar.gz")
sha256sums=("e4df651dfcde332f905e57da6be49a1cc696499f11853fb0395df29104274649")

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
