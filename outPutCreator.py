import os
import csv
from reportlab.pdfgen import canvas
from fpdf import FPDF

colors = []
metrics = []
discs = []
candidate = " "



class Metrics():
    def __init__(self, metric ,percentage ,width):
        self.metric = metric
        self.percentage = percentage
        self.width = width
    def setWidth(self, width):
        self.width = width
		
def	readMetrics():
	global metrics
	global discs
	file = "report.csv"
	with open(file) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			perc = row[1].split(".")[0]
			metrics.append(Metrics(row[0], perc ,1))
			line_count += 1
	file = "disc.csv"
	with open(file) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if line_count == 0 or  not row :
				line_count += 1
			else:
				if "." in row[1] :
					perc = row[1].split(".")[0]
				else :
					perc = row[1]
				discs.append(Metrics(row[0], perc ,1))
				line_count += 1
	
def setMetricsWidths():
	highPercentage = int(metrics[0].percentage)
	for metric in metrics :
		if int(metric.percentage) > highPercentage :
			highPercentage = int(metric.percentage)
	for metric in metrics :
		metric.width = (int(metric.percentage) * 100) / highPercentage
		
def setDiscsWidths():
	highPercentage = int(discs[0].percentage)
	for disc in discs :
		if int(disc.percentage) > highPercentage :
			highPercentage = int(disc.percentage)
	for disc in discs :
		disc.width = (int(disc.percentage) * 100) / highPercentage

class Color():
    def __init__(self, rPercentage ,gPercentage ,bPercentage):
        self.rPercentage = rPercentage
        self.gPercentage = gPercentage
        self.bPercentage = bPercentage

def setColorsChart() :
	global colors
	colors.append(Color(225,0,0))
	colors.append(Color(0,0,225))
	colors.append(Color(0,225,0))
	colors.append(Color(344,0,100))
	colors.append(Color(0,153,76))
	colors.append(Color(153,0,153))
	colors.append(Color(255,153,153))
	colors.append(Color(0,76,153))
	colors.append(Color(225,225,51))

#setLines(pdf file,x1 delimiter, ..,nbLines)
def setLines(self,x1,x2,y1,y2,nbLines) :
	self.set_line_width(1)
	i = 0
	pas_x = 10
	pas_y = 10

	for color in colors :
		i = i + 1
		if i<= nbLines :
			self.set_draw_color(color.rPercentage,color.gPercentage,color.bPercentage)
			if i % 2 == 0 :
				pas_x = pas_x + 5 + i
				self.line(x1-pas_x, y1+pas_y, x1-pas_x+25, y1+pas_y)
			else :
				pas_y = pas_y + 10 + i
				self.line(x2+pas_x, y2-pas_y, x2+pas_x+25, y2-pas_y)
		else :
			break

def setLine(self,x1,x2,y,nbLine, Metrics) :
	self.set_line_width(1)
	if len(Metrics.metric) == 1:
		data = str(Metrics.percentage)+"%"
	else:
		data = Metrics.metric + " "+str(Metrics.percentage)+"%"
	dataSize = 20 + (Metrics.width /10 )

	self.set_draw_color(colors[nbLine].rPercentage,colors[nbLine].gPercentage,colors[nbLine].bPercentage)
	self.line(x1, y, x2, y)
	self.set_y(y-10)
	if x1 < 50 :
		self.cell(-(x2+x2-x1))
	else :
		self.cell(x1 -50)
	self.set_font("Arial", size=dataSize)
	self.cell(w = 0, h = 10, ln =1, txt = data, border = 0, align = 'C')
		
def setCandidateName() :
	global candidate
	files_path = [os.path.abspath(x) for x in os.listdir()]

	# Excluding not .csv files
	files_path = [csv for csv in files_path if '.csv' in csv and 'disc' in csv]

	csvs = []
	for file in files_path:
		csvs += [file]
	
	candidate =""
	with open(csvs[0]) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				line_count += 1
				candidate = row[0].split(",")[0]

def main():
	pdf = FPDF()
	pdf.add_page()
	pdf.set_xy(0, 0)
	pdf.set_font('arial', 'B', 13.0)
	pdf.image("image_1.jpg", 75, 30)

	setCandidateName()
	setColorsChart()
	readMetrics()
	setMetricsWidths()
	setDiscsWidths()

	setLine(pdf, 45, 75, 70, 0, metrics[0])	
	setLine(pdf, 40, 70, 90, 1, metrics[1])
	setLine(pdf, 45, 75, 110, 2, metrics[2])
	setLine(pdf, 118, 148, 85, 3, metrics[3])
	setLine(pdf, 135, 165, 65, 4, metrics[4])
	setLine(pdf, 122, 152, 104, 5, metrics[5])
	setLine(pdf, 115, 145, 120, 6, metrics[6])
	pdf.set_font('arial', 'B', 13.0)

	#addCandidateName
	pdf.set_draw_color(0,0,0)
	
	pdf.set_y(140)
	pdf.cell(70)
	pdf.cell(w = 60, h = 10, ln =1, txt = candidate, border = 'B', align = 'C')
	
	#addDiscTestResult
	pdf.image("DISC.jpg", 65, 180, 80,80)
	setLine(pdf,45,65,200,0,discs[0])
	setLine(pdf,45,65,245,5,discs[1])
	setLine(pdf,145,165,200,8,discs[2])
	setLine(pdf,145,165,240,2,discs[3])

	#generateReportFile
	pdf.output('candidateSurvey.pdf', 'F')
  
if __name__== "__main__":
  main()
