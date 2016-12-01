# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=pathutil
pkgname=ruby-$_gemname
pkgver=0.14.0
pkgrel=1
pkgdesc='Like Pathname but a little less insane.'
arch=(any)
url='http://github.com/envygeeks/pathutils'
license=(MIT)
depends=('ruby' 'ruby-forwardable-extended')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('470eef7a82105a7d41228de6c312dc4f21d8e8ee6b7c80f98ebe366db83c7e507dbfa7cf820203ef8c802076c96b791dd79859213e978f8fa4894a2099e2c7bd')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
