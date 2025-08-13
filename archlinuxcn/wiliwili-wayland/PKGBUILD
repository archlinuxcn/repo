# Maintainer: Kimiblock Moe
# Contributor: Puqns67 <me@puqns67.icu>
# Contributor: yuioto <yuiotochan@outlook.com>


pkgname=wiliwili-wayland
_pkgname=wiliwili
pkgver=1.5.2
pkgrel=3
pkgdesc='专为手柄控制设计的第三方跨平台B站客户端, 使用 Wayland 运行并阻止唤醒独显'
arch=('x86_64' 'aarch64')
url='https://github.com/xfangfang/wiliwili'
license=('GPL-3.0-or-later')
depends=("mpv" "opencc" "pystring" "glibc" "curl" "hicolor-icon-theme" "openssl" "gcc-libs" "dbus" "zlib" "libwebp" "bash" "libpng")
makedepends=("cmake" "git" "libxi" "ninja" "python" "wayland-protocols" "sdl2")
source=("${_pkgname}"::"git+${url}.git#tag=v${pkgver}" "wiliwili.sh" "cn.xfangfang.wiliwili.desktop" "portable-config")
sha512sums=('7c88ed18be429bab8abdacf2063591eabf9f7fe82bd95c6a202b0af6807a755d4926a276872a995b3aa52c3de7f128ccfc884f8d95006989d63373f4c69d07bf'
            'cc97c4bdb168538d2f2485c3f54cb6ae11e3765b66848ae35ec8790b5fcba481a5170cdbcafc9b12e9498dcf8b8442b29843cbe9b6d8cbe425fccce71206df5e'
            '6dd399c8bb5950caa0e774922751af48ef16e7fe4c4daf4a67693a1183913e9b052461bb28aa287061358572f38920f6ddc0112e9a69a3385d5c0a0214d0684d'
            'ae7d1aaf6be7377387e08e768098c68ccdccf23fd7976d8a5f9785b157cd26f44aeb3f5e9442910e59a7f73d788d99bfb9374e697becb52410797f1e8543f63b')
conflicts=(wiliwili)
provides=(wiliwili)

function prepare() {
	git -C "${srcdir}/${_pkgname}" submodule update --init --recursive
}

function build() {
	cmake \
		-S "${srcdir}/${_pkgname}" \
		-B "${srcdir}/build" \
		-G Ninja \
		-D CMAKE_BUILD_TYPE=Release \
		-D CMAKE_INSTALL_PREFIX='/usr' \
		-D INSTALL=ON \
		-D PLATFORM_DESKTOP=ON \
		-D USE_SYSTEM_CURL=ON \
		-D USE_SYSTEM_OPENCC=ON \
		-D USE_SYSTEM_PYSTRING=ON \
		-D USE_SYSTEM_SDL2=ON \
 		-D GLFW_BUILD_WAYLAND=ON \
		-D GLFW_BUILD_X11=OFF

	ninja -C "${srcdir}/build" wiliwili
}

function package() {
	depends+=(portable)
	install -Dm755 portable-config "${pkgdir}"/usr/lib/portable/info/cn.xfangfang.wiliwili/config
	DESTDIR="${pkgdir}" ninja -C "${srcdir}/build" install
	install -Dm755 "${srcdir}/wiliwili.sh" "${pkgdir}/usr/bin/wiliwili-wayland"
	install -d "${pkgdir}/usr/lib/portable/overlay-usr"
	install -Dm755 "${pkgdir}/usr/bin/wiliwili" "${pkgdir}/usr/lib/portable/overlay-usr/wiliwili"
	rm "${pkgdir}/usr/bin/wiliwili"
	install -Dm644 "${srcdir}/cn.xfangfang.wiliwili.desktop" "${pkgdir}/usr/share/applications/cn.xfangfang.wiliwili.desktop"
	echo '''[Desktop Entry]
Type=Application
Name=WiliWili
GenericName=Stub for MPRIS
Icon=spotify
TryExec=portable
Exec=wiliwili-wayland
Terminal=false
NoDisplay=true''' >"${pkgdir}/usr/share/applications/wiliwili.desktop"
}
