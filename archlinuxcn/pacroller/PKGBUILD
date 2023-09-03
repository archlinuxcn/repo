# Maintainer: Jerry <isjerryxiao at outlook dot com>
_srcname=pacroller
pkgname=pacroller
pkgver=0.1.8
pkgrel=1
pkgdesc="Unattended upgrade for archlinux"
arch=('any')
url="https://github.com/isjerryxiao/pacroller"
license=('GPL3')
depends=('python')
makedepends=('python-setuptools' 'git')
optdepends=('needrestart')
backup=('etc/pacroller/config.json' 'etc/pacroller/smtp.json' 'etc/pacroller/telegram.json' 'etc/pacroller/known_output_override.py')
source=("$_srcname::git+https://github.com/isjerryxiao/pacroller#tag=${pkgver}")
md5sums=('SKIP')

package() {
    cd "$srcdir/$_srcname"
    python setup.py install --root="$pkgdir/" --optimize=1
    install -Dm644 "src/$_srcname/config.json" "$pkgdir/etc/pacroller/config.json"
    install -Dm600 "src/$_srcname/smtp.json" "$pkgdir/etc/pacroller/smtp.json"
    install -Dm600 "src/$_srcname/telegram.json" "$pkgdir/etc/pacroller/telegram.json"
    install -Dm644 "src/$_srcname/known_output_override.py" -t "$pkgdir/etc/pacroller"
    mkdir -p "$pkgdir/var/lib/pacroller"
    install -Dm644 "pacroller.service" "${pkgdir}/usr/lib/systemd/system/pacroller.service"
    install -Dm644 "pacroller.timer" "${pkgdir}/usr/lib/systemd/system/pacroller.timer"
}
