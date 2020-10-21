# Maintainer: DDoSolitary <DDoSolitary@gmail.com>
# Contributor: Rhys Davies <rhys@johnguant.com>

_gemname=launchy
pkgname=ruby-$_gemname
pkgver=2.5.0
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
sha512sums=('d80811009155d9cea6a2e69b5f7482aaec7d0bf23ecca4cbe72e440fb4eae1c38bc5904e863998f1966c7a99b98bad1f4456cec1cb076f96f5a99b835448b39f')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
