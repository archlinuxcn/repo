# Maintainer: zjuyk <ownbyzjuyk@gmail.com>
pkgname=ttf-material-design-iconic-font
_pkgname=material-design-iconic-font
pkgver=2.2.0
pkgrel=1
pkgdesc="Material Design Iconic Font is a full suite of material design icons (created and maintained by Google) with additional community-designed and brands icons for easy scalable vector graphics on websites or desktop."
arch=('any')
url="https://zavoloklom.github.io/material-design-iconic-font"
license=('CC-BY-SA-4.0 License')
depends=()
source=("https://github.com/zavoloklom/$_pkgname/releases/download/$pkgver/$_pkgname.zip")
sha256sums=('f0dd72ff822ffef5b693fe74da5cd7fc7146b5f7d46bfd5e008af56749fb0158')

package() {
	install -Dm644 $srcdir/fonts/Material-Design-Iconic-Font.ttf $pkgdir/usr/share/fonts/TTF/Material-Design-Iconic-Font.ttf
}
