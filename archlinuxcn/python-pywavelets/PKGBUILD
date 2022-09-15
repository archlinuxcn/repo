# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Francois Boulogne <fboulogne at april dot org>
_base=pywavelets
pkgname=python-${_base}
pkgver=1.4.0
pkgrel=1
pkgdesc="Wavelet transform module"
arch=(x86_64)
url="https://github.com/${_base}/${_base::3}t"
license=(MIT)
depends=(python-numpy)
makedepends=(python-setuptools cython)
# checkdepends=(python-pytest python-matplotlib)
source=(${url}/archive/v${pkgver}.tar.gz)
sha512sums=('41f6d6751daf8b287b345cece45583a153c44be3d478f0cfe9788a5199d19fb9959919cb498443e0a18d9f0bdeef9dc809d364e13929b2b1f28d5c78990dbfcb')

build() {
  cd ${_base::3}t-${pkgver}
  python setup.py build
}

# check() {
#   cd ${_base::3}t-${pkgver}
#   python setup.py install --root="${srcdir}/tmp_install" --optimize=1 --skip-build
#   cd ${srcdir}
#   MPLBACKEND=Agg PYTHONPATH="${srcdir}/tmp_install/$(python -c "import site; print(site.getsitepackages()[0])")/${_base::3}t:${PYTHONPATH}" python -m pytest ${_base::3}t-${pkgver}/${_base::3}t/tests
# }

package() {
  cd ${_base::3}t-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
