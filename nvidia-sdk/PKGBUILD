# Maintainer: Daniel Bermond < yahoo-com: danielbermond >

# NVIDIA Video Codec SDK
# You need to download the SDK file from NVIDIA's website. (registration required)
# Download website:
# https://developer.nvidia.com/nvidia-video-codec-sdk/

pkgname=nvidia-sdk
pkgver=7.0.1
pkgrel=2
pkgdesc="NVIDIA Video Codec SDK (NVENCODE API and NVDECODE API)"
arch=('i686' 'x86_64')
url="https://developer.nvidia.com/nvidia-video-codec-sdk/"
license=('custom')
source=("file://Video_Codec_SDK_${pkgver}.zip"
        'LICENSE')
sha256sums=('03acd43f04d72b2bc3bdcfd8d46c8f0e12be2aa7ace871589232a31269d08c86'
            '04881e31bd6997cea2d7ac1e9db4f26954230754bf1809333d8d0091a18d21ae')

package() {
	mkdir -p "${pkgdir}/usr/include/${pkgname}"
	mkdir -p "${pkgdir}/usr/include/${pkgname}/GL"
	mkdir -p "${pkgdir}/usr/lib/${pkgname}"
	mkdir -p "${pkgdir}/usr/share/doc/${pkgname}"
	
	# Includes
	cd "${srcdir}/Video_Codec_SDK_${pkgver}/Samples/common/inc"
	install -D -m644 *.h      "${pkgdir}/usr/include/${pkgname}"
	install -D -m644 ./GL/*.h "${pkgdir}/usr/include/${pkgname}/GL"
	
	# Lib
	cd "${srcdir}/Video_Codec_SDK_${pkgver}/Samples/common/lib/linux/${CARCH}"
	install -D -m644 libGLEW.a "${pkgdir}/usr/lib/${pkgname}/libGLEW.a"
	
	# Documentation
	cd "${srcdir}/Video_Codec_SDK_${pkgver}/doc"
	install -D -m644 * "${pkgdir}/usr/share/doc/${pkgname}"
	
	# License
	install -D -m644 "$srcdir"/LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
