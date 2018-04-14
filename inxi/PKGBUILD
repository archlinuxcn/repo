# Maintainer: Fabio 'Lolix' Loli <lolix@disroot.org> -> https://github.com/FabioLolix
# Contributor: Stefano Capitani <stefanoatmanjarodotorg>
# Contributor: Florian Pritz <f-p@gmx.at>

pkgname=inxi
pkgver=3.0.03
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
source=("${pkgname}-${pkgver}::https://github.com/smxi/inxi/archive/${pkgver}-1.tar.gz")
sha256sums=('80f2fef56567311dcae9a70c7d592cbc516c4000a643a5a9b938a28c12c5a90d')

package() {
  cd "${pkgname}-${pkgver}-1"
  install -D -m755 $pkgname "${pkgdir}/usr/bin/$pkgname"
  install -D -m755 $pkgname.1 "${pkgdir}/usr/share/man/man1/$pkgname.1"
}

