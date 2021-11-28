#########################
### Generating a console log in JSON format for the nodes of linkanalysis
#
### Requirements: 
#   -there are two topic models, one with 10.000 fetched tweets and one with 100.000
#   -the first model was made at hand, so only the 100.000 tweets large topic model will be made here
#   -topics were listed in Notebook_Topicmodel.Rmd
#   -lists are found in /Datenaufbereitung 10.000/Linkanalyse 10.000.docx and /Datenaufbereitung 100.000/Linkanalyse 100.000.docx
#   -words can show up twice, list was filtered in 10.000/Linkanalyse 10.000.xlsx and /Datenaufbereitung 100.000/Linkanalyse 100.000.xlsx
#   -array b with the words of the 100.000 topic model
# 
### Function
#   -for loop to print every word in the array in JSON format
# 
### Results:
#   -Console log with the nodes for the linkanalysis
#   -stored in JSON ready format 
#   -final results stored in /Datenaufbereitung 10.000/visNodes10.000.json and /Datenaufbereitung 100.000/visNodes100.000.json
#########################

b = [	"	ach 	","	afd 	","	allerd 	","	alten 	","	altern 	","	angst 	","	annalena 	","	arbeit 	","	argument 	","	arm 	","	armin 	","	aussage	","	außer 	","	auto 	","	baerbock 	","	bald 	","	bayern 	","	beiden 	","	bekannt 	","	bekommt 	","	berlin 	","	besond 	","	besser 	","	best 	","	bevölkerung 	","	bild 	","	bisher 	","	bitt 	","	bleiben 	","	brauchen 	","	bringen 	","	btw 	","	bundestag 	","	bundestagswahl 	","	bürger 	","	cdu 	","	cduabwaehlen 	","	cducsu 	","	china 	","	corona 	","	csu 	","	dabei 	","	dagegen 	","	dank 	","	darauf 	","	darf 	","	demo 	","	demokrati 	","	denken 	","	deren 	","	deutlich 	","	deutschen 	","	deutschland 	","	deutschlandabernormal	","	ding 	","	direkt 	","	dürfen 	","	ebenfal  	","	echt 	","	egal 	","	eigen 	","	eigentlich 	","	einfach	","	einzig 	","	endlich 	","	ergebni 	","	erklären 	","	ernsthaft 	","	erst 	","	ersten 	","	esken 	","	etc 	","	euro 	","	extrem 	","	falsch 	","	fdp 	","	fehler 	","	fff 	","	frage 	","	frau 	","	führt 	","	funktioniert 	","	gab 	","	ganz 	","	geben 	","	gebracht 	","	gefährlich 	","	gegeben 	","	gehen 	","	gehört 	","geld 	","	gemacht 	","	genau 	","	gerad 	","	gern 	","	gesagt 	","	geschicht 	","	gesetz 	","	gespannt 	","	gestern 	","	gewählt 	","	gewinnt 	","	gibt 	","	giffey 	","	gilt 	","	ging 	","	glauben 	","	gleich 	","	grad 	","	groko 	","	große 	","	größte 	","	grün 	","	gut 	","	habeck 	","	habt 	","	halten 	","	hast 	","	hätten  	","	haus 	","	herr 	","	heut 	","	hoffen 	","	hoffentlich 	","	hört 	","	hungerstreik 	","	hürde 	","	immer 	","	irgendein 	","	irgendwi 	","	jahr 	","	jamaika 	","	jung 	","	kannst 	","	kanzler 	","	kanzleramt 	","	kanzlerin 	","	kaum 	","	kinder 	","	klar 	","	klein 	","	klima 	","	klimaschutz 	","	klimastreik 	","	koalit 	","	kohl  	","	kommen 	","	komplett 	","	korrupt 	","	kosten 	","	kubicki 	","	kurz 	","	land 	","	lang 	","	laschet 	","	laschetdarfnichtkanzlerwerden 	","	laschetverhindern 	","	lassen 	","	läuft 	","	laut 	","	lauterbach 	","	leben 	","	leider 	","	letzten 	","	leut 	","	lieb 	","	liegen 	","	lindner 	","	link 	","	lustig 	","	maaßen 	","	macht 	","	mann 	","	medien 	","	mehr 	","	mehrheit 	","	meinung 	","	meisten 	","	menschen 	","	merkel 	","	mittlerweil 	","	möchte 	","	morgen 	","	müssen 	","	müsste	","	namen 	","	nazi 	","	nein 	","	nennen 	","	neue 	","	nie 	","	niemand 	","	nix 	","	nochmal 	","	oft	","	olaf 	","	opposit 	","	paar 	","	partei 	","	person 	","	persönlich 	","	platz 	","	politik 	","	problem 	","	propaganda 	","	querdenk 	","	raus 	","	recht 	","	reden 	","	regierung 	","	reicht 	","	richtig 	","	richtung 	","	rot-grün 	","	rrg 	","	sagen 	","	scheint 	","	scheiss 	","	scheuer 	","	schlecht 	","	schlimmer  	","	scholz 	","	schön 	","	schreiben 	","	schröder 	","	schwer 	","	sei  	","	seid 	","	seit 	","	setzen 	","	sicher 	","	sicherheit 	","	sieh 	","	söder 	","	sofort  	","	sogar 	","	sollen 	","	somit 	","	sonntag 	","	sorri 	","	sowas	","	sozial 	","	spd 	","	sprechen ","	stabil 	","	stehen 	","	stell  	","	stimme	","	tag 	","	tatsächlic 	","	teil 	","	thema 	","	tja 	","	toll 	","	trotzdem	","	tun 	","	tweet 	","	twitter 	","	überhaupt 	","	übrigen 	","	union 	","	unser 	","	unterstützen 	","	unwählbar 	","	usw 	","	verhindern 	","	verloren 	","	verstehen 	","	versucht 	","	via 	","	vielen 	","	vorbei 	","	wahl 	","	wähle 	","	wahlkampf	","	wahlprogramm 	","	wahr 	","	wahrheit 	","	wahrscheinlich 	","	wären 	","	warum 	","	weder 	","	wegen 	","	weidel 	","	weiß 	","	weit 	","	weiterhin 	","	welt 	","	wenig 	","	wer 	","	wichtig ","	wieso 	","	wirbt  	","	wirklich 	","	wirtschaft 	","	wohl 	","	wollt 	","	worden 	","	wort 	","	wurd 	","	zahlen 	","	zeigen 	","	zeit 	","	ziel	","	zukunft 	","	zumindest 	","	zusammen 	","	zwei 	"]


for x in range (1,351):
    print('{"id": ' + str(x) + ', "label": "' + str(b[x]) + '" , "group": 0},')

    x = x + 1