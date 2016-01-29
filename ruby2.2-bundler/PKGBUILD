# Maintainer: Jonne Haß <me@jhass.eu>

pkgname=ruby2.2-bundler
_gemname=${pkgname#ruby2.2-}
pkgver=1.11.2
pkgrel=1
pkgdesc="Manages an application's dependencies through its entire life, across many machines, systematically and repeatably."
arch=('any')
url="http://bundler.io"
license=('MIT')
depends=('ruby2.2')
options=('!emptydirs')
source=("https://rubygems.org/downloads/$_gemname-$pkgver.gem")
noextract=("$_gemname-$pkgver.gem")
sha256sums=('c7aa8ffe0af6e0c75d0dad8dd7749cb8493b834f0ed90830d4843deb61906768')

package() {
  cd "$srcdir"

  local _gemdir="$(ruby-2.2 -rubygems -e'puts Gem.default_dir')"
  HOME="/tmp" GEM_HOME="$_gemdir" GEM_PATH="$_gemdir" gem-2.2 install --no-user-install --ignore-dependencies \
    --no-ri --no-rdoc -i "$pkgdir/$_gemdir" "$_gemname-$pkgver.gem"
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE.md"

  install -d "$pkgdir/usr/bin/"
  ln -s "$_gemdir/bin/bundle" "$pkgdir/usr/bin/bundle-2.2"
}
