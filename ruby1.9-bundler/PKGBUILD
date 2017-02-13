# Maintainer: Jonne Haß <me@jhass.eu>
# Contributor: Alexsandr Pavlov <kidoz at mail dot ru>

pkgname=ruby1.9-bundler
_gemname=${pkgname#ruby1.9-}
pkgver=1.14.4
pkgrel=1
pkgdesc="Manages an application's dependencies through its entire life, across many machines, systematically and repeatably."
arch=('any')
url="http://bundler.io"
license=('MIT')
depends=('ruby1.9')
options=('!emptydirs')
source=("https://rubygems.org/downloads/$_gemname-$pkgver.gem")
noextract=("$_gemname-$pkgver.gem")
sha256sums=('dbcd7c05de13ff4a9ded7353fe761767e5777fe9c49d2f1420f50672cfaa4ec1')

package() {
  cd "$srcdir"

  local _gemdir="$(ruby-1.9 -rubygems -e'puts Gem.default_dir')"
  HOME="/tmp" GEM_HOME="$_gemdir" GEM_PATH="$_gemdir" gem-1.9 install --no-user-install --ignore-dependencies \
    --no-ri --no-rdoc -i "$pkgdir/$_gemdir" "$_gemname-$pkgver.gem"
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE.md"

  install -d "$pkgdir/usr/bin/"
  ln -s "$_gemdir/bin/bundle" "$pkgdir/usr/bin/bundle-1.9"
}
