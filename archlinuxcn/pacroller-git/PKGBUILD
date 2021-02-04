# Maintainer: Jerry <isjerryxiao at outlook dot com>
_srcname=pacroller
pkgname=pacroller-git
pkgver=0.0.5.2.g7c67531
pkgrel=2
pkgdesc="Unattended upgrade for archlinux"
arch=('any')
url="https://github.com/isjerryxiao/pacroller"
license=('GPL3')
depends=('python' 'pyalpm')
makedepends=('git')
provides=("pacroller")
conflicts=("pacroller")
backup=('etc/pacroller/config.json')
source=("$_srcname::git+https://github.com/isjerryxiao/pacroller.git")
md5sums=('SKIP')

pkgver() {
    cd "$srcdir/$_srcname"
    git describe --tags | sed 's/^v//;s/-/./g'
}

package() {
    cd "$srcdir/$_srcname"
    python setup.py install --root="$pkgdir/" --optimize=1
    install -Dm644 "src/$_srcname/config.json.example" "$pkgdir/etc/pacroller/config.json"
    mkdir -p "$pkgdir/var/lib/pacroller"
    install -Dm644 "pacroller.service" "${pkgdir}/usr/lib/systemd/system/pacroller.service"
    install -Dm644 "pacroller.timer" "${pkgdir}/usr/lib/systemd/system/pacroller.timer"
}
