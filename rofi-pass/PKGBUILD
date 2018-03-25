# Maintainer: Lex Black <autumn-wind at web dot de>

pkgname=rofi-pass
pkgver=2.0.1
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
md5sums=('2e78da9173977117b4236e18acd85861')


package() {
    make -C "${pkgname}-${pkgver}" DESTDIR="$pkgdir" PREFIX="/usr" install
}
