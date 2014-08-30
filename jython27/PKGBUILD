# $Id: PKGBUILD 67407 2012-03-11 12:49:30Z cbrannon $
# Maintainer: mitsuse <mitsuset at gmail>
## Original ##
#### Maintainer: Chris Brannon <cmbrannon79@gmail.com>
#### Contributor: Geoffroy Carrier <geoffroy.carrier@aur.archlinux.org>
#### Contributor: Richard Murri <admin@richardmurri.com>
pkgname=jython27
pkgver=2.7b3
_pkgver=2.7-b3
pkgrel=1
pkgdesc="An implementation of the Python language written in Java"
arch=('any')
url="http://www.jython.org/"
license=('PSF' 'APACHE' 'custom')
depends=('java-environment' 'bash')
provides=("jython=$pkgver")
backup=('opt/jython27/registry')
options=('!emptydirs')
install='jython.install'
source=(http://search.maven.org/remotecontent?filepath=org/python/jython-installer/$_pkgver/jython-installer-$_pkgver.jar
        'README.ArchLinux')
noextract=(jython-installer-${_pkgver}.jar)

package() {
	cd "$srcdir"
	java -jar jython-installer-${_pkgver}.jar -s -t standard -d "$pkgdir"/opt/"$pkgname"
	sed -i s*"${pkgdir}"**g "${pkgdir}"/opt/"${pkgname}"/jython
	# Get rid of hard-coded JAVA_HOME, since all the JDKs don't use
	# the same directory.
	sed -i '/^JAVA_HOME=.*$/d' "${pkgdir}"/opt/$pkgname/jython
	install -m755 -D "$pkgdir/opt/$pkgname/jython" "$pkgdir/usr/bin/$pkgname"
	install -m644 -D "$srcdir/README.ArchLinux" \
	    "$pkgdir/usr/share/doc/$pkgname/README.ArchLinux"
	rm "$pkgdir/opt/$pkgname/jython" "$pkgdir/opt/$pkgname/bin/jython"
	install -m644 -D "$pkgdir/opt/$pkgname/LICENSE.txt" \
	    "$pkgdir/usr/share/licenses/$pkgname/LICENSE.txt"
}

sha512sums=('2744d082cd0f6ad6117640b752516270b03b978f992cf093d2de8c3e13fcb98b96e7fdb34f3e137f25e103afbab529cf3be9cc1945a5b3b9624cd2f20efb68a4'
            '0ab0237d456f859b2cbb0739264bb978ad98b2c52153e89fc131aa60edf7837f41617c0e53cbde05688dfc0d6fb08f1d02ebbd41da99b07af72e34a11a83f0b9')
