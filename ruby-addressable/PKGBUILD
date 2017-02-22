# Maintainer: Mario Finelli <mario at finel dot li>
# Contributor: Artem Vorotnikov <artem at vorotnikov dot me>

_gemname=addressable
pkgname=ruby-$_gemname
pkgver=2.5.0
pkgrel=3
pkgdesc='URI Implementation'
arch=(any)
url='https://github.com/sporkmonger/addressable'
license=('Apache')
depends=(ruby ruby-public_suffix)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha256sums=('bc5bf921b39640675fbb3484cdb45e4241b4c88d8d5a7d85a3985424ad02b9c8')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE.txt"
}
