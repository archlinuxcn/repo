# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Diego <cdprincipe@gmail.com>

pkgname=numix-icon-theme-git
pkgver=0.r317.290d12e
pkgrel=1
pkgdesc='Base icon theme from the Numix project'
arch=('any')
url='http://numixproject.org/'
license=('GPL3')
makedepends=('git')
provides=('numix-icon-theme' 'numix-light-icon-theme')
conflicts=('numix-icon-theme' 'numix-light-icon-theme')
options=('!strip')
install='numix-icon-theme.install'
source=('git+https://github.com/numixproject/numix-icon-theme.git')
sha256sums=('SKIP')

pkgver() {
  cd numix-icon-theme

  printf "0.r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  cd numix-icon-theme

  install -dm 755 "$pkgdir"/usr/share/icons
  cp -dr --no-preserve='ownership' Numix{,-Light} "$pkgdir"/usr/share/icons/
}

# vim: ts=2 sw=2 et:
