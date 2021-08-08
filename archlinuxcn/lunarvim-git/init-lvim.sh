#!/bin/bash
mkdir -p ~/.config/lvim
cp /usr/share/doc/lunarvim/config.example.lua ~/.config/lvim/config.lua
lvim --headless +'autocmd User PackerComplete sleep 100m | qall' +PackerInstall
lvim --headless +'autocmd User PackerComplete sleep 100m | qall' +PackerSync
echo
echo "lunarvim runtime is inited for $(whoami)"
echo "clean up by:"
echo "    rm -rf ~/.config/lvim ~/.local/share/lunarvim"
