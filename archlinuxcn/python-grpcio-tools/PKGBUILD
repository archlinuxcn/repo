# Maintainer: Alexander Fasching <fasching.a91@gmail.com>
# Contributor: brent s. <bts[at]square-r00t[dot]net>
# Bugreports can be filed at https://github.com/alexf91/AUR-PKGBUILDs

pkgname='python-grpcio-tools'
pkgver=1.27.1
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
sha512sums=('b4e681ea2e635df74d2087f992b84a8069eab70ee9538d0e0463d391d307db5440197662d64d331fdac18ece324976a0e228a53082b4582d46a137b3e806aaa3')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}

# vim:set sw=2 et:
