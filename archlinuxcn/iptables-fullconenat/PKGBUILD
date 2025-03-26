# Maintainer: Edward Pacman <edward@edward-p.xyz>

_pkgbase=iptables
pkgbase=iptables-fullconenat
pkgname=(iptables-fullconenat iptables-fullconenat-nft)
pkgver=1.8.11
pkgrel=2
epoch=1
pkgdesc='Linux kernel packet control tool with FULLCONENAT support.'
arch=(x86_64)
license=('GPL-2.0-only')
url='https://www.netfilter.org/projects/iptables/index.html'
depends=(libnftnl libpcap libnfnetlink libnetfilter_conntrack bash)
makedepends=(linux-api-headers)
optdepends=("netfilter-fullconenat: kernel module for fullconenat")
provides=(libip4tc.so libip6tc.so libipq.so libxtables.so)
conflicts=(iptables)
install=${pkgbase}.install
backup=(etc/ethertypes etc/iptables/{ip,ip6}tables.rules)
source=(https://www.netfilter.org/projects/iptables/files/$_pkgbase-$pkgver.tar.xz{,.sig}
        empty.rules simple_firewall.rules empty-{filter,mangle,nat,raw,security}.rules
        {arp,eb,ip,ip6}tables.service iptables-{legacy,nft}-flush
        iptables-apply-default-path.patch
        "libipt_FULLCONENAT.c::https://raw.githubusercontent.com/llccd/netfilter-full-cone-nat/dev/libipt_FULLCONENAT.c"
        "libip6t_FULLCONENAT.c::https://raw.githubusercontent.com/llccd/netfilter-full-cone-nat/dev/libip6t_FULLCONENAT.c")
sha256sums=('d87303d55ef8c92bcad4dd3f978b26d272013642b029425775f5bad1009fe7b2'
            'SKIP'
            '630d774f089703c2c7370db6d7c188dae25d00c26feaa3d3de8eb52519033948'
            '9e83d7ae39d31881790f814930d44acbaeab1520adb2fb4fcb80f0bbfab174b9'
            '09b90da35c2c8cb0fbda63b300f06d2387a102ca53a40980ef0b49829e249528'
            '92755648f456e235d17a8faeb5f46d27af66eb4db10ea4bac0abd3e35e2dae07'
            '52bd70dff3e1e1a64127ad7ed86840834b79756c3bdb6947b7c6279ffe95dd48'
            '5768a471c0559848635c39d270e456bfa5c43eda65f5f6f666fea2d277183a37'
            '91161a73f323016a9efc5eabd16243d20f8ca2467995cf0eabfb95f845090121'
            'dd1a867085900eec1f1d4e12f97a1f44707c717246f6787ed42d4225343920d6'
            '82e09b4151d5c1dd0fc212189c670f8f29e8ec85e7e9cdc57f49dcea00d7e9ca'
            '78f090812b5bb9aec597ce2cf757da1c58ec772c60bf55f10267f06459aefd9b'
            'c37c69db5077a061fd72fc3b199712f1bed8688de8008f219223fadd6fa6c06f'
            '40680b3c877926a2bac698ea58f52d1d4b3ab152ee68ccd7fa7ca51aeedc3b2d'
            '6d3e7bdeebdaeaf83ed448f4d42a979c8c59fb5e919f6f860ed340c2c9afef1a'
            '770ceaedce26d05eb1b9d0c4c65f5b8e92facd1dc0652a29c859336d6bc347f6'
            '8db6a5a00ea5a40bb96a7bbdf4e4ce6bc92b5b6ef6c12b7a18559d1516e4c3e0'
            'dba600c891b5d7a83083f3baf076da7d80535a8d8a2fc6feae43faa650676470')
validpgpkeys=('C09DB2063F1D7034BA6152ADAB4655A126D292E4'
              '37D964ACC04981C75500FB9BD55D978A8A1420E4'
              '8C5F7146A1757A65E2422A94D70D1A666ACF2B21') # Netfilter Core Teamls

prepare() {
  mkdir build
  cd $_pkgbase-$pkgver

  cp ../libip{,6}t_FULLCONENAT.c extensions/
  # use system one
  rm include/linux/types.h

  ln -rs libiptc/linux_list.h include/libiptc

  # use Arch path
  patch -p0 -i ../iptables-apply-default-path.patch
}

build() {
  cd build
  ../$_pkgbase-$pkgver/configure \
    --prefix=/usr \
    --sysconfdir=/etc \
    --sbindir=/usr/bin \
    --libexecdir=/usr/lib \
    --enable-bpf-compiler \
    --enable-devel \
    --enable-libipq \
    --enable-shared
  sed -e 's/ -shared / -Wl,-O1,--as-needed\0/g' -i libtool
  make
}

package_iptables-fullconenat() {
  pkgdesc+=' (using legacy interface)'
  _package legacy
}

package_iptables-fullconenat-nft() {
  pkgdesc+=' (using nft interface)'
  depends+=(nftables)
  provides+=(iptables iptables-fullconenat arptables ebtables)
  conflicts+=(iptables iptables-fullconenat arptables ebtables)
  backup+=(etc/{arp,eb}tables.conf)

  _package nft

  install -Dt "$pkgdir/usr/lib/systemd/system" -m644 {arp,eb}tables.service
  touch "$pkgdir"/etc/{arp,eb}tables.conf
}

_package() {
  DESTDIR="$pkgdir" make -C build install

  for _x in {arp,eb,ip,ip6}tables{,-restore,-save} iptables-xml; do
    if [[ $1 = nft || $_x = ip* ]]; then
      ln -sf xtables-$1-multi "$pkgdir/usr/bin/$_x"
    else
      rm "$pkgdir/usr/bin/$_x"
    fi
  done

  install -Dt "$pkgdir/usr/lib/systemd/system" -m644 {ip,ip6}tables.service
  install -D iptables-$1-flush "$pkgdir/usr/lib/systemd/scripts/iptables-flush"

  install -Dm644 empty.rules "$pkgdir/etc/iptables/iptables.rules"
  install -Dm644 empty.rules "$pkgdir/etc/iptables/ip6tables.rules"
  install -Dt "$pkgdir/usr/share/iptables" -m644 *.rules
  ln -srt "$pkgdir/etc/iptables" "$pkgdir"/usr/share/iptables/{empty,simple_firewall}.rules
}

# vim:set sw=2 et:
