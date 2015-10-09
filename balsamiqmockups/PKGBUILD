# Maintainer: John K. Luebs <jkl@johnluebs.com>
# Contributor: Vojtěch Kusý <https://github.com/wojtha>

# I maintain this on github, feel free to submit a pull request to
# https://github.com/jkl1337/packages-archlinux.git

pkgname=balsamiqmockups
pkgver=2.2.28
license=('custom')
pkgrel=4
arch=('any')
pkgdesc="The Adobe Air based Mockup client. Not free or open source, there is a 7 day free trial."
url=('http://balsamiq.com/products/mockups')
source=("https://build_archives.s3.amazonaws.com/mockups-desktop/2.2/MockupsForDesktop2.2.28-2015.08.24.air"
        "http://media.balsamiq.com/files/BalsamiqEula.pdf"
        'fix-filetype-mime.patch'
        'balsamiqmockups.desktop'
        'vnd.balsamiq.bmml+xml.xml')
sha1sums=('4c541244c7214ede9e1e4aa498bf1b8c2df597fd'
          '1c9ad856fd7596fd8b5505a8ad43a713b16a37dc'
          '279e15c0c1bcffeabc97d9af3882c849735b5aa9'
          'cfe7240b7403ff47d63e9f8264581a40112607ff'
          '6f28b1fcc5758cb46c5f149d7896b53bdd027293')
noextract=("MockupsForDesktop2.2.28-2015.08.24.air")
install=balsamiqmockups.install
depends=(adobe-air-sdk desktop-file-utils lib32-libgl)
makedepends=(unzip)
conflicts=('balsamiq-mockups')

build () {
  cd "${srcdir}"

  mkdir -p $pkgname
  cd "${srcdir}/${pkgname}"
  unzip -o "${srcdir}/MockupsForDesktop2.2.28-2015.08.24.air"

  msg2 "Apply patch fix-filetype-mime.patch"
  patch -Np1 -i "$srcdir/fix-filetype-mime.patch"
}

package () {
  cd "${srcdir}"

  install -dm755 "${pkgdir}/opt/airapps"

  install -Dm644 BalsamiqEula.pdf "${pkgdir}/usr/share/licenses/balsamiqmockups/BalsamiqEula.pdf"
  install -dm755 "${pkgdir}/opt/airapps"
  cp -pr "${pkgname}" "${pkgdir}/opt/airapps"

  install -dm755 "${pkgdir}/usr/bin"
  echo "#!/bin/bash" > "${pkgdir}/usr/bin/balsamiqmockups"
  echo "/opt/adobe-air-sdk/bin/adl -nodebug /opt/airapps/balsamiqmockups/META-INF/AIR/application.xml /opt/airapps/balsamiqmockups/" >> "${pkgdir}/usr/bin/balsamiqmockups"
  chmod 755 "${pkgdir}/usr/bin/balsamiqmockups"

  for dim in 16 32 36 48 128 512; do
    install -d "$pkgdir"/usr/share/icons/hicolor/${dim}x${dim}/{apps,mimetypes}
    ln -s /opt/airapps/$pkgname/icons/mockups_ico_${dim}.png "${pkgdir}"/usr/share/icons/hicolor/${dim}x${dim}/apps/${pkgname}.png
    ln -s /opt/airapps/$pkgname/icons/mockups_doc_ico_${dim}.png "${pkgdir}"/usr/share/icons/hicolor/${dim}x${dim}/mimetypes/application-vnd.balsamiq.bmml+xml.png
  done

  install -Dm644 vnd.balsamiq.bmml+xml.xml "${pkgdir}/usr/share/mime/packages/vnd.balsamiq.bmml+xml.xml"
  install -Dm644 ${pkgname}.desktop "${pkgdir}/usr/share/applications/${pkgname}.desktop"
}
