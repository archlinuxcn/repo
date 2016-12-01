# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de

_gemname=colorator
pkgname=ruby-$_gemname
pkgver=1.1.0
pkgrel=1
pkgdesc='String core extensions for terminal coloring.'
arch=(any)
url='https://github.com/octopress/colorator'
license=(MIT)
depends=(ruby)
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
sha512sums=('196e99382062014bdc9ff39cb8bc099c7c3ffdfe1c0faef39cf4eeaee20e1fa1b2ae51a0f6746e71944892a6db314da141ad879afb40ad1f343d9cb8d7757cc4')
