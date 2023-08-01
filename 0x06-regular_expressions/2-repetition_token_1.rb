#!/usr/bin/env ruby
# This script matches hbtn starting with h ending n and
# can either match b or not is optional using ?


puts ARGV[0].scan(/hb?tn/).join
