# Creator: Herbert Knapp <herbert.knapp@edu.uni-graz.at>
# Maintainer: Milo Gilad <myl0gcontact@gmail.com>
pkgname=waterfox-bin
pkgver=56.2.13
pkgrel=1
pkgdesc="64-Bit optimized Firefox, no data collection, allows unsigned extensions"
arch=('x86_64')
url="https://www.waterfoxproject.org/"
license=('MPL')
depends=('libxt' 'libnotify' 'mime-types' 'nss' 'gtk2' 'gtk3' 'sqlite' 'dbus-glib')
optdepends=('alsa-lib' 'pulseaudio')
provides=("${pkgname%-bin}")
conflicts=("${pkgname%-bin}")
source=('waterfox.desktop' 'https://storage-waterfox.netdna-ssl.com/releases/linux64/installer/waterfox-'"${pkgver}"'.en-US.linux-x86_64.tar.bz2')

package() {
  install -d "${pkgdir}"/{usr/{bin,share/{applications,pixmaps}},opt}
  install -m644 "${srcdir}"/waterfox.desktop "${pkgdir}"/usr/share/applications/
  install -m644 "${srcdir}"/waterfox/browser/chrome/icons/default/default128.png "${pkgdir}"/usr/share/pixmaps/waterfox-icon.png
  cp -r waterfox "${pkgdir}"/opt/
  ln -s /opt/waterfox/waterfox "${pkgdir}"/usr/bin/
}
sha256sums=('ce7c07ffce4faab534b7961947b062a33a8fd377b9a6c51474bc0263ef35cc8d'
            '448507ca9bd90f934fb18ee927848af990cfac888b3ce495893b78af7dc696d1')
