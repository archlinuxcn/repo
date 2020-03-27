# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-torchgan-git
pkgver=0.0.4.r3.g1e3816e
pkgrel=1
pkgdesc="Research Framework for easy and efficient training of GANs based on PyTorch"
arch=(any)
url="https://github.com/torchgan/torchgan"
license=('MIT')
depends=(
  'python-numpy'
  'python-pillow'
  'python-fastprogress'
  'python-pytorch'
  'python-torchvision'
)
makedepends=(
  'git'
  'python-setuptools'
)
checkdepends=(
  'python-pytest'
)
provides=(python-torchgan=${pkgver})
conflicts=(python-torchgan)
source=("${pkgname}::git+https://github.com/torchgan/torchgan.git")
sha512sums=('SKIP')

get_pyver () {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

pkgver() {
  cd "${pkgname}"
  git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
	cd "${srcdir}/${pkgname}"
	python setup.py build
}

check() {
  cd "${srcdir}/${pkgname}"
  PYTHONPATH="${PWD}/build/lib pytest -v"
}

package() {
	cd "${srcdir}/${pkgname}"
	python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
 	install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  # delete tests folder as they're installed in wrong place
  rm -rfv "${pkgdir}/usr/lib/python$(get_pyver)/site-packages/tests"
}
# vim:set ts=2 sw=2 et:
