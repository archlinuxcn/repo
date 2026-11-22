# Maintainer: gilcu3
# Contributor: badcasa <sebastian.stueber [at] t-online [dot] de>

pkgname=isabelle
pkgver=2026
pkgrel=1
pkgdesc="A generic proof assistant. It allows mathematical formulas to be expressed in a formal language and provides tools for proving those formulas in a logical calculus."
arch=('x86_64' 'aarch64')
url="https://www.cl.cam.ac.uk/research/hvg/Isabelle/"
license=('custom:BSD')
groups=('science')
# Mirrors the Ubuntu package list in upstream's src/Pure/Tools/docker_build.scala
depends=('fontconfig' 'libgomp' 'libx11' 'libxext' 'libxi' 'libxrender' 'libxtst')
optdepends=('texlive-latexextra: document preparation'
            'texlive-bibtexextra: document preparation'
            'texlive-fontsextra: document preparation'
            'texlive-fontutils: document preparation'
            'texlive-mathscience: document preparation'
            'perl: HTML presentation of BibTeX databases (bib2xhtml)'
            'rlwrap: line editing in "isabelle console"'
            'openssh: SSH connections and remote builds'
            'gtk3: Isabelle/VSCode (bundled VSCodium)'
            'nss: Isabelle/VSCode (bundled VSCodium)'
            'alsa-lib: Isabelle/VSCode (bundled VSCodium)'
            'libxkbfile: Isabelle/VSCode (bundled VSCodium)')
# Bundled prebuilt binaries break when stripped (e.g. zipperposition)
options=('!strip')
_dist="https://isabelle.in.tum.de/website-Isabelle${pkgver//_/-}/dist"
source=(isabelle.desktop)
source_x86_64=("$_dist/Isabelle${pkgver//_/-}_linux.tar.gz")
source_aarch64=("$_dist/Isabelle${pkgver//_/-}_linux_arm.tar.gz")
sha256sums=('84b61a83692939ca9e08402f1c55a06e4ccac8941664435d20b0ef0ceed9f43a')
sha256sums_x86_64=('858c995b32216b3876bf395c3be843147d1f1eee404bc6c958d7534ee335e48d')
sha256sums_aarch64=('edfb1670d8bdfa42488829ca0379c219b874a1e7548340c9951ffd2250da5a7f')

package() {
  install -Dm644 "$pkgname.desktop" "$pkgdir/usr/share/applications/$pkgname.desktop"
  
	cd "$srcdir/Isabelle${pkgver//_/-}"
	mkdir -p $pkgdir/opt/isabelle
	cp -r * $pkgdir/opt/isabelle/
	$pkgdir/opt/isabelle/bin/isabelle install -d /opt/isabelle $pkgdir/usr/bin
}

