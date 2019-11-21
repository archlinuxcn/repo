# Maintainer: Shalygin Konstantin <k0ste@k0ste.ru>
# Contributor: Shalygin Konstantin <k0ste@k0ste.ru>
# Contributor: Evgeny Cherkashin <eugeneai@irnok.net>

pkgname='frr'
pkgver='7.2'
pkgrel='2'
pkgdesc='FRRouting (quagga fork) supports BGP4, OSPFv2, OSPFv3, ISIS, RIP, RIPng, PIM, LDP, BFD, VRRP, NHRP and EIGRP.'
arch=('any')
url="https://frrouting.org/"
license=('GPL2')
depends=('libcap' 'libnl' 'readline' 'ncurses' 'perl' 'pam' 'json-c' 'net-snmp'
	 'rtrlib' 'libyang' 'libunwind' 'c-ares')
makedepends=('patch' 'gcc' 'net-snmp' 'bison' 'perl-xml-libxml' 'python-sphinx')
checkdepends=('python-pytest')
optdepends=('rsyslog: syslog support')
conflicts=('quagga' 'babeld' 'quagga_cumulus')
provides=('quagga' 'quagga_cumulus')
backup=("etc/${pkgname}/${pkgname}.conf"
	"etc/${pkgname}/daemons.conf"
	"etc/${pkgname}/vtysh.conf")
source=("https://github.com/FRRouting/${pkgname}/archive/${pkgname}-${pkgver}.tar.gz"
        "${pkgname}.sysusers"
        "${pkgname}.tmpfiles"
        "${pkgname}_${pkgver}_Archlinux.patch"
	"frr-init-functions"
	"5213.patch")
sha256sums=('11dff4a4b2f705bf0a4fd2ca2f186b7f91a104d3a2a17c79bb4009d69b38c924'
            '9371cc0522d13621c623b5da77719052bdebdceb7ffdbdc06fc32a2f07118e7e'
            '6f8dd86ef9c600763faead3052908531e8dc8ef67058e6f7f8da01bf0fe4eb89'
            'fbbd0b6d40dffbdb850ecabf91ab6bd22da07aa2c7c6406af5e3816988905e02'
            'e6e2592a8b0b18f7f173186fb4ebf23e642b3d912179f0bb36251962ca64cd7a'
            'ff30c1de8008aa02a1bae619644837f835372bca2c2244ef50e8963f8341a4d7')

prepare() {
  cd "${srcdir}/${pkgname}-${pkgname}-${pkgver}"
  patch -p1 -i "${srcdir}/${pkgname}_${pkgver}_Archlinux.patch"
  patch -p1 -i "${srcdir}/5213.patch"

  autoreconf -fvi
  ./configure \
    --prefix="/usr" \
    --sbindir="/usr/bin" \
    --sysconfdir="/etc/${pkgname}" \
    --localstatedir="/run/${pkgname}" \
    --enable-exampledir="/usr/share/doc/${pkgname}/examples" \
    --with-libpam \
    --enable-snmp="agentx" \
    --enable-multipath=256 \
    --enable-user="${pkgname}" \
    --enable-group="${pkgname}" \
    --enable-vty-group="${pkgname}vty" \
    --enable-configfile-mask="0640" \
    --enable-logfile-mask="0640" \
    --enable-shell-access \
    --enable-systemd \
    --enable-rpki \
    --enable-fpm
}

build() {
  cd "${srcdir}/${pkgname}-${pkgname}-${pkgver}"
  make
}

check() {
  cd "${srcdir}/${pkgname}-${pkgname}-${pkgver}"
  make check
}

package() {
  cd "${srcdir}/${pkgname}-${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install

  install -Dm0444 "${startdir}/frr-init-functions" "${pkgdir}/usr/bin/"

  pushd "redhat"
  sed -ri 's|/var/run/frr|/run/frr|g' "${pkgname}.logrotate"
  install -Dm0644 "${pkgname}.logrotate" "${pkgdir}/etc/logrotate.d/${pkgname}"
  for d in babeld bgpd bfdd eigrpd isisd ldpd nhrpd ospf6d ospfd ospfd-instance@ pbrd pimd ripd ripngd staticd zebra; do
    install -Dm0644 ${d}.service "${pkgdir}/usr/lib/systemd/system/${d}.service"
  done
  install -Dm0644 "${pkgname}.pam" "${pkgdir}/etc/pam.d/${pkgname}"
  install -Dm0644 "${srcdir}/${pkgname}.tmpfiles" "${pkgdir}/usr/lib/tmpfiles.d/${pkgname}.conf"
  install -Dm0644 "${srcdir}/${pkgname}.sysusers" "${pkgdir}/usr/lib/sysusers.d/${pkgname}.conf"
  popd

  pushd "tools"
  sed -ri 's|/usr/lib/frr/|/usr/bin/|g' "${pkgname}.service"
  install -Dm0644 "${pkgname}.service" "${pkgdir}/usr/lib/systemd/system/${pkgname}.service"
  popd

  pushd "tools/etc"
  install -Dm0644 "${pkgname}/daemons" "${pkgdir}/etc/${pkgname}/daemons.conf"
  install -Dm0644 "iproute2/rt_protos.d/${pkgname}.conf" "${pkgdir}/etc/iproute2/rt_protos.d/${pkgname}.conf"
  install -Dm0644 "${pkgname}/${pkgname}.conf" "${pkgdir}/etc/${pkgname}/${pkgname}.conf"
  install -Dm0644 "${pkgname}/vtysh.conf" "${pkgdir}/etc/${pkgname}/vtysh.conf"
  install -Dm0644 "rsyslog.d/45-${pkgname}.conf" "${pkgdir}/etc/rsyslog.d/45-${pkgname}.conf"
  popd

  chown -R 177:177 "${pkgdir}/etc/frr"

  pushd "${pkgdir}/usr/bin"
    for file in frr frr-reload frrcommon.sh frrinit.sh watchfrr.sh;
    do
      sed -ri 's|/lib/lsb/init-functions|/usr/bin/frr-init-functions|g' "$file";
    done
    sed -ri 's|C_PATH/daemons\"|C_PATH/daemons.conf\"|g' frrcommon.sh
    sed -ri 's|load_old_config \"\$C_PATH/daemons.conf\"|load_old_config \"\$C_PATH/daemons\"|g' frrcommon.sh
  popd

  pushd "${pkgdir}/usr/lib/systemd/system"
    sed -ri 's|frrinit.sh|frr|g' frr.service
  popd
}
