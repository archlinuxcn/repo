# Maintainer: Colin Arnott <colin@urandom.co.uk>

pkgname=ruby-json
pkgver=2.3.0
pkgrel=1
pkgdesc="This is a JSON implementation as a Ruby extension in C"
arch=('x86_64')
url='https://rubygems.org/gems/json'
license=('Ruby')
depends=('ruby')
makedepends=('ruby-rdoc')
options=(!emptydirs)
source=(https://rubygems.org/downloads/${pkgname#ruby-}-$pkgver.gem)
noextract=(${pkgname#ruby-}-$pkgver.gem)
sha256sums=('b61691fd2087ac37141b75ff4287ce2c3f17251c713e97ef73b43b4bb2e0355b')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --no-user-install --ignore-dependencies -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" "${pkgname#ruby-}-$pkgver.gem"
  rm "$pkgdir/$_gemdir/cache/${pkgname#ruby-}-$pkgver.gem"
}
