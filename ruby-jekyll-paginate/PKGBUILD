# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=jekyll-paginate
pkgname=ruby-$_gemname
pkgver=1.1.0
pkgrel=1
pkgdesc='Built-in Pagination Generator for Jekyll'
arch=('any')
url='https://github.com/jekyll/jekyll-paginate'
license=('MIT')
depends=('ruby')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('91a11257d843306056f27a1717231c21c385317ef71c5a61c259a0406383cb5e5a6ecbb5d43eea2522a2c83dc42dd0c5927dabec3f21725d1cc8b54448d9cf0a')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE.txt"
}
