# Maintainer: Jingbei Li <i@jingbei.li>

pkgname=python-gcp-git
pkgver=0.1.4.r1.g36b2e13
pkgrel=1
pkgdesc="gcp is a file copy tool, freely inspired from cp, but with a few high-level functionnality."
arch=("any")
url="http://github.com/petronny/gcp"
license=('GPL3')
depends=('python' 'python-gobject2' 'python-dbus' 'dbus-glib')
source=("$pkgname::git+$url")
makedepends=('python-setuptools')
optdepends=('python-progressbar')
md5sums=('SKIP')

pkgver() {
	cd "${pkgname}"
	git describe --long --tags 2>/dev/null| sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd "$srcdir/$pkgname"
  python setup.py build
}

package() {
  cd "$srcdir/$pkgname"
  python setup.py install --root=/$pkgdir/ --optimize=1
}
