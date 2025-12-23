# Maintainer: gehenna14 <bernkastel1337@disroot.org>
# Contributor: Steffen Weber <-boenki-gmx-de->
# Contributor: Thayer Williams <thayer@archlinux.org>
# Contributor: James Rayner <james@archlinux.org>
# Contributor: Justin Gottula <justin@jgottula.com>
# Contributor: nyanpasu64 <nyanpasu64@tuta.io>

pkgname=tango-icon-theme
pkgver=0.8.90
pkgrel=17
pkgdesc="Icon theme that follows the Tango visual guidelines"
arch=('any')
url="http://tango.freedesktop.org"
license=('custom:public domain' 'custom:TRADEMARKS')
makedepends=('imagemagick' 'librsvg' 'icon-naming-utils' 'intltool' 'parallel')
options=(!strip !zipman)
source=(${url}/releases/${pkgname}-${pkgver}.tar.bz2
        symbol.svg
        TRADEMARKS
        imagemagick.patch
        convert-parallel-scalable.patch
        convert-parallel-22x22.patch)
md5sums=('b7b9b16480afb781a4c13f8bceb8688b'
         'e9c0c2e165f2883c3fa00277635ae4ae'
         '538362c9ff75fd6939d9024ac4329430'
	 'c6dc8bd449392af2a4f6f6e07fc8ed78'
         '61313bb3c31f5f525a7c2fc304500059'
         'd0c7068b7da4b78b65f2f3859a4bdbd7')

prepare() {
  cd ${pkgname}-${pkgver}
  patch < "${srcdir}/imagemagick.patch"

  # patch the makefiles so they will run parallel instances of ImageMagick,
  # instead of painfully running convert instances serially one-file-at-a-time
  # (DRAMATIC reduction in package build time for multi-core machines!)
  for file in scalable/*/Makefile.am; do
    patch -uN $file "${srcdir}/convert-parallel-scalable.patch"
  done
  for file in 22x22/*/Makefile.am; do
    [[ "$file" == *"/animations/"* ]] && continue
    patch -uN $file "${srcdir}/convert-parallel-22x22.patch"
  done

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
   magick -background none -density "%[fx:96*${size}/48]" "${srcdir}/symbol.svg" \
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
