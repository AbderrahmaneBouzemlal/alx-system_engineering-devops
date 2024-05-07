#!/usr/bin/env ruby
string = ARGV[0].scan(/(from:[+\w]+|to:[+\w]+|flags:[(-1|0|1):]+)/).join
string.slice! "from:"
string ["to:"] = ","
string ["flags:"] = ","
puts string
