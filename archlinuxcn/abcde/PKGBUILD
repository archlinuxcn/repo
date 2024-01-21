# Contributor: Jochem Kossen <j.kossen@home.nl>
# Contributor: Kevin Piche <kevin@archlinux.org>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>
# Maintainer: schuay <jakob.gruber@gmail.com>

pkgname=abcde
pkgver=2.9.3
pkgrel=5
pkgdesc='Frontend command-line utility that grabs tracks off a CD, encodes them to ogg or mp3 format, and tags them, all in one go'
arch=('any')
url='https://abcde.einval.com/'
license=('GPL')
depends=('bash' 'cd-discid' 'wget' 'vorbis-tools' 'which')
optdepends=('cdparanoia: Paranoia ripping support'
            'flac: FLAC encoding support'
            'glyr: album art support'
            'imagemagick: album art support'
            'lame: MP3 encoding support'
            'opus-tools: Opus encoding support'
            'python-eyed3: ID3 tag support'
            'vorbisgain: Ogg Vorbis normalization support')
backup=("etc/${pkgname}.conf")
source=("https://abcde.einval.com/download/abcde-${pkgver}.tar.gz"{,.sign}
        hostname.patch)
validpgpkeys=('CEBB52301D617E910390FE16587979573442684E'
              '742D444A5AFAF2951EF33E7BF8FB375D9CC820B3') # Steve McIntyre, Andrew Strong
sha256sums=('046cd0bba78dd4bbdcbcf82fe625865c60df35a005482de13a6699c5a3b83124'
            'SKIP'
            '6b4d8e70dbd34ad269db44fdb9f63eccc448b632cfc98d1b635c3ee6a77362ad')

prepare() {
  cd "${pkgname}-${pkgver}"
  sed -e "s:normalize-audio:normalize:g" -i ${pkgname}
  # https://bugs.archlinux.org/task/58046
  sed -i 's/^#CDDBMETHOD=musicbrainz/CDDBMETHOD=cddb/' abcde.conf
  # replace inetutils hostname with coreutils uname -n
  patch -Np1 -i ../hostname.patch
}

package() {
  make -C "${pkgname}-${pkgver}" DESTDIR="${pkgdir}" prefix=/usr sysconfdir=/etc install
}

