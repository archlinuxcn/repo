# Maintainer: DDoSolitary <DDoSolitary@gmail.com>

_gemname=tzinfo
pkgname=ruby-$_gemname-1
pkgver=1.2.8
pkgrel=1
pkgdesc='Daylight savings aware timezone library'
arch=(any)
url='http://tzinfo.github.io'
license=(MIT)
depends=(ruby ruby-thread_safe)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha256sums=('839c02a45feb42c0f11f4f030e118e33e1e1ddf9c01144d1e57764966034796a')
provides=('ruby-tzinfo')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
