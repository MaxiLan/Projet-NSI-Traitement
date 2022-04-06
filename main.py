import folium
import os
import webbrowser

c = folium.Map(location=[48.9066, 2.8125], zoom_start=2)

# création d'une carte


def carte(annee, poids, fichier):
    f1 = open("/home/maxime/Documents/Cours/NSI/Traitement/Projet/Meteorite_Landings.csv",
              'r', encoding='utf8')
    lignes = f1.readlines()
    ligne_sans_premiere = lignes[1:]
    nbr = 0
    for ligne in ligne_sans_premiere:
        ligne = ligne.strip()
        nom, id, valid, classe, masse, statut, date, lat, long, coord1, coord2 = ligne.split(
            ',')
        if poids and float(masse) > 100000:
            folium.Marker([float(lat), float(long)],
                          popup="Météorite : "+nom).add_to(c)
            nbr = nbr+1
        if annee and int(date) >= 2000:
            folium.Marker([float(lat), float(long)],
                          popup="Météorite : "+nom).add_to(c)
            nbr = nbr+1
    f1.close()
    c.save(fichier)
    return nbr


# création de 2 cartes
nbr2 = carte(
    True, False, '/home/maxime/Documents/Cours/NSI/Traitement/Projet/carte_trier_annee.html')
nbr1 = carte(
    False, True, '/home/maxime/Documents/Cours/NSI/Traitement/Projet/carte_trier_poids.html')

nb1 = str(nbr1)
nb2 = str(nbr2)


def page_html(fichier):
    f2 = open(fichier, 'w', encoding="utf-8")
    if fichier == '/home/maxime/Documents/Cours/NSI/Traitement/Projet/page_web2.html':
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
        <p>Il y a """+nb2+""" météorites qui sont tombées sur Terre après l'année 2000</p>
        <iframe src="carte_trier_annee.html" height="800" width="1000"></iframe><br>  
        <button id="bouton1" >Voir les météorites tombées aprèes l'année 2000 </button>
        <button id="bouton2">Voir les météorites de plus de 100 kg !</button>
        <script src='script.js'>
        </script>
        </body>
        </html>
      """
        )
        f2.close()
    else:
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
        <p>Il y a """+nb1+""" météorites de plus de 100 kg qui sont tombées sur Terre</p>
        <iframe src="carte_trier_poids.html" height="800" width="1000"></iframe><br>   
        <button id="bouton1">Voir les météorites tombées après l'année 2000</button>
        <button id="bouton2">Voir les météorites de plus de 100 kg !</button>
        <script src='script.js'>
        </script>
      </body>
      </html>
      """)
        f2.close()


page_html('/home/maxime/Documents/Cours/NSI/Traitement/Projet/page_web1.html')
page_html('/home/maxime/Documents/Cours/NSI/Traitement/Projet/page_web2.html')
webbrowser.open(
    os.getcwd()+"/home/maxime/Documents/Cours/NSI/Traitement/Projet/page_web1.html")
