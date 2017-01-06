# Maintainer: mortzprk <mortz.prk@gmail.com>
# Package Build Source: https://github.com/flaccid/archlinux-packages/blob/master/nixnote-beta/PKGBUILD

pkgname=nixnote-beta
_pkgname=nixnote2
pkgver=2.0_beta11
_pkgver="NixNote2%20-%20Beta%2011"
_beta_release="beta11"
pkgrel=2
pkgdesc="Formerly called nevernote, nixnote is a clone of Evernote designed to run on Linux"
url="http://www.sourceforge.net/projects/nevernote"
arch=('x86_64' 'i686')
license=('GPL2')
provides=('nixnote2')
conflicts=('nixnote' 'nixnote2-git')
replaces=('nixnote')
source=("nixnote2.desktop")

# QT4 Version. Uncomment lines below and comment out QT5 section
#depends=('mimetex' 'opencv' 'poppler-qt4' 'qt4' 'sqlite' 'tidyhtml' 'qtwebkit' 'libcurl-compat')
#sha256sums=('6c88cd5ae3f5c18e342fcf5165891b22d99818d3fe2ac2b124262b8ba23bb4d1')
#source_x86_64=("https://iweb.dl.sourceforge.net/project/nevernote/${_pkgver}/Linux/Qt4/${_pkgname}-2.0-${_beta_release}_amd64.tar.gz")
#sha256sums_x86_64=('c745a23e2fea052fe8308e51f05e782e586d625a765f3b1d626d82c75ce4f265')
#source_i686=("https://iweb.dl.sourceforge.net/project/nevernote/${_pkgver}/Linux/Qt4/${_pkgname}-2.0-${_beta_release}_i386.tar.gz")
#sha256sums_i686=('8fce0be65678b3154acdaa3551d8bf11bdf70a7e9b6feb93fc2448b1673b4c46')

# QT5 Version.
depends=('mimetex' 'opencv' 'poppler-qt5' 'qt5-base' 'qt5-webkit' 'sqlite' 'tidyhtml' 'qtwebkit' 'libcurl-compat')
sha256sums=('6c88cd5ae3f5c18e342fcf5165891b22d99818d3fe2ac2b124262b8ba23bb4d1')
source_x86_64=("https://iweb.dl.sourceforge.net/project/nevernote/${_pkgver}/Linux/Qt5/${_pkgname}-2.0-${_beta_release}_amd64.tar.gz")
sha256sums_x86_64=('39eb933160054abda2d3cb5b1b73a0113b7d96335b50b8c13f2375b1dff04e18')
source_i686=("https://iweb.dl.sourceforge.net/project/nevernote/${_pkgver}/Linux/Qt5/${_pkgname}-2.0-${_beta_release}_i386.tar.gz")
sha256sums_i686=('998ca65d53e1495be03ba25f90a6956239ec64cab72c699e5be21b0074ebd872')

package() {
    cp -R "${srcdir}/nixnote2/usr" "${pkgdir}/"
    install -D -m644 nixnote2.desktop ${pkgdir}/usr/share/applications/nixnote2.desktop
}
