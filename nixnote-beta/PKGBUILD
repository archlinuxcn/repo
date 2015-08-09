# Maintainer: Chris Fordham <chris at fordham-nagy dot id dot au> aka flaccid
# Contributor: J. Luck <jluck@udel.edu>
# Package Build Source: https://github.com/flaccid/archlinux-packages/blob/master/nixnote-beta/PKGBUILD

pkgname=nixnote-beta
_pkgname=nixnote2
pkgver=2.0
_pkgver="NixNote2%20-%20Beta%203"
_beta_release="beta3"
pkgrel=7
pkgdesc="Formerly called nevernote, nixnote is a clone of Evernote designed to run on Linux."
url="http://www.sourceforge.net/projects/nevernote/"
arch=('x86_64')
license=('GPL')
depends=('mimetex' 'opencv' 'poppler-qt4' 'qt4' 'sqlite' 'tidyhtml' 'qtwebkit')
provides=('nixnote2')
conflicts=('nixnote' 'nixnote2-git')
replaces=('nixnote')
source=("http://download2.polytechnic.edu.na/pub4/sourceforge/n/ne/nevernote/${_pkgver}/${_pkgname}-${pkgver}-${_beta_release}_amd64.tar.gz")
sha256sums=('09c22b0a3bc7eca73abc94feb82b719a3229b90c9607a367a62b5b0771fc3126')

package()
{
	cp -R "${srcdir}/nixnote2/usr" "${pkgdir}/"
}

# vim:set ts=2 sw=2 Et:
