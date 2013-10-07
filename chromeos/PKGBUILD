# Maintainer: Robert Pitt <robertpitt1988@gmail.com>
pkgname=chromeos
pkgver=1.0.0
pkgrel=2
pkgdesc="Installs Chromium OS browser. Adds shortcuts to user login, which enables Chromium OS UI right from the start."
url="https://plus.google.com/+RobertPitt"
install=chromeos.install
depends=(
		'matchbox-window-manager'
		'curl'
		'python'
		'python-dbus'
		'unzip'
)
#matchbox-window-manager, curl, python3, python-dbus
optdepends=('google-chrome-stable: Google Chrome browser
			 google-talkplugin: Hangouts, Google Talk plugin. Bound to chromeos')
arch=('x86_64')
license=('GPL')
md5sums=('5ba35b608541eab3f44ae2885b9c5ee0')
source=(wrap.zip)

build() {
	cd ${srcdir}

	msg "Finding latst ChromeOS Build"
	LKGR=$(curl --silent http://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_ChromiumOS/LAST_CHANGE)
	URL="http://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux_ChromiumOS/${LKGR}/chrome-linux.zip"

	msg "Downloading Chrome OS... Build: $LKGR"
	curl --silent -z "chrome-linux.zip" -o "chrome-linux.zip" -L "$URL"
	
	msg "Extracting Chrome OS... Build: $LKGR"
	unzip -qq "chrome-linux.zip" -d "$srcdir/opt"
}

package() {
	#Move the chrome os
	msg "Creating package structure"
	mv "$srcdir/opt" "$pkgdir"
	mv "$srcdir/usr" "$pkgdir"
	mv "$pkgdir/opt/chrome-linux" "$pkgdir/opt/chromeos"

	msg "Fixing file permissions..."
	chmod 775 -R "$pkgdir/opt/chromeos"
	chown root:root "$pkgdir/usr/bin/chromeos"
	chown root:root "$pkgdir/usr/bin/chromeos-dm"
	chown root:root "$pkgdir/usr/bin/chromeos-plain"
	chown root:root "$pkgdir/usr/share/xsessions/chromeos.desktop"
}