# Maintainer: éclairevoyant
# Contributor: dangerdev <dangerdev at disroot dot org>
# Contributor: Danct12 <danct12 at disroot dot org>
# Contributor: Bart Ribbers <bribbers at disroot dot org>

_pkgver_images_system="18.1-20230311"
_pkgver_images_system_x86="18.1-20230311"
_pkgver_images_system_arm="18.1-20230311"
_pkgver_images_system_arm64="18.1-20230311"
_pkgver_images_vendor="18.1-20230311"
_pkgver_images_vendor_x86="18.1-20230311"
_pkgver_images_vendor_arm="18.1-20230311"
_pkgver_images_vendor_arm64="18.1-20230311"
pkgname=waydroid-image
pkgver="${_pkgver_images_system//-/_}"
pkgrel=1
pkgdesc="LineageOS-based Android images for Waydroid"
arch=('x86_64' 'i686' 'armv7h' 'aarch64')
url='https://waydro.id'
license=('Apache')
depends=('waydroid')
_srcprefix="https://sourceforge.net/projects/waydroid/files/images"
source_x86_64=("$_srcprefix/system/lineage/waydroid_x86_64/lineage-$_pkgver_images_system-VANILLA-waydroid_x86_64-system.zip"
               "$_srcprefix/vendor/waydroid_x86_64/lineage-$_pkgver_images_vendor-MAINLINE-waydroid_x86_64-vendor.zip")
source_i686=("$_srcprefix/system/lineage/waydroid_x86/lineage-$_pkgver_images_system_x86-VANILLA-waydroid_x86-system.zip"
             "$_srcprefix/vendor/waydroid_x86/lineage-$_pkgver_images_vendor_x86-MAINLINE-waydroid_x86-vendor.zip")
source_armv7h=("$_srcprefix/system/lineage/waydroid_arm/lineage-$_pkgver_images_system_arm-VANILLA-waydroid_arm-system.zip"
               "$_srcprefix/vendor/waydroid_arm/lineage-$_pkgver_images_vendor_arm-MAINLINE-waydroid_arm-vendor.zip")
source_aarch64=("$_srcprefix/system/lineage/waydroid_arm64/lineage-$_pkgver_images_system_arm64-VANILLA-waydroid_arm64-system.zip"
                "$_srcprefix/vendor/waydroid_arm64/lineage-$_pkgver_images_vendor_arm64-MAINLINE-waydroid_arm64-vendor.zip")
sha256sums_x86_64=('5ca5f2a6db1b80ab9fc3ba2df021fd0ab77e183c2fcf2273a0763e6cab4f46a9'
                   '81951b1ffcd2f573588fa47f5ca4e10ec56219564361dbb1491a3d40b29149c2')
sha256sums_i686=('e22072b32e7129ddf354838726b4e4054dda44b8ef537e68a20b736dc4a51004'
                 '4ed842e83e0caf6476c11c8261b091658cb617cc94598bb15b7def4c334c8699')
sha256sums_armv7h=('588c06f6dad50c98b81d6070796a387a1a5ddfbcebc8810ec38f2b078b5e2355'
                   '4a71c9f36aa32a4e642b3f1afbeeb657d07358e7f43820d66adaf6b9b4d783d2')
sha256sums_aarch64=('f995eb8180a7de1fd092ad63b22afc5b0d72293e21c825ca87831ef5a169120e'
                    'd2361084202816d8c05e333873872e44ebd6d66645ca86c788e5d9928ef0aecc')

package() {
	install -Dm644 {system,vendor}.img -t "$pkgdir/usr/share/waydroid-extra/images/"
}
