# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=jekyll
pkgname=ruby-$_gemname
pkgver=3.4.3
pkgrel=1
pkgdesc='A simple, blog aware, static site generator.'
arch=(any)
url='https://github.com/jekyll/jekyll'
license=(MIT)
depends=('ruby' 'ruby-addressable' 'ruby-colorator' 'ruby-jekyll-sass-converter' 'ruby-jekyll-watch' 'ruby-kramdown' 'ruby-liquid-3' 'ruby-mercenary' 'ruby-pathutil' 'ruby-rouge-1' 'ruby-safe_yaml')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('e6696d069f401acb49af0d39dd05d9fe55a384711c95104fc970ab0ff9106eb9d66e7afd96c826da713388e68bef6524ad5863223c6595424d1cbb9a24745cd1')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
