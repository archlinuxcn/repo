# Maintainer: Sébastien Luttringer

pkgname=virtualbox-ext-oracle
pkgver=6.1.26
pkgrel=1
pkgdesc='Oracle VM VirtualBox Extension Pack'
arch=('any')
url='https://www.virtualbox.org/'
license=('custom:PUEL')
depends=('virtualbox')
optdepends=('rdesktop: client to connect vm via RDP')
options=('!strip')
install=virtualbox-ext-oracle.install
source=("https://download.virtualbox.org/virtualbox/$pkgver/Oracle_VM_VirtualBox_Extension_Pack-$pkgver.vbox-extpack")
noextract=("Oracle_VM_VirtualBox_Extension_Pack-$pkgver.vbox-extpack")
sha256sums=('aaa1a1f8615d5bd2e08b158ce6f415262fbb595e169e2d415c5b1844ac258eee')

prepare() {
  # shrink uneeded cpuarch
  [[ -d shrunk ]] || mkdir shrunk
  tar xfC "Oracle_VM_VirtualBox_Extension_Pack-$pkgver.vbox-extpack" shrunk
  rm -r shrunk/{darwin*,solaris*,win*}
  tar -c --gzip --file shrunk.vbox-extpack -C shrunk .
}

package() {
  install -Dm 644 shrunk.vbox-extpack \
    "$pkgdir/usr/share/virtualbox/extensions/Oracle_VM_VirtualBox_Extension_Pack-$pkgver.vbox-extpack"
  install -Dm 644 shrunk/ExtPack-license.txt \
    "$pkgdir/usr/share/licenses/$pkgname/PUEL"
}

# vim:set ts=2 sw=2 et:
