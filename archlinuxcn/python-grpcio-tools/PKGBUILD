# Maintainer: Alexander Fasching <fasching.a91@gmail.com>
# Contributor: brent s. <bts[at]square-r00t[dot]net>
# Bugreports can be filed at https://github.com/alexf91/AUR-PKGBUILDs

pkgname='python-grpcio-tools'
pkgver=1.27.2
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
sha512sums=('1e4f6f1daaf8bd6ca08419e8810e28c5d959634b47202f1932e530590ddb33c3e49c73edfd67e95dace7c4e8735372d3b0ffaa3686cb4a539d6205fa5d4ab24d')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}

# vim:set sw=2 et:
