# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=rouge
pkgname=ruby-$_gemname
pkgver=1.11.1
pkgrel=1
pkgdesc='Rouge aims to a be a simple, easy-to-extend drop-in replacement for pygments.'
arch=(any)
url='http://rouge.jneen.net/'
license=(MIT)
depends=('ruby')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('9cf1e20c1e2cfe2fe78171d4023b2b1237f9f0fdfaabdb3c0246558556c3c0aa1dfd62708e06d38b3615c817f4b700732b8281003272ac72c8e6ee894bc2cd87')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
