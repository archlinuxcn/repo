# Maintainer: Mario Finelli <mario dot finelli at yahoo dot com>

_gemname=http_parser.rb
pkgname=ruby-$_gemname
pkgver=0.6.0
pkgrel=2
pkgdesc="Ruby bindings to https://github.com/ry/http-parser and https://github.com/a2800276/http-parser.java"
arch=(i686 x86_64)
url='http://github.com/tmm1/http_parser.rb'
license=(MIT)
depends=(ruby ruby-benchmark_suite ruby-ffi ruby-json ruby-rake-compiler ruby-rspec ruby-yajl-ruby)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha256sums=('f11d0aec50ef26a7d1f991e627ac88acdb5979282aeba7a5c3be6ce0636ed196')

package() {
  cd "$srcdir"
  local _gemdir="$(ruby -e'puts Gem.default_dir')"

  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
}
