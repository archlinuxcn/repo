# Maintainer: 7Ji <pugokughin@gmail.com>

_model_canonical='ARM Mali-G610'
_model='mali-valhall-g610'
_firmware="${_model}-firmware"
_repo='https://github.com/JeffyCN/mirrors'
_firmware_commit='ca33693a03b2782edc237d1d3b786f94849bed7d'
_eula_commit='8605a3c81b60ac5bd8e492cc02e84a2e0aa8e524'

pkgname="${_firmware}"
# The actual DDK version uses -, but it is forbidden in pkgver
pkgver=g18p0.01eac0
pkgrel=1
pkgdesc="Firmware for ${_model_canonical}"
url='https://developer.arm.com/Processors/Mali-G610'
license=('custom')
source=(
  "${_repo}/raw/${_eula_commit}/END_USER_LICENCE_AGREEMENT.txt"
  "${_repo}/raw/${_firmware_commit}/firmware/g610/mali_csffw.bin"
)
sha256sums=(
  'a78acc73de9909efb879800d4daa4640c4aaa55cd751238a133954aba15e4285'
  '122f1ecc14d2de0fe93fc025f8c77e4531abd004fa172ffe69e40cd7d15d5c66'
)
arch=('aarch64' 'arm7h')
options=(!strip)

_package-firmware() {
  install -D --mode=644 mali_csffw.bin --target-directory="${pkgdir}"/usr/lib/firmware/
  install -D --mode=644 END_USER_LICENCE_AGREEMENT.txt --target-directory="${pkgdir}/usr/share/licenses/${pkgbase}"
}

eval "package_${_firmware}() {
  pkgdesc='Firmware for ${_model_canonical}'
  _package-firmware
}"