# Original maintainer: td123 <gostrc AT gmail DOT com>
# Previous maintainer: phoenixlzx < phoenixlzx AT phoenixsec DOT org >
# Maintainer:  P. A. López-Valencia <palopezv AT gmail DOT com>

# This file is provided to you under the terms of the BSD 2-clause
# license. <http://opensource.org/licenses/BSD-2-Clause>

# Patches welcome. Send pull requests to
# https://github.com/palopezv/vuze-bin-archlinux

pkgname=vuze
pkgver=5.0.0.0
pkgrel=6
# _ver=${pkgver//./} # Just for reference, this is how it should be done.
_ver=5000 # So people can download the file from the AUR page directly.
_extra= # Extra version used in debotched releases, usually takes months... Or years.
pkgdesc="The bittorrent kitchen-sink servlet."
provides=("azureus")
arch=('i686' 'x86_64')
url="http://azureus.sf.net/"
license=('GPL')
depends=('java-runtime' 'desktop-file-utils')
makedepends=('unzip')
install="$pkgname.install"
options=(!strip)
PKGEXT=".pkg.tar"

optdepends=(
	'xulrunner192: for vuze channels GUI. Long compile ahead.'
	'webkitgtk2: for vuze channels GUI instead of xulrunner192. Crash prone.'
	'vuze-plugin-mldht: Talk DHT to uTorrent, Transmission, etc.'
	'vuze-plugin-i2p: Use the i2p dark-net.'
	)

noextract=("Vuze_${_ver}${_extra}.jar" "azrating_1.4.2.jar" "azupnpav_0.4.7.zip")

source=(
	 "http://downloads.sourceforge.net/azureus/vuze/Vuze_${_ver}/Vuze_${_ver}${_extra}_linux.tar.bz2"
	 "http://downloads.sourceforge.net/azureus/vuze/Vuze_${_ver}/Vuze_${_ver}${_extra}.jar"
	 "http://plugins.vuze.com/plugins/azrating_1.4.2.jar"
	 "http://plugins.vuze.com/plugins/azupnpav_0.4.7.zip")

package() {
	cd "$srcdir/$pkgname"

        # Create target directories

        install -d "$pkgdir/usr/bin"
        install -d "$pkgdir/usr/share/vuze"
        install -d "$pkgdir/usr/share/applications"
        install -d "$pkgdir/usr/share/gconf/schemas"
        install -d "$pkgdir/usr/share/pixmaps"
        install -d "$pkgdir/usr/share/licenses/vuze"


	# Install desktop entries

	install -m644 vuze.desktop -t "$pkgdir/usr/share/applications"


	# Add magnet mime-type to desktop file.

	sed -i -e 's#\(x-bittorrent\)#\1;x-scheme-handler/magnet;#' \
		-e 's#^\(Exec=vuze \)%f#\1%U#' "$pkgdir/usr/share/applications/vuze.desktop"


	install -pm644 vuze.png -t "$pkgdir/usr/share/pixmaps"
	install -pm644 vuze.torrent.png -t "$pkgdir/usr/share/pixmaps"
	install -pm644 vuze.schemas -t "$pkgdir/usr/share/gconf/schemas"


	# install SWT

	if [[ $CARCH == i686 ]] ; then
		install -pm644 swt/swt32.jar -t "$pkgdir/usr/share/vuze"
	elif [[ $CARCH == x86_64 ]] ; then
		install -pm644 swt/swt64.jar -t "$pkgdir/usr/share/vuze"
	fi


	# install vuze

	install -m755 vuze -t "$pkgdir/usr/bin"


	# Fix internal directory name

	sed -i 's|#PROGRAM_DIR="/home/username/apps/azureus"|PROGRAM_DIR="/usr/share/vuze"|' "$pkgdir/usr/bin/vuze"


	# This should be all but... Sigh... 

	#install -pm644 Azureus2.jar -t "$pkgdir/usr/share/vuze"


	# Install system-wide plugins

	cp -a "$srcdir/$pkgname/plugins" "$pkgdir/usr/share/vuze"

	# install the license

	install -pm644 TOS.txt -t "$pkgdir/usr/share/licenses/vuze"
	
	
	# We really, really, shouldn't need anything below this line.

	install -pm644 "$srcdir/Vuze_${_ver}${_extra}.jar" -t "$pkgdir/usr/share/vuze"

	# When the updater fails to install in system directories, the program falls in an endless
	# loop. And won't push to the user directories either. They released these loose updates
	# less than 24 hours after main release yet won't release a fixed linux package.
	# And what about all the other out-dated junk? Disappointing.

	install -pm644 "$srcdir/azrating_1.4.2.jar" -t "$pkgdir/usr/share/vuze/plugins/azrating"
	unzip -qq -o -d "$pkgdir/usr/share/vuze/plugins/azupnpav" "$srcdir/azupnpav_0.4.7.zip"

	rm -f "$pkgdir/usr/share/vuze/plugins/azplugins/azplugins_2.1.6.jar"
	rm -f "$pkgdir/usr/share/vuze/plugins/azrating/azrating_1.3.1.jar"
	rm -f "$pkgdir/usr/share/vuze/plugins/azupnpav/azupnpav_0.4.4.jar"
	rm -f "$pkgdir/usr/share/vuze/plugins/azupnpav/azupnpav_0.4.6.jar"
}

sha256sums=('720f51155dbf95674e833d964fe4d2d3356588fe46d8a1df9735d8f29fe5d906'
            '037587fe5180d2488d7db4257afbe8ad32d9dc66a7ad3d1de7b56eb73e9b6569'
            '393b7fd8fec99f799c00b51ea49c0d8b36dce423b32308eeff7c40a9d892b7de'
            '5ce4ec2787deb44f693170f962c5aaa7a5ebcbb3f1d725c644b4de9fb3346a11')
