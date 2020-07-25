# Maintainer: Pablo Lezaeta <prflr 88 (arroba) gmail (dot) com>
# Maintainer: Víctor González <mrvikxd@gmail.com>
# Contributor: Thayer Williams <thayer@archlinux.org>

pkgname=archlinux-artwork
pkgver=1.6
pkgrel=6
pkgdesc='Official logos, icons, CD labels and other artwork for Arch Linux'
arch=("any")
url="http://www.archlinux.org/"
license=("CCPL:cc-by-nc-sa" "custom:TRADEMARKS")
source=("${pkgname}-${pkgver}.tar.gz::https://sources.archlinux.org/other/artwork/${pkgname}-${pkgver}.tar.gz")
md5sums=('85d812728309acaa6c9a07e41e3e7e65')

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  install -d "${pkgdir}/usr/share/archlinux"/{docs,cd-labels,icons,logos,wmlogos,web}
  install -m644 FONTS "${pkgdir}/usr/share/archlinux/docs"
  install -m644 TRADEMARKS "${pkgdir}/usr/share/archlinux/docs"
  install -m644 cd-labels/* "${pkgdir}/usr/share/archlinux/cd-labels"
  install -m644 icons/* "${pkgdir}/usr/share/archlinux/icons"
  install -m644 logos/* "${pkgdir}/usr/share/archlinux/logos"
  install -m644 wmlogos/* "${pkgdir}/usr/share/archlinux/wmlogos"
  install -m644 web/* "${pkgdir}/usr/share/archlinux/web"

  # add the custom license
  install -D -m644 TRADEMARKS "${pkgdir}/usr/share/licenses/${pkgname}/TRADEMARKS"
}
