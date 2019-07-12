# Creator: Herbert Knapp <herbert.knapp@edu.uni-graz.at>
# Maintainer: Milo Gilad <myl0gcontact@gmail.com>
pkgname=waterfox-bin
pkgver=56.2.12
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
sha512sums=('a7ece8f3f8ab8f5205d0acd863365ce9d7965550e8231ded380a89d8e5d2a220992380bdbc3a1f59f72588d40f82358b38ce7b3456c6f7c0066c13779b58ee85'
            'b83a0f0367a1d0dec08dc06d2172f9258caecafe350b68c47727d7d1401da9cfda47a2a13e271595b450e917669a7a4ce220da37c24b381bc98f150f436dad28')
