# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=jekyll
pkgname=ruby-$_gemname
pkgver=3.4.0
pkgrel=1
pkgdesc='A simple, blog aware, static site generator.'
arch=(any)
url='https://github.com/jekyll/jekyll'
license=(MIT)
depends=('ruby' 'ruby-addressable' 'ruby-colorator' 'ruby-jekyll-sass-converter' 'ruby-jekyll-watch' 'ruby-kramdown' 'ruby-liquid-3' 'ruby-mercenary' 'ruby-pathutil' 'ruby-rouge' 'ruby-safe_yaml')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('dcb015d18767148ec6b5b8b6f77209e8770de40e525b55d7fbc6f11907fe98fe314bd040a6132b26beddd8ae819f6efe35f755117baca7a23759a0894ca61e8e')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
