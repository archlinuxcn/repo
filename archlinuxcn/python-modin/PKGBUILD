# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=modin
pkgname=python-modin
pkgver=0.30.1
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
sha512sums=('9e49a4895dd25462261ef6e2e507e434cd015ad422367c6e7988dea0b08e506cc89d203314c3a586472fa38d71a5fdc60bc979a1fe17f8e8dfccc31d8df9e9ac')

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
