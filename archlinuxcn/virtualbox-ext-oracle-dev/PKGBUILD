# Maintainer: heavysink

pkgname=virtualbox-ext-oracle-dev
_pkgver=7.0.97-157803
pkgver=7.0.97.157803
pkgrel=1
pkgdesc='Oracle VM VirtualBox Extension Pack for virtualbox dev version'
arch=('any')
url='https://www.virtualbox.org/'
license=('custom:PUEL')
depends=('virtualbox-svn')
optdepends=('rdesktop: client to connect vm via RDP')
options=('!strip')
install=virtualbox-ext-oracle-dev.install
source=("https://www.virtualbox.org/download/testcase/Oracle_VM_VirtualBox_Extension_Pack-${_pkgver}.vbox-extpack")
provides=('virtualbox-ext-oracle')
conflicts=('virtualbox-ext-oracle')
noextract=("Oracle_VM_VirtualBox_Extension_Pack-$_pkgver.vbox-extpack")
sha256sums=('d812bf7d472beafcf3acd5c4d59c8f80b0893ee17d8ca435a7bc0e4ec8b74fef')

prepare() {
  # shrink uneeded cpuarch
  [[ -d shrunk ]] || mkdir shrunk
  tar xfC "Oracle_VM_VirtualBox_Extension_Pack-$_pkgver.vbox-extpack" shrunk
  rm -r shrunk/{darwin*,solaris*,win*}
  tar -c --gzip --file shrunk.vbox-extpack -C shrunk .
}

package() {
  install -Dm 644 shrunk.vbox-extpack \
    "$pkgdir/usr/share/virtualbox/extensions/Oracle_VM_VirtualBox_Extension_Pack-$pkgver.vbox-extpack"
  install -Dm 644 shrunk/ExtPack-license.txt \
    "$pkgdir/usr/share/licenses/$pkgname/PUEL"
}

