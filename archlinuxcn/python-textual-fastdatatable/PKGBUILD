# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="python-textual-fastdatatable"
_name="${pkgname#python-}"
pkgver=0.19.2
pkgrel=1
pkgdesc="A performance-focused reimplementation of Textual's DataTable widget"
arch=(any)
license=(MIT)
url="https://github.com/tconbeer/textual-fastdatatable"
depends=(python python-pyarrow python-pytz python-textual python-typing_extensions)
makedepends=(python-build python-installer python-hatchling python-setuptools python-wheel)
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name/-/_}-${pkgver}.tar.gz")
sha256sums=('97a692d4d02551b8d311758b8a9fb6e755a445dc457ac37633c981f74baa1441')

build(){
 cd "textual_fastdatatable-$pkgver"
 python -m build --wheel --no-isolation
}

package(){
 cd "textual_fastdatatable-$pkgver"
 python -m installer --destdir="$pkgdir" dist/*.whl
}

# vim: set ts=2 sw=2 et:
