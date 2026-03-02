# Résumé du Brief CI/CD - Formulaire Simplon

## Titre
> 67/100 caractères

```
Pipeline CI/CD Professionnelle - De la Veille au Déploiement Azure
```

---

## Description rapide
> 876/900 caractères

```
Ce brief propose la mise en place d'une pipeline CI/CD complète pour une application FastAPI. Les apprenants débutent par une veille technologique sur les concepts CI/CD, les outils (linters, formatters, scanners), puis implémentent progressivement : stratégie de branches Git avec protection, workflows GitHub Actions (lint, tests, sécurité), pre-commit hooks, containerisation Docker avec publication sur GHCR, versionnage sémantique automatique avec python-semantic-release, documentation MkDocs sur GitHub Pages, et déploiement continu sur Azure Container Apps. Le projet utilise uv comme gestionnaire de packages Python moderne et suit les conventions professionnelles (Conventional Commits, GitFlow simplifié). Durée estimée : 15-20h (phases principales) à 31h (avec bonus). Progression en 8 phases du niveau débutant à expert.
```

---

## Contexte
> 2847/6000 caractères

```
Dans le développement logiciel moderne, la maîtrise des pratiques CI/CD (Continuous Integration / Continuous Deployment) est devenue incontournable pour tout développeur professionnel.

Ce brief s'inscrit dans un contexte d'apprentissage pratique où l'apprenant travaille sur une application FastAPI existante présentant intentionnellement des problèmes de qualité (formatage, imports inutilisés, secrets en dur, manque de typage).

L'objectif est de transformer cette base de code en un projet professionnel avec une infrastructure DevOps complète.

PROBLÉMATIQUES ADRESSÉES :
- Comment automatiser les contrôles qualité du code ?
- Comment éviter les régressions grâce aux tests automatisés ?
- Comment standardiser les messages de commit pour un historique lisible ?
- Comment gérer les versions de manière automatique et fiable ?
- Comment déployer de manière sécurisée et reproductible ?

TECHNOLOGIES UTILISÉES :
- Python 3.13 avec FastAPI
- uv (gestionnaire de packages moderne, alternative à pip/poetry)
- GitHub Actions pour l'automatisation CI/CD
- Ruff (linting/formatting), Mypy (type checking), Bandit (sécurité)
- Docker et GitHub Container Registry (GHCR)
- python-semantic-release pour le versionnage automatique
- MkDocs Material pour la documentation
- Azure Container Apps et Cosmos DB pour le déploiement cloud

L'apprenant progresse de la compréhension théorique (veille) vers l'implémentation pratique, en passant par 8 phases structurées de difficulté croissante.
```

---

## Modalités pédagogiques
> 2156/6000 caractères

```
APPROCHE PÉDAGOGIQUE :
La formation adopte une approche "learn by doing" structurée en 8 phases progressives, débutant obligatoirement par une veille technologique avant toute implémentation.

PHASES D'APPRENTISSAGE :
- Phase 0 (3-4h) : Veille technologique - Recherche et documentation sur CI/CD, uv, Semantic Release, comparatif d'outils
- Phase 1 (1h) : Découverte du projet existant et identification des problèmes de qualité
- Phase 2 (2h) : Mise en place de la stratégie Git (branches, protection, Conventional Commits)
- Phase 3 (4-5h) : Création du pipeline CI complet (lint, typecheck, security, tests)
- Phase 4 (2h) : Configuration des pre-commit hooks
- Phase 5 (2h) : Build et push Docker vers GHCR
- Phase 6 (3h) : Semantic Release automatique
- Phase 7 - Bonus (2h) : Documentation MkDocs sur GitHub Pages
- Phase 8 - Bonus (4-6h) : Déploiement continu sur Azure

RESSOURCES FOURNIES :
- Documentation officielle des outils (liens directs)
- Vidéos tutorielles recommandées
- Templates de configuration à compléter
- Diagrammes d'architecture
- Exemples de code et workflows

TRAVAIL ATTENDU :
L'apprenant travaille en autonomie, crée des branches feature, soumet des Pull Requests, et documente ses choix techniques. Chaque phase inclut des questions de réflexion pour approfondir la compréhension.
```

