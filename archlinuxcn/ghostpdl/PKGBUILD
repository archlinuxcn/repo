# Maintainer: Chris Severance aur.severach AatT spamgourmet.com
# Contributor: vorbote P. A. López-Valencia;  palopezv on Google's email service
# Contributor: ... (unknown)
# Contributor: fnord0; fnord0 AAAAAAAAAAAAATTTTTTTTTTTTTTTTT riseup net

# Versions after 9.10 drop svg and pspcl6. The extra binaries will be
# installed if the version you choose has a makefile produces them.
# This PKGBUILD is tested to work with versions 9.10, 9.16, 9.18
# and should work with later versions.

# 6. What is GhostSVG?
# GhostSVG is an interpreter for SVG (Scalable Vector Graphics) files. This
# consists of an SVG interpreter hooked up to the Ghostscript graphics library.
# This project has acheived proof of concept, but is not actively being worked
# on.

set -u
pkgname='ghostpdl'
pkgver='9.50'
pkgrel='1'
pkgdesc='Ghostscript RIP for PS, PDF, PCL-5, PCL-XL, SVG and XPS.'
arch=('i686' 'x86_64')
url='https://www.ghostscript.com'
license=('AGPL')
depends=('ghostscript' 'glu' 'freeglut' 'libjpeg' 'libxt')
#_verwatch=('http://downloads.ghostscript.com/public/' "${pkgname}-\(.*\)\.tar\.bz2" 'l')
#source=("${_verwatch[0]}${pkgname}-${pkgver}.tar.bz2") # .gz and .bz2 are available. Unpacking .bz2 is a LOT slower so is not suited for package testing.
_giturl="https://github.com/ArtifexSoftware/${pkgname}-downloads"
_verwatch=("${_giturl}/releases.atom" '\s\+<title>Ghostscript/GhostPDL \([0-9\.]\+\)</title>.*' 'f')
source=("${_giturl}/releases/download/gs${pkgver//./}/${pkgname}-${pkgver}.tar.xz")
sha256sums=('eeaa4ef815f3871ff831ecf4b7e09ad472b47e8ea8e0fe8d59cac9aeda8355ff')

prepare() {
  set -u
  cd "${pkgname}-${pkgver}"
  # get rid of a harmless shell warning
  sed -e 's:^\(if test \)\($ac_cv_c_compiler_gnu\)\( = yes; then\)$:\1"\2"\3:g' -i 'configure'
  set +u
}

build() {
  set -u
  cd "${pkgname}-${pkgver}"
  if [ ! -s 'Makefile' ]; then
    ./configure --prefix='/usr'
  fi
  local _nproc="$(nproc)"; _nproc=$((_nproc>8?8:_nproc))
  nice make -s -j "${_nproc}"
  set +u
}

package() {
  set -u
  cd "${pkgname}-${pkgver}"
  if [ -f 'COPYING' ]; then
    install -Dpm644 'COPYING' -t "${pkgdir}/usr/share/licenses/${pkgname}/"
    install -Dpm644 'COPYING' "${pkgdir}/usr/share/licenses/${pkgname}/COPYING.AFPL"
    install -Dpm644 'COPYING' "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  else
    install -Dpm644 'LICENSE' -t "${pkgdir}/usr/share/licenses/${pkgname}/"
  fi

  install -d "${pkgdir}/usr/bin"
  local _exe
  for _exe in 'main/obj/pcl6' 'svg/obj/gsvg' 'language_switch/obj/pspcl6' 'xps/obj/gxps' 'bin/gpcl6' 'bin/gxps'; do
    if [ -x "${_exe}" ]; then # pspcl6 and svg were dropped after 9.10
      local _exeb="$(basename "${_exe}")"
      install -Dpm755 "${_exe}" "${pkgdir}/usr/share/${pkgname}/${_exeb}"
      ln -sf "/usr/share/${pkgname}/${_exeb}" "${pkgdir}/usr/bin/"
      if [ "${_exeb}" = 'gpcl6' ]; then
        ln -sf "/usr/share/${pkgname}/${_exeb}" "${pkgdir}/usr/bin/pcl6" # for compatibility
      fi
    fi
  done
  for _exe in 'tools/pcl2pdf' 'tools/pcl2pdfwr'; do
    ln -sf "/usr/share/${pkgname}/${_exe}" "${pkgdir}/usr/bin/"
  done

  if [ -d 'tools' ]; then
    cp -pr 'tools' "${pkgdir}/usr/share/${pkgname}/"
    cp -pr 'urwfonts' "${pkgdir}/usr/share/${pkgname}/"
    #install -d "${pkgdir}/usr/share/${pkgname}/doc"
    local _doc
    for _doc in 'README.txt' doc/ghost* 'doc/who_owns_what.txt'; do
      install -Dpm644 "${_doc}" -t "${pkgdir}/usr/share/${pkgname}/doc/" || :
    done
  else # as of 9.18
    cp -pr {xps,pcl}/'tools' "${pkgdir}/usr/share/${pkgname}/"
    cp -pr 'pcl/urwfonts' "${pkgdir}/usr/share/${pkgname}/"
    local _doc
    for _doc in 'doc/Readme.htm' doc/pclxps/ghost* 'doc/who_owns_what.txt'; do
      install -Dpm644 "${_doc}" -t "${pkgdir}/usr/share/${pkgname}/doc/" || :
    done
  fi

  set +u
}
set +u
