# Maintainer: FirstAirBender <noblechuk5[at]web[dot]de>
# Contributor: Tomislav Ivek <tomislav.ivek@gmail.com>

pkgname=('conan')
pkgver=2.6.0
pkgrel=1
pkgdesc="A distributed, open source, C/C++ package manager."
arch=('any')
url="https://conan.io"
license=('MIT')
makedepends=('python-setuptools' 'python-build' 'python-installer' 'python-wheel' 'patch')
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
provides=("conan")

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/conan-io/conan/archive/${pkgver}.tar.gz")

prepare() {
  cd $pkgname-$pkgver
  # Remove maximum version constraints
  sed -i -r 's|(.*),.*|\1|g' conans/requirements.txt
  sed -i -r 's|(.*),.*|\1|g' conans/requirements_server.txt
  sed -i -r 's|(.*),.*|\1|g' conans/requirements_dev.txt  
 }

build() {
  cd $pkgname-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd $pkgname-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -m755 -d "${pkgdir}/usr/share/licenses/conan"
  install -m644 LICENSE.md "${pkgdir}/usr/share/licenses/conan/"
  install -m755 -d "${pkgdir}/usr/share/doc/conan"
  install -m644 contributors.txt "${pkgdir}/usr/share/doc/conan/"
}
md5sums=('7ba65fa6446f38fcc97025c3c2268dcb')
