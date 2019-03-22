#!/bin/sh

cd reg_tmp && \
   tar -cvjSf reg_files.tar.bz2 * && \
   mv reg_files.tar.bz2 ../ && \
   cd ../
