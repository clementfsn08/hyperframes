# ecoleenmain : inventaire des fonctionnalités

> Exploration faite le 13 octobre 2026 avec le compte démo **Direction** (école « CPET MAMRE », Cotonou).
> Chaque page a été ouverte et capturée en 1440 px (ordinateur) et en 390 px (mobile), voir le dossier [`captures/`](captures/).
> Les documents générés pendant les tests (bulletins, tableau d'honneur, cartes, certificat) sont dans [`captures/pdf/`](captures/pdf/).

**En une phrase :** ecoleenmain réunit dans une seule application web (installable sur téléphone) la gestion des élèves, les notes et bulletins, la scolarité, la paie, l'emploi du temps et la communication avec les parents. Elle est pensée pour les écoles béninoises et **continue de fonctionner sans internet**.

---

## 1. Qui utilise l'application ?

| Profil | Ce qu'il fait dans ecoleenmain | Comment il accède |
|---|---|---|
| **Directeur / promoteur** (rôle « Direction ») | Accès complet : tableau de bord financier, paramètres de l'école, bulletins, tableau d'honneur, certificats, conduite, corrections de notes, comptes utilisateurs. | Compte principal de l'école. |
| **Secrétaire / comptable** | Inscriptions, fiches élèves, encaissement de la scolarité et reçus, messages aux parents, création des accès parents. | Compte utilisateur créé par la direction, limité aux menus cochés par elle (« Paramètres › Utilisateurs › Modifier les accès »). |
| **Enseignant** | Fait l'appel, cours par cours, et saisit les notes (interrogations, Devoir 1, Devoir 2) **uniquement pour ses classes et ses matières**. Une série enregistrée est verrouillée : seule la direction peut la corriger, en donnant un motif. Il ne peut pas toucher à la conduite. | Compte créé par la direction. Il ne voit que les classes des matières qui lui sont attribuées. |
| **Parent** | Consulte les notes, moyennes, appréciations et la conduite de son enfant, ses absences et retards, et l'état de la scolarité (dû, payé, reste). Un seul compte suffit pour plusieurs enfants (frères et sœurs). | Invitation envoyée depuis la fiche de l'élève (« Compte(s) parent › + Ajouter un parent »), par e-mail ou par lien envoyé sur WhatsApp. |

**Ce qui est unique :** l'école peut **masquer les notes au parent tant qu'une tranche de scolarité échue n'est pas soldée**. Le parent voit alors le reste à payer et un bouton « Solder la tranche ». Les notes réapparaissent dès que le paiement est enregistré. C'est un levier de recouvrement intégré, et la direction peut le désactiver.

> ⚠️ Je n'ai testé que le compte Direction. Les droits Enseignant et Parent ci-dessus viennent des guides officiels intégrés à l'application et des écrans de la direction (création d'accès parent, rôles utilisateurs). Pour des captures des espaces enseignant et parent, il me faut les identifiants de démo de ces comptes.

---

## 2. Fonctionnalités, module par module

### 2.1 Tableau de bord
- **À quoi ça sert :** voir l'état de l'école d'un coup d'œil : revenus du mois, élèves actifs, créneaux programmés, soldes impayés, graphique des revenus sur 6 mois, liste des impayés avec un bouton « Relancer », activité récente. Le bouton jaune **« Revenu reçu »** reste accessible depuis toutes les pages.
- **Pour qui :** directeur / promoteur.
- **Unique :** c'est le « tableau de bord du promoteur dans sa poche ». Les impayés sont visibles en temps réel, et on peut relancer en un clic.
- Captures : `dashboard_*`, `new-revenue_*`

### 2.2 Gestion des élèves
| Sous-menu | À quoi ça sert | Pour qui |
|---|---|---|
| Classes | Créer les classes, rattachées à un cycle, et voir l'effectif de chacune. | Direction |
| Cycles | Fixer le barème de notation par cycle : Primaire /10, Secondaire /20, Universitaire /10. | Direction |
| Inscrire un nouvel élève | Fiche complète : matricule automatique (ELE-2026-001), photo, naissance, quartier, contact WhatsApp et e-mail du parent. | Secrétariat |
| Inscrire un ancien élève | Réinscription d'une année sur l'autre, par recherche du nom : l'élève et son historique suivent. | Secrétariat |
| Liste des élèves | Liste filtrable par classe, export Excel, archives. La fiche donne accès au **certificat de scolarité** et aux **comptes parents**. | Secrétariat, direction |
| Importer des élèves | Inscrire toute une classe à partir d'un fichier Excel (modèle fourni). | Secrétariat |
| Cartes scolaires | Cartes d'identité scolaires, à l'unité ou pour toute une classe en PDF. | Secrétariat, direction |
| Total effectif | Statistiques garçons / filles par classe. | Direction |

**Ce qui est unique :**
- **Carte scolaire officielle :** drapeau du Bénin, « République du Bénin – Fraternité, Justice, Succès », ministère, photo, **QR code « VÉRIFIÉ »** et numéro « Si trouvée ». Toute une classe sort en un seul PDF (`captures/pdf/cartes-scolaires-TLE-AB.pdf`).
- **Certificat de scolarité numéroté** (N° 00004/2026-2027) en un clic. L'appréciation du travail est calculée à partir des notes. Deux formats : A5, ou A4 paysage avec 2 certificats à découper (`captures/pdf/certificat-scolarite-FASSINOU.pdf`).

### 2.3 Enseignants, Matières, Personnel
- **Enseignants :** liste de l'équipe pédagogique, statut (temps plein / vacataire), contact, archivage.
- **Matières :** code, **coefficient**, enseignant attribué, classes et volume horaire hebdomadaire. Cette attribution détermine ce que chaque enseignant voit.
- **Personnel :** personnel non enseignant (surveillants, comptables…) et masse salariale mensuelle.
- **Pour qui :** direction.

### 2.4 Emploi du temps
- **À quoi ça sert :** une grille du lundi au samedi, par classe, pour planifier les cours.
- **Unique :** **pas de conflit** possible, car un professeur ne peut pas être dans deux salles à la fois. L'emploi du temps sert aussi à faire l'appel cours par cours et à calculer la paie des vacataires à l'heure.
- **Pour qui :** direction (planification), enseignants (consultation).

### 2.5 Notes & résultats → bulletins et tableau d'honneur ⭐
- **À quoi ça sert :** saisir les notes (interrogations, Devoir 1, Devoir 2) par classe, matière et période, puis voir immédiatement la moyenne et le rang de chaque élève, avec la moyenne de la classe par matière.
- **Pour qui :** enseignants (saisie de leurs notes) et direction (consultation, corrections, import / export Excel, bulletins).
- **Actions testées :**
  - **« Télécharger les bulletins (PDF) »** sort un bulletin par élève de la classe, prêt à imprimer (`captures/pdf/bulletins-TLE-AB-T1.pdf`). ✅
  - **Bulletin individuel** (`bulletin-eleve_*`), avec impression ou téléchargement. ✅
  - **« Tableau d'honneur (2) »** sort un diplôme paysage par élève ayant au moins 12/20 (`captures/pdf/tableau-honneur-TLE-AB-T1.pdf`). ✅
  - **« Couleurs du bulletin »** et **« Couleurs du tableau d'honneur »** : 8 palettes prêtes (Bleu marine, Vert, Bordeaux…, « Couleurs nationales », « Bleu & or »…) ou des couleurs personnalisées, et le nom de l'école en filigrane. ✅
- **Ce qui est unique :**
  - **Calcul conforme au système béninois :** (moyenne des interrogations + Devoir 1 + Devoir 2) ÷ 3, avec des poids que l'école peut modifier. Rang par matière, appréciations automatiques (« Passable », « Assez bien », « Bien »…).
  - **Bulletin au format officiel :** République du Bénin, ministère, logo et filigrane de l'école, bilan des 3 trimestres et bilan annuel, décision du conseil, discipline (retards, absences, heures de consigne), observation du chef d'établissement. La case « Tableau d'honneur » se coche toute seule.
  - **Choix trimestres ou semestres :** toute l'application s'adapte (notes, bulletins, tableau d'honneur, espace parent).
  - **Notes verrouillées après saisie :** l'enseignant ne peut plus les modifier, et une correction par la direction exige un motif. On évite ainsi les notes « arrangées ».
- Captures : `grades_*`, `grades-tle_*`, `bulletin-eleve_*`, `couleurs-bulletin_*`, `couleurs-tableau-honneur_*`, `enter-grades_*`, `grades-import_*`

### 2.6 Conduite
- **À quoi ça sert :** chaque élève part d'une note fixée par l'école (18/20 dans la démo). La direction retire des points avec un motif (comportement, absences, retards) et peut ajouter des heures de colle.
- **Pour qui :** direction uniquement.
- **Unique :** la conduite devient automatiquement la **dernière ligne du bulletin** (coefficient 1). Les heures de colle sont reportées dans la partie « Discipline ».
- Captures : `conduite_*`

### 2.7 Absences (appel)
- **À quoi ça sert :** registre d'appel quotidien par classe et par cours. Tout le monde est « Présent » par défaut, on ne touche que les absents, retards et absences excusées.
- **Pour qui :** enseignants et surveillants. La direction ouvre ce menu aux comptes concernés.
- **Unique :** l'appel se fait **même sans internet**. Les absences et retards sont reportés automatiquement sur le bulletin, et une absence peut être signalée au parent en un clic via Messages.

### 2.8 Comptabilité
| Sous-menu | À quoi ça sert |
|---|---|
| Inscription & réinscription | Encaisser les frais d'inscription (nouveaux élèves) et de réinscription (anciens). |
| Frais de scolarité | Barème par classe en **3 tranches** avec dates limites. Pour chaque élève : dû, payé, reste, et statut (Payé / Partiel / Impayé). Les paiements se font en espèces, Mobile Money ou virement. **Reçu numéroté** pour chaque versement. |
| Paiement des enseignants | Salaire **à l'heure** pour les enseignants, calculé à partir de l'emploi du temps. Suivi du mois (payé / non payé). |
| Paiement des personnels | Salaire mensuel fixe du personnel non enseignant. |
| Dépenses | Dépenses de l'école par catégorie. |
| Avances sur salaire | Prêts au personnel, à déduire d'un mois précis. |

- **Pour qui :** comptable / secrétaire et direction.
- **Unique :** **tout est en F CFA, au franc près.** Un reçu numéroté empêche les contestations des parents. Hors connexion, un **reçu provisoire** (PROV-…) est remis au parent, puis le reçu officiel est disponible au retour du réseau. Ce module couvre à la fois les recettes et les salaires : c'est la trésorerie complète de l'école.
- Captures : `accounting-*`, `new-revenue_*`

### 2.9 Messages (e-mail et WhatsApp)
- **À quoi ça sert :** écrire aux parents (un élève, une classe, toute l'école), aux professeurs ou au personnel. Trois modèles sont rédigés au nom de l'école : **Absence**, **Convocation / réunion**, **Message libre**. L'historique indique l'état de chaque message (envoyé, ignoré, échoué).
- **Pour qui :** direction et secrétariat.
- **Unique :** **WhatsApp intégré.** Le bouton « Ouvrir WhatsApp » ouvre la conversation avec le message déjà écrit, il ne reste qu'à appuyer sur Envoyer. L'indicatif +229 est ajouté automatiquement. L'envoi par SMS est annoncé (« Bientôt disponible »).
- Captures : `messages-new_*`, `messages_*`

### 2.10 Hors connexion ⭐
- **À quoi ça sert :** pendant un délestage ou une coupure du réseau, on continue à faire l'appel, saisir les notes, encaisser la scolarité, inscrire des élèves, et même préparer la rentrée (classes, matières, emploi du temps). Tout est gardé sur l'appareil puis **envoyé automatiquement, dans l'ordre**, au retour d'internet.
- **Pour qui :** tout le personnel.
- **Unique :** c'est **l'argument différenciant n°1** face aux logiciels en ligne classiques. Aucune saisie n'est perdue et aucun doublon n'est possible. Un onglet « Saisies en attente » montre ce qui reste à envoyer. L'application **s'installe sur l'écran d'accueil** comme une vraie application (Android, iPhone ou ordinateur), sans passer par le Play Store.
- Captures : `hors-connexion_*`

### 2.11 Paramètres
- **Informations de l'établissement :** logo, nom, type, adresse, contacts. Pour la carte scolaire : République, devise, ministère, direction, drapeau personnalisable. Pour les certificats : ville et titre du signataire (« Le Directeur », « Le Proviseur »).
- **Organisation de l'année :** 3 trimestres ou 2 semestres.
- **Pondération des notes :** poids des interrogations et des devoirs, et note de conduite de départ.
- **Calendrier académique :** dates des périodes et des vacances, utilisées pour compter les absences sur les bulletins.
- **Utilisateurs :** créer les comptes (enseignants, secrétariat…), **choisir les menus visibles par chaque compte**, suspendre un accès.
- **Préférences et compte :** langue **FR / EN**, mot de passe, connexion Google.
- **Pour qui :** direction.

### 2.12 Abonnement et partenariat
- **Abonnement :** forfaits **Essentiel** (150 000 F CFA/an, jusqu'à 500 élèves), **Croissance** (200 000 F CFA/an, élèves illimités, le plus choisi) et **Flexible** (75 000 F CFA/trimestre). **Toutes les fonctionnalités sont incluses dans chaque forfait**, avec **14 jours d'essai gratuit** et sans carte bancaire.
- **Partenariat :** une école ou un directeur qui recommande ecoleenmain touche **10 % de chaque abonnement payé**, chaque année, retirable par **Mobile Money** dès 10 000 F CFA.
- **Pour qui :** promoteur / direction.

### 2.13 Aide
- 10 guides intégrés, chacun avec son public cible : « Premiers pas », « Faire l'appel », « Saisir les notes », « Bulletins, tableau d'honneur et certificats », « Encaisser la scolarité », « Espace parent »… Chaque guide est lisible en ligne, imprimable ou téléchargeable en PDF. L'accompagnement se fait sur WhatsApp.

---

## 3. Ce qui rend ecoleenmain unique (à retenir pour la vidéo)

1. **Fonctionne sans internet** : délestages et réseau faible ne bloquent plus l'école, et les données se synchronisent seules.
2. **Bulletins officiels en un clic** : moyennes, rangs et appréciations calculés au format béninois, avec logo et filigrane.
3. **Documents officiels prêts à imprimer** : cartes scolaires avec QR code, certificats numérotés, diplômes du tableau d'honneur.
4. **Scolarité sous contrôle** : 3 tranches, reçus numérotés, impayés en temps réel, et **notes masquées aux parents tant que la tranche n'est pas soldée**.
5. **WhatsApp intégré** pour prévenir les parents (absence, convocation).
6. **Un compte pour chacun** : direction, secrétariat, enseignants et parents, avec des droits précis pour chaque compte.
7. **Pensé pour le Bénin** : F CFA, Mobile Money, de la maternelle à la Terminale, trimestres ou semestres.
8. **Tout inclus, prix accessible** : dès 75 000 F CFA par trimestre, 14 jours d'essai gratuit.

---

## 4. Actions testées

| Action | Résultat |
|---|---|
| Connexion avec le compte démo | ✅ |
| Générer les bulletins de la classe TLE AB (1er trimestre, PDF de 3 pages) | ✅ `captures/pdf/bulletins-TLE-AB-T1.pdf` |
| Ouvrir le bulletin d'un élève | ✅ |
| Générer le tableau d'honneur (2 diplômes) | ✅ `captures/pdf/tableau-honneur-TLE-AB-T1.pdf` |
| Générer les cartes scolaires de la classe | ✅ `captures/pdf/cartes-scolaires-TLE-AB.pdf` |
| Générer un certificat de scolarité (FASSINOU Boris) | ✅ `captures/pdf/certificat-scolarite-FASSINOU.pdf`. **Attention : cela a créé le certificat n° 00004/2026-2027 dans la démo.** |
| Ouvrir les panneaux « Couleurs du bulletin » et « Couleurs du tableau d'honneur » | ✅ Ouverts sans rien enregistrer |
| Ouvrir le formulaire d'ajout d'un compte parent | ✅ Ouvert sans rien enregistrer |

**Volontairement non fait** (pour ne pas modifier les données ni contacter de vraies personnes) : enregistrer un paiement, envoyer un message, saisir ou modifier des notes, retirer des points de conduite, ajouter ou supprimer un élève ou un utilisateur, payer l'abonnement.

## 5. Remarques relevées pendant l'exploration
- Le compte démo contient peu de données : 3 élèves, la classe 5ème A est vide, les dates de trimestres ne sont pas configurées. **Pour la vidéo, il serait plus parlant de remplir la démo** (plusieurs classes, une trentaine d'élèves, des paiements) avant de refaire les captures.
- Bandeau visible sur la démo : « Il vous reste 9 jours avant la fin de votre essai ». Mieux vaut l'éviter dans la vidéo.
- Fonctions annoncées « Bientôt disponible » : envoi par SMS, authentification à deux facteurs.
