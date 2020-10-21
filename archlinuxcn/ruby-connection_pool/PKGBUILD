# Maintainer: Stelios Tsampas <loathingkernel @at gmail .dot com>

pkgname=ruby-connection_pool
pkgver=2.2.2
pkgrel=1
pkgdesc='Generic connection pool for Ruby'
arch=('any')
url='https://github.com/mperham/connection_pool'
license=('MIT')
depends=('ruby')
makedepends=('ruby-rdoc')
options=('!emptydirs')
source=("https://rubygems.org/downloads/connection_pool-$pkgver.gem")
noextract=("connection_pool-$pkgver.gem")
sha512sums=('74cb64aa3f183ee4e41f438133f60581e9f99a1d5b5daf61607cff2329bfb1fbd8810d87c35d709418a22ad925049e3e9403a602107452414a67aee1c6eecfe9')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir"/usr/bin connection_pool-$pkgver.gem
  rm "$pkgdir/$_gemdir"/cache/connection_pool-$pkgver.gem
  install -D -m644 "$pkgdir/$_gemdir"/gems/connection_pool-$pkgver/LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
