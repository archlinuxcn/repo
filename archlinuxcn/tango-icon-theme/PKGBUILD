# Maintainer: Steffen Weber <-boenki-gmx-de->
# Contributor: Thayer Williams <thayer@archlinux.org>
# Contributor: James Rayner <james@archlinux.org>

pkgname=tango-icon-theme
pkgver=0.8.90
pkgrel=14
pkgdesc="Icon theme that follows the Tango visual guidelines"
arch=('any')
url="http://tango.freedesktop.org"
license=('custom:public domain' 'custom:TRADEMARKS')
makedepends=('imagemagick' 'icon-naming-utils' 'intltool' 'librsvg')
options=(!strip !zipman)
source=(${url}/releases/${pkgname}-${pkgver}.tar.bz2
        symbol.svg
        TRADEMARKS
        rsvg.patch)
md5sums=('b7b9b16480afb781a4c13f8bceb8688b'
         'e9c0c2e165f2883c3fa00277635ae4ae'
         '538362c9ff75fd6939d9024ac4329430'
         '40cb8a4dd485bac0851c6fd2915d43ba')

prepare() {
  cd ${pkgname}-${pkgver}
  patch -p0 < "${srcdir}/rsvg.patch"
  autoreconf -fi
}

build() {
  cd ${pkgname}-${pkgver}
  ./configure --prefix=/usr --enable-png-creation
  make
}

package() {
  cd ${pkgname}-${pkgver}
  make DESTDIR="${pkgdir}" install

  # install licenses
  install -Dm644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -m644 ../TRADEMARKS "${pkgdir}/usr/share/licenses/${pkgname}/"

  cd "${pkgdir}/usr/share/icons/Tango"

  # function using imagemagick to combine symbols with default folder-icon
  # used below to create xdg-folders
  comp() {
  composite -gravity center \( ${size}x${size}/"$1".png -resize 50% \) \
   ${size}x${size}/places/folder.png ${size}x${size}/places/folder-"$2".png
  }

  for size in 16 22 24 32 48 64 72 96 128; do
   # replace default logo with Arch Linux's
   convert -background none "${srcdir}/symbol.svg" -resize ${size}x${size}  \
    "${size}x${size}/places/start-here.png"
   # create icon for category "Education"
   ln -s "../status/dialog-information.png" \
    "${size}x${size}/categories/applications-science.png"

   # create xdg-folders
   comp apps/internet-web-browser publicshare
   comp actions/go-down download
   comp actions/document-properties templates
   comp mimetypes/audio-x-generic music
   comp mimetypes/image-x-generic pictures
   comp mimetypes/video-x-generic videos
   comp mimetypes/x-office-document documents
  done

  install -Dm644 "${srcdir}/symbol.svg" \
   "scalable/places/start-here.svg"
  ln -s "../status/dialog-information.svg" \
   "scalable/categories/applications-science.svg"
}
