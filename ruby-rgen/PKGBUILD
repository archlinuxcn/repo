# Maintainer : Greg Sutcliffe <puppet-aur (at) emeraldreverie (dot) org>
# Contributor: Niels Abspoel <aboe76 (at) Gmail (dot) com>

_gemname=rgen
pkgname=ruby-$_gemname
#_rc=1
#_pkgver=0.6.2
#pkgver=${_pkgver}.rc${_rc}
pkgver=0.6.5
pkgrel=3
pkgdesc="Ruby Modelling and Generator Framework"
arch=(any)
url="http://ruby-gen.org"
license=('MIT')
depends=('ruby')
makedepends=('rubygems' 'binutils')
source=(https://rubygems.org/downloads/$_gemname-${pkgver//_/-}.gem)
noextract=($_gemname-${pkgver//_/-}.gem)

package() {
  cd "$srcdir"
  # _gemdir is defined inside package() because if ruby[gems] is not installed on
  # the system, makepkg will exit with an error when sourcing the PKGBUILD.
  local _gemdir="$(ruby -rubygems -e'puts Gem.default_dir')"

  gem install --no-user-install --ignore-dependencies -i "${pkgdir}${_gemdir}" \
    -n "${pkgdir}/usr/bin" "${_gemname}-${pkgver//_/-}.gem"
}
sha256sums=('bdaeb9ba57ff6150b407b3fefcc8fbe0bae74d509431c7f15517090fe74037e1')
