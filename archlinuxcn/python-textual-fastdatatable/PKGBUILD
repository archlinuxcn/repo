# Maintainer: AlphaJack <alphajack at tuta dot io>

pkgname="python-textual-fastdatatable"
_name="${pkgname#python-}"
pkgver=0.19.5
pkgrel=1
pkgdesc="A performance-focused reimplementation of Textual's DataTable widget"
arch=(any)
license=(MIT)
url="https://github.com/tconbeer/textual-fastdatatable"
depends=(python python-pyarrow python-pytz python-textual python-typing_extensions)
makedepends=(python-build python-installer python-hatchling python-setuptools python-wheel)
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name/-/_}-${pkgver}.tar.gz")
sha256sums=('5e6140e13f6a18d6ea827d1e97e9cb8be12253fad4ad58e14afd6dab966c35bc')

build(){
 cd "textual_fastdatatable-$pkgver"
 python -m build --wheel --no-isolation
}

package(){
 cd "textual_fastdatatable-$pkgver"
 python -m installer --destdir="$pkgdir" dist/*.whl
}

# vim: set ts=2 sw=2 et:
