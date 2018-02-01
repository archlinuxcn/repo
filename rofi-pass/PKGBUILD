# Maintainer: Lex Black <autumn-wind at web dot de>

pkgname=rofi-pass
pkgver=1.5.3
pkgrel=1
pkgdesc="bash script to handle pass storages in a convenient way"
arch=('any')
url='https://github.com/carnager/rofi-pass'
license=('GPL')
depends=('xdg-utils' 'rofi' 'gawk' 'pass' 'pwgen' 'xdotool' 'xclip')
optdepends=('passed-git: change fieldnames in password files')
conflicts=('rofi-pass-git')
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/carnager/${pkgname}/archive/${pkgver}.tar.gz)
md5sums=('915bdcaed20deb50de87dda845c23121')


package() {
    make -C "${pkgname}-${pkgver}" DESTDIR="$pkgdir" PREFIX="/usr" install
}
