#!/usr/bin/env ruby
# This prints str starting with h and ends with n and can
# have any single char in between
# ^ the char to start and $ the char to end with
# . matches any char apart from newline



puts ARGV[0].scan(/^h.n$/).join
