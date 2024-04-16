# Maintainer: Jonian Guveli <jonian@hardpixel.eu>
#
# Contributor: ValHue <vhuelamo at gmail dot com>
# Contributor: yaroslav <proninyaroslav@mail.ru>
# Contributor: mrbit <giacomogiorgianni@gmail.com>
#
pkgname="curlew"
pkgver=0.2.5
pkgrel=4
pkgdesc="Easy to use, Free and Open-Source Multimedia converter for Linux in Python"
url="https://curlew.sourceforge.io"
arch=("any")
license=('Waqf GPL')
depends=("python" "python-gobject" "python-dbus" "python-xdg" "xdg-utils" "ffmpeg" "mediainfo")
makedepends=("python-setuptools" "intltool" "librsvg")
optdepends=("curl: uploader support")
source=("http://downloads.sourceforge.net/project/${pkgname}/${pkgname}-${pkgver}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('8f645bc3a4897ac61eaec5be19c16b515d164552554ac0791a60731be1ea22a9')

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  sed -i "130 a\      packages=[]," setup.py

  python setup.py install --prefix=/usr --root="${pkgdir}/" --optimize=1
}
