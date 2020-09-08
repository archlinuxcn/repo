# Maintainer: Alfin Bakhtiar Ilhami <alfin at nuclea dot id>
# Maintainer: Jan-Tarek Butt <tarek at ring0 dot de>

pkgbase=bootstrap-studio
pkgname=bootstrap-studio
pkgver=5.2.1
pkgrel=3
pkgdesc='A powerful desktop app for creating responsive websites using the Bootstrap framework.'
url='https://bootstrapstudio.io/'
arch=('x86_64')
source=(
	$pkgname.AppImage::'https://bootstrapstudio.io/releases/desktop/'$pkgver'/Bootstrap%20Studio.AppImage'
	launcher.sh::'https://bootstrapstudio.io/releases/desktop/'$pkgver'/launcher.sh'
)

sha512sums=(
	'5a12934eba7611b317d2c0611232339628e3c2dc434703d483c4ff18eab5a405cce2d1fbb4ffff2cf353575d38f3a925747fa5f4d45be9d44982fb6d92f41f2e'
	'df0febc0427ee86caab4959657d24fdb20150c994a7825b229694579f9bfb5c32ebf16988195e1706f2031aeae794842af7356b68b91068293a51ae12b8b61bd'
)

package() {
	mv $pkgname.AppImage 'Bootstrap Studio.AppImage'
	sed -i '55,60d' launcher.sh
	sed -i '8,12d' launcher.sh
	bash launcher.sh
}

post_remove() {
	bash launcher.sh --uninstall
}
