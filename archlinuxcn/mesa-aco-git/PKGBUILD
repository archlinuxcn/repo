# Maintainer:  John Schoenick <johns@valvesoftware.com>
# Contributor: Lone_Wolf <lonewolf at xs4all dot nl>
# Contributor: Armin K. <krejzi at email dot com>
# Contributor: Kristian Klausen <klausenbusk@hotmail.com>
# Contributor: Egon Ashrafinia <e.ashrafinia@gmail.com>
# Contributor: Tavian Barnes <tavianator@gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Antti "Tera" Oja <antti.bofh@gmail.com>
# Contributor: Diego Jose <diegoxter1006@gmail.com>

pkgname=mesa-aco-git
pkgdesc="Mesa with the ACO compiler patchset, git version"
pkgver=19.3.0_devel.20191017.fe930ad92ab
pkgrel=7
arch=('x86_64')
makedepends=('git' 'python-mako' 'xorgproto'
              'libxml2' 'libx11'  'libvdpau' 'libva' 'elfutils' 'libomxil-bellagio' 'libxrandr'
              'ocl-icd' 'vulkan-icd-loader' 'libgcrypt'  'wayland' 'wayland-protocols' 'meson' 'ninja')
depends=('libdrm' 'libxxf86vm' 'libxdamage' 'libxshmfence' 'libelf'
         'libomxil-bellagio' 'libunwind' 'libglvnd>=1.2' 'wayland' 'lm_sensors' 'libclc' 'glslang')
optdepends=('opengl-man-pages: for the OpenGL API man pages')
provides=("mesa=$pkgver-$pkgrel"
          "mesa-git=$pkgver-$pkgrel"
          "vulkan-intel=$pkgver-$pkgrel"
          "vulkan-radeon=$pkgver-$pkgrel"
          "libva-mesa-driver=$pkgver-$pkgrel"
          "mesa-vdpau=$pkgver-$pkgrel"
          "vulkan-driver=$pkgver-$pkgrel"
          "opencl-mesa=$pkgver-$pkgrel"
          # mesa-vulkan-layer was renamed as it was brought in from AUR
          "mesa-vulkan-layer=$pkgver-$pkgrel"
          "vulkan-mesa-layer=$pkgver-$pkgrel"
          "opengl-driver"
          "opencl-driver"
          "mesa-libgl=$pkgver-$pkgrel")
conflicts=('mesa' 'mesa-git' 'opencl-mesa' 'vulkan-intel' 'vulkan-radeon' 'libva-mesa-driver' 'mesa-vdpau' 'mesa-vulkan-layer' 'vulkan-mesa-layer')
url="https://www.mesa3d.org"
license=('custom')
source=('mesa-aco::git+https://github.com/daniel-schuermann/mesa'
        'LICENSE'
        'mesa-headers.patch'
)

sha512sums=('SKIP'
            '25da77914dded10c1f432ebcbf29941124138824ceecaf1367b3deedafaecabc082d463abcfa3d15abff59f177491472b505bcb5ba0c4a51bb6b93b4721a23c2'
            'f83d52292f9b5144fc2f5b568cfb1d4bdebd37b877d34d9002335d79f66612123001c36a9615ed13f474771002672f2a445a89f3220d16b962e17087b6111644'
)


# NINJAFLAGS is an env var used to pass commandline options to ninja
# NOTE: It's your responbility to validate the value of $NINJAFLAGS. If unsure, don't set it.

# Users of alternative llvm packages may need to tweak the hard version dependency here, which ensures this package is
# rebuilt if the underlying llvm updates.
makedepends+=('llvm>=9.0.0' 'llvm<9.1' 'clang>=9.0.0' 'clang<9.1')
depends+=('llvm-libs>=9.0.0' 'llvm-libs<9.1')

