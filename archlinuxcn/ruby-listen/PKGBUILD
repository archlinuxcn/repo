# Maintainer: Bert Peters <bert@bertptrs.nl>
# Contributor: Carsten Feuls <archlinux@carstenfeuls.de>

pkgname=ruby-listen
pkgver=3.1.5
pkgrel=3
pkgdesc="The Listen gem listens to file modifications and notifies you about the changes. Works everywhere!"
arch=('any')
url="https://rubygems.org/gems/listen"
license=("MIT")
depends=('ruby' 'ruby-rb-inotify>=0.9' 'ruby-rb-fsevent>=0.9.3'
		 'ruby-ruby_dep>=1.2')
makedepends=('ruby-rdoc')
source=("https://rubygems.org/downloads/listen-$pkgver.gem")
noextract=("listen-$pkgver.gem")
options=('!emptydirs')
sha256sums=('bd9ab5f1615a7e491a2251c09f0fae9407ab3bd7650bdb517dda54ec6cae6507')

package() {
  local _gemdir="$(ruby -e'puts Gem.default_dir')"
  gem install --ignore-dependencies --no-user-install -i "$pkgdir/$_gemdir" -n "$pkgdir"/usr/bin listen-$pkgver.gem

  rm "$pkgdir/$_gemdir"/cache/listen-$pkgver.gem
  install -Dm0644 "$pkgdir/$_gemdir"/gems/listen-$pkgver/LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
