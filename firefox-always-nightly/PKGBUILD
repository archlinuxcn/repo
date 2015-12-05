# Maintainer : Félix Saparelli <aur @ passcod.name>
# Contributor: Cedric MATHIEU <me.xenom @ gmail.com>
# Contributor: coderoar <coderoar @ gmail.com>
# Contributor: Det <nimetonmaili @ gmail.com>
# Contributor: kang <kang @ mozilla.com>
# Contributor: John Reese <jreese @ noswap.com>
# Contributor: Paul Vinieratos <pvinis @ gmail.com>

pkgname=firefox-always-nightly
pkgdesc='Standalone web browser from mozilla.org, nightly build, always updating'
url='https://nightly.mozilla.org'
pkgver=99.0a1
pkgrel=7
arch=('i686' 'x86_64')
license=('MPL' 'GPL' 'LGPL')
_srcurl="https://ftp.mozilla.org/pub/firefox/nightly/latest-mozilla-central"
_version="$(curl -s "${_srcurl}/" | grep -Eo firefox-.+tar.bz2 | cut -d- -f2 | cut -d. -f1-2 | tail -n1)"
_file="firefox-${_version}.en-US.linux-${CARCH}"
curl -so {,${_srcurl}/}${_file}.checksums
_sumbz2="$(grep -E sha512.+${_file}\.tar\.bz2 ${_file}.checksums | cut -d\  -f1)"
_sumtxt="$(grep -E sha512.+${_file}\.txt ${_file}.checksums | cut -d\  -f1)"
source=("${_srcurl}/${_file}.tar.bz2"
        "${_srcurl}/${_file}.txt"
        'firefox-nightly.desktop'
        'firefox-nightly-safe.desktop'
        'vendor.js')
sha512sums=("${_sumbz2}"
            "${_sumtxt}"
            'd2d836b07288d2a13d01d668399df8a2a15884a58a7051303938bf74a30bdfc23a8bc57395494345727ae24e1dd9cab09c67a640a5c9e7a8df895f987e009dcd'
            '00caf982c072c7499433c494ecf2096542c4ddf368c4b97fb22672fd669683911d009a65a498b8a03da61ae9aa5a4e8bdaa6e58b148c2a5d7c008910b2af26a5'
            'bae5a952d9b92e7a0ccc82f2caac3578e0368ea6676f0a4bc69d3ce276ef4f70802888f882dda53f9eb8e52911fb31e09ef497188bcd630762e1c0f5293cc010')
depends=('alsa-lib'
         'dbus-glib'
         'gtk2'
         'libnotify'
         'libxt'
         'mime-types'
         'nss'
         'sqlite')
provides=('firefox-nightly')
conflicts=('firefox-nightly')

pkgver() {
  echo "${_version}.$(head -n1 ${_file}.txt | cut -c-8)"
}

package() {
  # Use VERIFY_GPG=1 to enable GnuPG signature verification.
  # You'll need Firefox's GnuPG release key.
  # Their current fingerprint is
  # 2B90 598A 745E 992F 315E  22C5 8AB1 3296 3A06 537A
  # shortid 0x15A0A4BC
  if [[ $VERIFY_GPG -eq 1 ]]; then
    msg "Verifying GnuPG signature..."
    FX_GPG="${_file}.checksums.asc"
    curl -OR "${_srcurl}/${_file}.checksums"
    curl -OR "${_srcurl}/${FX_GPG}"
    gpg --verify ${FX_GPG}
  fi

  #  uncomment this line to remove these
  #  rm -rf firefox/{extensions,plugins,searchplugins}
  install -d "${pkgdir}"/{usr/{bin,share/{applications,pixmaps}},opt}
  cp -r firefox "${pkgdir}/opt/firefox-nightly"

  ln -s /opt/firefox-nightly/firefox "${pkgdir}/usr/bin/firefox-nightly"
  install -m644 "${srcdir}"/{firefox-nightly.desktop,firefox-nightly-safe.desktop} "${pkgdir}/usr/share/applications/"
  install -m644 "${srcdir}/firefox/browser/icons/mozicon128.png" "${pkgdir}/usr/share/pixmaps/firefox-nightly-icon.png"
  install -Dm644 "${srcdir}/vendor.js" "${pkgdir}/opt/firefox-nightly/browser/defaults/preferences/vendor.js"
}
