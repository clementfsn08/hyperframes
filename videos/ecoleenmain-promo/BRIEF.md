---
workflow: product-launch-video
flow: automation
storyboard: yes
message: "Avec ecoleenmain, c'est votre école qui a les meilleures notes."
destination: youtube
aspect: 1920x1080
language: fr
audience: "Directeurs et promoteurs d'écoles privées au Bénin"
length: 55s
angle: "Avant/après « La nuit des bulletins » + la pub au format d'un bulletin de notes officiel"
voice: ff_siwis
---

## Intent

Publicité 16:9 de 45 à 60 secondes pour ecoleenmain (gestion scolaire, https://www.ecoleenmain.com),
destinée aux directeurs d'écoles au Bénin. Angle choisi par l'utilisateur : mélange des pistes 1 et 5.

- Piste 1 « La nuit des bulletins » : ouverture sombre, 2 h du matin, 287 bulletins à taper à la main.
- Piste 5 « Le bulletin d'ecoleenmain » : la pub prend la forme d'un bulletin de notes officiel qui
  note la gestion de l'école (Bulletins 20/20 Excellent, Recouvrement Très bien, Hors connexion
  Félicitations…), et se termine par un diplôme du tableau d'honneur décerné à « Votre école ».

Voix off féminine française, posée comme une voix publicitaire. Le script validé est dans SCRIPT.md.

## Assets

- ../../captures/*.png — vraies captures du site (compte démo Direction), 1440 px et 390 px ; ce sont les visuels de la vidéo.
- ../../captures/pdf/bulletins-TLE-AB-T1-1.png — vrai bulletin généré (PDF rendu en image).
- ../../captures/pdf/tableau-honneur-TLE-AB-T1-1.png — vrai diplôme du tableau d'honneur.
- ../../captures/pdf/cartes-scolaires-TLE-AB-1.png — vraies cartes scolaires avec QR code.
- ../../captures/pdf/certificat-scolarite-FASSINOU-1.png — vrai certificat de scolarité numéroté.
- ../../captures/recu-paiement_desktop-1440.png — vrai reçu officiel REC-2026-00001.
- ../../fonctionnalites.md — inventaire des fonctionnalités (source de vérité des promesses).

## Customizations

- Style laissé au choix de Claude : pub tech moderne, titres cinétiques qui claquent, captures flottantes
  en légère 3D avec zooms précis, transitions rapides, tampons « officiels » qui s'abattent.
- Couleurs ecoleenmain : bleu marine + jaune. Ouverture sombre et chaude (lampe de bureau), puis bascule lumineuse.
- Lignes du « bulletin » : 3 éléments maximum chacune (matière · note · appréciation) pour rester lisibles en 16:9.

## Notes

- Ne pas réutiliser le bandeau « Il vous reste 9 jours avant la fin de votre essai » : recadrer les captures.
- La démo ne contient que 3 élèves : privilégier les documents et les écrans les plus parlants, éviter de montrer des totaux minuscules.
- Références motion de l'utilisateur sur x.com non consultables (réseau bloqué) : style choisi par Claude.
- Pas de capture automatique du site (`hyperframes capture`) : les captures authentifiées existent déjà dans ../../captures.
