# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=modin
pkgname=python-modin
pkgver=0.35.0
pkgrel=1
pkgdesc='Speed up your Pandas workflows by changing a single line of code'
arch=('any')
url='https://github.com/modin-project/modin'
license=('Apache-2.0')
depends=(
  python-boto3
  python-botocore
  python-cloudpickle
  python-dask
  python-distributed
  python-fsspec
  python-numpy
  python-pandas
  python-psutil
  python-pytz
  python-rpyc
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/modin-project/modin/archive/${pkgver}.tar.gz")
sha512sums=('aca05ab14f00d030bc43fbb3385f1d94e049adeb9cc71523781b3a9d8d42d867a902ecdca312db01580f1ae61170a0f353dbc294a858dd0302cd373a1b439ff1')

prepare() {
  sed -i "s,SafeConfigParser,ConfigParser," "${srcdir}/${_pkgname}-${pkgver}/versioneer.py"
  sed -i "s,readfp,read_file," "${srcdir}/${_pkgname}-${pkgver}/versioneer.py"
}

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rfv "${pkgdir}${site_packages}/modin/tests"
}
# vim:set ts=2 sw=2 et:
