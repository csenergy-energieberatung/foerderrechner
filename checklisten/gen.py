import subprocess,html
CSS="""@page{size:A4;margin:15mm 16mm 13mm}
body{font-family:Inter,'Segoe UI',Arial,sans-serif;color:#1c2a3a;font-size:8.7pt;line-height:1.24}
img{height:15mm;display:block}
h1{color:#0A3A66;font-size:16.5pt;margin:4mm 0 .5mm}
.sub{color:#0072BC;margin-bottom:2mm;font-weight:600}
h2{color:#0A3A66;font-size:10.8pt;border-bottom:2px solid #0072BC;padding-bottom:.8mm;margin:3.6mm 0 1.4mm}
ul{list-style:none;padding:0;margin:0}
li{padding-left:6.5mm;position:relative;margin:.6mm 0}
li:before{content:"";position:absolute;left:0;top:.45mm;width:3.3mm;height:3.3mm;border:1.4px solid #0A3A66;border-radius:1px}
.n{background:#EEF5FB;border-left:4px solid #0072BC;padding:2mm 3mm;margin-top:3mm;font-size:9pt}
.w{background:#FFF4E5;border-left:4px solid #E08A00;padding:2mm 3mm;margin-top:3mm;font-size:9pt}
.f{margin-top:3.5mm;font-size:8pt;color:#555}"""
FOOT="Allgemeine Checkliste, keine Rechts- oder Steuerberatung. Maßgeblich sind die aktuellen Merkblätter der KfW. CS Energy · M. Eng. Shahin Aslankilic · Energieeffizienz-Experte · csenergy-energieberatung.de"
def page(fn,title,sub,secs,warn,note,stand):
    h=f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body><img src="logo.png"><h1>{title}</h1><div class="sub">{sub}</div>'
    for t,items in secs:
        h+=f'<h2>{t}</h2><ul>'+''.join(f'<li>{html.escape(i) if False else i}</li>' for i in items)+'</ul>'
    h+=f'<div class="w"><b>Wichtig:</b> {warn}</div><div class="n">{note}</div><div class="f">Stand der KfW-Merkblätter: {stand}. {FOOT}</div></body></html>'
    open(fn+'.html','w').write(h)
    subprocess.run(['node','-e',f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();await p.goto('file://'+process.cwd()+'/{fn}.html');await p.pdf({{path:'{fn}.pdf',format:'A4',printBackground:true,preferCSSPageSize:true}});await b.close()}})()"],check=True)

VB_N="Noch keinen Liefer-, Leistungs- oder Kaufvertrag <b>ohne Förderklausel</b> unterschreiben und nicht mit den Bauarbeiten beginnen, bevor der Antrag bei der KfW eingegangen ist. Planung und Beratung sind vorab erlaubt. Verträge mit der Bedingung „gültig bei Förderzusage“ sind unschädlich."
IDS="Ausweis oder Reisepass aller Antragsteller; Steuer-Identifikationsnummer"
pages=[
("Checkliste-KfW-297-298-Klimafreundlicher-Neubau","Checkliste KfW 297/298 · Klimafreundlicher Neubau (Wohngebäude)","Kredit mit Bestätigung zum Antrag (BzA) durch den Energieeffizienz-Experten",
[("1. Vor dem Antrag",["Energieeffizienz-Experte beauftragt (aus der Expertenliste, unabhängig von Bauausführenden und Lieferanten)",
 "Bei der Stufe „mit QNG“: Berater für Nachhaltigkeit und QNG-Zertifizierungsstelle beauftragt",
 "Bank, Sparkasse, Bausparkasse oder Versicherung als Finanzierungspartner gewählt",
 "Bauplan, Baubeschreibung und Berechnungsunterlagen für den Effizienzhaus-Nachweis (liefern Architekt oder Planer)",
 "Grundstücks- bzw. Eigentumsnachweis (Grundbuchauszug oder Kaufvertrag)",IDS]),
 ("2. Antrag",["Bestätigung zum Antrag (BzA) vom Experten erhalten und unterschrieben",
 "Antrag über den Finanzierungspartner gestellt; maßgeblich ist der Eingang bei der KfW",
 "Beim Erwerb vom Bauträger: Kaufvertrag mit Haftung des Verkäufers für die Förderstufe prüfen"]),
 ("3. Während der Bauphase",["Verträge mit Handwerkern und Lieferanten sauber gesammelt",
 "Rechnungen auf Euro und Deutsch, mit Leistung, Arbeitsleistung und Objektadresse",
 "Alle Rechnungen unbar bezahlt (Überweisung), Kontoauszüge aufbewahren",
 "Eigenleistung: nur Materialkosten sind förderfähig, dazu ist eine Bestätigung nach Durchführung nötig"]),
 ("4. Nach Fertigstellung",["Bestätigung nach Durchführung (BnD) vom Experten, vom Kreditnehmer unterschrieben",
 "Bei QNG: Zertifikat für QNG-PLUS oder QNG-PREMIUM",
 "Nachweis der Mittelverwendung bei der KfW einreichen (spätestens 36 Monate nach Vollauszahlung)",
 "Unterlagen 10 Jahre aufbewahren, mindestens 10 Jahre zweckentsprechend nutzen"])],
VB_N,"<b>Fristen:</b> Kreditabruf 12 Monate nach Zusage (verlängerbar). Ab dem 13. Monat fällt eine Bereitstellungsprovision von 0,15 % pro Monat an. Abgerufene Beträge innerhalb von 12 Monaten verwenden.","Juli 2026 (Merkblatt 297/298)"),
("Checkliste-KfW-300-Wohneigentum-fuer-Familien","Checkliste KfW 300 · Wohneigentum für Familien (Neubau)","Zinsverbilligter Kredit für selbstgenutztes Wohneigentum mit Kind im Haushalt",
[("1. Voraussetzungen prüfen",["Mindestens ein Kind unter 18 Jahren im Haushalt",
 "Bei Antragstellung kein Wohneigentum vorhanden; mindestens 50 % Eigentumsanteil am Objekt",
 "Zu versteuerndes Haushaltseinkommen höchstens 90.000 € bei einem Kind, plus 10.000 € je weiterem Kind",
 "Maßgeblich ist der Durchschnitt des zweiten und dritten Vorjahres vor Antrag",
 "Die Förderung kann nur einmal je Antragsteller in Anspruch genommen werden"]),
 ("2. Unterlagen für den Antrag",["Einkommensteuerbescheide der beiden maßgeblichen Vorjahre",
 "Geburtsurkunden aller Kinder unter 18 Jahren im Haushalt",
 "Bestätigung zum Antrag (BzA) vom Energieeffizienz-Experten, unterschrieben",
 "Bank, Sparkasse, Bausparkasse oder Versicherung als Finanzierungspartner gewählt",
 IDS]),
 ("3. Bauphase",["Verträge erst nach dem Antrag bei der KfW (oder mit Förderklausel) abschließen",
 "Rechnungen auf Euro und Deutsch, unbar bezahlt, Kontoauszüge aufbewahren"]),
 ("4. Nach dem Einzug",["Meldebestätigung (Hauptwohnsitz im Objekt)",
 "Grundbuchauszug mit Ihnen als Eigentümer",
 "Bestätigung nach Durchführung (BnD) vom Experten",
 "Rechnungen und Zahlungsnachweise; Nachweis der Mittelverwendung bei der KfW einreichen"])],
VB_N,"<b>Pflichten:</b> mindestens 5 Jahre Selbstnutzung ab Einzug (Unterbrechung höchstens 2 Jahre), mindestens 10 Jahre Wohnnutzung. Nachweis der Mittelverwendung spätestens 36 Monate nach Vollauszahlung. Unterlagen 10 Jahre aufbewahren.","Dezember 2025 (Merkblatt 300)"),
("Checkliste-KfW-261-Sanierung-Effizienzhaus","Checkliste KfW 261 · Sanierung zum Effizienzhaus","Kredit mit Tilgungszuschuss, Bestätigung zum Antrag (BzA) durch den Energieeffizienz-Experten",
[("1. Vor dem Antrag",["Energieeffizienz-Experte beauftragt (aus der Expertenliste, unabhängig von Handwerkern und Lieferanten)",
 "Sanierungskonzept bzw. Effizienzhaus-Berechnung, Zielstufe (z. B. 85, 70, 55, 40)",
 "Eigentumsnachweis (Grundbuchauszug); bei Nicht-Eigentümern Einverständnis des Eigentümers",
 "Bestandsunterlagen: Baujahr, Pläne, Fotos von Dach, Fassade, Fenstern, Heizung",
 "Finanzierungspartner gewählt (Bank, Sparkasse, Versicherung)",IDS]),
 ("2. Antrag",["Bestätigung zum Antrag (BzA) vom Experten erhalten und unterschrieben",
 "Antrag über den Finanzierungspartner bei der KfW gestellt (maßgeblich ist der Eingang bei der KfW)",
 "Bei Baudenkmal: zusätzliches Formular in der BzA; bei sonstiger erhaltenswerter Bausubstanz Bestätigung der Kommune"]),
 ("3. Umsetzung",["Aufträge an Fachfirmen erst nach Antrag (oder mit Förderklausel)",
 "Rechnungen mit Name, Maßnahme, Leistungszeitraum und Objektadresse, auf Deutsch",
 "Unbar bezahlt, Kontoauszüge aufbewahren; Anzahlungen sind möglich, solange die Bauarbeiten erst nach Antrag beginnen"]),
 ("4. Nachweis",["Bestätigung nach Durchführung (BnD) vom Experten mit Belegliste, vom Kreditnehmer unterschrieben",
 "BnD mindestens 4 Monate vor dem Verrechnungstermin des Tilgungszuschusses einreichen",
 "Fachplanung und Baubegleitung: Rechnungen sammeln (50 % Tilgungszuschuss möglich)",
 "Unterlagen 10 Jahre aufbewahren, 10 Jahre Wohnnutzung"])],
VB_N,"<b>Fristen:</b> Kreditabruf 12 Monate nach Zusage (verlängerbar um bis zu 24 Monate). Nachweis der Mittelverwendung innerhalb von 54 Monaten nach Zusage. Zwischen KfW-Sanierung (BEG WG) und BEG-Einzelmaßnahmen gilt eine Sperrfrist von 3 Jahren.","September 2026 (Merkblatt 261)"),
("Checkliste-KfW-458-Heizungsfoerderung","Checkliste KfW 458 · Heizungsförderung für Privatpersonen","Zuschuss für neue Heizung, Antrag im Portal „Meine KfW“",
[("1. Voraussetzungen",["Sie sind Eigentümer eines Wohngebäudes (Eigenheim, Wohnung oder vermietet); keine GbR, kein Nießbrauch",
 "Gebäude: Bauantrag oder Bauanzeige liegt mindestens 5 Jahre zurück",
 "Neue Heizung mit Optimierung des Heizungsverteilsystems (z. B. hydraulischer Abgleich)",
 "Keine gebrauchten Anlagen, keine Eigenbauanlagen"]),
 ("2. Vor dem Antrag",["Angebot des Fachunternehmens mit Typ, Leistung und Kosten",
 "Bestätigung zum Antrag (BzA) von Energieeffizienz-Experte oder Fachunternehmen",
 "Registrierung im Portal „Meine KfW“; Antragsteller muss mit der registrierten Person identisch sein",
 "Steuer-Identifikationsnummer",
 "Selbstnutzer mit Bonus: Meldebestätigung und Grundbuchauszug (Details siehe Punkt 4)"]),
 ("3. Antrag und Beauftragung",["Antrag stellen, bevor ein Vertrag ohne Bedingung geschlossen wird",
 "Liefer- oder Leistungsvertrag nur mit Bedingung „gültig bei KfW-Zusage“ und voraussichtlichem Umsetzungsdatum",
 "Erst nach der Zusage den Einbau starten"]),
 ("4. Nachweise nach dem Einbau",["Bestätigung nach Durchführung (BnD) mit 15-stelliger BnD-ID",
 "Schlussrechnung (keine Teil- oder Zwischenrechnung) mit Name laut Zusage, Objektadresse, Rechnungsnummer, Datum und Betrag; unbar bezahlt",
 "Klimageschwindigkeitsbonus: Meldebestätigung (Hauptwohnsitz) und Grundbuchauszug",
 "Einkommensbonus: Meldebestätigungen aller Haushaltsmitglieder, Grundbuchauszug, Einkommensteuerbescheide des zweiten und dritten Kalenderjahres vor Antrag (keine Lohnsteuerbescheinigungen, keine Rentenbescheide)",
 "Familienzuschlag: Meldebestätigung des minderjährigen Kindes und Nachweis der Kindergeldberechtigung",
 "Bei Bedarf: Formular zum hydraulischen Abgleich (VdZ)",
 "Alle Unterlagen als PDF, höchstens 10 MB je Datei"])],
"Der Antrag muss <b>vor</b> Vorhabenbeginn gestellt sein. Ein Vertrag ohne Förderbedingung oder der Baustart davor schließt die Förderung aus.","<b>Fristen:</b> Bewilligungszeitraum 36 Monate ab Zusage. Nachweise innerhalb von 6 Monaten nach der letzten Rechnung, sonst verfällt der Zuschuss. 10 Jahre Aufbewahrung und Nutzung. Förderhöhe und Boni hängen vom Einzelfall ab, sie rechnen wir im Angebot.","September 2026 (Merkblatt 458)"),
]

COMMON=[("Schritt 1 · Beratung und Beauftragung",["Auftrag bzw. Beratungsvertrag mit CS Energy (Beauftragungsunterlagen 10 Jahre aufbewahren)","Vollmacht, falls CS Energy Anträge oder Bestätigungen für Sie einreicht","Gewünschte Maßnahmen und Budget kurz notiert"])]
EXTRA={
"Checkliste-KfW-297-298-Klimafreundlicher-Neubau":[("Weitere Dokumente je Schritt",["<b>Beratung:</b> Auftrag an CS Energy, Vollmacht, Baugenehmigung bzw. Bauantrag, Lageplan, Bauzeichnungen (Grundrisse, Schnitte, Ansichten)","<b>Antrag:</b> Selbstauskunft und Einkommensnachweise für die Bank (je nach Bank), Kaufvertrag oder Bauvertrag mit Förderklausel, Baubeschreibung","<b>Umsetzung:</b> Angebote und Aufträge der Gewerke, Produkt- und Datenblätter der Bauteile (Dämmung, Fenster, Heizung, Lüftung), Fotodokumentation der Bauphasen","<b>Nachweis:</b> Abnahmeprotokolle, Inbetriebnahmeprotokoll der Heizung, Schlussrechnungen mit Kontoauszügen, Einzugsbestätigung"])],
"Checkliste-KfW-300-Wohneigentum-fuer-Familien":[("Weitere Dokumente je Schritt",["<b>Beratung:</b> Auftrag an CS Energy, Vollmacht, Baugenehmigung bzw. Bauantrag, Lageplan, Bauzeichnungen","<b>Antrag:</b> Selbstauskunft und Einkommensnachweise für die Bank (je nach Bank), Kauf- oder Bauvertrag mit Förderklausel, Nachweis, dass kein weiteres Wohneigentum vorhanden ist (z. B. Grundbuchauszüge)","<b>Umsetzung:</b> Angebote und Aufträge der Gewerke, Produkt- und Datenblätter, Fotodokumentation","<b>Nachweis:</b> Abnahmeprotokolle, Schlussrechnungen mit Kontoauszügen, Meldebestätigung nach Einzug, Grundbuchauszug"])],
"Checkliste-KfW-261-Sanierung-Effizienzhaus":[("Weitere Dokumente je Schritt",["<b>Beratung:</b> Auftrag an CS Energy, Vollmacht, Energieausweis oder Verbrauchsabrechnungen der letzten Jahre, Bestandspläne, Fotos des Gebäudes, Schornsteinfeger-Protokoll","<b>Antrag:</b> Selbstauskunft und Einkommensnachweise für die Bank (je nach Bank), Angebote der Fachfirmen (mit Förderklausel), Sanierungskonzept bzw. iSFP","<b>Umsetzung:</b> Aufträge und Bauzeitenplan, Produkt- und Datenblätter (Dämmstoffe, Fenster, Heizung, Lüftung), Fotodokumentation vor, während und nach der Sanierung","<b>Nachweis:</b> Unternehmererklärungen bzw. Protokolle der Fachfirmen (z. B. Luftdichtheit, hydraulischer Abgleich), Schlussrechnungen mit Kontoauszügen, Abnahmeprotokolle"])],
"Checkliste-KfW-458-Heizungsfoerderung":[("Weitere Dokumente je Schritt",["<b>Beratung:</b> Auftrag an CS Energy, Vollmacht für die Antragstellung im Portal, Fotos der alten Heizung und des Heizraums, Typenschild, Verbrauchsabrechnungen, Schornsteinfeger-Protokoll","<b>Antrag:</b> Angebot mit Gerätetyp und Datenblatt (förderfähige Anlage), Heizlastberechnung bzw. Auslegung, Planung der Optimierung des Heizungsverteilsystems","<b>Umsetzung:</b> Auftragsbestätigung mit Förderklausel, Fotos vom Einbau, Nachweis der Demontage bzw. Entsorgung der Altanlage","<b>Nachweis:</b> Inbetriebnahmeprotokoll, Protokoll hydraulischer Abgleich, Schlussrechnung mit Kontoauszug, Typenschild-Foto der neuen Anlage"])],
}
for p in pages: page(p[0],p[1],p[2],p[3]+EXTRA[p[0]],p[4],p[5],p[6])

