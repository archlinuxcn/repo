# Maintainer: farseerfc <farseerfc@archlinuxcn.org>
# Contributor: Andreas Hauser <andy-aur@splashground.de>

pkgname=jave
pkgver=5
pkgrel=10
pkgdesc="Java Ascii Versatile Editor - graphics editor for editing texts instead of images."
url="http://www.jave.de/"
license=("custom")
depends=("java-environment" "sh")
optdepends=('figlet: provide base figlet fonts'
'figlet-fonts: provide additional asciiart fonts')
arch=('any')
source=("${url}download/${pkgname}${pkgver}.zip"
        "${url}download/license.txt"
        "jave.sh")

package() {
	mkdir -p $pkgdir/usr/share/java/$pkgname
    install -Dm755 $srcdir/jave.sh $pkgdir/usr/bin/jave
    install -Dm644 $srcdir/license.txt $pkgdir/usr/share/licenses/jave/license.txt

	mv $srcdir/* $pkgdir/usr/share/java/$pkgname
	rm $pkgdir/usr/share/java/$pkgname/$pkgname.sh
	rm $pkgdir/usr/share/java/$pkgname/license.txt
	rm $pkgdir/usr/share/java/$pkgname/$pkgname*.zip
	rm $pkgdir/usr/share/java/$pkgname/fonts -r

	cd  $pkgdir/usr/share/java/$pkgname/
	ln -s  /usr/share/figlet/fonts fonts
}

sha512sums=('370320a046b1e06132c29b8de71f8a38ef82983ba6a838f4fd01f697deca1a94e9df8c05efd1496d7c619ccbfa95fcea58060dfe8022cd9ec52a395cce0098ae'
            'b6d4b455e9bfa8e094a425f102ba8e8a2b2028485dee71e0b1808b262d01976ee8059cd5055d431f4378b966152c3030ff3768d18caa34941b4e7204d9be6fc7'
            '710314dba9740f0133193ba6e45d7482d0fa1fc5f4ea2de8d3b9a61b139e0b2a278893ca19b335f009e4514f2a156dec05d9307437720c38231e7b1a40e0eff5')
