# Maintainer: FadeMind <fademind@gmail.com>
# Contributor: Thomas Mudrunka <harvie@@email..cz>
# Contributor: Thomas Mudrunka <harvie@@email..cz>
# You can also contact me on http://blog.harvie.cz/

pkgname=figlet-fonts
pkgver=1.0 #23.03.2014
pkgrel=3
pkgdesc="Additional asciiart fonts for figlet"
arch=('any')
license=('GPL')
url="http://www.figlet.org/fontdb.cgi"
depends=('figlet')
optdepends=('jave: create cool ascii-art and figlets')
source=("ours.tar.gz::ftp://ftp.figlet.org/pub/figlet/fonts/ours.tar.gz"
	"contributed.tar.gz::ftp://ftp.figlet.org/pub/figlet/fonts/contributed.tar.gz"
	"international.tar.gz::ftp://ftp.figlet.org/pub/figlet/fonts/international.tar.gz"
	"ms-dos.tar.gz::ftp://ftp.figlet.org/pub/figlet/fonts/ms-dos.tar.gz"
	'figlet-gallery')
sha256sums=('10184c883faa63e91c8c7d99f100fe2f76195221ff8863d29c1beef88f666e69'
            '2c569e052e638b28e4205023ae717f7b07e05695b728e4c80f4ce700354b18c8'
            'e6493f51c96f8671c29ab879a533c50b31ade681acfb59e50bae6b765e70c65a'
            'd3678a98b3b058ae4ded8525f51a1c53b3c6e6833793cf7cf98fcd9550ed7e70'
            '0021d92bfea79921402425feb014289520e604b7f9f1a3838df994facde0f9ec')
         
package() {
	msg 'Copying figlet fonts...'
	install -dm755 ${pkgdir}/usr/share/figlet/fonts/
	find ${srcdir} | grep -i flf$ | while read font; do
        msg2 "${font##*/}";
        cp -f "$font" ${pkgdir}/usr/share/figlet/fonts/
	done;

	msg 'Removing figlets which are already in official distribution...'
	ls -1 ${srcdir}/ours/ | while read i; do
	rm -rf "$pkgdir/usr/share/figlet/fonts/$i";
	done;

	msg 'Installing figlet-gallery script...'
	install -Dm755 ${srcdir}/figlet-gallery ${pkgdir}/usr/bin/figlet-gallery
	find ${pkgdir}/usr/share/figlet/fonts -type f -exec chmod 644 {} \;
        find ${pkgdir}/usr/share/figlet/fonts -type d -exec chmod 755 {} \;
}
