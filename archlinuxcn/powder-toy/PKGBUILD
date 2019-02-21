# Maintainer: farseerfc <farseerfc@archlinuxcn.org>
# Contributor:	refujee		<gmail.com: refujee>
# Contributor:	sausageandeggs	<archlinux.us: sausageandeggs>
# Contributor:	Jesse Jaara	<gmail.com: jesse.jaara>

# Set to 'y' if you want native optimizations (-march=native)
# based on your hardware. Enabled automatically if -march
# is set to native in makepkg.conf.
NATIVE_OPTIMIZATIONS=n



pkgname=powder-toy
#pkgver=${_sver}.${_mver}
pkgver=94.0
_sver=${pkgver/.*/}
_mver=${pkgver/*./}
_build=340
pkgrel=3
pkgdesc="Desktop version of the classic falling sand physics sandbox, simulates air pressure, velocity & heat!"
arch=(i686 x86_64)
depends=('sdl2' 'lua52' 'fftw' 'bzip2' 'zlib')
makedepends=('python2' 'scons')
url="http://powdertoy.co.uk/"
license=('GPL3')
source=("${pkgname}-${pkgver}-${_build}.tar.gz::http://github.com/ThePowderToy/The-Powder-Toy/archive/v${pkgver}.tar.gz"
	${pkgname}.desktop ${pkgname}.png)

prepare() {
  cd "${srcdir}/The-Powder-Toy-${pkgver}"

  #Disable the updates. I cant get the buildsystem to not compile a beta version.
  #Also I do not know the logic behind the generated snapshotids.
  sed 's|//#define I|#define I|' -i src/Config.h

}

build() {
  unset _xarch _ssever _native
  cd "${srcdir}/The-Powder-Toy-${pkgver}"

  if $(grep -q 'pni' -i /proc/cpuinfo); then
    _ssever="sse3"
  elif $(grep -q sse2 -i /proc/cpuinfo); then
    _ssever="sse2"
  elif $(grep -q sse -i /proc/cpuinfo); then
    _ssever="sse"
  else
    _ssever="no-sse"
  fi

#  if [ NATIVE_OPTIMIZATIONS == "y"  ] || $(echo ${CXXFLAGS} | grep -q -- "-march=native"); then
#    _native="--native"
#  fi

  if [ "${CARCH}" == "x86_64" ]; then
    _xarch="--64bit"
  fi

  msg2 "building powder with options with following extra flags ${_xarch} --${_ssever} ${_native}"
  scons --lin ${_xarch} --release --${_ssever} ${_native} --save-version=${_sver} \
	--minor-version=${_mver} --build-number=${_build} ${MAKEFLAGS} \
    --lua52

  mv build/{powder*,binary}
}

package() {
  install -Dm 755 "${srcdir}/The-Powder-Toy-${pkgver}/build/binary" "${pkgdir}/usr/bin/powder-toy"
  install -Dm 644 "${srcdir}/${pkgname}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
  install -Dm 644 "${srcdir}/${pkgname}.png" "${pkgdir}/usr/share/pixmaps/${pkgname}.png"
}

md5sums=('56a0a8485d20549ed5291b1d04c665af'
         '8901d334c53c04738cbd3518c80fa37c'
         'bb40bf9c2fa3982e2872b5d32de3b006')
