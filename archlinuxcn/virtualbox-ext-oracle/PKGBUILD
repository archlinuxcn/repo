# Maintainer: Sébastien Luttringer

pkgname=virtualbox-ext-oracle
pkgver=7.0.6
_filever="${pkgver}a-155176"
pkgrel=2
pkgdesc='Oracle VM VirtualBox Extension Pack'
arch=('any')
url='https://www.virtualbox.org/'
license=('custom:PUEL')
depends=("virtualbox=${pkgver}")
optdepends=('rdesktop: client to connect vm via RDP')
options=('!strip')
install=virtualbox-ext-oracle.install
source=("https://download.virtualbox.org/virtualbox/${pkgver}/Oracle_VM_VirtualBox_Extension_Pack-${_filever}.vbox-extpack")
noextract=("Oracle_VM_VirtualBox_Extension_Pack-${_filever}.vbox-extpack")
sha256sums=('292961aa8723b54f96f89f6d8abf7d8e29259d94b7de831dbffb9ae15d346434')

prepare() {
  # shrink uneeded cpuarch
  [[ -d shrunk ]] || mkdir shrunk
  tar xfC "Oracle_VM_VirtualBox_Extension_Pack-${_filever}.vbox-extpack" shrunk
  rm -r shrunk/{darwin*,solaris*,win*}
  tar -c --gzip --file shrunk.vbox-extpack -C shrunk .
}

package() {
  install -Dm 644 shrunk.vbox-extpack \
    "$pkgdir/usr/share/virtualbox/extensions/Oracle_VM_VirtualBox_Extension_Pack-${_filever}.vbox-extpack"
  install -Dm 644 shrunk/ExtPack-license.txt \
    "$pkgdir/usr/share/licenses/${pkgname}/PUEL"
}

# vim:set ts=2 sw=2 et:
