# Brief Monitoring V3

---

## Titre

Monitoring & Observabilité : Prometheus, Grafana et Stress Testing avec FastAPI

---

## Description rapide

Formation complète de 14 heures pour maîtriser le monitoring et l'observabilité d'une application FastAPI en production. Les apprenants instrumentent leur API avec des métriques Prometheus variées (counters CRUD, gauges, histograms de prix, erreurs par type), déploient une stack Docker complète (Prometheus, Grafana, node-exporter, cAdvisor), maîtrisent le langage PromQL à travers des exercices progressifs, créent des dashboards Grafana professionnels couvrant l'application, l'infrastructure et les containers, puis effectuent des tests de charge avec Locust pour identifier les goulots d'étranglement. L'approche est mixte : exemples guidés avec annotations pédagogiques + exercices autonomes pour développer l'autonomie.

---

## Contexte

En production, une application sans monitoring est un avion sans tableau de bord : tout semble fonctionner jusqu'au crash. L'observabilité permet de comprendre l'état interne d'un système à partir de ses sorties (métriques, logs, traces) et d'anticiper les problèmes avant qu'ils n'impactent les utilisateurs.

Cette formation s'appuie sur votre API Items FastAPI existante (CRUD basique avec PostgreSQL). Vous allez la transformer en application observable en ajoutant 3 couches de visibilité :

**1. Métriques applicatives (instrumentation Python)**
Vous instrumentez votre code avec la librairie prometheus_client pour exposer des métriques métier :
- Counters CRUD : items_created_total, items_read_total, items_updated_total, items_deleted_total
- Gauge items_total : nombre d'items actuellement en base (monte au create, descend au delete)
- Histogram items_price_histogram : distribution des prix des items créés (buckets adaptés : 1€ à 1000€)
- Counter avec labels http_errors_total : erreurs segmentées par type (validation, not_found, server_error)
- Gauge app_uptime_seconds : temps depuis le démarrage
- Histogram db_query_duration_seconds : latence des requêtes DB
Le prometheus-fastapi-instrumentator ajoute automatiquement les métriques HTTP standards (requêtes, latences, codes de statut).

**2. Métriques infrastructure (exporters)**
Deux exporters enrichissent considérablement les données disponibles :
- node-exporter (port 9100) : expose ~100+ métriques système — CPU par mode (user, system, idle, iowait), RAM (totale, disponible, cache), disque (espace, I/O), réseau (octets entrants/sortants, paquets, erreurs), load average
- cAdvisor (port 8080) : expose les métriques par container Docker — CPU, mémoire (usage vs limite), réseau et I/O disque pour chaque container de la stack

**3. Visualisation et analyse (Grafana + Locust)**
Les métriques sont collectées par Prometheus (scraping toutes les 15s) et visualisées dans Grafana. L'outil Locust génère de la charge réaliste pour observer le comportement sous stress.

**Architecture technique complète :**
- FastAPI (port 8000) : API avec endpoint /metrics
- PostgreSQL : base de données
- Prometheus (port 9090) : collecte et stockage time-series, 4 jobs de scraping (prometheus, fastapi, node-exporter, cadvisor)
- Grafana (port 3000) : dashboards et visualisations
- node-exporter (port 9100) : métriques système hôte
- cAdvisor (port 8080) : métriques containers Docker
- Locust (port 8089) : génération de charge

Cette stack représente un setup de monitoring réaliste en production. Les apprenants découvrent l'ensemble de la chaîne : de l'instrumentation du code à l'interprétation des dashboards sous charge.

**Prérequis :**
- API Items FastAPI fonctionnelle (CRUD + PostgreSQL)
- Docker et Docker Compose installés
- Bases Python et FastAPI maîtrisées

---

## Modalités pédagogiques

La formation suit une progression en 6 phases sur 2 jours, alternant présentations guidées et exercices autonomes.

**Phase 0 — Veille & Concepts (1h30)**
Approche mixte lecture/recherche. Les apprenants étudient les fondamentaux : différence monitoring vs observabilité, les 3 piliers (métriques, logs, traces), l'architecture pull de Prometheus, les 4 types de métriques (Counter, Gauge, Histogram, Summary), et le rôle de Grafana. Recherche complémentaire sur PromQL et les bonnes pratiques de nommage. Quiz collectif de validation.

**Phase 1 — Instrumentation FastAPI (1h30)**
Présentation guidée du code d'instrumentation avec annotations pédagogiques détaillées. Le formateur explique chaque métrique du fichier metrics.py : pourquoi un Counter pour les opérations CRUD (ne fait que monter), pourquoi un Gauge pour items_total (reflète l'état courant), pourquoi un Histogram pour les prix (distribution, pas juste une moyenne), pourquoi des labels sur http_errors_total (segmentation sans multiplication des métriques). Démonstration des routes instrumentées : le pattern try/except avec comptage des erreurs par type, l'incrémentation du gauge au create et sa décrémentation au delete, l'observation du prix dans l'histogram. Configuration du endpoint /metrics avec prometheus-fastapi-instrumentator. Exercice autonome : adapter le code à sa propre API, ajouter une métrique custom métier.

**Phase 2 — Setup Prometheus & PromQL (2h)**
Déploiement guidé de la stack Docker : docker-compose.yml avec 6 services (api, db, prometheus, node-exporter, cadvisor, grafana). Configuration de prometheus.yml avec 4 jobs de scraping. Vérification des targets dans l'interface Prometheus. Atelier PromQL avec requêtes essentielles : métriques brutes, rate(), agrégations by(), histogram_quantile(), taux d'erreur. Exercices autonomes progressifs en 6 niveaux :
- Basiques : compteurs, taux, totaux HTTP
- Agrégations : opérations CRUD combinées, requêtes par méthode
- Percentiles : latence P50/P95/P99
- Infrastructure : CPU%, RAM Go, disque%, réseau Mo/s (node-exporter)
- Containers : CPU et RAM par container (cAdvisor)
- Métriques custom : items_total, prix médian, erreurs par type

Cheat sheet PromQL fournie avec tables de référence pour les fonctions principales, node-exporter et cAdvisor.

**Phase 3a — Premier Dashboard Grafana (1h30)**
Setup guidé de Grafana + datasource Prometheus. Création pas-à-pas du dashboard "HTTP Overview" avec 6 panels :
1. Requêtes/seconde (Time series)
2. Latence P95 (Time series)
3. Taux d'erreur avec seuils colorés (Stat)
4. Requêtes en cours (Gauge)
5. CPU Usage % depuis node-exporter (Time series)
6. Memory Usage % depuis node-exporter (Gauge)

**Phase 3b — Dashboards Personnalisés (3h)**
Phase 100% autonome et créative. Planification : analyse du besoin, choix du public cible, sélection des métriques. Création de dashboards avec contraintes minimales : 6+ panels, 3+ types de visualisation, au moins 1 métrique custom et 1 panel infrastructure. Suggestions de métriques fournies dans 5 catégories : HTTP, Business (avec items_total, prix histogram, erreurs par type), Database, Infrastructure (node-exporter : CPU, RAM, disque, réseau, load), Containers (cAdvisor : CPU, mémoire, réseau, I/O par container). Approches possibles : SRE, Product, Performance, Overview, RED.

**Phase 4 — Stress Testing Locust (2h) — Optionnel**
Script Locust fourni avec 2 profils utilisateur (CRUD complet + lecture seule). 3 paliers de charge guidés puis autonomes (20, 100, 200 users). Observation en temps réel dans Grafana. Identification du point de rupture.

**Phase 5 — Analyse & Optimisation (1h15) — Optionnel**
Rapport de stress test, présentation par groupe, propositions d'optimisation (pool DB, cache, SQL, scaling). Synthèse sur la méthodologie RED (Rate, Errors, Duration) et les seuils de production.

