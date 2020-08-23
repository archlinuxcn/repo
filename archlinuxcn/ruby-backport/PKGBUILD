# Maintainer: mnussbaum <michaelnussbaum08@gmail.com>

_gemname=backport
pkgname=ruby-backport
pkgver=1.1.2
pkgrel=0
pkgdesc="A pure Ruby library for event-driven IO"
arch=("any")
depends=(ruby)
makedepends=(rubygems)
url="https://github.com/castwide/backport"
noextract=($_gemname-$pkgver.gem)
license=("MIT")
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
sha256sums=("6c17bb30a2e3fefe1739bbc2a17ad71578b2e7ab9582f8d0019e96eeafa4b2f6")

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"

  gem install \
    --ignore-dependencies \
    --no-user-install \
    -i "$pkgdir/$_gemdir" \
    -n "$pkgdir/usr/bin" \
    $_gemname-$pkgver.gem

  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
}
