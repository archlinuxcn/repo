# Maintainer: Denis Kasak <dkasak AT termina.org.uk>

pkgname=english-wordnet
pkgdesc="A fork of the Princeton Wordnet developed under an open source methodology."
pkgver=2025
pkgrel=3
arch=('any')
conflicts=(wordnet-common)
provides=(wordnet-common)
url="https://en-word.net/"
license=("custom")
source=("https://en-word.net/static/english-wordnet-${pkgver}.zip"
        "https://raw.githubusercontent.com/globalwordnet/english-wordnet/refs/tags/${pkgver}-edition/LICENSE.md")
sha256sums=('38b16326159f51853626b7d24a44c453fa88ab33f06fce5ec8fc5996d1c2be93'
            '672cc8b5663e8dc74c4b07a9dcf477193853575b119908fd3dc0aeeb60a9dbbb')

package() {
  install -d -m755 "${pkgdir}/usr/share/wordnet"
  install -m644 "${srcdir}"/oewn${pkgver}/* "${pkgdir}/usr/share/wordnet"

  # Support programs expecting old data location
  ln -s /usr/share/wordnet "${pkgdir}/usr/share/wordnet/dict"

  install -D -m644 LICENSE.md "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
