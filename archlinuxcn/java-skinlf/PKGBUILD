# Contributor: Victor Dmitriyev <mrvvitek@gmail.com>
# Maintainer: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Simon Lipp <sloonz+aur@gmail.com>

pkgname=java-skinlf
pkgver=6.7
pkgrel=5
pkgdesc="Skinning engine for Swing"
arch=('any')
url="http://l2fprod.com/skinlf/"
license=(APACHE)
depends=('java-runtime')
#source=('https://skinlf.dev.java.net/files/documents/66/37801/skinlf-6.7-20060722.zip')
# ftp.archlinux.org -> sources.archlinux.org
source=('https://sources.archlinux.org/other/community/java-skinlf/skinlf-6.7-20060722.zip')
md5sums=('09b41b511b51e465a052483b598d68f3')

package() {
  install -D --mode=644 $srcdir/skinlf-6.7/lib/skinlf.jar $pkgdir/usr/share/java/skinlf/skinlf.jar
  install -D --mode=644 $srcdir/skinlf-6.7/lib/nativeskin.jar $pkgdir/usr/share/java/skinlf/nativeskin.jar
}
