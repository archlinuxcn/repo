# Maintainer: Butui Hu <hot123tea123@gmal.com>
# Contributor: Sebastiaan Lokhorst <sebastiaanlokhorst@gmail.com>

pkgname=imagej2
pkgver=2.0.0_rc_71
_pkgver=${pkgver//_/-}
pkgrel=1
pkgdesc='Open scientific N-dimensional image processing'
arch=('x86_64')
url='https://imagej.net'
license=('BSD')
depends=(
  'glibc'
  'java-runtime=8'
)
makedepends=(
  'gendesk'
  'java-environment=8'
  'maven'
)
source=("https://github.com/imagej/imagej/archive/imagej-${_pkgver}.tar.gz")
sha256sums=('ef93850c9d1c5a8247295bc92e1c742579c5616305e7cbc661f24da2643b5169')

prepare() {
  echo 'Creating desktop file'
  gendesk -f -n --pkgname ${pkgname} \
    --pkgdesc "${pkgdesc}" \
    --categories 'Graphics;Science;Biology;' \
    --icon "${pkgname}" \
    --exec "${pkgname} %f"
}

build() {
  cd imagej-imagej-${_pkgver}

  # only building with Java 8 is supported
  # https://github.com/imagej/imagej/issues/197#issuecomment-403531162
  export PATH=/usr/lib/jvm/java-8-openjdk/jre/bin/:$PATH
  mvn -Papp -Ppopulate-app
}

package() {
  install -d "${pkgdir}/opt" "${pkgdir}/usr/bin" "${pkgdir}/usr/share/pixmaps"
  cp -r "${srcdir}/imagej-imagej-${_pkgver}/ImageJ.app" "${pkgdir}/opt/${pkgname}"
  rm -rfv "${pkgdir}/opt/${pkgname}/Contents" "${pkgdir}/opt/${pkgname}/*.exe"

  cat > "${pkgdir}/usr/bin/${pkgname}" << EOF
#!/bin/bash
if [ -d /usr/lib/jvm/java-8-jdk/bin ]; then
  PATH=/usr/lib/jvm/java-8-jdk/bin:${PATH} /opt/${pkgname}/ImageJ-linux64
elif [ -d /usr/lib/jvm/java-8-openjdk/bin ]; then
  PATH=/usr/lib/jvm/java-8-openjdk/bin:${PATH} /opt/${pkgname}/ImageJ-linux64
else
  echo "Error, no compatiable java found! ${pkgname} depends on java 8"
fi
EOF

  chmod 755 "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 "imagej-imagej-${_pkgver}/logo/imagej.png" "${pkgdir}/usr/share/pixmaps/${pkgname}.png"
  install -Dm644 "${srcdir}/${pkgname}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
  install -Dm644 "${srcdir}/imagej-imagej-${_pkgver}/LICENSE.txt" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
