# Contributor:  Jiachen Yang <farseerfc@gmail.com>
arch=(i686 x86_64)
pkgname=eminent-awesome34-git
pkgver=2010.10.06.gf7a4803
pkgrel=2
pkgdesc="Effortless wmii-style dynamic tagging for the awesome window manager version 3.4"
license=('GPL')
url="http://git.glacicle.org/eminent"

depends=('awesome34')
makedepends=('git' 'lua')
conflicts=('eminent')
provides=('eminent')

#_gitroot=git://github.com/guotsuan/eminent.git
_gitname=eminent

source=("git://github.com/GGLucas/eminent.git")
md5sums=('SKIP')

pkgver() {
    #cd $_gitname
    #echo $(git rev-list --count master).$(git rev-parse --short master)


  cd "${srcdir}/${_gitname}"
      git log -1 --format="%cd.g%h" --date=short | sed 's/-/./g'
}


build() {
  cd $_gitname
  luac -o eminent.luac eminent.lua
}

package() {
  cd $_gitname
  install -D -m644 eminent.lua ${pkgdir}/usr/share/awesome/lib/eminent.lua
  install -D -m644 eminent.luac ${pkgdir}/usr/share/awesome/lib/eminent.luac
}
