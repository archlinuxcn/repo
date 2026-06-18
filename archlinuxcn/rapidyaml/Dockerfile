FROM brianrobt/archlinux-aur-dev:latest

RUN sudo pacman -Syu --noconfirm

# Copy local AUR package files to the container
COPY --chown=builder:builder .SRCINFO PKGBUILD ./

# Install build dependencies
RUN yay -S --noconfirm \
  cmake \
  ninja \
  python-setuptools \
  python-setuptools-git \
  python-setuptools-scm \
  python-cmake-build-extension \
  swig

# Build the package
# RUN makepkg -si