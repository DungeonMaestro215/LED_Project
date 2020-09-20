def writePix(r, g, b, idx):
	#open text doc with RGB data for each pix
	#overwrite file at line idx with rgb values in CSV format
	#Ex: 255,255,255,

	fileR = open("PixStorage.txt", "r")
	linesR = fileR.readlines()
	fileR.close()

	linesR[idx] = str(r) + "," + str(g) + "," + str(b) + ",\n"

	fileW = open("PixStorage.txt", "w")
	fileW.writelines(linesR)
	fileW.close()

	return


def readPix(pixels):
	#open text doc with RGB data for each pix
	#read file line by line and update pixel object
	#return the array

	file = open("PixStorage.txt", "r")		
	lines = file.readlines()

	for n, l in enumerate(lines):

		rgb = l.split(",")

		pixels[n] = (int(rgb[0]), int(rgb[1]), int(rgb[2]))

	file.close()

	return