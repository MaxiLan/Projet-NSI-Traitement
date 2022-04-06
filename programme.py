import folium
import os
import webbrowser

c = folium.Map(location=[48.9066, 2.8125], zoom_start=2)

def carte(annee, poids, fichier):
  f1 = open("/home/maxime/Documents/Cours/NSI/Traitement/Projet/Meteorite_Landings.csv", 'r', encoding='utf8')
  lignes = f1.readlines()
  ligne_sans_premiere = lignes[1:]
  for ligne in ligne_sans_premiere:
      ligne = ligne.strip()
      nom, id, valid, classe, masse, statut, date, lat, long, coord1, coord2 = ligne.split(',')
      if poids and float(masse)>100000:
        folium.Marker([float(lat),float(long)],popup="Météorite"+nom).add_to(c)
      if annee and int(date)>=2000:
        folium.Marker([float(lat),float(long)],popup="Météorite"+nom).add_to(c)
  f1.close()
  c.save(fichier)


def page_html(fichier):
    f2 = open(fichier, 'w', encoding="utf-8")
    f2.write(
        """
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Chutes de météorites</title>
	      <link rel="stylesheet" href="style.css">
      </head>
    <body>
      <h2>Les différentes chutes de météorites dans le monde :</h2>
      <p>Carte :</p>
      <iframe src="carte_trier_annee.html" height="800" width="1000"></iframe>
      <a href='carte_trier_poids.html'>Cliquer ici pour voir les météorites de plus de 100 kg</a>
      <a href='carte_trier_annee.html'>Cliquer ici pour voir les météorites tombées après l'année 2000</a>
      <script>
      script.js
      </script>
    </body>
    </html>
    """)
    f2.close()

carte(False, True, 'carte_trier_poids.html')
carte(True, False, 'carte_trier_annee.html')
carte()
page_html('page_web.html')
webbrowser.open(os.getcwd()+"/page_web.html")