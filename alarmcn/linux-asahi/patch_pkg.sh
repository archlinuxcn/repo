#!/bin/sh

sed -i -e 's/_package()/_origin_package()/' PKGBUILD

cat >> PKGBUILD <<EOF
_package() {
  _origin_package
  cd "\$srcdir/\$_srcname"
  local kernver="\$(<version)"
  local modulesdir="\$pkgdir/usr/lib/modules/\$kernver"
  install -Dm644 "\$(make -s image_name)" "\$modulesdir/vmlinuz"
  install -Dm644 arch/arm64/boot/Image "\$modulesdir/vmlinuz-nogz"
}
EOF
