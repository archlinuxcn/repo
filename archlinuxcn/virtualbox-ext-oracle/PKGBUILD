# Maintainer: Sébastien Luttringer

pkgname=virtualbox-ext-oracle
_version=6.1.13-139853
pkgver=${_version/-/.}
pkgrel=1
pkgdesc='Oracle VM VirtualBox Extension Pack'
arch=('any')
url='https://www.virtualbox.org/'
license=('custom:PUEL')
depends=("virtualbox")
optdepends=('rdesktop: client to connect vm via RDP')
options=('!strip')
install=virtualbox-ext-oracle.install
source=("https://www.virtualbox.org/download/testcase/Oracle_VM_VirtualBox_Extension_Pack-${_version}.vbox-extpack")
noextract=("Oracle_VM_VirtualBox_Extension_Pack-$pkgver.vbox-extpack")
sha256sums=('4f9400e40529df61001b5ef4334d5928aa4cd3f9b7035e9cb33357cca108abb5')

prepare() {
  # shrink uneeded cpuarch
  [[ -d shrunk ]] || mkdir shrunk
  tar xfC "Oracle_VM_VirtualBox_Extension_Pack-${_version}.vbox-extpack" shrunk
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
