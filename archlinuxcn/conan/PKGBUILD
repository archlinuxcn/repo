# Maintainer: Tomislav Ivek <tomislav.ivek@gmail.com>

pkgname=('conan')
pkgver=1.43.2
pkgrel=1
pkgdesc="A distributed, open source, C/C++ package manager."
arch=('any')
url="https://conan.io"
license=('MIT')
makedepends=('python-setuptools' 'patch')
depends=('python-pyjwt>=1.4.0'
         'python-requests>=2.25'
         'python-urllib3>=1.26.6'
         'python-colorama>=0.3.3'
         'python-yaml>=3.11'
         'python-patch-ng>=1.17.4'
         'python-fasteners>=0.14.1'
         'python-six>=1.10.0'
         'python-node-semver>=0.6.1'
         'python-distro>=1.0.2'
         'python-pygments>=2.0'
         'python-tqdm>=4.28.1'
         'python-jinja>=2.9'
         'python-dateutil>=2.7.0'
         'python-bottle>=0.12.8'
         'python-pluginbase>=0.5')

source=("https://github.com/conan-io/conan/archive/${pkgver}.tar.gz" "arch-reqs.patch")

prepare() {
  cd $pkgname-$pkgver
  patch -Np1 -i "${srcdir}/arch-reqs.patch"
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
md5sums=('02f51ca610abb85ec70bcb7f9d42aefd'
         'b47d49751ebacf9078e1d60c2b85991b')
