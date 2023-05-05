#!/usr/bin/env ruby

# regex that accepts one argument and passes it to a regular expression matching method
puts ARGV[0].scan(/School/).join
