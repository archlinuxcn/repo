# Maintainer: mnussbaum <michaelnussbaum08@gmail.com>

_gemname=e2mmap
pkgname=ruby-e2mmap
pkgver=0.1.0
pkgrel=0
pkgdesc="A Ruby module for defining custom exceptions with specific messages"
arch=("any")
depends=(ruby)
makedepends=(rubygems)
url="https://github.com/ruby/e2mmap"
noextract=($_gemname-$pkgver.gem)
license=("BSD")
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
sha256sums=("45ee6bba2d97a7d91ee0885774261feee87e28c598355df31e93b56196ec0f59")

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
