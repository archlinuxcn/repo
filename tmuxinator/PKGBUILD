# Contributor: Luca Cesari < luca AT cesari DOT me>
_gemname=tmuxinator
pkgname=tmuxinator
pkgver=0.11.1
pkgrel=1
pkgdesc="Manage complex tmux sessions easily"
arch=(any)
url="https://github.com/aziz/tmuxinator"
license=(MIT)
depends=(ruby ruby-erubis ruby-thor ruby-xdg ruby-rdoc)
makedepends=(rubygems)
source=(http://rubygems.org/downloads/tmuxinator-$pkgver.gem)
noextract=(tmuxinator-$pkgver.gem)
md5sums=('bec5e560844ba409c72f9978d91258db')

package() {
    cd $srcdir
    export HOME='/tmp'
    local _gemdir="$(ruby -rrubygems -e'puts Gem.default_dir')"
    install -d -m 755 ${pkgdir}/usr/bin
    gem install --no-user-install --ignore-dependencies -i "${pkgdir}${_gemdir}" -n ${pkgdir}/usr/bin ${_gemname}-${pkgver}.gem

    rm "${pkgdir}/${_gemdir}/cache/${_gemname}-${pkgver}.gem"
}

# vim:set ts=2 sw=2 :
