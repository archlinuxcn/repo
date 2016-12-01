# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=liquid
pkgname=ruby-$_gemname-3
pkgver=3.0.6
pkgrel=1
pkgdesc='A secure, non-evaling end user template engine with aesthetic markup.'
arch=(any)
url='http://www.liquidmarkup.org'
license=(MIT)
depends=('ruby')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/MIT-LICENSE" "$pkgdir/usr/share/licenses/$pkgname/MIT-LICENSE"
}
sha512sums=('8ec5baa4b4fd5a49fce968fad4b42b9841c690463be944dc5ba52b016cb70dca90fadd42398a0555b376a665fc79359613055755b5bbb6bb77014d61a2074383')
