# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=yajl-ruby
pkgname=ruby-$_gemname
pkgver=1.3.0
pkgrel=1
pkgdesc='Ruby C bindings to the excellent Yajl JSON stream-based parser library.'
arch=('any')
url='http://github.com/brianmario/yajl-ruby'
license=('MIT')
depends=('ruby')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('351e46fb7037541096172bac5c3dcadaa6ac9650ac6aae46de2b4ba31b82427f596bade2b233d0d8e916927800e83b7930b5ceeb9d7340edd02c323f9c0b3116')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
}
