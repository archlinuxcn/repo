#!/bin/bash -e

unshare -m bash <<'EOF'
mount --make-rprivate /
for f in /etc/pacman.d/*.sync; do
  filename="${f%.*}"
  mount --bind "$f" "$filename"
done
pacman -Sy
EOF
