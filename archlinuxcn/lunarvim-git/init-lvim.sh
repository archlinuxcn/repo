#!/bin/bash
mkdir -p ~/.config/lvim
ln -s /usr/share/doc/lunarvim/config.example-no-ts.lua ~/.config/lvim/config.lua
mkdir -p ~/.local/share/lunarvim
ln -s /usr/share/lunarvim ~/.local/share/lunarvim/lvim
echo "Installing Packer..."
git clone https://github.com/wbthomason/packer.nvim ~/.local/share/lunarvim/site/pack/packer/start/packer.nvim
echo "PackerInstall..."
lvim --headless +'autocmd User PackerComplete sleep 100m | qall' +PackerInstall
echo "PackerSync..."
lvim --headless +'autocmd User PackerComplete sleep 100m | qall' +PackerSync
rm ~/.config/lvim/config.lua
cp /usr/share/doc/lunarvim/config.example.lua ~/.config/lvim/config.lua
echo "Installing treesitter parsers.."
ln -s /usr/share/lunarvim/prebuild/nvim-treesitter/parser/* \
	~/.local/share/lunarvim/site/pack/packer/start/nvim-treesitter/parser/
ln -s /usr/share/lunarvim/prebuild/nvim-treesitter/parser-info/* \
	~/.local/share/lunarvim/site/pack/packer/start/nvim-treesitter/parser-info/
echo
echo "lunarvim runtime is inited for $(whoami)"
echo "clean up by:"
echo "    rm -rf ~/.config/lvim ~/.local/share/lunarvim"
