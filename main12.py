from urllib import request

minhaUrl = 'https://www.google.com/search?q=aprenda+python'
minhaPagina = request.urlopen(minhaUrl)

status = minhaPagina.code

print(type(minhaPagina))
print(status)