# LLVM NOTE: The upstream mesa-git package provides these alternative suggestions.  Really, these packages should all
#            have the necessary provides to make selecting these manually here unnecessary, and we've disabled them
#            because they break aurhelpers such as yay.
#
## MESA_WHICH_LLVM is an environment variable used to determine which llvm package tree is used to built mesa-git against.
## Adding a line to makepkg.conf that sets this value is the simplest way to ensure a specific choice.
##
## 1: llvm-minimal-git (aur) preferred value
## 2: AUR llvm-git
## 3: llvm-git from LordHeavy unofficial repo
## 4  llvm (stable from extra) Default value
###  if [[ ! $MESA_WHICH_LLVM ]] ; then
###      MESA_WHICH_LLVM=4
###  fi
###
###  case $MESA_WHICH_LLVM in
###      1)
###          # aur lone_wolf-llvm-git
###          makedepends+=('llvm-minimal-git')
###          depends+=('llvm-libs-minimal-git')
###          ;;
###      2)
###          # aur llvm-git
###          # depending on aur-llvm-* to avoid mixup with LH llvm-git
###          makedepends+=('aur-llvm-git')
###          depends+=('aur-llvm-libs-git')
###          ;;
###      3)
###          # mesa-git/llvm-svn (lordheavy unofficial repo)
###          makedepends+=('llvm-git' 'clang-git')
###          depends+=('llvm-libs-git')
###          ;;
###      4)
###          # extra/llvm
###          makedepends+=(llvm=8.0.0 clang=8.0.0)
###          depends+=(llvm-libs=8.0.0)
###          ;;
###      *)
###  esac

pkgver() {
    cd mesa-aco
    read -r _ver <VERSION
    echo ${_ver/-/_}.$(git log -n1 --format="%cd" --date=format:%Y%m%d HEAD).$(git rev-parse --short HEAD)
}

prepare() {
    # although removing _build folder in build() function feels more natural,
    # that interferes with the spirit of makepkg --noextract
    if [  -d _build ]; then
        rm -rf _build
    fi

    cd "$srcdir"/mesa-aco

    # Apply this until ACO is rebased and contains it
    if ! git show b57fa7ca49f7ddb67ac47f392de05af388e73565 &>/dev/null; then
      patch -Np1 -i "$srcdir"/mesa-headers.patch
    fi
}

build () {
    meson setup mesa-aco _build \
       -D b_ndebug=true \
       -D buildtype=plain \
       --wrap-mode=nofallback \
       -D prefix=/usr \
       -D sysconfdir=/etc \
       -D platforms=x11,wayland,drm,surfaceless \
       -D dri-drivers=i915,i965,r200,r100,nouveau \
       -D gallium-drivers=r300,r600,radeonsi,nouveau,svga,swrast,virgl,iris \
       -D vulkan-drivers=amd,intel \
       -D dri3=true \
       -D egl=true \
       -D gallium-extra-hud=true \
       -D gallium-nine=true \
       -D gallium-omx=bellagio \
       -D gallium-va=true \
       -D gallium-vdpau=true \
       -D gallium-xa=true \
       -D gallium-xvmc=false \
       -D gbm=true \
       -D gles1=true \
       -D gles2=true \
       -D glvnd=true \
       -D glx=dri \
       -D libunwind=true \
       -D llvm=true \
       -D lmsensors=true \
       -D osmesa=gallium \
       -D shared-glapi=true \
       -D gallium-opencl=icd \
       -D valgrind=false \
       -D vulkan-overlay-layer=true \
       -D tools=[]

    meson configure _build
    ninja  $NINJAFLAGS -C _build
}

package() {
  DESTDIR="$pkgdir" ninja $NINJAFLAGS -C _build install

  # indirect rendering
  ln -s /usr/lib/libGLX_mesa.so.0 "${pkgdir}"/usr/lib/libGLX_indirect.so.0

  install -Dt "$pkgdir"/usr/share/licenses/$pkgname "$srcdir"/LICENSE
}
