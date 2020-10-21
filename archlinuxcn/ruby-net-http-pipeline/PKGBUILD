# Maintainer: DDoSolitary <DDoSolitary@gmail.com>
# Contributor: Rhys Davies <rhys@johnguant.com>

_gemname=net-http-pipeline
pkgname=ruby-$_gemname
pkgver=1.0.1
pkgrel=3
pkgdesc='An HTTP/1.1 pipelining implementation atop Net::HTTP'
arch=(any)
url='http://docs.seattlerb.org/net-http-pipeline'
license=()
depends=(ruby)
makedepends=(ruby-rdoc)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha1sums=('a4054e2def2ea1ef570dccc6c26d8875d38c24e8')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
}
