# Maintainer: tjbp (archlinux@tjbp.net)
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Jonne Haß <me@jhass.eu>
# Contributor: Hyacinthe Cartiaux <hyacinthe.cartiaux@free.fr>
# Contributor: Anatol Pomozov <anatol.pomozov@gmail.com>
# Contributor: Alexsandr Pavlov <kidoz at mail dot ru>

pkgname=ruby-bundler1
_gemname=${pkgname#ruby-}
pkgver=1.17.3
pkgrel=1
pkgdesc="Manages an application's dependencies through its entire life, across many machines, systematically and repeatably. Locked to <2.0, as required by Rails 4 (for example)."
arch=('any')
url='http://bundler.io'
license=('MIT')
depends=('ruby')
makedepends=('ruby-rdoc')
options=('!emptydirs')
source=("https://rubygems.org/downloads/bundler-$pkgver.gem")
noextract=("bundler-$pkgver.gem")
sha512sums=('658de4228bc12fa5ca6ce335f76fff773f64da9f3d12f5097b4fd28d4c4f4d2a5bf12dce761b3d95432c5ea6a5aafae895df87c26660a4567db8b682aff48c02')

package() {
  cd "$srcdir"

  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  HOME="/tmp" GEM_HOME="$_gemdir" GEM_PATH="$_gemdir" gem install --no-user-install --ignore-dependencies \
     -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" "bundler-$pkgver.gem"
  mv "$pkgdir/usr/bin/bundler" "$pkgdir/usr/bin/bundler1"
  mv "$pkgdir/usr/bin/bundle" "$pkgdir/usr/bin/bundle1"
  sed -i "s/>= 0.a/< 2.0/" "$pkgdir/usr/bin/bundler1"
  sed -i "s/>= 0.a/< 2.0/" "$pkgdir/usr/bin/bundle1"
  rm "$pkgdir/$_gemdir/cache/bundler-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/bundler-$pkgver/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE.md"
}
