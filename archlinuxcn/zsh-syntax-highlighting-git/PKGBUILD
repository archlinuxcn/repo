# Maintainer: DDoSolitary <DDoSolitary@gmail.com>
# Contributor: Amanoel Dawod <amoka at amanoel dot com>
# Contributor: Sam Stuewe <halosghost at archlinux dot info>
# Contributor: mjheagle <mjheagle8@gmail.com>

_pkgname=zsh-syntax-highlighting
pkgname="${_pkgname}-git"
pkgver=0.8.0.alpha1.pre.redrawhook.r50.gebef4e5
pkgrel=1
pkgdesc="Fish shell like syntax highlighting for Zsh (from git)"
arch=('any')
url="https://github.com/zsh-users/zsh-syntax-highlighting"
license=('BSD')
depends=('zsh>=4.3.9')
makedepends=('git')
provides=($_pkgname)
conflicts=($_pkgname)
install="${_pkgname}.install"
source=("git+$url.git")
sha256sums=('SKIP')

pkgver() {
  cd $_pkgname
  git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd $_pkgname
  make
}

package() {
  cd $_pkgname
  make PREFIX="/usr" SHARE_DIR="${pkgdir}/usr/share/zsh/plugins/$_pkgname" DESTDIR="${pkgdir}" install
  # create symlink for using with oh-my-zsh
  ln -s "zsh-syntax-highlighting.zsh" \
       "${pkgdir}/usr/share/zsh/plugins/$_pkgname/zsh-syntax-highlighting.plugin.zsh"

  # licence
  install -dm755 "${pkgdir}/usr/share/licenses/$_pkgname"
  ln -s "/usr/share/doc/$_pkgname/COPYING.md" \
        "${pkgdir}/usr/share/licenses/$_pkgname/COPYING"
}
