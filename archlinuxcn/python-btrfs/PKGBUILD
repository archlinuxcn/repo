# Maintainer: Timofey Titovets <nefelim4ag@gmail.com>

pkgname=python-btrfs
pkgver=11
pkgrel=1
pkgdesc="Python Btrfs"
arch=('any')
url="https://github.com/knorrie/python-btrfs"
license=('GPL2')
depends=('python')
makedepends=('git')
source=("$pkgname"::"git://github.com/knorrie/python-btrfs.git#tag=v${pkgver}")
md5sums=('SKIP')

package() {
    cd "$srcdir/${pkgname}/"
    python ./setup.py install --root="$pkgdir/" --prefix=/usr --optimize=1
}
