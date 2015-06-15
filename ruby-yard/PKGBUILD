# Maintainer: Jerome Leclanche <jerome@leclan.ch>

_gemname=yard
pkgname=ruby-$_gemname
pkgver=0.8.7.6
pkgrel=1
pkgdesc="Documentation tool for consistent and usable documentation in Ruby."
arch=("any")
url="http://yardoc.org"
license=("MIT")
depends=("ruby")
makedepends=("rubygems")
source=("http://gems.rubyforge.org/gems/$_gemname-$pkgver.gem")
noextract=("$_gemname-$pkgver.gem")
sha256sums=("3da10884b94fa25b7476f619b1d2cfb61290e10673965c545975630cd88a46b6")


package() {
	cd "$srcdir"
	local _gemdir="$(ruby -rubygems -e"puts Gem.default_dir")"
	gem install --no-user-install --ignore-dependencies -i "$pkgdir$_gemdir" -n "$pkgdir/usr/bin" "$_gemname-$pkgver.gem"
	install -D "$pkgdir$_gemdir/gems/${_gemname}-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}
