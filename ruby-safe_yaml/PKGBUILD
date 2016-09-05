# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de>

_gemname=safe_yaml
pkgname=ruby-$_gemname
pkgver=1.0.4
pkgrel=1
pkgdesc='SameYAML provides an alternative implementation of YAML.load suitable for accepting user input in Ruby applications.'
arch=(any)
url='https://github.com/dtao/safe_yaml'
license=('MIT')
depends=('ruby')
options=(!emptydirs)
source=(https://rubygems.org/downloads/$_gemname-$pkgver.gem)
noextract=($_gemname-$pkgver.gem)
sha512sums=('ecc944a6e5f0862acf1413d7ab38bd35b56405893bb8064be2b8a056f0164d3710afaa2f6ef65868770e855ecf54a87bf9ddae2241c3c2957ca001ca04b04c5a')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir/usr/bin" $_gemname-$pkgver.gem
  rm "$pkgdir/$_gemdir/cache/$_gemname-$pkgver.gem"
  install -D -m644 "$pkgdir/$_gemdir/gems/$_gemname-$pkgver/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE.txt"
}
