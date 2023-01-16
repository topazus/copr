function readAll(file)
    local f = assert(io.open(file, "rb"))
    local content = f:read("*all")
    f:close()
    return content
end
function write_to_file(file,content)
    local f = assert(io.open(file, "w"))
    local content = f:write(content)
    f:close()
end
file="./makefiles/Mf-install.in"
data=readAll(file)
data=data:gsub("444","644")
data=data:gsub("555","755")
write_to_file(file,data)
