# Maintainer: Dave Brown <d.brown@bigdavedev.com>
# Contributor: theblazehen <com.theblazehen@post - reverse>
pkgname=xinit-xsession
pkgver=1
pkgrel=3
pkgdesc="Allows ~/.xinitrc to be run as a session from your display manager"
arch=('any')
license=("GPL3")
provides=('xinit-xsession')
depends=('bash')
source=('xinitrcsession-helper' 'xinitrc.desktop')
sha1sums=('0b3ee35032ba0cef758d61154c1bfbb858b8827c'
          '9665e18bd24aca0afd9d46d3c9200893fd12a391')

package() {
        install -d -m 755 ${pkgdir}/usr/bin
        cp xinitrcsession-helper ${pkgdir}/usr/bin/
        install -d ${pkgdir}/usr/share/xsessions
        cp xinitrc.desktop ${pkgdir}/usr/share/xsessions/
}
