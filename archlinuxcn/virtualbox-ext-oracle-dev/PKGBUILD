# Maintainer: heavysink

pkgname=virtualbox-ext-oracle-dev
_pkgver=7.0.97-160850
pkgver=7.0.97.160850
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
sha256sums=('a07701fba28db01412f75bdaebc4bd56f6e5721f3a8ada93f47092d7b614825c')

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

