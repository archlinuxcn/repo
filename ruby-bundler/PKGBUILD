# Maintainer: Jonne Haß <me@jhass.eu>
# Contributor: Hyacinthe Cartiaux <hyacinthe.cartiaux@free.fr>
# Contributor: Anatol Pomozov <anatol.pomozov@gmail.com>
# Contributor: Alexsandr Pavlov <kidoz at mail dot ru>

pkgname=ruby-bundler
_gemname=${pkgname#ruby-}
pkgver=1.10.4
pkgrel=1
pkgdesc="Manages an application's dependencies through its entire life, across many machines, systematically and repeatably."
arch=('any')
url='http://bundler.io'
license=('MIT')
depends=('ruby')
options=('!emptydirs')
source=("https://rubygems.org/downloads/$_gemname-$pkgver.gem")
noextract=("$_gemname-$pkgver.gem")
sha256sums=('180284a435d24ef325d7897196032e64424a6efc1d7b0b6b13b61574d98ca2f5')

package() {
  cd "$srcdir"

  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  HOME="/tmp" GEM_HOME="$_gemdir" GEM_PATH="$_gemdir" gem install --no-user-install --ignore-dependencies \
     -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" "$_gemname-$pkgver.gem"
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE.md"
}
