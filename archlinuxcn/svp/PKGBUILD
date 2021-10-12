# Maintainer: phiresky <phireskyde+git@gmail.com>
pkgname=svp
pkgver=4.5.210
_pkgver=${pkgver}-1
pkgrel=2
epoch=
pkgdesc="SmoothVideo Project 4 (SVP4)"
arch=('x86_64')
url="https://www.svp-team.com/wiki/SVP:Linux"
license=('custom')
groups=()
depends=(libmediainfo qt5-svg qt5-script qt5-declarative vapoursynth libusb xdg-utils lsof)
makedepends=(p7zip)
checkdepends=()
optdepends=(
	'mpv-git: needed for mpv vapoursynth support'
	'ocl-icd: for GPU acceleration'
)
provides=()
conflicts=()
replaces=()
backup=()
options=(!strip)
install=${pkgname}.install
changelog=
#source=("https://gist.githubusercontent.com/phiresky/1e2cbd30bed4e5978771af232d11afd1/raw/svp4-linux.$pkgver.tar.bz2")
source=("https://www.svp-team.com/files/svp4-linux.${_pkgver}.tar.bz2")
# I am rehosting the binaries taken from
# http://www.svp-team.com/files/svp4-linux-64.tbz2
# at https://gist.github.com/phiresky/1e2cbd30bed4e5978771af232d11afd1
# so they are correctly versioned and old versions still exist
# update 2019-10-06: svp-team.com now uses versioned file names.
# I'll keep rehosting them for now since i don't trust them to actually keep old versions.
noextract=()
sha256sums=('940d539ba50e4455fdaebbec07db03870f98f101fbb4ceadda013d1e00c90883')
validpgpkeys=()

prepare() {
	rm -rf "$srcdir/installer"
	mkdir "$srcdir/installer"
	echo "Finding 7z archives in installer..."
	LANG=C grep --only-matching --byte-offset --binary --text  $'7z\xBC\xAF\x27\x1C' "$srcdir/svp4-linux-64.run" |
		cut -f1 -d: |
		while read ofs; do dd if="$srcdir/svp4-linux-64.run" bs=1M iflag=skip_bytes status=none skip=$ofs of="$srcdir/installer/bin-$ofs.7z"; done

	echo "Extracting 7z archives from installer..."
	for f in "$srcdir/installer/"*.7z; do
		7z -bd -bb0 -y x -o"$srcdir/extracted/" "$f" || true
	done
}

#pkgver() {
#	xmllint --xpath '/Updates/PackageUpdate[Name="core.full"]/Version/text()' "$srcdir/installer/metadata/Updates.xml" | tr '-' '.'
#}

package() {
	mkdir -p "$pkgdir"/{opt/svp,usr/bin,usr/share/licenses/svp}
	if [[ -d "$srcdir/extracted/licenses" ]]; then
		mv "$srcdir/extracted/licenses" "$pkgdir/usr/share/licenses/$pkgname"
	fi
	mv "$srcdir/extracted/"* "$pkgdir/opt/$pkgname"
	# rm "$pkgdir/opt/$pkgname/extensions/libsvpcode.so" # previously this extension caused the whole thing to segfault. lmk if that's still the case
	ln -s "/opt/$pkgname/SVPManager" "$pkgdir/usr/bin/SVPManager"
	chmod -R +rX "$pkgdir/opt/svp" "$pkgdir/usr/share"
}
