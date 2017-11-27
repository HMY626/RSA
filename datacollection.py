for i in range(2, 21):
	with open('Frame'+str(i), 'r') as file0:
		data = file0.readlines()
		N0 = data[0][0:256]
		e0 = data[0][256:512]
		c0 = data[0][512:768]
		with open('data.txt', 'a') as f:
			f.writelines('N%s = %s\n' % (str(i), N0))
			f.writelines('e%s = %s\n' % (str(i), e0))
			f.writelines('c%s = %s\n\n\n' % (str(i), c0))
			f.close()
		file0.close()

#with open('Frame1', 'r') as file0:
#	data1 = file0.readlines()
#	N0 = data1[0][0:256]
#	e0 = data1[0][256:512]
#	c0 = data1[0][512:768]
#	with open('data.txt', 'a') as f:
#		f.writelines('N1 = %s\n' % (N0))
#		f.writelines('e1 = %s\n' % (e0))
#		f.writelines('c1 = %s\n\n\n' % (c0))
#		f.close()
#	file0.close()


