# Asset Descriptions

⚠️  No vision credentials — descriptions below are catalog-derived (alt text, headings, section context, filename) instead of Vision-generated. To get richer Vision descriptions on the next capture, set GEMINI_API_KEY (or GOOGLE_API_KEY), or HYPERFRAMES_VERTEX_PROJECT_ID plus HYPERFRAMES_VERTEX_SERVICE_ACCOUNT for Vertex service-account auth, and re-run.

The `logo-<hash>.svg` filename prefix is a structural hint (DOM said this SVG was inside a `<header>`, home-link `<a>`, or had an aria-label matching the page brand). To pick the actual brand logo without Vision, open the `logo-*` candidates in a previewer or rasterize them with `sharp` before referencing — composing a fake logo ships off-brand in the final video.

- svgs/logo-072732f6.svg — logo 072732f6
- svgs/logo-0fc0d4eb.svg — logo 0fc0d4eb
- svgs/logo-248bfe77.svg — logo 248bfe77
- svgs/logo-4d49a864.svg — logo 4d49a864
- svgs/logo-50b5eaea.svg — logo 50b5eaea
- svgs/logo-a7778929.svg — logo a7778929
- svgs/logo-ac17354f-2.svg — logo ac17354f 2
- svgs/logo-ac17354f-3.svg — logo ac17354f 3
- svgs/logo-ac17354f-4.svg — logo ac17354f 4
- svgs/logo-ac17354f-5.svg — logo ac17354f 5
- svgs/logo-ac17354f-6.svg — logo ac17354f 6
- svgs/logo-ac17354f.svg — logo ac17354f
- svgs/logo-c5671373.svg — logo c5671373
- svgs/svg-178f6454.svg — svg 178f6454
- svgs/svg-54dd4dd8.svg — svg 54dd4dd8

## Brand (downloaded from the live site)

- brand/logo.png — LOGO OFFICIEL ecoleenmain : main bleu marine tenant une toque avec point jaune + barres, wordmark "ecole" bleu marine, "en" jaune, "main" bleu marine. 1730x377, fond transparent. Logo de fin.
- brand/logo-mark.png — symbole seul (main + toque), 340x377, transparent.
- brand/icon.png — icône d'application 512x512 (carré arrondi).

## Real authenticated screens (compte démo Direction, école CPET MAMRE) — the video's featured assets

- screens/dashboard-clean_desktop-1440.png — Tableau de bord SANS le bandeau d'essai : 4 cartes (Revenus ce mois 100 000 F CFA, Élèves actifs, Créneaux, Soldes impayés 680 000 F CFA), graphe revenus mensuels, liste « Soldes impayés » avec boutons Relancer. 1440x826.
- screens/dashboard_mobile-390.png — même tableau de bord sur téléphone (contient le bandeau d'essai en haut : recadrer sous y≈850). 780x2878.
- screens/grades-tle_desktop-1440.png — Notes & résultats, classe TLE AB : boutons « Télécharger les bulletins (PDF) », « Tableau d'honneur (2) », tableau moyennes par matière, rangs 1er/2e. 1440x900.
- screens/bulletin-eleve_desktop-1440.png — page Bulletin de notes de FASSINOU Boris (aperçu web), boutons Imprimer / Télécharger PDF. 1440x1283.
- screens/accounting-tuition_desktop-1440.png — Frais de scolarité : Total dû 780 000, payé 100 000, restant 680 000 ; statuts Partiel/Impayé ; historique avec bouton « Reçu ». 1440x900.
- screens/recu-paiement_desktop-1440.png — Reçu officiel REC-2026-00001 : en-tête République du Bénin, 100 000 F CFA, « Cent Mille Francs CFA Seulement », situation du compte, QR code, signature caissier. 1440x1202.
- screens/hors-connexion_mobile-390.png — page Hors connexion sur téléphone (pastille verte « Connecté », liste élèves gardée sur l'appareil). 780x1688. Superposer une pastille orange « Hors connexion » reconstruite.
- screens/hors-connexion_desktop-1440.png — même page sur ordinateur.
- screens/student-cards_desktop-1440.png — Cartes scolaires : liste classe + « Télécharger toutes les cartes (PDF) ».
- screens/carte-scolaire-eleve_desktop-1440.png — aperçu web d'une carte scolaire.
- screens/fiche-eleve_desktop-1440.png / certificat-formulaire_desktop-1440.png — fiche élève et formulaire « Certificat de scolarité ».
- screens/ajout-utilisateur-enseignant_desktop-1440.png — « Créer un utilisateur », rôle Enseignant, Professeur associé, menus cochables.
- screens/messages-new_desktop-1440.png / messages-new_mobile-390.png — Nouveau message : destinataires parents/profs/personnel, modèles Absence/Convocation, canal Email/WhatsApp, aperçu du message.
- screens/messages_desktop-1440.png — Historique des messages avec bouton « Ouvrir WhatsApp ».
- screens/conduite_desktop-1440.png, schedule_desktop-1440.png, enter-grades_desktop-1440.png, couleurs-bulletin_desktop-1440.png — écrans secondaires.

## Real generated documents (PDF rendus à 220 dpi)

- docs/bulletins-TLE-AB-T1.png — VRAI BULLETIN DE NOTES officiel (A4 portrait) : République du Bénin, ministère, CPET MAMRE, logo, filigrane, tableau matières vert, bilans trimestres, décision du conseil, case Tableau d'honneur cochée.
- docs/tableau-honneur-TLE-AB-T1.png — VRAI DIPLÔME du tableau d'honneur (A4 paysage) : cadre bordeaux/orange, drapeau du Bénin, « TABLEAU D'HONNEUR », GODO Joseph, 14,90/20.
- docs/cartes-scolaires-TLE-AB.png — planche de 3 VRAIES CARTES D'IDENTITÉ SCOLAIRES vertes avec drapeau, photo, QR code « VÉRIFIÉ ».
- docs/certificat-scolarite-FASSINOU.png — VRAI CERTIFICAT DE SCOLARITÉ N° 00004/2026-2027 (A5), vert, filigrane.
