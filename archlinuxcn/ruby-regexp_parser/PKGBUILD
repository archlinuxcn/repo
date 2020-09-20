# Maintainer: Mario Finelli <mario at finel dot li>

_gemname=regexp_parser
pkgname=ruby-${_gemname}
pkgver=1.7.1
pkgrel=1
pkgdesc="A library for tokenizing, lexing, and parsing Ruby regular expressions."
arch=(any)
depends=(ruby)
makedepends=(rubygems ruby-rdoc)
url="https://github.com/ammar/regexp_parser"
noextract=($_gemname-$pkgver.gem)
license=(MIT)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
sha256sums=('2401a4eedf9334c2fa7a1026d807594b059c4873265b899cf0000926f2fdca80')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"

  gem install \
    --ignore-dependencies \
    --no-user-install \
    -i "$pkgdir/$_gemdir" \
    -n "$pkgdir/usr/bin" \
    $_gemname-$pkgver.gem

  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"

  install -Dm0644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
