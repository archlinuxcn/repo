# Maintainer: Carsten Feuls <archlinux@carstenfeuls.de> 

pkgname=ruby-listen
pkgver=3.0.5
pkgrel=1
pkgdesc="The Listen gem listens to file modifications and notifies you about the changes. Works everywhere!"
arch=('any')
url="https://rubygems.org/gems/listen"
license=("MIT")
depends=('ruby' 'ruby-rb-inotify>=0.9' 'ruby-rb-fsevent>=0.9.3')
source=("https://rubygems.org/downloads/listen-$pkgver.gem")
noextract=("listen-$pkgver.gem")
options=('!emptydirs')
sha256sums=('6ffc223ba68736cfa7b1d16b4ecb9c380f15c05cdf749a02a5201937af685ca0')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir"/usr/bin listen-$pkgver.gem

  rm "$pkgdir/$_gemdir"/cache/listen-$pkgver.gem
  install -Dm0644 "$pkgdir/$_gemdir"/gems/listen-$pkgver/LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
