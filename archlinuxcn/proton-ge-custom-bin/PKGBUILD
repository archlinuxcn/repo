## Maintainer:     Jaja <jaja@mailbox.org>
## Co-Maintainer:  floriplum <floriplum@mailbox.org>
## Co-Maintainer:  various people submitting to 'chaotic-aur' repo
## Credits:        barfin (aka RogueGirl) <barfin@protonmail.com>

## Linted using:
##   $ shellcheck PKGBUILD -e SC2034,SC2148,SC2154
## Formated using:
##   $ shfmt -w PKGBUILD

## pkginfo
pkgdesc='A fancy custom distribution of Valves Proton with various patches'
pkgname=proton-ge-custom-bin
pkgver=GE_Proton9_19
pkgrel=1
epoch=1
arch=('x86_64')
license=('BSD' 'LGPL' 'zlib' 'MIT' 'MPL' 'custom')
changelog=changelog.md
provides=('proton' "proton-ge-custom=${pkgver/_/.}")
conflicts=('proton-ge-custom')

## dependencies
depends=('python'
  'vulkan-icd-loader'
  'lib32-openal'
  'lib32-vkd3d'
  # libav support #
  'lib32-libva'
  'ffmpeg4.4'
  'lib32-speex'
  'lib32-libtheora'
  'lib32-libvdpau'
  # gstreamer support #
  'gst-plugins-bad-libs'
  'lib32-gst-plugins-base-libs'
  'libjpeg6-turbo'
  'graphene'
  'lib32-libjpeg6-turbo'
  'lib32-libgudev'
  'lib32-mpg123'
  'libsoup'
  # other #
  'lib32-openssl-1.1'
  'lib32-libusb')
optdepends=('kdialog: KDE splash dialog support'
  'zenity: GNOME splash dialog support'
  'python-kivy: splash dialog support (big picture mode)'
  'steam: use proton with steam like intended'
  'lib32-vulkan-icd-loader: dxvk dependency for 32bit prefixes'
  'vulkan-driver: driver to be used by dxvk'
  'winetricks: protonfixes backend - highly recommended'
  'wine: support for 32bit prefixes'
  'xboxdrv: gamepad driver service')

## makepkg options
options=(!strip emptydirs)
install=pleasenote.install

## fix naming conventions, matching upstream
_pkgname=${pkgname//-bin/}
_pkgver=${pkgver//_/-}
_srcdir=${_pkgver}

## paths and files
_protondir=usr/share/steam/compatibilitytools.d/${_pkgname}
_licensedir=usr/share/licenses/${pkgname}
_execfile=usr/bin/proton
_protoncfg=${_protondir}/user_settings.py

## user edited files to backup
backup=("${_protoncfg}")

## sources
url='https://github.com/GloriousEggroll/proton-ge-custom'
source=("${_pkgver}_${pkgrel}.tar.gz::${url}/releases/download/${_pkgver}/${_pkgver}.tar.gz"
  'user_settings.py'
  'launcher.sh'
  'pam_limits.conf')
sha512sums=('12005fbee734e4c0c55b710dd3d30330ae710598c4e189cb5b80fa0ba70384523dbf7003bc72906eb0b20d900f2fcd60914a42a2416d9408c924cb1e6e272a8a'
            'babe2a461118bef6a777656a10bb89abeee2c8c3ed4285eb1b99f5ba517b779f18372d1d93ed2cce63b0d8111cf0b08e14a0c92435680239f6936783c3e4cbc5'
            '78ede6d50f9c43407da511c8b37dcf60aae2ddbd461c0081f0d0ce3de08ace3a84dee86e9253acbac829b47c5818ef4e1a354ccb05feaa9853ce279dc3f903fd'
            'c64898bd41801470925fb0efdcf7d247e5cb476fb4745f83ceeccf12041474e5c309fb1c2ac1483b419d12b4ade7668c046bebded4e3bf4708737ee505b080a1')

build() {
  ## patches
  sed -i "s|_proton=echo|_proton=/${_protondir}/proton|" "${srcdir}"/launcher.sh
  sed -i -r 's|"GE-Proton.*"|"Proton-GE"|' "${_srcdir}"/compatibilitytool.vdf
  ## fixes from namcap inspection
  strip --preserve-dates --strip-unneeded "${_srcdir}"/files/bin/wine*
}

package() {
  ## create paths
  install -d "${pkgdir}/${_protondir}/"
  install -d "${pkgdir}/${_licensedir}/"
  install -d "${pkgdir}/$(dirname ${_execfile})/"
  install -d "${pkgdir}/etc/security/limits.d/"
  ## licenses
  mv "${_srcdir}/LICENSE" "${pkgdir}/${_licensedir}/license"
  mv "${_srcdir}/LICENSE.OFL" "${pkgdir}/${_licensedir}/license_OFL"
  mv "${_srcdir}/PATENTS.AV1" "${pkgdir}/${_licensedir}/license_AV1"
  ## config files
  install --mode=0775 --group=50 "${srcdir}"/user_settings.py "${pkgdir}/${_protoncfg}"
  install --mode=0644 "${srcdir}"/pam_limits.conf "${pkgdir}"/etc/security/limits.d/10-games.conf
  ## executables
  mv "${_srcdir}"/* "${pkgdir}/${_protondir}"
  install --mode=0755 "${srcdir}"/launcher.sh "${pkgdir}/${_execfile}"
}
