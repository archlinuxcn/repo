# Maintainer:  Chris Severance aur.severach aATt spamgourmet dott com
# Maintainer:  Lone_Wolf <lonewolf@xs4all.nl>
# Contributor: Steven She <mintcoffee@gmail.com>
# Contributor: vbPadre <vbPadre@gmail.com>

# TODO: cndrvcups-common-lb and cndrvcups-lb should be a single split package

set -u
pkgbase='cndrvcups-common-lb'
pkgname="${pkgbase}"
# used this name to avoid conflict with the existing cndrvcups-common (no longer in aur) which was wrong version for cndrvcups-lb
#_pkgname='cndrvcups-common'
#_pkgver='3.40'; _commonver='3.80'; _dl='8/0100002708/17'
_pkgver='3.50'; _commonver='3.90'; _dl='8/0100007658/05'
pkgver="${_commonver}"
pkgrel='1'
pkgdesc='common printer driver modules for cndrvcups-lb package, built from source'
arch=('i686' 'x86_64')
# Direct links to the download reference go bad on the next version. We want something that will persist for a while.
url='https://www.canon.co.uk/for_work/products/office_print_copy_solutions/office_black_white/imagerunner_1730i/'
#url='https://www.usa.canon.com/internet/portal/us/home/support/details/printers/black-and-white-laser/mf212w/imageclass-mf212w'
license=('GPL' 'MIT' 'custom')
depends=('libglade')
depends_i686=('gcc-libs')
depends_x86_64=("${depends_i686[@]/#/lib32-}")
makedepends=('autoconf' 'automake')
makedepends+=('glib2' 'gtk2')
options=('!emptydirs' '!strip')
options+=('staticlibs')
_srcdir="${pkgname%-lb}-${pkgver}"
source=(
  "http://gdlp01.c-wss.com/gds/${_dl}/linux-UFRII-drv-v${_pkgver//\./}-uken.tar.gz"
)
sha256sums=('c00324177a6f77f0a6deb4ecc6bee8150607dd4029bad3dfc1a521f84f811e7f')
sha512sums=('2eeb1448cb76ac156e1e5f6df46141ee5605b0bed1c25f31b0f039fb9f579fe3d5732b132cae391e78276c550febc19366f958d1fb53c93f955303f1f5c37ab3')

# build instructions are adapted from upstream file
# cndrvcups-common.spec

prepare() {
  set -u
  bsdtar -xf "linux-UFRII-drv-v${_pkgver//\./}-uken/Sources/${_srcdir}-1.tar.gz"
  set +u
}

build() {
  set -u

  set +u; msg2 'Building buftool'; set -u
  cd "${_srcdir}/buftool"
  autoreconf -i
  ./autogen.sh --prefix='/usr/' --enable-progpath='/usr/bin' --libdir='/usr/lib'

  set +u; msg2 'Building cngplp'; set -u
  cd '../cngplp'
  autoreconf -i
  LIBS='-lgtk-x11-2.0 -lgobject-2.0 -lglib-2.0 -lgmodule-2.0' \
  ./autogen.sh --prefix='/usr' --libdir='/usr/lib'

  set +u; msg2 'Building backend'; set -u
  cd '../backend'
  autoreconf -i
  ./autogen.sh --prefix='/usr' --libdir='/usr/lib'

  set +u; msg2 'Building all'; set -u
  cd "${srcdir}/${_srcdir}"
  make

  set +u; msg2 'Building c3plmod_ipc'; set -u
  cd 'c3plmod_ipc'
  make

  set +u
}

package() {
  set -u

  cd "${_srcdir}"

  declare -A _lib32dirs=([i686]='lib' [x86_64]='lib32')
  local _lib32dir="${_lib32dirs[${CARCH}]}"

  make install DESTDIR="${pkgdir}"

  install -Dpm644 'Rule/canon-laser-printer.usb-quirks' -t "${pkgdir}/usr/share/cups/usb/"

  cd 'c3plmod_ipc'
  make install DESTDIR="${pkgdir}" LIBDIR='/usr/lib'
  cd ..

  cd 'libs'
  install -s -Dpm755 'c3pldrv' -t "${pkgdir}/usr/bin/"
  local _libs=(
    'libcaiowrap.so.1.0.0'
    'libcaiousb.so.1.0.0'
    'libc3pl.so.0.0.1'
    'libcaepcm.so.1.0'
    'libColorGear.so.0.0.0'
    'libColorGearC.so.1.0.0'
    'libcanon_slim.so.1.0.0'
  )
  install -s -Dpm755 "${_libs[@]}" -t "${pkgdir}/usr/${_lib32dir}/"

  cd '../data'
  install -Dpm644 *.[Ii][Cc][Cc] *.PRF -t "${pkgdir}/usr/share/caepcm/"

  local _lib _libt
  cd "${pkgdir}/usr/${_lib32dir}"
  for _lib in "${_libs[@]}"; do
    echo "soname ${_lib}"
    test -f "${_lib}" || echo "${}"
    if [[ "${_lib}" =~ ^(lib[^.]+\.so\.[0-9]+)\. ]]; then
      _libt="${BASH_REMATCH[1]}"
      ln -s "${_lib}" "${_libt}"
      _libt="${_libt%.*}"
      ln -s "${_lib}" "${_libt}"
    fi
  done

  cd "${pkgdir}/usr/lib"
  _libs=('libcanonc3pl.so.1.0.0')
  for _lib in "${_libs[@]}"; do
    echo "soname ${_lib}"
    test -f "${_lib}" || echo "${}"
    if [[ "${_lib}" =~ ^(lib[^.]+\.so\.[0-9]+)\. ]]; then
      _libt="${BASH_REMATCH[1]}"
      ln -s "${_lib}" "${_libt}"
      _libt="${_libt%.*}"
      ln -s "${_lib}" "${_libt}"
    fi
  done

  # according to Gentoo ebuild v2.90 c3pldrv dlopens the absolute path
  # /usr/lib/libc3pl.so
  if [ "${CARCH}" = 'x86_64' ]; then
    ln -s '../lib32/libc3pl.so' -t "${pkgdir}/usr/lib/"
  fi

  cd "${srcdir}/${_srcdir}"
  if [ "$(vercmp "${pkgver}" '3.50')" -lt 0 ]; then
    install -Dpm644 LICENSE-* -t "${pkgdir}/usr/share/licenses/${pkgname}/"
  else
    local _lics=(
      $(find -type 'f' -name 'LICENSE.txt')
    )
    local _lic _licd _lico
    for _lic in "${_lics[@]}"; do
      _licd="$(dirname "${_lic}")"
      _licd="$(basename "${_licd}")"
      _lico="LICENSE.${_licd}.txt"
      echo "license ${_lico}"
      install -Dpm644 "${_lic}" "${pkgdir}/usr/share/licenses/${pkgname}/${_lico}"
    done
  fi
  install -Dpm644 README* -t "${pkgdir}/usr/share/doc/${pkgname}/"

  # The filter works in /usr/bin but it's expected in .../cups/filter/
  install -d "${pkgdir}/usr/lib/cups/filter/"
  ln -s '/usr/bin/c3pldrv' -t "${pkgdir}/usr/lib/cups/filter/"

  set +u
}
set +u
