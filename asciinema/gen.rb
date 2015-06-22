#!/usr/bin/env ruby

require 'erb'
require 'open-uri'

VERSION = ARGV[0]

url = "https://github.com/asciinema/asciinema-cli/releases/download/v#{VERSION}/sha1sum.txt"
lines = open(url).each_line
linux_lines = lines.grep(/linux/)
SHA1_SUMS = Hash[linux_lines.map { |line| line.strip.split(/\s+/).reverse }]

def sha1sum(arch)
  SHA1_SUMS[SHA1_SUMS.keys.grep(/#{arch}/).first]
end

SHA1_386 = sha1sum('386')
SHA1_ARM = sha1sum('arm')
SHA1_AMD64 = sha1sum('amd64')

erb = ERB.new(File.read('PKGBUILD.erb'))
puts erb.result(binding)
