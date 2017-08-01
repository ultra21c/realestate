#!/usr/bin/python

def meme():
	md = {}
	with open('./data/1.dat') as f:
		price_dict = {}
		for line in f.readlines():
			row = line.strip().split('\t')
			apt_name = row[4]
			key = apt_name + "_" +  row[5].replace(' ','')
			if key in md:
				price_dict[key].append(long(row[8].replace(' ', '').replace(',','')))
				tmp_price = long(md[key][8].replace(' ', '').replace(',',''))
				cur_price = long(row[8].replace(' ', '').replace(',',''))
				if tmp_price < cur_price:
					md[key][8] = row[8]
			else:
				md[key] = row
				price_dict[key] = [long(row[8].replace(' ', '').replace(',',''))]
		for key in price_dict:
			md[key].append(sum(price_dict[key])/len(price_dict[key]))
	return md

def junse():
	jd = {}
	with open('./data/2.dat') as f:
		price_dict = {}
		for line in f.readlines():
			row = line.strip().split('\t')
			apt_name = row[4]
			key = apt_name + "_" +  row[6].replace(' ','')
			if key in jd:
				price_dict[key].append(long(row[9].replace(' ', '').replace(',','')))
				tmp_price = long(jd[key][9].replace(' ', '').replace(',',''))
				cur_price = long(row[9].replace(' ', '').replace(',',''))
				if tmp_price > cur_price:
					jd[key][9] = row[9]
			else:
				jd[key] = row
				price_dict[key] = [long(row[9].replace(' ', '').replace(',',''))]
		for key in price_dict:
			jd[key].append(sum(price_dict[key])/len(price_dict[key]))
			
	return jd

def refine(s):
	return s.replace(' ','')

def main():
	md = meme()
	jd = junse()
	for m in md:
		if m in jd:
			juns = float(jd[m][6].replace(' ',''))
			mes = float(md[m][5].replace(' ',''))
			diff_s = abs(mes - juns)
			if diff_s < 5:
				junp = long(jd[m][9].replace(' ','').replace(',',''))
				mep = long(md[m][8].replace(' ','').replace(',',''))
				gap_p = mep - junp
				gap_a = md[m][12] - jd[m][14]
				name, py = refine(m).split('_')
				addr = md[m][0].split(' ')[3]
				print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s'%(
								addr, 
								name, 
								py, 
								refine(jd[m][11]), 
								refine(md[m][9]),
								refine(jd[m][9]),
								refine(md[m][8]), 
								jd[m][14], 
								md[m][12], 
								gap_p,
								gap_a)
		
			

if __name__ == '__main__':
	main()
