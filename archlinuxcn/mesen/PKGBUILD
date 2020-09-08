# Maintainer:  Andrew O'Neill <andrew at meanjollies dot com>
# Contributor: John Jenkins <twodopeshaggy@gmail.com>

pkgname=mesen
_pkgname=Mesen
pkgver=0.9.9
pkgrel=1
pkgdesc='A cross-platform NES/Famicom emulator'
arch=('x86_64')
makedepends=('clang' 'gendesk' 'zip' 'msbuild-stable')
depends=('mono' 'sdl2')
url='https://github.com/SourMesen/Mesen'
license=('GPL3')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha256sums=('8c638a9910b8de6cf628ceefb226c2f636e4397b0629f58a8ffb304984d68ea9')

prepare() {
  cd "${_pkgname}-${pkgver}"

  # Prevent duplicate .desktop from getting created
  sed -i 's/CreateShortcutFile(desktopFile, mimeTypes);//' GUI.NET/Config/FileAssociationHelper.cs

  gendesk --pkgname "${_pkgname}" --pkgdesc "${pkgdesc}" --exec "/usr/bin/mesen" -n

  # Invoke using mono in a wrapper, since wine (if installed) would open it otherwise
  cat > "${pkgname}" << EOF
#!/bin/sh
/usr/bin/mono /opt/Mesen/Mesen "\$@"
EOF
}

build() {
  cd "${_pkgname}-${pkgver}"

  make
}

package() {
  cd "${_pkgname}-${pkgver}"
  install -Dm755 ${pkgname} "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 ${_pkgname}.desktop "${pkgdir}/usr/share/applications/${_pkgname}.desktop"

  cd "${srcdir}/${_pkgname}-${pkgver}/GUI.NET/Resources"
  install -Dm644 ${_pkgname}Icon.png "${pkgdir}/usr/share/pixmaps/${_pkgname}.png"

  cd "${srcdir}/${_pkgname}-${pkgver}/bin/x64/Release"
  install -Dm755 ${_pkgname}.exe "${pkgdir}/opt/${_pkgname}/${_pkgname}"

  cd "${srcdir}/${_pkgname}-${pkgver}/InteropDLL/obj.x64"
  install -Dm644 lib${_pkgname}Core.x64.dll "${pkgdir}/usr/lib/lib${_pkgname}Core.dll"
}
