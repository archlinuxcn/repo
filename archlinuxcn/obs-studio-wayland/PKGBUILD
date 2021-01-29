# Maintainer: Antoine Damhet <xdbob at lse.epita.fr>
# Original-Maintainer: Jonathan Steel <jsteel at archlinux.org>
# Contributor: Benjamin Klettbach <b.klettbach@gmail.com>

_pkgname=obs-studio
pkgname=$_pkgname-wayland
provides=("$_pkgname")
conflicts=("$_pkgname")
pkgver=26.0.2
pkgrel=1
pkgdesc="Free, open source software for live streaming and recording (with wayland patches)"
arch=('x86_64')
url="https://obsproject.com"
license=('GPL2')
depends=('ffmpeg' 'jansson' 'libxinerama' 'libxkbcommon-x11' 'mbedtls'
         'qt5-svg' 'qt5-x11extras' 'curl' 'jack' 'gtk-update-icon-cache')
makedepends=('cmake' 'libfdk-aac' 'libxcomposite' 'x264' 'vlc' 'swig' 'python' 'luajit')
optdepends=('libfdk-aac: FDK AAC codec support'
            'libxcomposite: XComposite capture support'
            'libva-intel-driver: hardware encoding'
            'libva-mesa-driver: hardware encoding'
            'luajit: scripting support'
            'python: scripting support'
            'vlc: VLC Media Source support'
            'wlrobs-hg: screen capture on wlroots compositors')
