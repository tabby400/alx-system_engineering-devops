#!/usr/bin/env ruby
# This prints a regular expression that must match 10
# digit phone number ^ shows the pattern to start at
# beginning of input text \d matches digits 0 to 9
# $ pattern to end at end of input text


puts ARGV[0].scan(/^\d{10}$/).join
