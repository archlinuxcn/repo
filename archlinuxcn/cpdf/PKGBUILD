# Maintainer: Chris Severance aur.severach aATt spamgourmet dott com
# From camlpdf
# Contributor: oliver < a t >  first . in-berlin . de
# From cpdf-bin
# Contributor: 2ion <dev@2ion.de>

# TODO: Build smpdf when the sources become available.
# TODO: Is smpdf still needed? I don't see it in the binaries>2.2.1
# TODO: Remove conflicts when cpdf-bin is fixed

# cpdf-bin
# TODO: Change conflicts and provides
# TODO: provies=$pkgver
# TODO: Add depends camlpdf

set -u
_pkgname='cpdf'
pkgname="${_pkgname}"
pkgver='2.3.1'
pkgrel=1
pkgdesc='Coherent Graphics ## to manipulate PDF files including merge, encrypt, decrypt, scale, crop, rotate, bookmarks, stamp, logos, page numbers'
arch=('x86_64' 'i686')
url='http://community.coherentpdf.com'
license=('custom')
depends=("camlpdf>=${pkgver}")
makedepends=('ocaml' 'ocaml-findlib')
conflicts=('cpdf-bin') # temporary
options=('!makeflags' 'staticlibs')

_srcfile="v${pkgver}"
_srcdir="${_pkgname}-source-${_srcfile#v}"; _srcdirname="${_srcdir}"

_giturl="https://github.com/johnwhitington/${_pkgname}-source"
_verwatch=("${_giturl}/releases.atom" "\s\+<title>v\([^<]\+\)</title>.*" 'f') # RSS
source=(
  "${_srcdirname}.tar.gz::${_giturl}/archive/${_srcfile}.tar.gz"
)
if [ "$(vercmp "${pkgver}" '2.1.1')" -le 0 ]; then # need smpdf
  pkgdesc="${pkgdesc//##/cpdf and smpdf}"
  # https://github.com/coherentgraphics/cpdf-binaries/commits/master
  declare -gA _binhashes=(
    [2.1.1]='17372d86935f7541ae0bc7ff0b9eebb721af0cb0'
    #[2.2]='8e308f25a329e6ac3728a69afdc1ef531a24767c'
    #[2.3]='0ae87ebc9f077ae95a40abdba761b135424d01e8'
  )
  _binver="${pkgver}"; _binhash="${_binhashes[${_binver}]}"; unset _binhashes
  #_srcdirmast="${_pkgname}-binaries-master"; _srcmastname="${_srcdirmast}"
  _srcdirmast="${_pkgname}-binaries-${_binhash}"; _srcmastname="${_pkgname}-binaries-${_binver}"
  unset _binhash _binver

  source+=("${_srcmastname}.tar.gz::https://github.com/coherentgraphics/cpdf-binaries/archive/${_srcdirmast##*-}.tar.gz")
  unset _srcmastname
else
  pkgdesc="${pkgdesc//##/cpdf}"
fi
unset _srcfile _srcdirname
md5sums=('c422e7abdbe934953e5b071a7cd016c8')
sha256sums=('d98a543422905684bf8893944fa6bed79fd335d2208a3b474a4d646be5bcb67b')

_pkgver_disabled() {
  set -u
  cd "${_srcdir}"
  git describe --long | sed -e 's:^v::g' -e 's/\([^-]*-g\)/r\1/' -e 's/-/./g'
  set +u
}

_setvars() {
  OCAMLFIND_DESTDIR="${pkgdir}/$(ocamlfind printconf destdir)"
  OCAMLFIND_LDCONF="${pkgdir}/$(ocamlfind printconf ldconf)"
}

build() {
  set -u
  cd "${_srcdir}"

  local OCAMLFIND_DESTDIR OCAMLFIND_LDCONF; _setvars
  make -s OCAMLFIND_DESTDIR="${OCAMLFIND_DESTDIR}"
  set +u; msg2 'A broken make, fixed by running it again.'; set -u
  make -s OCAMLFIND_DESTDIR="${OCAMLFIND_DESTDIR}"
  set +u
}

package() {
  set -u
  cd "${_srcdir}"

  local OCAMLFIND_DESTDIR OCAMLFIND_LDCONF; _setvars
  install -d "${OCAMLFIND_DESTDIR}"
  make -s install -d OCAMLFIND_DESTDIR="${OCAMLFIND_DESTDIR}" OCAMLFIND_LDCONF="${OCAMLFIND_LDCONF}"

  if [ ! -z "${_srcdirmast:-}" ]; then
    declare -A _arch=([i686]='Linux32' [x86_64]='Linux64')
    install -Dpm755 "${srcdir}/${_srcdirmast}/LosslessPDFCompressor/${_arch[${CARCH}]}/smpdf" -t "${pkgdir}/usr/bin/"
    install -Dpm644 "${srcdir}/${_srcdirmast}/LosslessPDFCompressor/smpdfmanual.pdf" -t "${pkgdir}/usr/share/doc/${_pkgname}/"
    install -Dpm644 "${srcdir}/${_srcdirmast}/LICENSE" -t "${pkgdir}/usr/share/licenses/${_pkgname}/"
  fi

  install -Dpm755 'cpdf' -t "${pkgdir}/usr/bin/"
  install -Dpm644 'cpdf.1' -t "${pkgdir}/usr/share/man/man1/"
  sed -e "s:cpdfmanual.pdf:/usr/share/doc/${_pkgname}/&:g" -i "${pkgdir}/usr/share/man/man1/cpdf.1"
  install -Dpm644 'cpdfmanual.pdf' -t "${pkgdir}/usr/share/doc/${_pkgname}/"

  set +u
}
set +u
