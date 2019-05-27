# Maintainer: brent s. <bts[at]square-r00t[dot]net>
validpgpkeys=('748231EBCBD808A14F5E85D28C004C2F93481F6B')
# Bug reports can be filed at https://bugs.square-r00t.net/index.php?project=3
# News updates for packages can be followed at https://devblog.square-r00t.net
pkgname=('python-grpcio-tools' 'python2-grpcio-tools')
pkgver=1.20.0
pkgrel=1
pkgdesc="Python protobuf generator for GRPC"
arch=('any')
url="https://grpc.io/"
license=('Apache' )
_pkgname=grpcio-tools
install=
changelog=
noextract=()
makedepends=('python-setuptools' 'python2-setuptools')
source=("https://files.pythonhosted.org/packages/source/g/${_pkgname}/${_pkgname}-${pkgver}.tar.gz"
        "${_pkgname}-${pkgver}.tar.gz.sig")
sha512sums=('b03b442fa5dc239919423e7eed5d6865924a4bc9369defc688b5ce72eb2b00580f9fb7a52a8a05cb255aee03000e9379dd7e8dae4a441811622e015d25792c0c'
            'SKIP')

package_python-grpcio-tools() {
  depends=('python' 'python-grpcio' 'python-protobuf')

  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1
}

package_python2-grpcio-tools() {
  depends=('python2' 'python2-grpcio' 'python2-protobuf')

  cd "${srcdir}/${_pkgname}-${pkgver}"
  python2 setup.py install --root="${pkgdir}" --optimize=1
}
