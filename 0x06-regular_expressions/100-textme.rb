#!/usr/bin/env ruby
print ARGV[0].scan(/(?<=from:)([A-Z]+)?([a-z]+)?(\+?[0-9]+)?/).join
print (",")
print ARGV[0].scan(/(?<=to:)([A-Z]+)?([a-z]+)?(\+?[0-9]+)?/).join
print (",")
print ARGV[0].scan(/(?<=flags:)([0-9\-:]+)?/).join
