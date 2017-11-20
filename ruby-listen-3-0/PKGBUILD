# Maintainer: Shengyu Zhang <la@archlinuxcn.org>
# Contributor: Carsten Feuls <archlinux@carstenfeuls.de>

pkgname=ruby-listen-3-0
_pkgname=ruby-listen
pkgver=3.0.8
pkgrel=2
pkgdesc='The Listen gem listens to file modifications and notifies you about the changes. Works everywhere! version < 3.1'
arch=('any')
url='https://rubygems.org/gems/listen'
license=('MIT')
depends=('ruby' 'ruby-rb-inotify>=0.9' 'ruby-rb-fsevent>=0.9.3')
source=("https://rubygems.org/downloads/listen-$pkgver.gem")
noextract=("listen-$pkgver.gem")
options=('!emptydirs')
sha256sums=('91845635a094f81de2af4ec334340dd8458d9b86486471c2dc9747e7173c1ed0')
provides=("$_pkgname=$pkgver")
conflicts=('ruby-listen')
replaces=('ruby-listen')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir"/usr/bin listen-$pkgver.gem

  rm "$pkgdir/$_gemdir"/cache/listen-$pkgver.gem
  install -Dm0644 "$pkgdir/$_gemdir"/gems/listen-$pkgver/LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
