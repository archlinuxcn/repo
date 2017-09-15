# Maintainer: Jerome Leclanche <jerome@leclan.ch>

_pkgname=sass
pkgname=ruby-$_pkgname
pkgver=3.5.1
pkgrel=1
pkgdesc="Tools and Ruby libraries for the CSS3 extension languages: Sass and SCSS."
arch=("any")
url="http://sass-lang.com/"
license=("MIT")
depends=("ruby-yard" "ruby-maruku")
makedepends=("rubygems")
source=("http://gems.rubyforge.org/gems/$_pkgname-$pkgver.gem")
noextract=("$_pkgname-$pkgver.gem")
sha256sums=("8b3e2cd24e545e4753f7aaebfb789b1e3a6727921a40bf3b9aef4eda727b4cb8")


package() {
	local _gemdir="$(/usr/bin/ruby -rubygems -e"puts Gem.default_dir")"
	/usr/bin/gem install --no-user-install --ignore-dependencies -i "$pkgdir$_gemdir" -n "$pkgdir/usr/bin" "$_pkgname-$pkgver.gem"
	install -D "$pkgdir$_gemdir/gems/$_pkgname-$pkgver/MIT-LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
