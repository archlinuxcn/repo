# Maintainer: Vojtěch Aschenbrenner <v@asch.cz>

_gemname=locale
pkgname=ruby-$_gemname
pkgver=2.1.1
pkgrel=1
pkgdesc='Ruby-Locale is the pure ruby library which provides basic APIs for localization.'
arch=(any)
url='https://github.com/ruby-gettext/locale'
license=(Ruby LGPLv3+)
depends=(ruby)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha1sums=('d31ee2630b8f5d10043992856a7a368c67de3e5c')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/COPYING" "$pkgdir/usr/share/licenses/$pkgname/COPYING"
}
