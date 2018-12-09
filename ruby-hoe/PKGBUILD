# Maintainer: Bernhard Landauer <oberon@manjaro.org>
# Contributor: Alexsandr Pavlov <kidoz at mail dot ru>

_gemname=hoe
pkgname=ruby-$_gemname
pkgver=3.16.2
pkgrel=1
pkgdesc="Hoe is a rake/rubygems helper for project Rakefiles"
arch=(any)
url="http://www.zenspider.com/projects/hoe.html"
license=("MIT")
depends=('ruby')
makedepends=('ruby-rdoc')
options=('!emptydirs')
source=("https://rubygems.org/downloads/$_gemname-$pkgver.gem")
noextract=($_gemname-$pkgver.gem)
md5sums=('2a49e7b47501ddf0517ab0d9fe851d60')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" "$_gemname-$pkgver.gem"
}
