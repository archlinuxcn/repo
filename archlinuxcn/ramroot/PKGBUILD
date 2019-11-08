# Maintainer: Chris Magyar <c.magyar.ec@gmail.com>

pkgname=ramroot
pkgver=2.0.1
pkgrel=1
_gitrepo=ramroot
_gituser=arcmags
_gitver=2.0.1
pkgdesc="Load root file system to zram during boot"
arch=('x86_64')
url="https://github.com/$_gituser/$_gitrepo"
license=('GPL3')
conflicts=('liveroot')
depends=('mkinitcpio')
install=ramroot.install
source=("$pkgname-$pkgver.tar.gz::$url/archive/$_gitver.tar.gz"
    ramroot.install)
md5sums=('2204111b9f337f191d9d9d12282efff4'
    'cd9b4ef8c10a6eafead22453f8cf4ec0')

package() {
	cd "$pkgname-$pkgver"
    install -D -m644 usr/lib/initcpio/hooks/ramroot \
        "$pkgdir/usr/lib/initcpio/hooks/ramroot"
    install -D -m644 usr/lib/initcpio/install/ramroot \
        "$pkgdir/usr/lib/initcpio/install/ramroot"
    install -D -m644 usr/lib/ramroot/ramroot.conf \
        "$pkgdir/usr/lib/ramroot/ramroot.conf"
    install -D -m644 usr/lib/ramroot/ramroot.conf \
        "$pkgdir/etc/ramroot.conf"
    install -D -m644 usr/lib/ramroot/ramroot/etc/issue \
        "$pkgdir/etc/ramroot/etc/issue"
    install -D -m644 usr/share/man/man8/ramroot.8 \
        "$pkgdir/usr/share/man/man8/ramroot.8"
    install -D -m644 usr/share/man/man5/ramroot.conf.5 \
        "$pkgdir/usr/share/man/man5/ramroot.conf.5"
    install -D -m755 ramroot "$pkgdir/usr/bin/ramroot"
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/ramroot/LICENSE"
}
