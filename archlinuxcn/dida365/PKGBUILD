# Maintainer: Shengyu Zhang <la@archlinuxcn.org>
# Contributor: Agustin Cisneros <agustincc@tutanota.com>

pkgname=dida365
_pkgname=dida
pkgver=1.0.50
pkgrel=1

pkgdesc='Todo list, checklist and task manager app, Linux desktop application'
arch=('x86_64')
url='https://www.dida365.com/about/download'
license=('custom')
depends=('alsa-lib' 'gtk3' 'nss')
source=("${_pkgname}-${pkgver}.deb::https://cdn.dida365.cn/download/linux/linux_deb_x64/${_pkgname}-${pkgver}-amd64.deb"
        "LICENSE")
sha256sums=('fa4d50092af619a2573c07fd503d5ac1601d051ce1946298528f40dbc1327905'
            'e409ffec880f4b6578f03d0bc9f6fd3207bb6777c27f3e9f77c6ad54ebb312a2')

package() {
  cd "${srcdir}"

  tar -xf data.tar.xz -C "${pkgdir}"
  gunzip "${pkgdir}/usr/share/doc/${_pkgname}/changelog.gz"

  # Use symlink to run the program
  sed -i 's/^Exec=.*/Exec=dida %U/' "${pkgdir}/usr/share/applications/dida.desktop"

  mkdir -p "${pkgdir}/usr/lib" "${pkgdir}/usr/bin/"
  mv "${pkgdir}/opt/dida" "${pkgdir}/usr/lib/${_pkgname}"
  rmdir "${pkgdir}/opt"
  ln -srf "${pkgdir}/usr/lib/${_pkgname}/dida" "${pkgdir}/usr/bin/dida"

  # Install license from https://dida365.com/about/tos
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE"
  # Included licenses in .deb
  mv "${pkgdir}/usr/lib/${_pkgname}/LICENSE.electron.txt" \
     "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE.electron.txt"
  mv "${pkgdir}/usr/lib/${_pkgname}/LICENSES.chromium.html" \
     "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSES.chromium.html"
}
