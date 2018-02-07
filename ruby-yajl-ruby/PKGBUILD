# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=yajl-ruby
pkgname=ruby-$_gemname
pkgver=1.3.1
pkgrel=2
pkgdesc='Ruby C bindings to the excellent Yajl JSON stream-based parser library.'
arch=('any')
url='http://github.com/brianmario/yajl-ruby'
license=('MIT')
depends=('ruby' 'ruby-rdoc')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('f18b47f1fd0b039bfec01db0ee298296199fbf91b22a00042e1220a1d8471f72424c082b696829e48ce7dee7514510dd731c2bc36fe29bd08ba7246c820621f4')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "${pkgdir}/usr/lib/ruby/gems/2.5.0/gems/yajl-ruby-1.3.1/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/MIT-LICENSE"
}