---

## Modalités d'évaluation
> 1284/3000 caractères

```
L'évaluation s'effectue sur 4 niveaux de maîtrise progressifs :

NIVEAU FONDAMENTAL (Phases 0-3) :
- Veille technologique complète et documentée (VEILLE_CICD.md)
- Comparatif d'outils avec justifications (COMPARATIF_OUTILS.md)
- Stratégie Git avec branches protégées fonctionnelles
- Pipeline CI complète (lint, type check, security, tests)
- Utilisation correcte des Conventional Commits

NIVEAU INTERMÉDIAIRE (Phases 4-6) :
- Pre-commit hooks opérationnels
- Image Docker buildée et publiée sur GHCR
- Semantic release automatique fonctionnel
- Au moins 2 releases créées avec CHANGELOG généré
- Code nettoyé et conforme aux standards

NIVEAU AVANCÉ (Phase 7 - Bonus) :
- Documentation MkDocs générée automatiquement
- Déploiement sur GitHub Pages
- Docstrings complètes au format Google

NIVEAU EXPERT (Phase 8 - Bonus) :
- Déploiement automatique sur Azure Container Apps
- Base de données Cosmos DB configurée
- Monitoring avec Application Insights
- Health checks automatiques fonctionnels

L'évaluation intègre une analyse réflexive sur les choix techniques effectués.
```

---

## Livrables attendus
> 1647/3000 caractères

```
DOCUMENTS DE VEILLE :
- VEILLE_CICD.md : Réponses documentées sur CI/CD, uv, Semantic Release, MkDocs
- COMPARATIF_OUTILS.md : Tableaux comparatifs (linters, formatters, type checkers, security scanners) avec notes et justifications
- PROBLEMES_DETECTES.md : Liste d'au moins 20 problèmes identifiés dans le code initial

CONFIGURATION GIT :
- Branches main et develop créées et protégées
- Règles de protection configurées sur GitHub
- Historique de commits respectant Conventional Commits

FICHIERS CI/CD :
- .github/workflows/ci.yml : Pipeline CI (lint, typecheck, security, tests)
- .github/workflows/build.yml : Build et push Docker vers GHCR
- .github/workflows/release.yml : Semantic release automatique
- .pre-commit-config.yaml : Configuration pre-commit complète

CONFIGURATION PROJET :
- pyproject.toml enrichi (ruff, mypy, pytest, semantic-release)
- Dockerfile optimisé
- Code source corrigé (formatage, typage, sécurité)

LIVRABLES BONUS :
- mkdocs.yml et structure docs/ pour la documentation
- .github/workflows/docs.yml : Déploiement GitHub Pages
- .github/workflows/cd-azure.yml : Déploiement Azure
- Au moins 2 releases GitHub avec tags et CHANGELOG.md
```

---

## Critères de performance
> 1456/3000 caractères

```
QUALITÉ DU CODE :
- Aucune erreur Ruff (linting et formatage)
- Aucune erreur Mypy (typage strict)
- Aucun secret détecté par Bandit ou detect-secrets
- Couverture de tests suffisante
- Imports organisés et code mort supprimé

PIPELINE CI/CD :
- Tous les jobs CI passent (lint, typecheck, security, tests)
- Pre-commit bloque les commits non conformes
- CI s'exécute automatiquement sur push/PR
- Temps d'exécution optimisé (cache uv activé)

GESTION DES VERSIONS :
- Commits respectant strictement Conventional Commits
- Versionnage sémantique automatique fonctionnel
- CHANGELOG généré automatiquement
- Releases GitHub créées avec tags appropriés

CONTAINERISATION :
- Image Docker build et run localement sans erreur
- Image publiée sur GHCR avec tags corrects
- Image pullable et fonctionnelle depuis GHCR

DOCUMENTATION (Bonus) :
- Documentation générée sans erreur
- Accessible sur GitHub Pages
- Docstrings au format Google

DÉPLOIEMENT AZURE (Bonus) :
- Application accessible sur URL publique
- Health check retourne 200 OK
- Variables d'environnement sécurisées
```
