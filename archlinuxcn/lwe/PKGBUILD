pkgname=lwe
pkgver=0.9.11
pkgrel=1
pkgdesc="Linux dynamic wallpaper shell for Wallpaper Engine content"
arch=('x86_64')
url="https://github.com/YangYuS8/lwe"
license=('Apache-2.0')
depends=('cairo' 'desktop-file-utils' 'gdk-pixbuf2' 'glib2' 'gtk3' 'hicolor-icon-theme' 'libsoup3' 'mpv' 'pango' 'webkit2gtk-4.1')
provides=('lwe')
conflicts=('lwe-git')
source=("lwe_0.9.11_amd64.deb::https://github.com/YangYuS8/lwe/releases/download/v0.9.11/lwe_0.9.11_amd64.deb")
sha256sums=('SKIP')

package() {
	cd "${srcdir}"
	bsdtar -xf "lwe_${pkgver}_amd64.deb"

	local data_archive=""
	for candidate in data.tar.zst data.tar.xz data.tar.gz; do
		if [ -f "${candidate}" ]; then
			data_archive="${candidate}"
			break
		fi
	done

	if [ -z "${data_archive}" ]; then
		echo "No Debian payload archive found in deb package"
		return 1
	fi

	bsdtar -xf "${data_archive}" -C "${pkgdir}"
}
