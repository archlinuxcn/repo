# Maintainer: Maxime Gauduin <alucryd@archlinux.org>

pkgname=numix-circle-icon-theme-git
pkgver=0.r1677.fe74d83
pkgrel=1
pkgdesc='Circle icon theme from the Numix project'
arch=('any')
url='http://numixproject.org/'
license=('GPL3')
depends=('numix-icon-theme-git')
makedepends=('git')
provides=('numix-circle-icon-theme' 'numix-circle-light-icon-theme')
conflicts=('numix-circle-icon-theme' 'numix-circle-light-icon-theme')
options=('!strip')
install='numix-circle-icon-theme.install'
source=('numix-circle-icon-theme::git+https://github.com/numixproject/numix-icon-theme-circle.git')
sha256sums=('SKIP')

pkgver() {
  cd numix-circle-icon-theme

  printf "0.r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  cd numix-circle-icon-theme

  install -dm 755 "${pkgdir}"/usr/share/icons
  cp -dr --no-preserve='ownership' Numix-Circle{,-Light} "${pkgdir}"/usr/share/icons/
}

# vim: ts=2 sw=2 et:
