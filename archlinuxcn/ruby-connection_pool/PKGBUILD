# Maintainer: Stelios Tsampas <loathingkernel @at gmail .dot com>

_gemname=connection_pool
pkgname=ruby-$_gemname
pkgver=2.2.5
pkgrel=1
pkgdesc='Generic connection pool for Ruby'
arch=('any')
url='https://github.com/mperham/connection_pool'
license=('MIT')
depends=('ruby')
makedepends=('ruby-rdoc')
options=('!emptydirs')
source=("https://rubygems.org/downloads/$_gemname-$pkgver.gem")
noextract=("$_gemname-$pkgver.gem")
sha512sums=('3bc4e4d241cd4b1adb00d341aafe7795bbf0eff459ace962670d83c20c0eaa0d42f49a1f5e61c2327ff4fcbf3abfbc6f6c910f7a31d4a0f62bc55c782ab20e45')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem \
    install \
    --ignore-dependencies \
    --no-user-install \
    -i "$pkgdir/$_gemdir" \
    -n "$pkgdir/usr/bin" \
    "$_gemname-$pkgver".gem

  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"

  install -Dm644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
