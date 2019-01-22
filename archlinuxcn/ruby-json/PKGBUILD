# Maintainer: Colin Arnott <colin@urandom.co.uk>

pkgname=ruby-json
pkgver=2.1.0
pkgrel=6
pkgdesc="This is a JSON implementation as a Ruby extension in C"
arch=('x86_64')
url='http://json-jruby.rubyforge.org/'
license=('Ruby')
depends=('ruby')
makedepends=('ruby-rdoc')
options=(!emptydirs)
source=(https://rubygems.org/downloads/${pkgname#ruby-}-$pkgver.gem)
noextract=(${pkgname#ruby-}-$pkgver.gem)
sha512sums=('bffbe462e952bca321d4325ecb9c5e9f61e51cad13758581ecfaa6a038bac4e30dc7db50bd897086a5592f6fc437d0e0909f91e279aaf4dd71cf127100c3550b')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --no-user-install --ignore-dependencies -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" "${pkgname#ruby-}-$pkgver.gem"
  rm "$pkgdir/$_gemdir/cache/${pkgname#ruby-}-$pkgver.gem"
}
