# Maintainer: Bert Peters <bert@bertptrs.nl>
# Previous: Artem Vorotnikov <artem@vorotnikov.me>

_gemname=rake-compiler
pkgname=ruby-$_gemname
pkgver=1.0.7
pkgrel=1
pkgdesc='Rake-based Ruby Extension (C, Java) task generator.'
arch=(any)
url='https://github.com/rake-compiler/rake-compiler'
license=(MIT)
depends=(ruby)
makedepends=(ruby-rdoc)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha256sums=('755de500565a06900d7f4286f1c761f5681a88c2420f64a27db4f2dd6e0a14dd')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE.txt"
}
