# Maintainer: Fredy García <frealgagu at gmail dot com>
# Contributor: Jameson Pugh <imntreal@gmail.com>
# Contributor: tjbp (archlinux@tjbp.net)
 
pkgname=shashlik-bin
pkgver=0.9.3
pkgrel=3
pkgdesc="A way to run Android applications on a standard Linux desktop as easily and simply as possible"
arch=("x86_64")
url="http://www.shashlik.io"
license=("GPL")
depends=("lib32-libgl")
optdepends=("kdialog" "python")
provides=("${pkgname%-bin}")
conflicts=("${pkgname%-bin}")
source=("${pkgname}-${pkgver}.deb::http://static.davidedmundson.co.uk/shashlik/${pkgname%-bin}_${pkgver}.deb")
sha256sums=("a0a9daaeea0436ec8bd90b97112694974f7cf121d5a54083244488ff2d86dbaa")

build() {
  cd "${srcdir}"
  
  msg2 "Extracting data from debian package"
  bsdtar -xf data.tar.xz -C .
  
  msg2 "Adding write permissions to folder /opt/shashlik/android/system"
  chmod u+w "${srcdir}/opt/shashlik/android/system"
}

package() {
  cd "${srcdir}"
  
  install -dm755 "${pkgdir}/usr/bin"
  install -dm755 "${pkgdir}/opt/${pkgname}"
  
  msg2 "Installing application into /opt/${pkgname}"
  cp -r "${srcdir}/opt/${pkgname%-bin}/"* "${pkgdir}/opt/${pkgname}/"

  msg2 "Creating links into /usr/bin"
  ln -s /opt/${pkgname}/bin/${pkgname%-bin}-run "${pkgdir}/usr/bin/"
  ln -s /opt/${pkgname}/bin/${pkgname%-bin}-install "${pkgdir}/usr/bin/"
}
