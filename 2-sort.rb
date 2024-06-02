###
#
#  Sort integer arguments (ascending) 
#
###

result = []
ARGV.each do |arg|
    # skip if not integer
    next if arg !~ /^-?[0-9]+$/

    # convert to integer
    i_arg = arg.to_i
    
    # insert result at the right position
  inserted = false
  result.each_with_index do |value, index|
    if i_arg < value
      result.insert(index, i_arg)
      inserted = true
      break
    end
  end
  
  # Append to the end if not inserted in the loop
  result << i_arg unless inserted
end

puts result
