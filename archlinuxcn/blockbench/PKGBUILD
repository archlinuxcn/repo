# Maintainer: txtsd <aur.archlinux@ihavea.quest>
# Contributor: mrAppleXZ <mr.applexz@gmail.com>

pkgname=blockbench
pkgver=5.1.6
pkgrel=1
pkgdesc='A low-poly 3D model editor'
arch=(x86_64 armv7h)
url='https://blockbench.net'
license=(GPL-3.0-or-later)
_electron=electron
depends=(
  "${_electron}"
  bash
  glibc
  imlib2
  libx11
)
makedepends=(git npm)
options=(!debug)
source=(
  "${pkgname}::git+https://github.com/JannisX11/blockbench#tag=v${pkgver}"
  "${pkgname}.desktop"
)
sha256sums=('fc85439b0c30e8c0c903f99d6e3d9ed9208430547acaba9fa395a9b9db7f4645'
            '5a64727fcf696b3497190d441556322b4d0ffb70f560ba8eba6ef79ac5c36e8c')

prepare() {
  cd "${pkgname}"

  npm install
}

build() {
  cd "${pkgname}"

  _electronDist=/usr/lib/${_electron}
  _electronVersion=$(cat ${_electronDist}/version)

  npm run publish-linux -- --linux --x64 --dir
}

package() {
  _electronDist=/usr/lib/${_electron}
  _electronVersion=$(cat ${_electronDist}/version)
  _electronVersionMajor=${_electronVersion%%.*}
  _electronDir=${_electronDist}${_electronVersionMajor}

  install -d "${pkgdir}/usr/"{bin,share/{pixmaps,applications}}
  install -d "${pkgdir}/${_electronDist}${_electronVersionMajor}/resources"

  echo -e "#!/bin/bash\nexec ${_electron} ${_electronDist}${_electronVersionMajor}/resources/${pkgname}.asar \"\$@\"" > "${pkgdir}/usr/bin/${pkgname}"
  chmod 755 "${pkgdir}/usr/bin/${pkgname}"

  install "${pkgname}/icon.png" "${pkgdir}/usr/share/pixmaps/${pkgname}.png"
  install "${pkgname}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
  install "${pkgname}/dist-electron/linux-unpacked/resources/app.asar" "${pkgdir}${_electronDist}${_electronVersionMajor}/resources/${pkgname}.asar"
}
