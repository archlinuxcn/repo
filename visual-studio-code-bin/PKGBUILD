# Maintainer: D. Can Celasun <can[at]dcc[dot]im>

pkgname=visual-studio-code-bin
_pkgname=visual-studio-code
pkgver=1.26.0
pkgrel=2
pkgdesc="Visual Studio Code: Editor for building and debugging modern web and cloud applications (official binary version)"
arch=('x86_64' 'i686')
url="https://code.visualstudio.com/"
license=('custom: commercial')
provides=('vscode' 'visualstudiocode' 'visual-studio-code')
replaces=('visual-studio-code')
conflicts=('visual-studio-code')
makedepends=(patchelf)
depends=(fontconfig libxtst gtk2 python cairo alsa-lib nss gcc-libs libnotify libxss gconf)
optdepends=('gvfs: Needed for move to trash functionality')
source_x86_64=(code_x64_${pkgver}.tar.gz::https://vscode-update.azurewebsites.net/${pkgver}/linux-x64/stable
               ${_pkgname}.desktop
               https://archive.archlinux.org/packages/g/glibc/glibc-2.27-3-${CARCH}.pkg.tar.xz
               )
source_i686=(code_ia32_${pkgver}.tar.gz::https://vscode-update.azurewebsites.net/${pkgver}/linux-ia32/stable
              ${_pkgname}.desktop
              https://archive.archlinux.org/packages/g/glibc/glibc-2.27-3-${CARCH}.pkg.tar.xz
              )
options=("!strip" "staticlibs")
noextract=("glibc-2.27-3-${CARCH}.pkg.tar.xz")
sha256sums_x86_64=('618ca429e23777ef6b512c0cbd78bc711a7cf6f58752d9f805ced1dc62abb8f0'
                   '488592034dd5f979083bbd80788d33e253bb3ac3e52d50faee80e715a924a212'
                   'a9e1b18d7f613be660556dbd6883781e88a0f5113230147e230d3e2f268792dc')
sha256sums_i686=('fd150bee8e1be4f5461013b8fee19f855200d046643e4ea5387aad170ad5f12b'
                 '488592034dd5f979083bbd80788d33e253bb3ac3e52d50faee80e715a924a212'
                 'a9e1b18d7f613be660556dbd6883781e88a0f5113230147e230d3e2f268792dc')
package() {
  _pkg=VSCode-linux-x64
  if [ "${CARCH}" = "i686" ]; then
    _pkg=VSCode-linux-ia32
  fi

  install -d "${pkgdir}/usr/share/licenses/${_pkgname}"
  install -d "${pkgdir}/opt/${_pkgname}"
  install -d "${pkgdir}/usr/bin"
  install -d "${pkgdir}/usr/share/applications"
  install -d "${pkgdir}/usr/share/icons" 

  install -m644 "${srcdir}/${_pkg}/resources/app/LICENSE.txt" "${pkgdir}/usr/share/licenses/${_pkgname}/LICENSE"
  install -m644 "${srcdir}/${_pkg}/resources/app/resources/linux/code.png" "${pkgdir}/usr/share/icons/${_pkgname}.png"
  install -m644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"

  cp -r "${srcdir}/${_pkg}/"* "${pkgdir}/opt/${_pkgname}" -R
  ln -s /opt/${_pkgname}/bin/code "${pkgdir}"/usr/bin/code

  _ldir="/opt/$_pkgname"
  _pdir="$pkgdir/$_ldir"
  _pexe="$_pdir/code"
  mkdir -p "$_pdir/glibc"
  tar -xJC "$_pdir/glibc" -f "glibc-2.27-3-$CARCH.pkg.tar.xz"
  rm "$_pdir/glibc/"{.BUILDINFO,.INSTALL,.MTREE,.PKGINFO}
  patchelf --set-interpreter "$_ldir/glibc/usr/lib/ld-linux-x86-64.so.2" "$_pexe"
  patchelf --set-rpath "$_ldir:$_ldir/glibc/usr/lib" "$_pexe"
}
