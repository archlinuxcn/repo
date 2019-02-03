# Maintainer: Lars HagstrÃ¶m <lars@foldspace.nu>
pkgname=s-tui
pkgver=0.8.2
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
sha1sums=('a2d5234f4cd4cf21cde0ea9283d9a91a84f7b77b')
conflicts=("s-tui-git")


package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}
