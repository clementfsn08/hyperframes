---
format: 1920x1080
duration: 55s
message: "Avec ecoleenmain, c'est votre école qui a les meilleures notes."
arc: BAB — before (la nuit des bulletins) → bridge (le bulletin de votre école) → 5 matières notées → décision du conseil → CTA
audience: Directeurs et promoteurs d'écoles privées au Bénin
mode: collaborative
music: calm corporate piano, hopeful, light pulse
---

## Frame 1 — La nuit des bulletins

- type: hook
- blueprint: dataviz-countup
- scene: Bureau dans le noir à 2 h du matin, piles de cahiers, compteur « 287 bulletins restants »
- duration: 6.5s
- transition_in: cut
- status: built
- voiceover: "Deux heures du matin. Il vous reste deux cent quatre-vingt-sept bulletins à taper… à la main."
- asset_candidates: none (scène typographique et graphique ; cahiers, lampe et calculatrice dessinés en CSS/SVG)

Avant. La douleur que tout directeur connaît : les nuits de fin de trimestre. Ambiance sombre et chaude
(halo de lampe de bureau ambre), horloge 02:00 qui bat, compteur rouge « 287 » qui ne descend presque pas.

## Frame 2 — Et si votre école avait les meilleures notes ?

- type: product_intro
- blueprint: kinetic-type-beats
- scene: La lumière s'allume ; un en-tête « BULLETIN DE NOTES — Votre école — 1er trimestre » s'imprime
- duration: 4.5s
- transition_in: flash
- status: built
- voiceover: "Et si, cette année, c'était votre école qui avait les meilleures notes ?"
- asset_candidates: brand/logo-mark.png

Le pont. Bascule du noir au clair : la pub devient un bulletin de notes officiel (en-tête République du
Bénin / ministère reproduit du vrai bulletin, nom de l'établissement « Votre école »). Promesse posée au beat 2.

## Frame 3 — Bulletins : 20/20 Excellent

- type: feature_showcase
- blueprint: device-surface-showcase
- scene: Ligne « Bulletins · 20/20 · Excellent » ; la vraie page Notes & résultats flotte, puis le vrai bulletin PDF se déplie
- duration: 8s
- transition_in: slide-up
- status: built
- voiceover: "Bulletins : vingt sur vingt. Moyennes, rangs, appréciations… tout se calcule seul, à votre logo, en un clic."
- asset_candidates: screens/grades-tle_desktop-1440.png, docs/bulletins-TLE-AB-T1.png

Preuve 1 — le gain de temps. La ligne de bulletin s'écrit en haut (matière · note · appréciation) ;
« Moyennes », « rangs », « appréciations » sont pointés sur la vraie capture au moment où la voix les nomme ;
« en un clic » = clic sur « Télécharger les bulletins (PDF) » → le vrai bulletin officiel glisse au premier plan.

## Frame 4 — Recouvrement : Très bien

- type: benefit_highlight
- blueprint: camera-journey
- scene: Ligne « Recouvrement · 18/20 · Très bien » ; frais de scolarité, puis le vrai reçu REC-2026-00001
- duration: 8s
- transition_in: slide-up
- status: built
- voiceover: "Recouvrement : très bien. Chaque versement a son reçu numéroté, et les impayés s'affichent en temps réel."
- asset_candidates: screens/accounting-tuition_desktop-1440.png, screens/recu-paiement_desktop-1440.png, screens/dashboard-clean_desktop-1440.png

Preuve 2 — l'argent. La caméra plonge sur le reçu (numéro REC-2026-00001 et montant en lettres mis en
valeur), puis recule sur la carte « Soldes impayés » du tableau de bord (680 000 F CFA, boutons Relancer).

## Frame 5 — Hors connexion : Félicitations

- type: feature_showcase
- blueprint: device-surface-showcase
- scene: Ligne « Hors connexion · 19/20 · Félicitations » ; téléphone avec la vraie page Hors connexion, pastille orange, synchronisation
- duration: 7s
- transition_in: blackout-flicker
- status: built
- voiceover: "Délestage ? Votre école continue, même sans internet. Tout part au retour du réseau."
- asset_candidates: screens/hors-connexion_mobile-390.png

Preuve 3 — l'argument différenciant. Micro-coupure (l'écran grésille/assombrit une fraction de seconde),
la pastille verte « Connecté » devient orange « Hors connexion · 3 saisies en attente », puis au retour
du réseau elle repasse au vert avec « ✓ Envoyé ».

## Frame 6 — Documents officiels : Excellent

- type: benefit_highlight
- blueprint: grid-card-assemble
- scene: Ligne « Documents officiels · Excellent » ; les vraies cartes scolaires, le certificat et le tableau d'honneur arrivent en éventail
- duration: 6.5s
- transition_in: slide-up
- status: built
- voiceover: "Cartes scolaires, certificats, tableau d'honneur : prêts à imprimer."
- asset_candidates: docs/cartes-scolaires-TLE-AB.png, docs/certificat-scolarite-FASSINOU.png, docs/tableau-honneur-TLE-AB-T1.png

Preuve 4 — l'image de l'école. Chaque document tombe sur la table quand la voix le nomme
(cartes → certificat → tableau d'honneur), « prêts à imprimer » = le trio se range proprement.

## Frame 7 — Communication : Très bien

- type: benefit_highlight
- blueprint: comparison-split
- scene: Ligne « Communication · Très bien » ; à gauche création d'un compte enseignant, à droite message WhatsApp aux parents
- duration: 6.5s
- transition_in: slide-up
- status: built
- voiceover: "Enseignants et parents ont chacun leur compte, et WhatsApp prévient les familles."
- asset_candidates: screens/ajout-utilisateur-enseignant_desktop-1440.png, screens/messages-new_desktop-1440.png

Preuve 5 — tout le monde dans la boucle. Deux panneaux en miroir : rôle « Enseignant » (accès limité à ses
classes) et aperçu du message d'absence avec un bouton « Ouvrir WhatsApp » qui pulse.

## Frame 8 — Décision du conseil

- type: benefit_highlight
- blueprint: titlecard-reveal
- scene: Un tampon « TABLEAU D'HONNEUR » s'abat ; le diplôme au nom de « Votre école » apparaît
- duration: 5s
- transition_in: cut
- status: built
- voiceover: "Décision du conseil : inscrite au tableau d'honneur."
- asset_candidates: docs/tableau-honneur-TLE-AB-T1.png

Le climax. Le bulletin de « Votre école » se termine : moyenne générale 19/20, case « Tableau d'honneur »
cochée, tampon jaune qui s'abat ; le diplôme (style du vrai tableau d'honneur) porte « Votre école ».

## Frame 9 — ecoleenmain, dans votre main

- type: cta
- blueprint: logo-assemble-lockup
- scene: Le logo ecoleenmain s'assemble ; « Toute votre école, dans votre main. » ; ecoleenmain.com · 14 jours offerts
- duration: 6.5s
- transition_in: crossfade
- status: built
- voiceover: "ecoleenmain. Toute votre école, dans votre main. Essai gratuit de quatorze jours."
- asset_candidates: brand/logo.png, brand/logo-mark.png

Signature + appel à l'action : logo officiel, slogan du site, URL et « 14 jours offerts · sans carte bancaire ».
