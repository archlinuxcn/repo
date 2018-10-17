# Maintainer: Sam Stuewe <halosghost at archlinux dot info>
# Contributor: mjheagle <mjheagle8@gmail.com>
_name='zsh-syntax-highlighting'
pkgname="${_name}-git"
pkgver=0.4.0.r167.gfdaeec4
pkgrel=1
pkgdesc='Fish shell like syntax highlighting for Zsh'
url='https://github.com/zsh-users/zsh-syntax-highlighting'
arch=('any')
license=('Custom')
depends=('zsh>=4.3.9')
makedepends=('git')
provides=('zsh-syntax-highlighting')
conflicts=('zsh-syntax-highlighting')
install="${_name}.install"
source=("${_name}::${url//https/git}")
sha256sums=('SKIP')

pkgver() {
   cd "${srcdir}/${_name}"
   git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

package() {
    cd "${srcdir}/${_name}"
    make DESTDIR="${pkgdir}" PREFIX='/usr' install
}
