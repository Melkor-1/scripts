f = File.open("list.h")

loc = 0
comments = 0
while line = f.gets
  if commented ||= line.match(/^\/\*/)
    commented = nil if line.match(/\*\/$/)
	comments += 1
  elsif line.match(/^\s*\/\//)
    comments += 1
  else	
  	loc +=1 unless line.match(/^\s*\n/)
  end
end

puts loc
puts comments
