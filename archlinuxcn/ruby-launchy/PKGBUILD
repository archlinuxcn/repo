# Maintainer: DDoSolitary <DDoSolitary@gmail.com>
# Contributor: Rhys Davies <rhys@johnguant.com>

_gemname=launchy
pkgname=ruby-$_gemname
pkgver=2.5.2
pkgrel=1
pkgdesc='Launchy is helper class for launching cross-platform applications in a fire and forget manner.'
arch=(any)
url='http://github.com/copiousfreetime/launchy'
license=(ISC)
depends=(ruby ruby-addressable)
makedepends=(ruby-rdoc)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('40777dabd25e6646c6673b33d9d296b66de7976fdf7454c9a7ae809a161ed992572b2232d94591731a7c8405875803172c6fafd09a5570f09e5eb119e23e7773')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
