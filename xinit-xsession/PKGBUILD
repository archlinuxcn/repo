#Maintainer: theblazehen <com.theblazehen@post - reverse>
pkgname=xinit-xsession
pkgver=1
pkgrel=1
pkgdesc="Allows ~/.xinitrc to be run as a session from your display manager"
arch=('any')
licence=("unknown")
provides=('xinit-xsession')
source=('xinitrcsession-helper' 'xinitrc.desktop')
md5sums=('SKIP' 'SKIP')

package() {
        install -d -m 755 ${pkgdir}/usr/bin
        cp xinitrcsession-helper ${pkgdir}/usr/bin/
        install -d ${pkgdir}/usr/share/xsessions
        cp xinitrc.desktop ${pkgdir}/usr/share/xsessions/
}
