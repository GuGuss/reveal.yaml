from os import path
from yaml import load
def getHtml(pres, js):
	folder = path.join("data", pres)
	pres_file = open(path.join(folder, "index.yaml"), "r")
	pres_yaml = pres_file.read()
	pres_file.close()
	pres_yaml = load(pres_yaml)

	#much to do; now only parsing the slides and outputting pure html

	html = ""
	html += "<!doctype html>\n<html>\n"
	#TODO: HEAD
	html += "\t<body>\n"
	#TODO: divs and ids
	html += parse_slide(pres_yaml, 2)
	#TODO: divs and ids
	html += "\t</body>\n"
	html += "</html>\n"
	return(html)

def parse_slide(slide, tabs):
	slide_html = ""
	tabs_to_insert = ""
	for tab in tabs:
		tabs_to_insert += "\t"
	try:
		slide_html += tabs_to_insert + parse_md(slide["md"]) + "\n"
	except KeyError:
		try:
			slide_html += tabs_to_insert + slide["text"] + "\n"
		except KeyError:
			for x in slide["slides"]:
				slide_html += parse_slide(x, tabs + 1)


	return (slide_html)

def parse_md(md):
	#TODO
	return(md)
