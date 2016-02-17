# Maintainer: farkasity <farkasity@gmail.com>

_gemname=rak
pkgname=$_gemname
pkgver=1.4
pkgrel=1
pkgdesc='Grep replacement in pure Ruby.'
arch=(any)
url='http://rak.rubyforge.org/'
license=(MIT)
depends=(ruby)
source=(http://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha256sums=('1220260bc317f5b7eaad4915d4435319ac27819bf480a96b203ae0052f71093e')

package() {
  local _gemdir="$(ruby -rubygems -e 'puts Gem.default_dir')"
  gem install --no-user-install --ignore-dependencies -i "$pkgdir/$_gemdir" $_gemname-$pkgver.gem

  install -D -m755 "$pkgdir/$_gemdir/bin/rak" "$pkgdir/usr/bin/rak"
}
