# Maintainer: Silvio Knizek <killermoehre@gmx.net>
pkgname=reflector-timer
pkgver=9
pkgrel=1
pkgdesc='A service and timer for the reflector mirrorlist upgrade.'
arch=('any')
url='http://xyne.archlinux.ca/projects/reflector/'
license=('GPL')
depends=('reflector' 'systemd')
backup=('etc/conf.d/reflector.conf')
source=('reflector.service'
        'reflector.timer'
        'reflector.conf')
md5sums=('642fe54d10c585ef0b15f3b4431f3b53'
         '5c66e6429a94bd46d164fbdd0f30dbd9'
         '49bcaf54be9aede73c5e1523f6594e4b')

package() {
    install -D -m 644 'reflector.service' "$pkgdir/usr/lib/systemd/system/reflector.service"
    install -D -m 644 'reflector.timer' "$pkgdir/usr/lib/systemd/system/reflector.timer"
    install -D -m 644 'reflector.conf' "$pkgdir/usr/share/reflector-timer/reflector.conf"
}
