# Maintainer: Bert Peters <bert@bertptrs.nl>
# Previous: Artem Vorotnikov <artem@vorotnikov.me>

_gemname=rake-compiler
pkgname=ruby-$_gemname
pkgver=1.0.4
pkgrel=2
pkgdesc='Rake-based Ruby Extension (C, Java) task generator.'
arch=(any)
url='https://github.com/rake-compiler/rake-compiler'
license=(MIT)
depends=(ruby)
makedepends=(ruby-rdoc)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('009118df874ec63ea1257b6b2e8626848df6f223e16dfc834d6346ffad6ac4b7acaabfe9d5f4a97591f725ba3353ed5329f67ce9cf7564c71855f4aeed2727b0')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE.txt"
}
