#!/usr/bin/env ruby
# This requires a regexp that matches a start with h and b with
# two to five t's between and ending in n


puts ARGV[0].scan(/hbt{2,5}n/).join
