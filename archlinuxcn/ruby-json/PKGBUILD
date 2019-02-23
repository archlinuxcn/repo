# Maintainer: Colin Arnott <colin@urandom.co.uk>

pkgname=ruby-json
pkgver=2.2.0
pkgrel=2
pkgdesc="This is a JSON implementation as a Ruby extension in C"
arch=('x86_64')
url='https://rubygems.org/gems/json'
license=('Ruby')
depends=('ruby')
makedepends=('ruby-rdoc')
options=(!emptydirs)
source=(https://rubygems.org/downloads/${pkgname#ruby-}-$pkgver.gem)
noextract=(${pkgname#ruby-}-$pkgver.gem)
sha256sums=('9dd1437156773f72c096058ec837faac1b00077121a3fd574e68f895ea3aa96b')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --no-user-install --ignore-dependencies -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" "${pkgname#ruby-}-$pkgver.gem"
  rm "$pkgdir/$_gemdir/cache/${pkgname#ruby-}-$pkgver.gem"
}
