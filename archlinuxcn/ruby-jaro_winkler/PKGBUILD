# Maintainer: Mario Finelli <mario at finel dot li>

_gemname=jaro_winkler
pkgname=ruby-${_gemname}
pkgver=1.5.4
pkgrel=1
pkgdesc="Ruby & C implementation of Jaro-Winkler distance algorithm which supports UTF-8 string."
arch=('i686' 'x86_64')
depends=(
  ruby
)
makedepends=(rubygems ruby-rdoc)
url="https://github.com/tonytonyjan/jaro_winkler"
noextract=($_gemname-$pkgver.gem)
license=('MIT')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem
        https://raw.githubusercontent.com/tonytonyjan/jaro_winkler/master/LICENSE.txt)
sha256sums=('50c3e83c5a9e8769c1cf5b73c8b51bb6eebbf8852a0ee53bf6ad6e4dc63414f9'
            'a40f9981c2904f09be8912c97ae593bb88a9d247044d2cadfa24b85ad33b9c42')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"

  gem install \
    --ignore-dependencies \
    --no-user-install \
    -i "$pkgdir/$_gemdir" \
    -n "$pkgdir/usr/bin" \
    $_gemname-$pkgver.gem

  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"

  install -Dm0644 "$srcdir/LICENSE.txt" \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
