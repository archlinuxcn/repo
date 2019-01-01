# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>

pkgname=fop-hyph
pkgver=2.2
pkgrel=1
pkgdesc="The hyphenation pattern files compiled for FOP"
arch=('any')
url="http://offo.sourceforge.net/"
license=('unknown')
depends=('java-runtime' 'fop>=1.0')
source=("http://sourceforge.net/projects/offo/files/offo-hyphenation/2.2/offo-hyphenation-compiled.zip")
md5sums=('5ec09cce6d8a09bc53a6441790021ecf')

package() {
	cd "${srcdir}/offo-hyphenation-compiled/"
	install -Dm644 "${pkgname}.jar" "${pkgdir}/usr/share/java/${pkgname}/${pkgname}.jar"
}

# vim:set ts=2 sw=2 et:
