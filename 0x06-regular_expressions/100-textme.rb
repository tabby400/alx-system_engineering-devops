#!/usr/bin/env ruby
# This script outputs sender the sender and
# the receiver phone number and name
# Shows the flags used
# /w matches any word char



def get_data(text_in)

  the_matches = text_in.scan(/\[from:(\+?\w+)\] \[to:(\+?\w+)\] \[flags:(-?\d:-?\d:-?\d:-?\d:-?\d)\]/)
  data = the_matches.map { |match| "#{match[1]},#{match[2]}" }
  data.join(",")
end

if ARGV.empty?
  puts "provide the input text."
else
  text_in = ARGV[0]
  output = get_data(text_in)
  puts output
end
