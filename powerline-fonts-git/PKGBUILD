# Maintainer: Devin Christensen <quixoten at gmail dot com>
pkgname=powerline-fonts-git
pkgver=r98.6ac4c01
pkgrel=1
pkgdesc="Powerline fonts for X11 and the console"
arch=('any')
url=('https://github.com/powerline/fonts')
license=('CPL')
depends=(fontconfig xorg-font-utils )
makedepends=('git')
conflicts=(
  otf-droid-sans-mono-powerline-git
  otf-inconsolata-dz-powerline-git
  otf-inconsolata-g-powerline-git
  otf-inconsolata-powerline-git
  otf-meslo-powerline-git
  otf-sauce-code-powerline-git
  powerline-fonts
  terminess-powerline-font-git
  ttf-anonymice-powerline-git
  ttf-dejavu-sans-mono-powerline-git
  ttf-literation-mono-powerline-git
  ttf-monofur-powerline-git
  ttf-ubuntu-mono-derivative-powerline-git
  monaco-powerline-font-git
  otf-droidsansmono-powerline-git
  otf-source-code-pro-powerline-git
  source-code-pro-fonts-powerline
  terminess-powerline-font
  ttf-anonymous-pro-powerline
  ttf-anonymous-pro-powerline-git
  ttf-dejavusansmono-powerline-git
  ttf-inconsolata-dz-powerline
  ttf-liberation-mono-powerline-git
  ttf-meslo-powerline-git
  ttf-powerline-fonts-git
  ttf-ubuntu-mono-powerline-git
)
install=$pkgname.install
source=('git://github.com/powerline/fonts.git')
md5sums=('SKIP')

pkgver() {
  cd fonts
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  cd $srcdir/fonts
  find . -iname "*.ttf" -execdir install -Dm644 {} $pkgdir/usr/share/fonts/TTF/{} \;
  find . -iname "*.otf" -execdir install -Dm644 {} $pkgdir/usr/share/fonts/OTF/{} \;
  find . -iname "*.pcf.gz" -execdir install -Dm644 {} $pkgdir/usr/share/fonts/misc/{} \;
  find . -iname "*.psf.gz" -execdir install -Dm644 {} $pkgdir/usr/share/kbd/consolefonts/{} \;
}
