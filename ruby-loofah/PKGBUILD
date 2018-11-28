# Maintainer: Matej Grabovsky <matej.grabovsky at gmail>

_gemname=loofah
pkgname=ruby-$_gemname
pkgver=2.2.0
pkgrel=2
pkgdesc='HTML sanitization for Rails applications'
arch=(any)
url='https://github.com/flavorjones/loofah'
license=(MIT)
depends=(ruby ruby-nokogiri)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha256sums=('0e4184f2ad3555094522cd00b7498f3b36e64c28f5298112d36ed1bfb2e74601')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" \
    -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/MIT-LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/MIT-LICENSE"
}

