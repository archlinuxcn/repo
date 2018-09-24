# Maintainer: Fabio 'Lolix' Loli <lolix@disroot.org> -> https://github.com/FabioLolix
# Contributor: Stefano Capitani <stefanoatmanjarodotorg>
# Contributor: Florian Pritz <f-p@gmx.at>

pkgname=inxi
pkgver=3.0.24
pkgrel=1
pkgdesc="Full featured CLI system information tool"
arch=('any')
url="https://github.com/smxi/inxi"
license=('GPL')
depends=('coreutils' 'pciutils' 'perl' 'procps-ng')
optdepends=(
  "bind-tools: -i wlan IP"
  "dmidecode: inxi -M if no sys machine data"
  "file: inxi -o unmounted file system"
  "hddtemp: inxi -Dx show hdd temp"
  "iproute2: inxi -i ip lan"
  "kmod: inxi -Ax,-Nx module version"
  "lm_sensors: inxi -s sensors output"
  "mesa-demos: inxi -G glx info"
  "net-tools: inxi -i ip lan-deprecated"
  "perl-io-socket-ssl: -U; -w,-W; -i (if dig not installed)"
  "perl-cpanel-json-xs: --output json - required for export"
  "perl-json-xs: --output json - required for export (legacy)"
  "perl-xml-dumper: --output xml - Crude and raw"
  "systemd-sysvcompat: inxi -I runlevel"
  "sudo: inxi -Dx hddtemp-user;-o file-user"
  "tree: --debugger 20,21 /sys tree"
  "usbutils: inxi -A usb audio;-N usb networking"
  "wmctrl: -S active window manager (not all wm)"
  "xorg-xdpyinfo: inxi -G multi screen resolution"
  "xorg-xprop: inxi -S desktop data"
  "xorg-xrandr: inxi -G single screen resolution"
)
options=('zipman')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/smxi/inxi/archive/${pkgver}-1.tar.gz")
sha256sums=('3f1e5a88fe8cf697f86caea4763911102e163d0cdb63ddf21bda1a67e51f780d')

package() {
  cd "${pkgname}-${pkgver}-1"
  install -D -m755 $pkgname "${pkgdir}/usr/bin/$pkgname"
  install -D -m755 $pkgname.1 "${pkgdir}/usr/share/man/man1/$pkgname.1"
}

