# Maintainer: Lars Hagström <lars@foldspace.nu>
pkgname=s-tui
pkgver=0.8.3
pkgrel=1
pkgdesc="Terminal UI stress test and monitoring tool "
arch=('any')
url="https://github.com/amanusk/s-tui"
license=('GPL2')
groups=()
depends=('stress' 'python' 'python-urwid' 'python-psutil' 'python-setuptools')
options=(!emptydirs)
install=
source=("$url/archive/v$pkgver.tar.gz")
sha1sums=('07882feedfbf4a709128c2f004e452c947379dda')
conflicts=("s-tui-git")


package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}
