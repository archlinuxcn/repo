# Maintainer: Lex Black <autumn-wind at web dot de>

pkgname=rofi-pass
pkgver=2.0.2
pkgrel=1
pkgdesc="bash script to handle pass storages in a convenient way"
arch=('any')
url='https://github.com/carnager/rofi-pass'
license=('GPL')
depends=('xdg-utils' 'rofi' 'gawk' 'pass' 'pwgen' 'xdotool' 'xclip')
optdepends=('passed-git: change fieldnames in password files'
            'pass-otp: for OTP support')
conflicts=('rofi-pass-git')
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/carnager/${pkgname}/archive/${pkgver}.tar.gz)
md5sums=('f32e96d186bbd32a84e43974628efb9d')


package() {
    make -C "${pkgname}-${pkgver}" DESTDIR="$pkgdir" PREFIX="/usr" install
}
