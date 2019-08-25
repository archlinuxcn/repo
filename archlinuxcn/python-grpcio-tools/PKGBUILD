# Maintainer: Alexander Fasching <fasching.a91@gmail.com>
# Contributor: brent s. <bts[at]square-r00t[dot]net>
# Bugreports can be filed at https://github.com/alexf91/AUR-PKGBUILDs

pkgname='python-grpcio-tools'
pkgver=1.23.0
pkgrel=1
pkgdesc="Python protobuf generator for GRPC"
arch=('x86_64' 'i686')
url="https://grpc.io/"
license=('Apache' )
_pkgname=grpcio-tools
install=
changelog=
noextract=()
depends=('python' 'python-grpcio' 'python-protobuf')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/g/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha512sums=('306e1de073bffd036643dee6fdaf8c2f48cf810fc4403b02a5b2aa44ba77d8c985181b23ec20d787261786b1c6e4930f8e5a253752da95beeb257ff0555175cb')

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1
}