source=(
  $_pkgname-$pkgver.tar.gz::https://github.com/jp9000/obs-studio/archive/$pkgver.tar.gz
  fix_python_binary_loading.patch
  0001-deps-glad-Add-EGL.patch
  0002-libobs-opengl-Rename-gl-x11.c-to-gl-x11-glx.c.patch
  0003-libobs-opengl-Factor-out-GLX-winsys.patch
  0004-libobs-opengl-Introduce-the-X11-EGL-winsys.patch
  0005-deps-glad-Make-X11-required-as-well.patch
  0006-ci-Install-qtbase5-private-dev-on-Linux.patch
  0007-libobs-nix-Move-X11-specific-code-to-obs-nix-x11.c.patch
  0008-libobs-Introduce-the-concept-of-a-Unix-platform.patch
  0009-UI-Set-the-Unix-platform-on-startup.patch
  0010-linux-capture-Fail-to-load-when-running-on-EGL.patch
  0011-libobs-Add-a-Wayland-platform.patch
  0012-libobs-opengl-Try-to-use-the-platform-display-if-ava.patch
  0013-libobs-opengl-Introduce-an-EGL-Wayland-renderer.patch
  0014-UI-Retrieve-Wayland-surface-from-QWindow.patch
  0015-UI-Destroy-display-when-becoming-invisible.patch
  0016-UI-Don-t-create-obs_display-when-QTToGSWindow-fails.patch
  0017-UI-Rename-callback-to-match-signal-name.patch
  0018-UI-Disable-and-ignore-Always-On-Top-on-Wayland-platf.patch
  0019-UI-Make-OBSQTDisplay-CreateDisplay-public-and-allow-.patch
  0020-UI-Check-for-Expose-and-PlatformSurface-events-to-cr.patch
  0021-Don-t-create-native-widget-siblings.patch
  0022-Cleanup-native-widgets.patch
  0023-libobs-graphics-Add-Linux-only-device_texture_create.patch
  0024-deps-glad-Add-DMA-BUF-EGL-extensions.patch
  0025-libobs-opengl-Implement-DMA-BUF-importing-on-EGL-ren.patch
)
sha512sums=('e93c312543f38702aee1cf2ed229e0a5faf876340f418d792353126c42d913fd70ebefce830b3ffa5ee6a5d42d4c84fa35673a436b7b7de5ce14becdaa2d7819'
            '93ad704cef425073b417d1ed95e076f688a6e45cdf589472c65e437d77297303f31dd8f15c7d5e30f83276a6396b732dfb5a695db9c773911aaa0423c5262177'
            '456973a51bbb3e84974525de757bc3c88c67faf0c36366a6787b72b30ba978491bfb1161d5364cf7b0174ced1fe8b04c0e2e4c13c6f88c79dbeb151ce24eb38f'
            '231b518b34951924ba0f7da56379036cdf2d08e9259365e67f617ed458e21c4a2d5193e25200d6270bf74f462a9916085a3f3aa9f4edd35c8e501922bef6f1b6'
            '3cdb29a4d3b639769758e8ea1d94a36baa89fec5e93110d1256ff275d83267c10f09888e6e29639d299e8322256d80ba19072519ae080bd461bc8cc2171e0405'
            '57e430c1ea3945c0ad9a33414c32a35623f870b0c9aaf79fc3e03a00f1ad8e2c890c28e509bf241ecd73f573c367b33262b6291d82f519d0b5234a76c1d72f7d'
            '09d71bf1a2f3e96a6bbba05d34e77407520741f9b302471d515af8d37f3f221b68f5656fd3c88899786044813743eb765c4bfbeab33fd3faf4f9a738f44873a3'
            '7bc1ea2d79b9c95f6fe12b77aa491f2072a2e417528ce95901b520fcfb80268dfd3bc14009b13932f833fbb7941427089b4e7d005b473863405f71c9a6c1987d'
            '19dfc1438743c18512190e663f313fcf0d0b11dbdff685e23f732c7234ce2b3b60c923c91035576979843f97a28ff9c877ffb9866b79e04a42e5c0df4988f762'
            '00a37e551cfb9218df7e431b55e8d882244ce06a52c70b8dbff145493fedba0c19d9cc39cbc53c7c2ad0cf4e6886f1302bd0b7eb9ff0de31ff9938e060e35d7c'
            '075ba030b5b2ebb54213eebb34523cce48abf53118c3c21bca9bd6e40c984f3739e3581a0ee0cec0e63f42a496c1dc42fbf12a8714133c7b6ad0ee1027326e5b'
            'd8aed1389391239a2e71525b66f9652958c8248a7bf9bfa5c296af72976c6d293635d16fed58a162e6a5228f15302530754619dd57c2db6156b9db631274762b'
            '25ba2513de78e335d8ba3c711fce9b0dfa2fe7d144a2ac8147fcf7a26a0dd9b69d26b1c809f519ddcb550d217fb2ceb8ff44f126dcd4913ffe9b624c00e17110'
            '3333b94a266a21654b3fab1eff67cf370cacf942f4d8ff29680a868dd3748c664378a4de28ca62e2a21146b737ea197e641cdb8691b73743a030bc79a0044259'
            'b93cb4764e5330ea273370e577382240bc0f42f7b3e2916ba04b0e4a30fb20f3388d83fab1ede3204807f38927014945d6e2a374edb2040bed847b4ca2228977'
            '049cc567be0ec4e7994762ce30d95f496f05dd4996b742ba4f6be746f0a2d7f1e92491eb07d9f71047dacd094e5c632147e81c0a71f91f857fd0eb36f0a085a4'
            '58628d12e62bd0a2193425e5b4ec8a2cb8f843c17ed25c69ac867340c4438bead99d8b0aee1dda45238cad1c05c29d41d24e7b0931a6ef60c2ef8cdfe71045e4'
            '08dc77ce5fd0452adbd260015aca618d3f2aa15ae8ed716e1349bbf4f67af293f1857fd2c50e79cde3cf00739605dc5bb240bcf1983e8229bc1c70453fd2d435'
            '8842240e2e6c73cc2921e80c9fb1ff02dd6d916d50c448f467a10f8db754d65f09271f741853a61cb5c6de96b5804b9215e11e7d3e5fcffe283ea6358693ca56'
            '7580a5aeb005e713a1bcb7f51d8088e6a55a417b17e034ffad98007278f4b00edc3433bb0c27ee7fcab4332c670318e26429d58e7e7e21c39d0f636d886f0573'
            '5474e2ee6a83501a96d3b392c696eca272c022a2415546dcdc577cd9a245759024935bd71e762b2057db5cd4e7368c17fde55e77c529a299d22cd19ade9ae456'
            'd3591a8cb41c8cdad9519ae5c382de288151a697e27eeff4e7c31a8988f653c98b95b43a260cd3a3a72aa1b48d61b6c101c4b1c7060a1afbc83d0a15f66cbf02'
            'c8e7126f0cfb569553df57db294aa960429275758be1b723eba1428c2564ba1c02fd8c614a3a886b932e0466d7470aa10ab078426ec42e62c8fb4c5ebf59ed30'
            '9481184036b937bef673c7bdcc3031d74ff037423f38f81708a428f7e25f5dd8a86efd55dd4d53b898d3fceb549640542f8fdf0724d98c102409d4bf1b5a39a4'
            'a9ebedad561e6c7bcf33858bf9e8fa71d331d3b95007675e7cd3edd640fb9b23a5ff956749198618c3350912eab82aa87a2d979016e891c12d1df580d28de081'
            '29ff61d5b0519f072c38973c281dc176f6250d734619689544a6c47f6975cb0ec53f9b66550864b80b889c5626120df1b0b2f08f3f7056221f91ffed2ef495b6'
            '028c6c012c6f73a172cb9fc11e7631261f33a4f8b4d86bbb55ad098cd1be64f00dcad623b90be7c0fabf3ff5ff86aeb60f4b2e5bee7cf4b055f905b018595b56')

prepare() {
  cd $_pkgname-$pkgver

  for patch in ../*.patch; do
    patch -Np1 -i "$patch"
  done
}

build() {
  cd $_pkgname-$pkgver

  mkdir -p build; cd build

  cmake -DCMAKE_INSTALL_PREFIX="/usr" \
    -DBUILD_CAPTIONS=ON \
    -DOBS_VERSION_OVERRIDE="$pkgver-$pkgrel" ..

  make
}

package() {
  cd $_pkgname-$pkgver/build

  make install DESTDIR="$pkgdir"
}
