C = input('來自哪個國家:')
Y = input('請書輸入年齡:')
Y = int(Y)
if C == '台灣':
	if Y >= 18:
		print('可以考駕照')
	else:
	    print('你還不能考駕')
elif C == '美國':
	if Y >= 16 :
		print('可以開車')
	else :
		print('不能開車')
	