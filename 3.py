
def count(string,index):
    c = 0
    item = string[index]
    for i in string[index:]:
        if i == item:
            c += 1
        else:
            break
    return f"{c}{item}"

def nth_element(x,n):
	i = 0
	y = ''
	while i <= (len(x) - 1):
		p = count(x,i)
		i += int(p[0])
		y += p
	if n <=1:
		return y
	return nth_element(y,n-1)


def main(n):
    x = '1'
    l = nth_element(x,n)
    print(l)
