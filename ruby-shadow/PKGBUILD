# Maintainer: Greg Sutcliffe <greg.sutcliffe@gmail.com>>

pkgname=ruby-shadow
pkgver=2.2.0
pkgrel=2
pkgdesc="This module provides access to shadow passwords on Linux and Solaris"
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h')
url="https://github.com/apalmblad/ruby-shadow"
license=('CPL')
depends=('ruby')
makedepends=('rubygems')
source=(http://gems.rubyforge.org/gems/$pkgname-$pkgver.gem)
md5sums=('2d7b05fd5097f675fce5dbabe34d0e61')
noextract=($pkgname-$pkgver.gem)

package() {
  cd "$srcdir"
  # _gemdir is defined inside package() because if ruby[gems] is not installed on
  # the system, makepkg will exit with an error when sourcing the PKGBUILD.
  local _gemdir="$(ruby -rubygems -e'puts Gem.default_dir')"

  gem install --no-user-install --ignore-dependencies -i "$pkgdir$_gemdir" \
    -n "$pkgdir/usr/bin" "$pkgname-$pkgver.gem"
}