**Phase 6 — Alerting Prometheus (2h) — Bonus**
Règles d'alerte YAML (HighErrorRate, HighLatency). Configuration Alertmanager.

---

## Modalités d'évaluation

L'évaluation est continue et basée sur la validation progressive des livrables à chaque phase.

**Évaluation par phase :**

Phase 0 : Quiz collectif (5 questions) avec minimum 80% de réussite. Vérification du document VEILLE_OBSERVABILITE.md couvrant les réponses aux questions de recherche sur PromQL et les bonnes pratiques.

Phase 1 : Vérification technique — endpoint /metrics accessible et retournant des métriques, au moins 1 métrique custom visible, au moins 1 route instrumentée avec timer et compteur.

Phase 2 : Vérification technique — Prometheus accessible sur :9090, les 3 targets (fastapi, node-exporter, cadvisor) en statut UP, métriques système et containers visibles. Exercices PromQL réussis (6 exercices couvrant les requêtes basiques, agrégations, percentiles, infrastructure, containers et métriques custom).

Phase 3a : Dashboard "HTTP Overview" créé avec 6 panels fonctionnels affichant des données en temps réel, incluant les panels infra CPU et RAM via node-exporter.

Phase 3b : Dashboard(s) personnalisé(s) respectant les contraintes minimales — 6+ panels, 3+ types de visualisation, 1+ métrique custom, 1+ panel infrastructure. Document DASHBOARD_DESIGN.md avec justification des choix.

Phase 4 (optionnel) : 3 tests de charge effectués (20, 100, 200 users), métriques relevées dans un tableau comparatif, point de rupture identifié avec symptôme et métrique critique.

Phase 5 (optionnel) : Rapport RAPPORT_STRESS_TEST.md complété, 3 optimisations proposées avec impact attendu et complexité.

**3 niveaux de réussite :**
- Fondamental (obligatoire) : concepts compris, app instrumentée, Prometheus déployé, 2+ dashboards, tests Locust exécutés
- Intermédiaire (attendu) : 4 dashboards complets, maîtrise PromQL, exercices autonomes réussis, point de rupture identifié, optimisations proposées
- Avancé (bonus) : variables dans dashboards, alerting configuré, optimisations implémentées et testées

---

## Livrables attendus

repo github (dans le repo gituhb ( minimum : docker compose + json (des dashboards) + capture d'écrans des dashboards

---

## Critères de performance

**Instrumentation (Phase 1) :**
- Les métriques sont correctement typées : Counter pour les événements cumulatifs, Gauge pour les valeurs instantanées, Histogram pour les distributions
- Le gauge items_total reflète fidèlement le nombre d'items en base (inc au create, dec au delete)
- Les erreurs sont segmentées par type via labels (validation, not_found, server_error) et non par métriques séparées
- L'histogram de prix utilise des buckets adaptés au domaine métier
- Les compteurs sont incrémentés APRÈS le succès de l'opération, pas avant

**Infrastructure (Phase 2) :**
- Les 4 targets Prometheus sont en statut UP (fastapi, node-exporter, cadvisor, prometheus)
- Les requêtes PromQL sont syntaxiquement correctes et retournent des résultats cohérents
- L'apprenant sait écrire des requêtes pour les 3 sources : métriques applicatives, node-exporter et cAdvisor

**Dashboards (Phase 3) :**
- Chaque panel a un titre clair, des unités appropriées (req/s, %, secondes, Mo) et des seuils de couleur pertinents
- Le dashboard couvre au moins 3 niveaux : applicatif (HTTP, CRUD), infrastructure (CPU, RAM) et business (items_total, prix)
- Les visualisations sont adaptées aux données : Time series pour les tendances, Stat/Gauge pour les valeurs instantanées, Heatmap pour les distributions
- Le design suit les bonnes pratiques : métriques critiques en haut, regroupement logique, pas de surcharge visuelle

