# Maintainer: Tomislav Ivek <tomislav.ivek@gmail.com>

pkgname=('conan')
pkgver=2.1.0
pkgrel=1
pkgdesc="A distributed, open source, C/C++ package manager."
arch=('any')
url="https://conan.io"
license=('MIT')
makedepends=('python-setuptools' 'patch')
depends=('sqlite'
         'python-requests>=2.25'
         'python-urllib3>=1.26.6'
         'python-colorama>=0.4.3'
         'python-yaml>=6.0'
         'python-patch-ng>=1.17.4'
         'python-fasteners>=0.15'
         'python-distro>=1.4.0'
         'python-jinja>=3.0'
         'python-dateutil>=2.8.0'
         'python-bottle>=0.12.8'
         'python-pluginbase>=0.5'
         'python-pyjwt>=2.4.0')
conflicts=('conan1')

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/conan-io/conan/archive/${pkgver}.tar.gz")

prepare() {
  cd $pkgname-$pkgver
  # Remove maximum version constraints
  sed -i -r 's|(.*),.*|\1|g' conans/requirements.txt
  sed -i -r 's|(.*),.*|\1|g' conans/requirements_server.txt
  sed -i -r 's|(.*),.*|\1|g' conans/requirements_dev.txt  
 }

build() {
  cd "$srcdir/conan-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/conan-$pkgver"
  python setup.py install --optimize=1 --root=${pkgdir}
  install -m755 -d "${pkgdir}/usr/share/licenses/conan"
  install -m644 LICENSE.md "${pkgdir}/usr/share/licenses/conan/"
  install -m755 -d "${pkgdir}/usr/share/doc/conan"
  install -m644 contributors.txt "${pkgdir}/usr/share/doc/conan/"
}
md5sums=('ec244a1ff81f35748c6490aa150b0a21')
