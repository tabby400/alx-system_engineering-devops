#!/usr/bin/env ruby
# This prints hb and then allows t to occur zero
# or more times using * before t and ends with n



puts ARGV[0].scan(/hbt*n/).join
