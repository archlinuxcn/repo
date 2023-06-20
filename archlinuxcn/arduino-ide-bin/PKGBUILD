# Maintainer: SuperNinja_4965
# Contributor: FabioLolix
# Contributor: netroy

pkgname=arduino-ide-bin
pkgver=2.1.0
pkgrel=1
pkgdesc="Arduino prototyping platform IDE, rewrite based on the Theia IDE framework."
arch=(x86_64)
url="https://github.com/arduino/arduino-ide"
license=(AGPL3)
depends=(libxkbfile libxss nss libsecret git)
optdepends=('libusb: Needed for some libraries or boards'
            'usbutils: Needed for stm32 boards using st-link'
            'libusb-compat: Needed for the `micronucleus` cli utility'
            'python-pyserial: Needed for esptool')
provides=(arduino-ide)
conflicts=(arduino-ide)
replaces=(arduino-ide-beta-bin)
options=(!strip)
source=("https://github.com/arduino/arduino-ide/releases/download/${pkgver}/arduino-ide_${pkgver}_Linux_64bit.zip"
        "https://www.arduino.cc/wiki/370832ed4114dd35d498f2f449b4781e/arduino.svg")
sha256sums=('846766712ea00fa70ac8f57b462b219a02558936ce116a14f117bed0dd3a7640'
            '4137981bcb4057c2e0092f22faea287767f102e0b48497d22cd55e8d6988e4ac')

prepare() {
	echo -e "[Desktop Entry]\nType=Application\nName=Arduino IDE v2\nGenericName=Arduino IDE v2\nComment=Open-source electronics prototyping platform\nExec=arduino-ide %U\nIcon=arduino-ide-v2\nTerminal=false\nMimeType=text/x-arduino;\nCategories=Development;IDE;Electronics;\nKeywords=embedded electronics;avr;microcontroller;\nStartupWMClass=Arduino IDE" > arduino-ide-v2.desktop
}

package() {
	install -dm755 "$pkgdir/opt/"
	mv "arduino-ide_${pkgver}_Linux_64bit" "arduino-ide"
	chmod -R 755 "arduino-ide"
	cp -r "arduino-ide" "$pkgdir/opt/arduino-ide"
	install -dm755 "$pkgdir/usr/bin"
	ln -s "/opt/arduino-ide/arduino-ide" "$pkgdir/usr/bin/arduino-ide"
	install -Dm644 "arduino-ide-v2.desktop" "$pkgdir/usr/share/applications/arduino-ide-v2.desktop"
	install -Dm644 "arduino.svg" "$pkgdir/usr/share/pixmaps/arduino-ide-v2.svg"
}
