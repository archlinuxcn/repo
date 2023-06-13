# Maintainer : Antoine Viallon <antoine+aur@lesviallon.fr>

pkgname=video2x
pkgver=4.8.1
pkgrel=1
pkgdesc="Machine learning video/GIF/image upscaling"
url="https://video2x.org/"
arch=("any")
license=("GPL3")
depends=(
	"python"
	"ffmpeg"
	"python-pyaml"
	"python-avalon_framework" # AUR
	"python-colorama"
	"patool" # AUR, should be named python-patool
	"python-pillow"
	#"python-pyqt5"
	"python-requests"
	"python-tqdm"
	"python-magic"
)
optdepends=(
	"waifu2x-ncnn-vulkan: for anime/cartoon upscaling and JPEG denoising - fast"
	"realsr-ncnn-vulkan: real photos upscaling and denoising - slow"
	"srmd-ncnn-vulkan: general purpose upscaling and image restoration"
	"waifu2x-converter-cpp: C++ implemenation of waifu2x working on all platforms"
)
source=(
	"https://github.com/k4yt3x/video2x/archive/${pkgver}.tar.gz"
	"etc_config_file.patch"
	"video2x.yaml"
)
sha256sums=('a372027fb09c45f6624db8839b46fa34b4c3c639ba19fe9d192f9ef0a4ed9c46'
            '9d027d3f8ca5bdf4e7c543fe5cd18e5024cf7ce0e74c2d52db0a3d1ca27fcc5e'
            'dae9fb91b965d27a868ab71e36c8d6633f0c4be770c8f70c2ea41bc957b7c796')

prepare() {
	cd "${srcdir}/${pkgname}-${pkgver}/src"

	patch video2x.py "${srcdir}/etc_config_file.patch"
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}/src"

	mkdir -p "${pkgdir}/usr/share/video2x/"
	mkdir -p "${pkgdir}/usr/share/video2x/wrappers"
	mkdir -p "${pkgdir}/usr/bin"

	for file in "image_cleaner.py upscaler.py video2x.py exceptions.py bilogger.py progress_monitor.py"; do
		install -D -m755 ${file} "${pkgdir}/usr/share/video2x/"
	done

	for file in wrappers/*.py; do
		install -D -v -m755 ${file} "${pkgdir}/usr/share/video2x/wrappers/"
	done

	mkdir -p "${pkgdir}/etc"
	install -D -m644 "${srcdir}/video2x.yaml" "${pkgdir}/etc/video2x.yaml"

	ln -s /usr/share/video2x/video2x.py "${pkgdir}/usr/bin/video2x"
}
