# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=rouge
pkgname=ruby-$_gemname
pkgver=2.0.7
pkgrel=1
pkgdesc='Rouge aims to a be a simple, easy-to-extend drop-in replacement for pygments.'
arch=(any)
url='http://rouge.jneen.net/'
license=(MIT)
depends=('ruby')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('9baf3e3170f0fdba9693eee52e7a730dead7319828416aaf8b13541cf761e265af42a116adda19d982cae141cbbd27119fe09f88b68211fb1f2ca73822b9689f')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
