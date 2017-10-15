# Maintainer: mortzprk <mortz.prk@gmail.com>
# Contributor: yaroslav <proninyaroslav@mail.ru>
# Contributor: Chris Fordham <chris at fordham-nagy dot id dot au> aka flaccid
# Contributor: J. Luck <jluck@udel.edu>
# Package Build Source: https://github.com/flaccid/archlinux-packages/blob/master/nixnote/PKGBUILD

pkgname=nixnote
_pkgname=nixnote2
pkgver=2.0.2
_pkgver="NixNote2%20-%202.0.2"
pkgrel=2
pkgdesc="Formerly called nevernote, nixnote is a clone of Evernote designed to run on Linux"
url="http://www.sourceforge.net/projects/nevernote"
arch=('x86_64' 'i686')
license=('GPL2')
conflicts=('nixnote2' 'nixnote-beta')
depends=('mimetex' 'opencv' 'poppler-qt5' 'qt5-webkit' 'sqlite' 'tidyhtml' 'libcurl-compat' 'hunspell' 'libpng' 'intel-tbb' 'openexr' 'ffmpeg' 'libdc1394')
source=("nixnote2.desktop")
sha256sums=('227e6b13fce129adb492b1ab4b94eb3b56777a5939d02ae606b07f217bdb6182')
source_x86_64=("https://netcologne.dl.sourceforge.net/project/nevernote/${_pkgver}/qt5/${_pkgname}-${pkgver}_amd64.tar.gz")
sha256sums_x86_64=('c98454ac08d10849a8acdc496e7ac3435a052da511486903f67ddb7b03a8d7f5')
source_i686=("https://netix.dl.sourceforge.net/project/nevernote/${_pkgver}/qt5/${_pkgname}-${pkgver}_i386.tar.gz")
sha256sums_i686=('51c0c20df825920b6e2a55a0cf8d0bf49ddfdab5dad600894240a4e24645423a')

package() {
    cp -R "${srcdir}/nixnote2/usr" "${pkgdir}/"
    install -D -m644 nixnote2.desktop ${pkgdir}/usr/share/applications/nixnote2.desktop
}
