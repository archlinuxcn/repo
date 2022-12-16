# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=torchdata
_py=cp310
pkgname=python-torchdata
pkgver=0.5.1
pkgrel=1
pkgdesc='A PyTorch repo for data loading and utilities to be shared by the PyTorch domain libraries'
arch=('x86_64')
url='https://github.com/pytorch/data'
license=('BSD')
depends=(
  python-portalocker
  python-pytorch
  python-requests
  python-urllib3
)
makedepends=(
  python-installer
)
source=("https://files.pythonhosted.org/packages/${_py}/${_pkgname::1}/${_pkgname}/${_pkgname//-/_}-${pkgver}-${_py}-${_py}-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"
        "https://github.com/pytorch/data/raw/main/LICENSE"
)
sha512sums=('d93b7de0a8f283439d18739da8c3959419add073b1292e1ed9bd67ff0635547c8d1757657c643a1ec2757dab00c1e95cc5575ca1c0a6b783bc15ab13c131ddbb'
            '2d437cc8226bf32ddcf8e12f2583c5777afd3d9932b6b97a65f8fcf3d115a64749ebf37737fa9a69cea01e59649ba49b011ab219d1636ad970e79613a406f837')

package() {
  python -m installer --destdir="${pkgdir}" *.whl
  install -Dm644 "${srcdir}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
