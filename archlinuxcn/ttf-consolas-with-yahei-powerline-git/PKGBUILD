# Contributor: katt <magunasu.b97@gmail.com>
# Contributor: Edward Pacman <edward@edward-p.xyz>
_pkgname='consolas-with-yahei'
pkgname=ttf-$_pkgname-powerline-git
pkgver=r14.b6e9163
pkgrel=1
pkgdesc="Consolas-with-Yahei with powerline patched with nerd-fonts)"
arch=(any)
url='https://github.com/crvdgc/Consolas-with-Yahei'
license=(unknown)
makedepends=(git)
provides=(ttf-$_pkgname)
conflicts=(ttf-$_pkgname)
source=("git+$url.git")
md5sums=('SKIP')

pkgver() {
  cd "Consolas-with-Yahei"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  mkdir -p "$pkgdir"/usr/share/fonts/$_pkgname
  chmod -R 755 "$pkgdir"/usr/
  cp Consolas-with-Yahei/ttf/Consolas-with-Yahei\ Nerd\ Font.ttf "$pkgdir"/usr/share/fonts/$_pkgname/consnerd.ttf
  cp Consolas-with-Yahei/ttf/Consolas-with-Yahei\ Bold\ Nerd\ Font.ttf "$pkgdir"/usr/share/fonts/$_pkgname/consnerdb.ttf
  cp Consolas-with-Yahei/ttf/Consolas-with-Yahei\ Italic\ Nerd\ Font.ttf "$pkgdir"/usr/share/fonts/$_pkgname/consnerdi.ttf
  cp Consolas-with-Yahei/ttf/Consolas-with-Yahei\ Bold\ Italic\ Nerd\ Font.ttf "$pkgdir"/usr/share/fonts/$_pkgname/consnerdz.ttf
}
