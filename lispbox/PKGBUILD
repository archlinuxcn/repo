# Maintainer: Phoenixlzx < phoenixlzx@dreamcoder.me >

pkgname=lispbox
pkgver=0.7
pkgrel=3
pkgdesc='Lispbox is an IDE for Common Lisp development.It is just a pre-configured packaging of the Emacs editing environment, SLIME (The Superior Lisp Interaction Mode for Emacs), the Quicklisp library manager, and the Clozure Common Lisp compiler.'
arch=('i686' 'x86_64')
url='http://www.common-lisp.net/project/lispbox/'
license=('GPL')
depends=('gtk2' 'libjpeg6' 'libpng12')
source=("http://www.common-lisp.net/project/lispbox/test_builds/lispbox-0.7-ccl-1.6-linuxx86.tar.gz" "http://www.archlinuxcn.org/download/lispbox.desktop")
md5sums=('b7e8283bb740adb1b656924088ed0f42' '21fcf1a018c67b323c5f74c247074695')
[[ $CARCH == 'x86_64' ]] && source=("http://www.common-lisp.net/project/lispbox/test_builds/lispbox-0.7-ccl-1.6-linuxx86-64.tar.gz" "http://www.archlinuxcn.org/download/lispbox.desktop") && md5sums=('132a3f508581e566c721cda1a511d5f4' '21fcf1a018c67b323c5f74c247074695')

package() {
  install -d ${pkgdir}/opt
  cp -r lispbox-0.7 ${pkgdir}/opt
  sed -i 's%#PROGRAM_DIR="/home/username/apps/lispbox-0.7"%PROGRAM_DIR="/opt/lispbox-0.7"%' ${pkgdir}/opt/lispbox-0.7/lispbox.sh
  install -Dm644 lispbox.desktop  ${pkgdir}/usr/share/applications/lispbox.desktop
}

