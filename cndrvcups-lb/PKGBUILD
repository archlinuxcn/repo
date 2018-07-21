# Maintainer:  Chris Severance aur.severach aATt spamgourmet dott com
# Maintainer:  Lone_Wolf <lonewolf@xs4all.nl>
# Contributor: Steven She <mintcoffee@gmail.com>
# Contributor: vbPadre <vbPadre@gmail.com>

# TODO: cndrvcups-common-lb and cndrvcups-lb should be a single split package

set -u
pkgbase='cndrvcups-lb'
pkgname="${pkgbase}"
#_pkgver='3.40'; _commonver='3.80'; _dl='8/0100002708/17'
_pkgver='3.50'; _commonver='3.90'; _dl='8/0100007658/05'
pkgver="${_pkgver}"
pkgrel='1'
pkgdesc='Canon UFR II /LIPSLX printer driver build from source for LBP iR MF ImageCLASS ImageRUNNER Laser Shot i-SENSYS ImagePRESS ADVANCE printers and copiers'
arch=('i686' 'x86_64')
# Direct links to the download reference go bad on the next version. We want something that will persist for a while.
url='https://www.canon.co.uk/for_work/products/office_print_copy_solutions/office_black_white/imagerunner_1730i/'
#url='https://www.usa.canon.com/internet/portal/us/home/support/details/printers/black-and-white-laser/mf212w/imageclass-mf212w'
license=('custom')
depends=("cndrvcups-common-lb>=${_commonver}") # >= makes upgrades easier
depends_i686=('libxml2')
depends_x86_64=("${depends_i686[@]/#/lib32-}")
optdepends_i686=('libjpeg6-turbo: improves printing results for color imageRUNNER/i-SENSYS LBP devices')
optdepends_x86_64=("${optdepends_i686[@]/#/lib32-}")
makedepends=('autoconf' 'automake')
makedepends+=('gzip')
conflicts=('cndrvcups-lb-cpca')
options=('!emptydirs' '!strip')
options+=('!libtool')
install="${pkgname}.install"
_srcdir="${pkgbase}-${pkgver}"
source=(
  "http://gdlp01.c-wss.com/gds/${_dl}/linux-UFRII-drv-v${_pkgver//\./}-uken.tar.gz"
  'how-to.txt'
)
sha256sums=('c00324177a6f77f0a6deb4ecc6bee8150607dd4029bad3dfc1a521f84f811e7f'
            '62c4bfe3e4155e5e805b51eaa4b9dd3581ba029259c2817d9ebe66077aad7280')
sha512sums=('2eeb1448cb76ac156e1e5f6df46141ee5605b0bed1c25f31b0f039fb9f579fe3d5732b132cae391e78276c550febc19366f958d1fb53c93f955303f1f5c37ab3'
            '736e1785c443c4d129c8801a127410012889f46691259e8a7f6a54106a0647beb5b6267aabb78b3ed0a1c7a9d8ce216e159515d3aad425812e5be52c8b58e4ee')

# build instructions are adapted from upstream file
# cndrvcups-lb.spec

prepare() {
  set -u
  bsdtar -xf "linux-UFRII-drv-v${_pkgver//\./}-uken/Sources/${_srcdir}-1.tar.gz"
  set +u
}

build() {
  set -u

  set +u; msg2 'Building ppd'; set -u
  cd "${_srcdir}/ppd"
  autoreconf -fi
  ./autogen.sh --prefix='/usr'

  set +u; msg2 'Building pstoufr2cpca'; set -u
  cd '../pstoufr2cpca'
  autoreconf -fi
  ./autogen.sh --prefix='/usr' --libdir='/usr/lib'

  set +u; msg2 'Building cpca'; set -u
  cd '../cpca'
  autoreconf -fi
  ./autogen.sh --prefix='/usr' --enable-progpath='/usr/bin' --libdir='/usr/lib'

  set +u; msg2 'Building cngplp'; set -u
  cd '../cngplp'
  aclocal
  autoreconf -fi
  ./autogen.sh --prefix='/usr' --libdir='/usr/lib'

  set +u; msg2 'Building cngplp/files'; set -u
  cd 'files'
  autoreconf -fi
  ./autogen.sh --prefix='/usr'

  set +u; msg2 'Building all'; set -u
  cd "${srcdir}/${_srcdir}"
  make

  set +u
}

package() {
  set -u

  cd "${_srcdir}"

  declare -A _lib32dirs=([i686]='lib' [x86_64]='lib32')
  local _lib32dir="${_lib32dirs[${CARCH}]}"

  make install DESTDIR="${pkgdir}"
  gzip "${pkgdir}/usr/share/cups/model"/*.ppd

  cd 'libs'
  install -s -Dpm755 'cnpkbidi' -t "${pkgdir}/usr/bin/"
  install -Dpm4755 'cnpkmoduleufr2' -t "${pkgdir}/usr/bin/"

  local _libs=(
    'libcanonufr2.so.1.0.0'
    'libufr2filter.so.1.0.0'
    'libEnoJBIG.so.1.0.0'
    'libEnoJPEG.so.1.0.0'
    'libcaiocnpkbidi.so.1.0.0'
    'libcnlbcm.so.1.0'
  )
  install -s -Dpm755 "${_libs[@]}" -t "${pkgdir}/usr/${_lib32dir}/"
  install -Dpm755 'libcanonufr2.la' -t "${pkgdir}/usr/${_lib32dir}/"

  install -Dpm644 cnpkbidi_info* -t "${pkgdir}/usr/share/cnpkbidi/"
  install -Dpm644 ThLB* -t "${pkgdir}/usr/share/ufr2filter/"

  cd '../data'
  install -Dpm644 CnLB* -t "${pkgdir}/usr/share/caepcm/"

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

  # according to Gentoo ebuild v2.90 c3pldrv dlopens the absolute path
  # /usr/lib/libcnlbcm.so
  if [ "${CARCH}" = 'x86_64' ]; then
    ln -s '../lib32/libcnlbcm.so' -t "${pkgdir}/usr/lib/"
  fi

  cd "${srcdir}/${_srcdir}"
  if [ "$(vercmp "${pkgver}" '3.50')" -lt 0 ]; then
    install -Dpm644 LICENSE-*.txt -t "${pkgdir}/usr/share/licenses/${pkgname}/"
    install -Dpm644 "${srcdir}/linux-UFRII-drv-v340-uken/Documents/guide-ufr2-3.4xUK.tar.gz" -t "${pkgdir}/usr/share/doc/${pkgname}/"
  else
    local _lics=(
      $(find -type 'f' -name 'LICENSE*.txt')
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

  set +u
}
set +u
