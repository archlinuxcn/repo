# Maintainer: Latif Sulistyo <latipun@aur.archlinux.org>

# shellcheck disable=2034,2154
# shellcheck shell=bash

_pkgname=Kvantum
pkgname=kvantum-theme-catppuccin-git
pkgver=r5.04be2ad
pkgrel=1
pkgdesc="Soothing pastel theme for Kvantum"
arch=('any')
url="https://github.com/catppuccin/$_pkgname"
license=('MIT')
makedepends=('git')
depends=('kvantum')
provides=("catppuccin-kvantum-theme")
source=("git+$url.git")
sha256sums=('SKIP')

pkgver() {
  cd "$srcdir/$_pkgname" || exit 1
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  cd "$_pkgname/src" || exit 1
  install -dm755 "$pkgdir/usr/share/Kvantum"
  cp -r Catppuccin-* "$pkgdir/usr/share/Kvantum"
}
