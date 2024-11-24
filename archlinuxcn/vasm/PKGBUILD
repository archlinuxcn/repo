#
# PKGBUILD: vasm
#
# Maintainer: Uffe Jakobsen <_microtop_-at-_starion_-_dot_-_dk_>
#
# NOTE: to comply with semantic versioning (https://semver.org/) version string X.Y.0-letter is used
#

_pkgver="1_9f"

pkgname="vasm"
pkgver="1.9.0_f"
pkgrel=0
pkgdesc="Portable and retargetable 6502 6800 6809 arm c16x jagrisc m68k pdp11 ppc qnice test tr3200 vidcore x86 z80 assembler."
arch=('i686' 'x86_64')
url="http://sun.hasenbraten.de/vasm/"
license=('custom')
depends=()
#makedepends=('texinfo')
#source=(http://sun.hasenbraten.de/vasm/release/vasm.tar.gz) # latest unversioned source url
#source=(http://server.owl.de/~frank/tags/${pkgname}${_pkgver}.tar.gz)
source=(http://phoenix.owl.de/tags/${pkgname}${_pkgver}.tar.gz)
sha256sums=('a09d4ff3b5ec50bb7538fb97b9539141376580b590586463569783c36438ebe8')


# TODO: dynamic lists based on dirs below vasm/cpus, vasm/syntax, vasm/output_*.c/.h
#CPU_LIST="6502 6800 6809 arm c16x jagrisc m68k pdp11 ppc qnice test tr3200 vidcore x86 z80"
CPU_LIST="6502 6800 6809 arm c16x jagrisc m68k pdp11 ppc qnice test tr3200 vidcore x86 z80"
SYNTAX_LIST="std madmac mot oldstyle" # test
OUTPUT_LIST="aout bin cdef elf errors hunk ihex srec test tos vobj xfile"

prepare()
{
  cd "${srcdir}/${pkgname}"
}

build()
{
  cd "${srcdir}/${pkgname}"
  echo "CPU_LIST: ${CPU_LIST}"
  echo "SYNTAX_LIST: ${SYNTAX_LIST}"
  for CPU in ${CPU_LIST}; do
    for SYNTAX in ${SYNTAX_LIST}; do
      echo "CPU=${CPU} SYNTAX=${SYNTAX}:"
      make CPU=${CPU} SYNTAX=${SYNTAX}
    done
  done

  #make doc/vasm.pdf # some users report texi problems (1.8i)
  #make doc/vasm.html # currently fails due to missing html file (1.8i)
}

package()
{
  cd "${srcdir}/${pkgname}"
  mkdir -p "${pkgdir}/usr/bin"
  echo "CPU_LIST: ${CPU_LIST}"
  echo "SYNTAX_LIST: ${SYNTAX_LIST}"
  for CPU in ${CPU_LIST}; do
    for SYNTAX in ${SYNTAX_LIST}; do
      echo "CPU=${CPU} SYNTAX=${SYNTAX}:"
      cp "vasm${CPU}_${SYNTAX}" "${pkgdir}/usr/bin/vasm_${CPU}_${SYNTAX}"
      ln -s "vasm_${CPU}_${SYNTAX}" "${pkgdir}/usr/bin/vasm${CPU}_${SYNTAX}"
    done
  done

  #mkdir -p "${pkgdir}/usr/share/doc/vasm/"
  #install -m644 doc/vasm.pdf "${pkgdir}/usr/share/doc/vasm/"
}

#
# EOF
#
