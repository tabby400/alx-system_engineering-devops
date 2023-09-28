#!/usr/bin/env ruby
# This prints texts starting with h with characters in
# between and end with n , matches bt with one or more
# t's  + indicates the preceeding character must apperar
# once or more times


puts ARGV[0].scan(/hbt+n/).join
