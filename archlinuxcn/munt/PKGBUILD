# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
# Contributor: Tom < reztho at archlinux dot org >
# Based on the munt-git package from Franco Tortoriello
pkgbase=munt
pkgname=(munt munt-qt munt-daemon munt-smf2wav)
pkgdesc='Software synthesizer emulating pre-GM MIDI devices such as the Roland MT-32, CM-32L, CM-64 and LAPC-I'
pkgver=2.7.2
_tag="libmt32emu_${pkgver//./_}"
pkgrel=2
arch=(i686 x86_64 aarch64)
url=http://munt.sourceforge.net
license=('GPL-2.0 OR LGPL-2.1')
makedepends=(cmake qt6-multimedia portaudio)
source=("$pkgbase-$pkgver.tar.gz::https://github.com/munt/munt/archive/refs/tags/$_tag.tar.gz"
        munt-daemon.service)
b2sums=('af97564a099c8d38d31f1725dfcd7807a3e3fd64d0fe82dc45d783589ac11c694e6d45a3231b19e10ce2bba6325f343f836bc94b9696779366ca773e50dab88d'
        '40a006d8138ff0492e3fef89a5b7d74a5d255259da08f575e989ac569ff5a181351b06e175fcf846d68aeca97cd5a1dec2c128037f760db2046850f5ca3641d8')

build () {
	rm -rf _build
	cmake -S "$pkgname-$_tag" -B _build \
		-DBUILD_SHARED_LIBS=ON \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-Dmunt_WITH_MT32EMU_QT=ON \
		-Dmunt_WITH_MT32EMU_SMF2WAV=ON
	make -C _build

	make -C "$pkgname-$_tag/mt32emu_alsadrv" \
		INCLUDES="-I$(pwd)/_build/mt32emu/include" \
		CXXFLAGS="-L$(pwd)/_build/mt32emu $CXXFLAGS -Wno-write-strings -Wno-unused-result" \
		mt32d
}

package_munt () {
	install -dm755 "$pkgdir/usr/share/mt32-rom-data"
	make -C _build/mt32emu DESTDIR="$pkgdir" install

	pkgdesc+=" (library)"
	install=$pkgname.install
}

package_munt-qt () {
	make -C _build/mt32emu_qt DESTDIR="$pkgdir" install

	pkgdesc+=" (Qt GUI application)"
	depends+=("munt=$pkgver" qt6-multimedia hicolor-icon-theme portaudio)
}

package_munt-daemon () {
	cd "$pkgbase-$_tag/mt32emu_alsadrv"

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
	make -C _build/mt32emu_smf2wav DESTDIR="$pkgdir" install

	pkgdesc+=" (smf2wav tool)"
	depends+=("munt=$pkgver" glib2)
}
