# Maintainer: Cayde Dixon <me@cazzar.net>
# Contributor: Anthony Anderson <aantony4122@gmail.com>


_branch='discord'

pkgname=discord
pkgver=0.0.5
pkgrel=2
pkgdesc="All-in-one voice and text chat for gamers that's free and secure."
arch=('x86_64')
url='https://discordapp.com/'
license=('custom')
depends=('gtk2' 'gconf' 'libnotify' 'libxss' 'glibc' 'alsa-lib' 'nspr' 'nss' 'libc++')
optdepends=(
  'libpulse: For pulseaudio support'
  'noto-fonts-emoji: Google font for emoji support.'
  'ttf-symbola: Font for emoji support.'
)

install="Discord.install"
source=(Discord.desktop LICENSE)
source_x86_64=("https://dl.discordapp.net/apps/linux/${pkgver}/${_branch}-${pkgver}.tar.gz")
md5sums=('a9046504943624ac4861983d67a1404b'
         '26b3229c74488c64d94798e48bc49fcd')
md5sums_x86_64=('18a8e7f86d26a1472dbfff060e1671e4')



#This is always latest build, right now I do not know of a version param.

package() {
  # Install the main files.
  install -d "${pkgdir}/opt/${pkgname}"
  cp -a "${srcdir}/Discord/." "${pkgdir}/opt/${pkgname}"

  # Exec bit
  chmod 755 "${pkgdir}/opt/${pkgname}/Discord"


  # Desktop Entry
  install -d "${pkgdir}/usr/share/applications"
  install "${srcdir}/Discord.desktop" "${pkgdir}/usr/share/applications"

  # Main binary
  install -d "${pkgdir}/usr/bin"
  #install "${srcdir}/Discord.sh" "${pkgdir}/usr/bin/discord"
  ln -s "/opt/${pkgname}/Discord" "${pkgdir}/usr/bin/${pkgname}"

  # Create symbolic link to the icon
  install -d "${pkgdir}/usr/share/pixmaps"
  ln -s "/opt/${pkgname}/discord.png" "${pkgdir}/usr/share/pixmaps/${pkgname}.png"

  # License
  install -Dm644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
