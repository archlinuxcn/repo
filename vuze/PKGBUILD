# Original maintainer: td123 <gostrc at gmail.com>
# Previous maintainer: phoenixlzx < phoenixlzx at phoenixsec.org >
# Maintainer: Vorbote <palopezv at gmail.com>

# This file is provided to under the terms of the BSD 2-clause
# licence. <http://opensource.org/licenses/BSD-2-Clause>

# Patches welcome. Send pull requests to
# https://github.com/vorbote/archlinux-vuze

pkgname=vuze
pkgver=4.9.0.0
pkgrel=1
_ver=${pkgver//./}
_extra=
pkgdesc="One of the most powerful bitTorrent client with GUI in the world, written in Java."
arch=('i686' 'x86_64')
url="http://azureus.sf.net/"
license=('GPL')
depends=('java-runtime' 'desktop-file-utils')
optdepends=(
	'xulrunner192: for vuze channels GUI. Long compile ahead.'
	'webkitgtk2: for vuze channels GUI instead of xulrunner192. Crash prone.'
	)
install=vuze.install
options=(!strip)

source=(
  "http://downloads.sourceforge.net/azureus/vuze/Vuze_${_ver}/Vuze_${_ver}${_extra}_linux.tar.bz2")

package() {
  cd "${srcdir}/${pkgname}"

  #install systemwide plugins
  mkdir -p "${pkgdir}/usr/share/vuze"
  cp -a "${srcdir}/${pkgname}/plugins" "${pkgdir}/usr/share/vuze/"

  # Add magnet mimetype to desktop file.
  # This works as shoot-from-the-hip hack but I feel so dirty,
  # I'll go get a shower now.
  #
  # And I missed the magic %U. Thanks j_r0dd for the prodding.
  #
  sed -i.bak -e 's#\(x-bittorrent\)#\1;x-scheme-handler/magnet;#' \
    -e 's#^\(Exec=vuze \)%f#\1%U#' vuze.desktop


  #install desktop entries
  install -Dm644 vuze.desktop  "${pkgdir}/usr/share/applications/vuze.desktop"
  install -Dm644 vuze.png "${pkgdir}/usr/share/pixmaps/vuze.png"
  install -Dm644 vuze.torrent.png "${pkgdir}/usr/share/pixmaps/vuze.torrent.png"
  install -Dm644 vuze.schemas "${pkgdir}/usr/share/gconf/schemas/vuze.schemas"

  # install SWT
  if [[ $CARCH == i686 ]] ; then
    install -Dm644 swt/swt32.jar "${pkgdir}/usr/share/vuze/swt32.jar"
  elif [[ $CARCH == x86_64 ]] ; then
    install -Dm644 swt/swt64.jar "${pkgdir}/usr/share/vuze/swt64.jar"
  fi

  # install vuze
  install -Dm755 vuze "${pkgdir}/usr/bin/vuze"
  sed -i 's|#PROGRAM_DIR="/home/username/apps/azureus"|PROGRAM_DIR="/usr/share/vuze"|' ${pkgdir}/usr/bin/vuze
  install -Dm644 Azureus2.jar "${pkgdir}/usr/share/vuze/Azureus2.jar"

}

sha256sums=('1e8c9e7c6005cfefe212d4abd02c18e35a3d5b9a6722712e464ef17633235300')
