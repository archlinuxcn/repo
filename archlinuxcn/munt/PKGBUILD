# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
# Contributor: Tom < reztho at archlinux dot org >
# Based on the munt-git package from Franco Tortoriello
pkgbase=munt
pkgname=(munt munt-qt munt-daemon munt-smf2wav)
pkgdesc='Software synthesizer emulating pre-GM MIDI devices such as the Roland MT-32, CM-32L, CM-64 and LAPC-I'
pkgver=2.7.0
pkgrel=6
arch=(i686 x86_64 aarch64)
url=http://munt.sourceforge.net
license=('GPL-2.0 OR LGPL-2.1')
makedepends=(cmake qt6-multimedia portaudio)
source=("$pkgbase-$pkgver.tar.gz::https://sourceforge.net/projects/$pkgbase/files/$pkgbase/$pkgver/$pkgbase-$pkgver.tar.gz/download"
        munt-daemon.service)
b2sums=('099beab9a568bbe9775730a8bf4d541ea367a78e12d726f3b1cd418d7b6d802f2d8680fa29a005f43b5b8c5f0a942f3ad95f120d295be71b77c379c5adb3f2c7'
        '40a006d8138ff0492e3fef89a5b7d74a5d255259da08f575e989ac569ff5a181351b06e175fcf846d68aeca97cd5a1dec2c128037f760db2046850f5ca3641d8')

build () {
	cd "$pkgname-$pkgver" 
	cmake \
		-DBUILD_SHARED_LIBS=ON \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-Dmunt_WITH_MT32EMU_QT=ON \
		-Dmunt_WITH_MT32EMU_SMF2WAV=ON
	make

	make -C mt32emu_alsadrv \
		INCLUDES="-I$(pwd)/mt32emu/include" \
		CXXFLAGS="-L$(pwd)/mt32emu $CXXFLAGS -Wno-write-strings -Wno-unused-result" \
		mt32d
}

package_munt () {
	install -dm755 "$pkgdir/usr/share/mt32-rom-data"
	make -C "$pkgbase-$pkgver/mt32emu" DESTDIR="$pkgdir" install

	pkgdesc+=" (library)"
	install=$pkgname.install
}

package_munt-qt () {
	make -C "$pkgbase-$pkgver/mt32emu_qt" DESTDIR="$pkgdir" install

	pkgdesc+=" (Qt GUI application)"
	depends+=("munt=$pkgver" qt6-multimedia hicolor-icon-theme portaudio)
}

package_munt-daemon () {
	cd "$pkgbase-$pkgver/mt32emu_alsadrv"

	install -Dm644 "$srcdir/$pkgname.service" \
		"$pkgdir/usr/lib/systemd/system/$pkgname.service"
	install -Dm644 README.txt "${pkgdir}/usr/share/doc/${pkgname}/README"
	install -Dm755 mt32d "${pkgdir}/usr/bin/mt32d"

	pkgdesc+=" (ALSA driver daemon)"
	depends+=("munt=$pkgver" alsa-lib gcc-libs)
	replaces=(munt-alsadrv)
	conflicts=(munt-alsadrv)
	install=$pkgname.install
}

package_munt-smf2wav () {
	make -C "$pkgbase-$pkgver/mt32emu_smf2wav" DESTDIR="$pkgdir" install

	pkgdesc+=" (smf2wav tool)"
	depends+=("munt=$pkgver" glib2)
}
