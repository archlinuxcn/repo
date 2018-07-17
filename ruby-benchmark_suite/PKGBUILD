# Maintainer: Mario Finelli <mario at finel dot li>

_gemname=benchmark_suite
pkgname=ruby-$_gemname
pkgver=1.0.0
pkgrel=2
pkgdesc='A set of enhancements to the standard library benchmark.rb.'
arch=('any')
url='http://github.com/evanphx/benchmark_suite'
options=(!emptydirs)
license=('MIT')
noextract=($_gemname-$pkgver.gem)
depends=('ruby' 'ruby-benchmark-ips')
makedepends=('rubygems' 'ruby-rdoc')
source=("https://rubygems.org/downloads/$_gemname-$pkgver.gem")
sha256sums=('8dddd2129b9b691b3d0af33289a2805505ea4845aa33ac9f586a1cd0bc6d9e6a')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"

  gem install \
    --ignore-dependencies \
    --no-user-install \
    -i "$pkgdir/$_gemdir" \
    -n "$pkgdir/usr/bin" \
    $_gemname-$pkgver.gem

  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
}
