# Maintainer: Michael Bromilow <dev at mail subdomain of bromilow dot uk>
# Contributor: Tércio Martins <echo dGVyY2lvd2VuZGVsQGdtYWlsLmNvbQo= | base64 -d>

_pkgname=rectangle-packer
pkgname=python-${_pkgname}-git
pkgver=2.0.2.r16.g46fa636
pkgrel=1
pkgdesc="Pack a set of rectangles into a bounding box with minimum area"
arch=('i686' 'pentium4' 'x86_64')
url="https://github.com/Penlect/rectangle-packer"
license=('MIT')
depends=('python')
makedepends=('git' 'cython' 'python-build' 'python-installer' 'python-setuptools')
provides=('python-rectangle-packer')
conflicts=('python-rectangle-packer')
source=("${_pkgname}::git+${url}.git")
sha512sums=('SKIP')

pkgver() {
  cd "${srcdir}/${_pkgname}"
  git describe --long --abbrev=7 | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd "${srcdir}/${_pkgname}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${_pkgname}"
  python -m installer --destdir="${pkgdir}" dist/*.whl

  install -Dm 644 "LICENSE.md" \
                  "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md"
}
