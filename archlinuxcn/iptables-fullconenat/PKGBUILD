# Maintainer: Edward Pacman <edward@edward-p.xyz>

_pkgbase=iptables
pkgbase=iptables-fullconenat
pkgname=(iptables-fullconenat iptables-fullconenat-nft)
pkgver=1.8.4
pkgrel=1
epoch=1
pkgdesc='Linux kernel packet control tool with FULLCONENAT support.'
arch=(x86_64)
license=(GPL2)
url='https://www.netfilter.org/projects/iptables/index.html'
depends=(libnftnl libpcap libnfnetlink libnetfilter_conntrack bash netfilter-fullconenat-dkms-git)
makedepends=(linux-api-headers)
provides=('iptables')
conflicts=(iptables)
install=${pkgbase}.install
backup=(etc/ethertypes etc/iptables/{ip,ip6}tables.rules)
source=(https://www.netfilter.org/projects/iptables/files/$_pkgbase-$pkgver.tar.bz2{,.sig}
        empty.rules simple_firewall.rules empty-{filter,mangle,nat,raw,security}.rules
        {arp,eb,ip,ip6}tables.service iptables-{legacy,nft}-flush
        "libipt_FULLCONENAT.c::https://raw.githubusercontent.com/Chion82/netfilter-full-cone-nat/master/libipt_FULLCONENAT.c")
sha1sums=('cd5fe776fb2b0479b3234758fc333777caa1239b'
          'SKIP'
          '83b3363878e3660ce23b2ad325b53cbd6c796ecf'
          'f085a71f467e4d7cb2cf094d9369b0bcc4bab6ec'
          'd9f9f06b46b4187648e860afa0552335aafe3ce4'
          'c45b738b5ec4cfb11611b984c21a83b91a2d58f3'
          '1694d79b3e6e9d9d543f6a6e75fed06066c9a6c6'
          '7db53bb882f62f6c677cc8559cff83d8bae2ef73'
          'ebbd1424a1564fd45f455a81c61ce348f0a14c2e'
          '95b0ee26f03132a948fea9f2136b2e2e6a4b40fe'
          'b668ba50d55030c68431a95756bc1f291d74b2b2'
          '8d66d21fa4cbfe2a80478301af94ba54f65e4ea0'
          '9cec592787e32451f58fa608ea057870e07aa704'
          'd10af7780d1634778d898c709e2d950aa1561856'
          '15c1684f3e671f4d0ede639a7c9c08e1a841511c'
          '6defc372f039b484948c9bb6d88737967818b2dd')
validpgpkeys=('C09DB2063F1D7034BA6152ADAB4655A126D292E4') # Netfilter Core Team

prepare() {
  mkdir build
  cd $_pkgbase-$pkgver

  cp ../libipt_FULLCONENAT.c extensions/
  # use system one
  rm include/linux/types.h
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
  provides=(iptables iptables-fullconenat arptables ebtables)
  conflicts=(iptables iptables-fullconenat arptables ebtables)
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
