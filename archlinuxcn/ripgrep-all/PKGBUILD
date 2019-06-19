# Maintainer: phiresky <phireskyde+aur@gmail.com>

pkgname=ripgrep-all
pkgver=0.9.2
pkgrel=1
arch=(x86_64)
pkgdesc="rga: ripgrep, but also search in PDFs, E-Books, Office documents, zip, tar.gz, etc."
url="https://github.com/phiresky/ripgrep-all"
license=('AGPL3')
depends=('ripgrep' 'pandoc' 'poppler' 'ffmpeg')
archivename="ripgrep_all-${pkgver}-${arch}-unknown-linux-musl"
source=("https://github.com/phiresky/ripgrep-all/releases/download/${pkgver}/${archivename}.tar.gz")
sha1sums=('59bbe4209948a7a3b74ed9fd06983c757dae747e')

package() {
  cd "$srcdir/$archivename"
  mkdir -p "$pkgdir/usr/bin"
  cp rga rga-preproc "$pkgdir/usr/bin"
}
