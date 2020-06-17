# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix
# Contributor: Stefano Capitani <stefanoatmanjarodotorg>
# Contributor: Florian Pritz <f-p@gmx.at>

pkgname=inxi
pkgver=3.1.01
pkgrel=1
pkgdesc="Full featured CLI system information tool"
arch=(any)
url="https://github.com/smxi/inxi"
license=(GPL3)
depends=(coreutils pciutils perl procps-ng)
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
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/smxi/inxi/archive/${pkgver}-1.tar.gz")
sha256sums=('0b46e0dd3e5391c7005d08fa52365037f27bd8d7d0a56a6900d18e11720b1c7c')

package() {
  cd "${pkgname}-${pkgver}-1"
  install -D -m755 $pkgname "${pkgdir}/usr/bin/$pkgname"
  install -D -m755 $pkgname.1 "${pkgdir}/usr/share/man/man1/$pkgname.1"
}

