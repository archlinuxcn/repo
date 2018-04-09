# Maintainer: Fabio 'Lolix' Loli <lolix@disroot.org> -> https://github.com/FabioLolix
# Contributor: Stefano Capitani <stefanoatmanjarodotorg>
# Contributor: Florian Pritz <f-p@gmx.at>

pkgname=inxi
pkgver=2.9.12
pkgrel=1
pkgdesc="script to get system information"
arch=('any')
url="https://github.com/smxi/inxi"
license=('GPL')
depends=('coreutils' 'gawk' 'grep' 'pciutils' 'perl' 'procps-ng' 'sed')
optdepends=(
  "dmidecode: inxi -M if no sys machine data"
  "file: inxi -o unmounted file system"
  "hddtemp: inxi -Dx show hdd temp"
  "net-tools: inxi -i ip lan-deprecated"
  "iproute2: inxi -i ip lan"
  "lm_sensors: inxi -s sensors output"
  "usbutils: inxi -A usb audio;-N usb networking"
  "kmod: inxi -Ax,-Nx module version"
  "systemd-sysvcompat: inxi -I runlevel"
  "sudo: inxi -Dx hddtemp-user;-o file-user"
  "mesa-demos: inxi -G glx info"
  "xorg-xdpyinfo: inxi -G multi screen resolution"
  "xorg-xprop: inxi -S desktop data"
  "xorg-xrandr: inxi -G single screen resolution"
)
options=('zipman')
_commit=e43933452fb8f99fee31a26d7adf03b670c5ffab
source=("$pkgname-$pkgver.tar.gz::$url/archive/$_commit.tar.gz")
sha256sums=('b6c041bff3189bfc662eb72eb7ba3ca9bb19c408e4ababaeea723a91e5198224')

pkgver() {
    cd "${pkgname}-${_commit}"

    # change version
    awk '/self_version=/ {print $2}' inxi | cut -c 16-21
}

prepare() {
    cd "${pkgname}-${_commit}"
    
    # temp move inxi to pinxi
    mv inxi pinxi

    # patches here

    # temp move pinxi back to inxi
    mv pinxi inxi
}

package() {
    cd "${pkgname}-${_commit}"
  install -D -m755 $pkgname "${pkgdir}/usr/bin/$pkgname"
  install -D -m755 $pkgname.1 "${pkgdir}/usr/share/man/man1/$pkgname.1"
}

