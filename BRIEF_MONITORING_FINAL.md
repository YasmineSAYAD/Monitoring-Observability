# 📊 Brief Monitoring & Observabilité - Formation Complète

![Monitoring](https://img.shields.io/badge/Monitoring-Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Visualization](https://img.shields.io/badge/Visualization-Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.121+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Formation](https://img.shields.io/badge/Durée-14h-blue?style=for-the-badge)
![Approche](https://img.shields.io/badge/Approche-Mixte-purple?style=for-the-badge)

---

## 📖 Introduction

Formation complète de **14 heures** pour maîtriser le monitoring et l'observabilité avec **Prometheus** et **Grafana**.

> ✅ **Approche mixte** : Exemples de code et configurations détaillés avec explications + exercices pratiques autonomes pour approfondir

> 🎯 **Public** : Développeurs souhaitant mettre en place du monitoring en production

---

![Monitoring Dashboard](images/monitoring.png)

---

## 🎯 Objectifs d'apprentissage

À la fin de cette formation, vous serez capable de :

- [ ] 🔍 Comprendre les concepts clés de l'observabilité (métriques, logs, traces)
- [ ] 📊 Instrumenter une application FastAPI avec des métriques Prometheus
- [ ] 📈 Déployer et configurer Prometheus avec Docker Compose
- [ ] 🔍 Maîtriser le langage de requête PromQL
- [ ] 📉 Créer des dashboards Grafana professionnels
- [ ] 💥 Effectuer des tests de charge avec Locust
- [ ] 📐 Lire et interpréter les métriques de performance
- [ ] 🎯 Identifier les goulots d'étranglement et optimiser
- [ ] 🚨 Mettre en place des alertes (bonus)

---

## 🏗️ Architecture de la solution

```
┌─────────────────────────────────────────────┐
│        APPLICATION FASTAPI                  │
│  ✓ Métriques instrumentées                  │
│  ✓ Endpoint /metrics exposé                 │
└──────────────┬──────────────────────────────┘
               │ HTTP GET /metrics (toutes les 15s)
               ▼
┌─────────────────────────────────────────────┐
│           PROMETHEUS                        │
│  ✓ Collecte et stocke les métriques         │
│  ✓ Base de données time-series              │
│  ✓ Langage de requête PromQL                │
└──────────────┬──────────────────────────────┘
               │ Datasource Prometheus
               ▼
┌─────────────────────────────────────────────┐
│           GRAFANA                           │
│  ✓ Dashboards de visualisation              │
│  ✓ Graphiques temps réel                    │
│  ✓ Alertes visuelles                        │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│           LOCUST                            │
│  ✓ Génération de charge                     │
│  ✓ Tests de performance                     │
└─────────────────────────────────────────────┘
```

### 🎥 Vidéo de présentation


Pour mieux comprendre cette architecture et son fonctionnement, regardez cette vidéo explicative :

📺 **[Cliquez ICI --> Prometheus & Grafana](https://youtu.be/TQQhm_kNuQY)**

---

## 📚 Phase 0 : Veille & Concepts d'Observabilité (1h30)

![Durée](https://img.shields.io/badge/Durée-1h30-blue)
![Type](https://img.shields.io/badge/Type-Mixte-purple)
![Difficulté](https://img.shields.io/badge/Difficulté-⭐_Facile-brightgreen)

### 🎯 Objectif

Comprendre les concepts fondamentaux de l'observabilité à travers une présentation guidée et des recherches complémentaires ciblées.

### 📋 Déroulement (1h30)

#### **00:00-00:45 | Partie 1 : Lecture autonome des concepts fondamentaux**

**📖 À lire attentivement** - Prenez des notes sur les points importants

---

### 1️⃣ Monitoring vs Observabilité : Quelle différence ?

**Scénario** : Votre application en production ralentit soudainement.

| Approche            | Monitoring                            | Observabilité                            |
| ------------------- | ------------------------------------- | ---------------------------------------- |
| **Question posée**  | "L'app est-elle up ?"                 | "**Pourquoi** cette requête est lente ?" |
| **Réponse obtenue** | "Oui, mais latence élevée"            | "DB surcharge + requête N+1 sur /users"  |
| **Type d'action**   | ⚠️ Réactif - Attendre une alerte       | ✅ Proactif - Investiguer librement       |
| **Outils**          | Dashboards fixes, alertes prédéfinies | Exploration ad-hoc, corrélation          |
| **Métaphore**       | Tableau de bord de voiture            | Boîte noire d'avion                      |

**💡 En résumé** :
- **Monitoring** = Savoir **QUAND** ça casse (alertes)
- **Observabilité** = Comprendre **POURQUOI** ça casse (investigation)

> ⚠️ **Important** : Le monitoring est un **sous-ensemble** de l'observabilité. On ne peut pas avoir de l'observabilité sans monitoring, mais on peut avoir du monitoring sans observabilité complète.

---

### 2️⃣ Les 3 piliers de l'observabilité

Pour rendre un système observable, on combine **3 types de données** :

#### 📊 **Pilier 1 : MÉTRIQUES**

**Définition** : Données numériques agrégées dans le temps

**Exemples concrets** :
```
- CPU: 45%
- Mémoire RAM: 2.3 GB / 8 GB
- Requêtes HTTP/seconde: 1250 req/s
- Latence P95: 120ms
- Erreurs 5xx: 12 en 5 minutes
```

**Avantages** :
- ✅ Léger (peu de stockage)
- ✅ Permet des tendances et graphiques
- ✅ Alertes faciles à configurer

**Cas d'usage** : Dashboards temps réel, alerting, capacity planning

---

#### 📝 **Pilier 2 : LOGS**

**Définition** : Événements textuels horodatés

**Exemple concret** :
```
2025-01-15 10:23:45 INFO  [api] User 42 logged in successfully
2025-01-15 10:23:47 ERROR [db]  Connection pool exhausted (timeout: 30s)
2025-01-15 10:23:48 WARN  [api] Retry attempt 1/3 for user 42
```

**Avantages** :
- ✅ Contexte détaillé (stack traces, user IDs)
- ✅ Debugging précis

**Cas d'usage** : Investigation d'erreurs, audit, debugging

---

#### 🔍 **Pilier 3 : TRACES**

**Définition** : Suivi d'une requête à travers plusieurs services

**Exemple concret** :
```
Request ID: #12345 | Total: 177ms
├─ API Gateway      →  5ms
├─ Auth Service     → 12ms
├─ Items API        → 50ms
│  ├─ DB Query      → 120ms  ⚠️ SLOW!
│  └─ Cache Check   →   5ms
└─ Response         →  5ms
```

**Avantages** :
- ✅ Vue end-to-end d'une requête
- ✅ Identifie le service lent dans une chaîne

**Cas d'usage** : Microservices, distributed systems

---

> 💡 **Focus de cette formation** : Nous nous concentrons sur les **MÉTRIQUES** (le pilier le plus important pour commencer et le plus facile à mettre en place).

---

### 3️⃣ Qu'est-ce que Prometheus ?

**Prometheus** est une base de données time-series open-source spécialisée dans le stockage de métriques.

#### Architecture : Pull vs Push

```
┌─────────────────────────────────────┐
│  ARCHITECTURE PULL (Prometheus)     │
└─────────────────────────────────────┘

    Application                Prometheus
    ┌─────────┐               ┌──────────┐
    │  /metrics│◄──── GET ────┤ Scraper  │
    │ endpoint │               │ (toutes  │
    │          │               │ les 15s) │
    └─────────┘               └──────────┘

    ✅ Prometheus contrôle la fréquence
    ✅ L'app n'a pas besoin de connaître Prometheus
    ✅ Détection automatique si l'app est down
```

vs

```
┌─────────────────────────────────────┐
│  ARCHITECTURE PUSH (ex: StatsD)     │
└─────────────────────────────────────┘

    Application                Collector
    ┌─────────┐               ┌──────────┐
    │ Envoie  │─── PUSH ─────►│ Reçoit   │
    │ metrics │               │ metrics  │
    │         │               │          │
    └─────────┘               └──────────┘

    ❌ L'app doit connaître le collector
    ❌ Peut surcharger le réseau
```

#### Caractéristiques de Prometheus

| Caractéristique        | Détail                             |
| ---------------------- | ---------------------------------- |
| 🗄️ **Base time-series** | Stocke (timestamp, valeur)         |
| ⬅️ **Pull HTTP**        | Scrape `/metrics` toutes les 15s   |
| 📊 **Format texte**     | Simple, lisible par un humain      |
| 🔍 **PromQL**           | Langage de requête puissant        |
| ⏱️ **Rétention**        | Configurable (par défaut 15 jours) |
| 💾 **Stockage local**   | Pas de dépendance externe          |

---

### 4️⃣ Les 4 types de métriques Prometheus

#### 📊 **Counter** : Valeur qui ne fait qu'augmenter

**Comportement** : ⬆️ Ne peut jamais diminuer (sauf redémarrage)

**Exemple** :
```python
http_requests_total{method="GET", status="200"} 45678
```

**Cas d'usage** :
- Nombre total de requêtes HTTP
- Nombre d'erreurs
- Nombre d'utilisateurs inscrits

**⚠️ Important** : Pour avoir un taux/s, utiliser `rate()` dans PromQL
```promql
rate(http_requests_total[5m])  # Requêtes par seconde sur 5 min
```

---

#### 📈 **Gauge** : Valeur qui peut monter ET descendre

**Comportement** : ⬆️⬇️ Mesure instantanée

**Exemple** :
```python
memory_usage_bytes 2684354560  # 2.5 GB
cpu_usage_percent 45.2
active_connections 127
```

**Cas d'usage** :
- Utilisation mémoire/CPU
- Nombre de connexions actives
- Température serveur
- File d'attente (queue size)

**⚠️ Important** : Utiliser directement la valeur, pas besoin de `rate()`

---

#### ⏱️ **Histogram** : Distribution de valeurs avec buckets

**Comportement** : 📊 Répartit les valeurs dans des intervalles (buckets)

**Exemple** :
```python
http_request_duration_seconds_bucket{le="0.1"} 8234    # < 100ms
http_request_duration_seconds_bucket{le="0.5"} 9876    # < 500ms
http_request_duration_seconds_bucket{le="1.0"} 10234   # < 1s
http_request_duration_seconds_bucket{le="+Inf"} 10500  # Total
```

**Cas d'usage** :
- Latences HTTP
- Temps de requête DB
- Tailles de réponses

**💡 Permet de calculer les percentiles** :
```promql
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))
# = P95 : 95% des requêtes sont plus rapides que cette valeur
```

---

#### 📉 **Summary** : Similaire à Histogram mais avec percentiles précalculés

**Comportement** : 📈 Calcule P50, P90, P95, P99 côté application

**Exemple** :
```python
http_request_duration_seconds{quantile="0.5"} 0.12   # P50 (médiane)
http_request_duration_seconds{quantile="0.95"} 0.45  # P95
http_request_duration_seconds{quantile="0.99"} 1.2   # P99
```

**Différence avec Histogram** :

|             | Histogram                          | Summary               |
| ----------- | ---------------------------------- | --------------------- |
| Calcul      | Côté Prometheus (PromQL)           | Côté application      |
| Flexibilité | ✅ Peut changer les percentiles     | ❌ Percentiles fixes   |
| Performance | ✅ Léger côté app                   | ❌ Plus lourd côté app |
| Agrégation  | ✅ Peut agréger plusieurs instances | ❌ Difficile à agréger |

**💡 Recommandation** : Préférer **Histogram** en général

---

### 5️⃣ Découverte de Grafana

**Grafana** est un outil de visualisation qui transforme vos métriques en dashboards interactifs.

#### Rôle dans la stack

```
┌──────────────┐
│  Prometheus  │  Collecte et stocke les métriques
└──────┬───────┘
       │ Datasource
       ▼
┌──────────────┐
│   Grafana    │  Visualise les métriques
└──────────────┘
```

#### Fonctionnalités principales

| Fonctionnalité       | Description                                  |
| -------------------- | -------------------------------------------- |
| 📊 **Dashboards**     | Tableaux de bord personnalisables            |
| 🔌 **Multi-sources**  | Prometheus, InfluxDB, MySQL, etc.            |
| 📈 **Visualisations** | Time series, Gauge, Stat, Heatmap, Pie chart |
| 🚨 **Alerting**       | Notifications Slack, Email, etc.             |
| 👥 **Collaboration**  | Partage de dashboards                        |

#### Types de visualisations

```
📈 TIME SERIES
└─ Courbes temporelles (ex: CPU over time)

📊 GAUGE
└─ Jauge visuelle (ex: Disk usage: 45%)

🔢 STAT
└─ Valeur numérique avec seuils de couleur

🔥 HEATMAP
└─ Carte de chaleur (ex: distribution latences)

🥧 PIE CHART
└─ Camembert (ex: répartition requêtes par endpoint)
```

---

### ✅ Auto-évaluation

**Avant de passer à la suite, vérifiez que vous comprenez** :

- [ ] La différence entre monitoring et observabilité
- [ ] Les 3 piliers de l'observabilité
- [ ] Pourquoi Prometheus utilise le Pull
- [ ] Quand utiliser Counter vs Gauge vs Histogram
- [ ] Le rôle de Grafana dans la stack

**Si un point n'est pas clair, relisez la section correspondante** !

---

#### **00:45-01:15 | Partie 2 : Recherche complémentaire ciblée (30min)**

**Objectif** : Approfondir les concepts avec des ressources de qualité.

**Mission 1 : Comprendre PromQL (15min)**

**Ressources recommandées** :
- 📖 [Prometheus - Query Basics](https://prometheus.io/docs/prometheus/latest/querying/basics/)
- 🎥 [YouTube : "PromQL tutorial"](https://www.youtube.com/watch?v=RC1ivt-ZN_U)

**Questions à explorer** :
1. Quelle est la différence entre `rate()` et `increase()` ?
2. Comment filtrer des métriques par label ?
3. Que fait la fonction `histogram_quantile()` ?

**Livrable** : Document `VEILLE_OBSERVABILITE.md` avec vos réponses

**💡 Astuce** : Testez les exemples dans la démo Prometheus : https://demo.promlabs.com/

---

**Mission 2 : Best Practices Prometheus (15min)**

**Ressources** :
- 📖 [Prometheus Best Practices - Naming](https://prometheus.io/docs/practices/naming/)
- 📖 [Grafana Dashboard Best Practices](https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/best-practices/)

**Questions** :
1. Comment nommer correctement une métrique ?
2. Quand utiliser des labels vs créer plusieurs métriques ?
3. Quels sont les dashboards anti-patterns à éviter ?

**Livrable** : Document `VEILLE_OBSERVABILITE.md` avec vos réponses

---

#### **01:15-01:30 | Partie 3 : Quiz et discussion collective (15min)**

**Quiz rapide (5 questions)** :

1. ❓ Monitoring vs Observabilité : quelle différence ?
2. ❓ Citez les 3 piliers de l'observabilité
3. ❓ Quel type de métrique pour compter les requêtes HTTP ?
4. ❓ Quel type de métrique pour l'utilisation RAM actuelle ?
5. ❓ Que signifie P95 ?

**Discussion collective** :
- Partage des découvertes de la recherche
- Questions/réponses sur les concepts

---

### 📚 Ressources pour aller plus loin (optionnelles)

- 📖 [Red Hat - Qu'est-ce que l'observabilité ?](https://www.redhat.com/fr/topics/devops/what-is-observability)
- 📖 [OpenTelemetry - Observability Primer](https://opentelemetry.io/docs/concepts/observability-primer/)
- 📄 **Documentation** : `images/Observabilité_Performance_et_Stress_Testing.pdf` (si disponible)
- 📕 **Livre** : "Observability Engineering" - Charity Majors (O'Reilly)

---

### 📦 Livrables Phase 0

**Livrable** : Document `VEILLE_OBSERVABILITE.md` avec vos réponses

---

### ✅ Validation Phase 0

- [ ] Document `VEILLE_OBSERVABILITE.md` complété avec toutes les réponses
- [ ] Concepts d'observabilité compris (3 piliers)
- [ ] Différence monitoring vs observabilité maîtrisée
- [ ] Types de métriques Prometheus connus (Counter, Gauge, Histogram, Summary)
- [ ] Bases de PromQL comprises
- [ ] Rôle de Prometheus et Grafana clair
- [ ] Quiz réussi (80% minimum)

---

## 📊 Phase 1 : Instrumentation FastAPI (1h30)

![Durée](https://img.shields.io/badge/Durée-1h30-blue)
![Type](https://img.shields.io/badge/Type-Guidé_+_Exercices-purple)
![Difficulté](https://img.shields.io/badge/Difficulté-⭐⭐_Moyen-yellow)

### 🎯 Objectif

Instrumenter votre application FastAPI pour exposer des métriques Prometheus.

### 📁 Approche pédagogique

- **Exemples de code** : Fichiers complets avec annotations détaillées à créer
- **Exercices** : Vous devez adapter le code à votre propre API

### 🎓 Déroulement (1h30)

#### **00:00-00:30 | Présentation du code de métriques**

**📄 Exemple de code : `app/monitoring/metrics.py`**

```python
"""
Module de métriques Prometheus pour l'API Items
EXEMPLE DE CODE avec annotations pédagogiques
"""

from prometheus_client import Counter, Histogram, Gauge, Info
import time

# ℹ️ INFO : Informations statiques sur l'application
app_info = Info(
    'fastapi_app_info',
    'Information about the FastAPI application'
)

# 📊 COUNTER : Compteurs pour les opérations CRUD
items_created_total = Counter(
    'items_created_total',
    'Nombre total d\'items créés depuis le démarrage'
)

items_read_total = Counter(
    'items_read_total',
    'Nombre total de lectures d\'items'
)

items_updated_total = Counter(
    'items_updated_total',
    'Nombre total d\'items mis à jour'
)

items_deleted_total = Counter(
    'items_deleted_total',
    'Nombre total d\'items supprimés'
)

# 📈 GAUGE : Valeur instantanée (monte ET descend)
db_connection_pool_size = Gauge(
    'db_connection_pool_size',
    'Taille actuelle du pool de connexions DB'
)

items_total = Gauge(
    'items_total',
    'Nombre d\'items actuellement en base de données'
)

app_uptime_seconds = Gauge(
    'app_uptime_seconds',
    'Temps écoulé depuis le démarrage de l\'application (secondes)'
)

# ⏱️ HISTOGRAM : Distribution de valeurs avec buckets
db_query_duration_seconds = Histogram(
    'db_query_duration_seconds',
    'Durée des requêtes base de données (secondes)',
    buckets=[0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0]
)

items_price_histogram = Histogram(
    'items_price_histogram',
    'Distribution des prix des items créés (euros)',
    buckets=[1, 5, 10, 25, 50, 100, 250, 500, 1000]
)

# ❌ COUNTER avec labels : Erreurs par type
http_errors_total = Counter(
    'http_errors_total',
    'Nombre total d\'erreurs HTTP par type',
    ['type']  # Labels : validation, not_found, server_error
)

# 🎯 Context Manager pour mesurer automatiquement les durées
class DatabaseQueryTimer:
    """Context manager pour mesurer le temps d'exécution d'une requête DB."""

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start_time
        db_query_duration_seconds.observe(duration)
```

**Explications** :
- **Counter** : Pour compter des événements (créations, lectures, etc.) — ne fait que monter
- **Counter avec labels** : Même chose mais segmenté par catégorie (`http_errors_total` par type d'erreur)
- **Gauge** : Pour des valeurs qui montent et descendent (items en base, connexions, uptime)
- **Histogram** : Pour mesurer des distributions (latences, mais aussi prix !)
- **Buckets** : Intervalles de mesure adaptés au contexte (ms pour les latences, € pour les prix)

---

#### **00:30-00:50 | Routes instrumentées**

**📄 Exemple de code : `app/routes/items.py`**

```python
from app.monitoring.metrics import (
    items_created_total,
    items_read_total,
    items_updated_total,
    items_deleted_total,
    items_total,
    items_price_histogram,
    http_errors_total,
    DatabaseQueryTimer
)
from fastapi import HTTPException

@router.post("/", response_model=ItemResponse, status_code=201)
def create_item(item: ItemCreate, db: Session = Depends(get_session)):
    """Créer un nouvel item."""
    try:
        # 📊 Mesurer la durée de la requête DB
        with DatabaseQueryTimer():
            new_item = ItemService.create(db, item)

        # 📊 Incrémenter le compteur APRÈS succès
        items_created_total.inc()
        # 📈 Mettre à jour le gauge (monte au create)
        items_total.inc()
        # 📊 Observer le prix dans l'histogram
        items_price_histogram.observe(item.price)

        return new_item
    except ValueError:
        http_errors_total.labels(type='validation').inc()
        raise HTTPException(status_code=422, detail="Données invalides")

@router.get("/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_session)):
    """Récupérer un item par ID."""
    with DatabaseQueryTimer():
        item = ItemService.get_by_id(db, item_id)

    if not item:
        http_errors_total.labels(type='not_found').inc()
        raise HTTPException(status_code=404, detail="Item non trouvé")

    items_read_total.inc()
    return item

@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_session)):
    """Supprimer un item."""
    with DatabaseQueryTimer():
        deleted = ItemService.delete(db, item_id)

    if not deleted:
        http_errors_total.labels(type='not_found').inc()
        raise HTTPException(status_code=404, detail="Item non trouvé")

    items_deleted_total.inc()
    # 📉 Mettre à jour le gauge (descend au delete)
    items_total.dec()
```

**Points clés** :
- ✅ Mesurer AVANT de compter
- ✅ Incrémenter APRÈS succès
- ✅ Un compteur par opération
- ✅ Le Gauge `items_total` monte (.inc) au create et descend (.dec) au delete
- ✅ L'Histogram `items_price_histogram` observe chaque prix créé
- ✅ Les erreurs sont catégorisées par label `type` (validation, not_found)

---

#### **00:50-01:10 | Configuration du endpoint /metrics**

**📄 Exemple de code : `app/main.py`**

```python
from prometheus_fastapi_instrumentator import Instrumentator
from app.monitoring.metrics import app_info

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    SQLModel.metadata.create_all(engine)

    app_info.info({
        'version': '1.0.0',
        'environment': 'development'
    })

    yield

app = FastAPI(title="Items API", lifespan=lifespan)

# 📊 Instrumentation automatique
instrumentator = Instrumentator(
    should_group_status_codes=False,
    should_ignore_untemplated=True,
    should_instrument_requests_inprogress=True,
    excluded_handlers=["/metrics"],
)

instrumentator.instrument(app).expose(app, endpoint="/metrics")

app.include_router(items_router)
```

---

#### **01:10-01:30 | 💪 EXERCICE AUTONOME**

**Mission** : Adapter le code à votre API

**Tâches** :

1. **Créer les fichiers de métriques** dans votre projet
   ```bash
   # Créer le répertoire si nécessaire
   mkdir -p app/monitoring
   # Créer le fichier metrics.py avec les exemples ci-dessus
   ```

2. **Ajouter une métrique custom** pour votre domaine métier
   - Exemple : `orders_total`, `users_registered_total`, etc.

3. **Instrumenter UNE de vos routes** (pas toutes)
   - Choisir une route importante
   - Ajouter le timer et le compteur

4. **Tester** :
   ```bash
   uvicorn app.main:app --reload
   curl http://localhost:8000/metrics
   ```

**Livrable** :
- [ ] Endpoint `/metrics` accessible
- [ ] Au moins 1 métrique custom visible
- [ ] Au moins 1 route instrumentée

---

### 📚 Ressources complémentaires

- 📖 [prometheus_client - Documentation](https://github.com/prometheus/client_python)
- 📖 [prometheus-fastapi-instrumentator](https://github.com/trallnag/prometheus-fastapi-instrumentator)

---

### ✅ Validation Phase 1

- [ ] Fichiers de métriques copiés et compris
- [ ] Application instrumentée
- [ ] Endpoint `/metrics` accessible
- [ ] Métriques custom créées et testées
- [ ] Comprend Counter vs Gauge vs Histogram

---

## 🔧 Phase 2 : Setup Prometheus & PromQL (2h)

![Durée](https://img.shields.io/badge/Durée-2h-blue)
![Type](https://img.shields.io/badge/Type-Guidé_+_Exercices-purple)
![Difficulté](https://img.shields.io/badge/Difficulté-⭐⭐_Moyen-yellow)

### 🎯 Objectifs

- Déployer Prometheus avec Docker Compose
- Configurer le scraping de l'application
- Maîtriser les requêtes PromQL de base

### 📁 Fichiers de configuration à créer

```
projet/
├── docker-compose.yml              ✅ Stack complète
├── Dockerfile                      ✅ Image FastAPI
└── prometheus/
    └── prometheus.yml              ✅ Configuration
```

---

### 🎓 Déroulement (2h)

#### **00:00-00:30 | Déploiement Docker**

**📄 Exemple de configuration : `docker-compose.yml`**

```yaml
version: '3.8'

services:
  # Application FastAPI
  api:
    build: .
    container_name: fastapi_app
    ports:
      - "8000:8000"
    networks:
      - monitoring
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/items_db
    depends_on:
      - db

  # Base de données PostgreSQL
  db:
    image: postgres:16-alpine
    container_name: postgres_db
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: items_db
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - monitoring

  # Prometheus
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--storage.tsdb.retention.time=30d'
    ports:
      - "9090:9090"
    networks:
      - monitoring

  # Node Exporter — métriques système (CPU, RAM, disque, réseau)
  node-exporter:
    image: prom/node-exporter:latest
    container_name: node_exporter
    ports:
      - "9100:9100"
    networks:
      - monitoring
    restart: unless-stopped

  # cAdvisor — métriques des containers Docker (CPU/RAM par container)
  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    container_name: cadvisor
    ports:
      - "8080:8080"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
    networks:
      - monitoring
    restart: unless-stopped

volumes:
  postgres_data:
  prometheus_data:

networks:
  monitoring:
    driver: bridge
```

> 💡 **node-exporter** expose ~100+ métriques système gratuitement. **cAdvisor** ajoute les métriques par container Docker. Ensemble, ils permettent de construire des dashboards d'infrastructure complets.

**📄 Exemple de configuration : `prometheus/prometheus.yml`**

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'fastapi'
    static_configs:
      - targets: ['api:8000']
    metrics_path: '/metrics'
    scrape_interval: 10s

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node-exporter:9100']

  - job_name: 'cadvisor'
    static_configs:
      - targets: ['cadvisor:8080']
```

**Lancement** :

```bash
# Créer les répertoires nécessaires
mkdir -p prometheus

# Créer les fichiers de configuration avec les exemples ci-dessus
# - docker-compose.yml
# - prometheus/prometheus.yml

# Lancer la stack
docker compose up -d

# Vérifier
docker compose ps
```

---

#### **00:30-00:50 | Exploration de Prometheus**

**Interface Prometheus** :

1. Ouvrir http://localhost:9090
2. Menu **Status** → **Targets**
   - Vérifier que `fastapi` est UP 🟢
3. Page **Graph**
   - Première requête : `items_created_total`

---

#### **00:50-01:30 | Atelier PromQL - Requêtes essentielles**

**Requêtes à maîtriser** :

```promql
# 1. Métrique brute
items_created_total

# 2. Taux par seconde (moyenne 5min)
rate(items_created_total[5m])

# 3. Total requêtes HTTP/s
sum(rate(http_requests_total[5m]))

# 4. Requêtes par endpoint
sum(rate(http_requests_total[5m])) by (handler)

# 5. Latence P95
histogram_quantile(0.95,
  rate(http_request_duration_seconds_bucket[5m])
)

# 6. Taux d'erreur en %
(sum(rate(http_requests_total{status=~"5.."}[5m])) /
 sum(rate(http_requests_total[5m]))) * 100
```

**Pour chaque requête** :
- Expliquer ce qu'elle fait
- Tester dans Prometheus
- Observer le résultat

---

#### **01:30-02:00 | 💪 EXERCICES AUTONOMES PromQL**

**Exercice 1 : Métriques basiques**

Écrire les requêtes PromQL pour :

1. Afficher le nombre total d'items supprimés
2. Calculer le taux de lecture par seconde (moyenne 5min)
3. Trouver le nombre total de requêtes HTTP reçues

**Exercice 2 : Agrégations**

1. Calculer le total de toutes les opérations CRUD
   ```promql
   sum(items_created_total + items_read_total + items_updated_total + items_deleted_total)
   ```

2. Afficher les requêtes HTTP par méthode (GET, POST, etc.)
   ```promql
   sum(rate(http_requests_total[5m])) by (method)
   ```

**Exercice 3 : Percentiles**

1. Calculer la latence P50 (médiane)
2. Calculer la latence P99
3. Calculer la latence P95 des requêtes DB

**Exercice 4 : Métriques Infrastructure (node-exporter)**

1. Afficher le pourcentage d'utilisation CPU
2. Afficher la RAM disponible en Go
3. Afficher l'espace disque utilisé en %
4. Calculer le trafic réseau entrant en Mo/s

**Exercice 5 : Métriques Containers (cAdvisor)**

1. Afficher l'utilisation CPU par container
2. Afficher la mémoire utilisée par container en Mo

**Exercice 6 : Nouvelles métriques custom**

1. Afficher le nombre actuel d'items en base (`items_total`)
2. Calculer le prix médian (P50) des items créés
3. Afficher le taux d'erreurs par type (validation vs not_found)

**Solutions à tester** :

<details>
<summary>Voir les solutions</summary>

```promql
# Exercice 1
items_deleted_total
rate(items_read_total[5m])
sum(http_requests_total)

# Exercice 2
sum(items_created_total + items_read_total + items_updated_total + items_deleted_total)
sum(rate(http_requests_total[5m])) by (method)

# Exercice 3
histogram_quantile(0.50, rate(http_request_duration_seconds_bucket[5m]))
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))
histogram_quantile(0.95, rate(db_query_duration_seconds_bucket[5m]))

# Exercice 4 — Infrastructure (node-exporter)
100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
node_memory_MemAvailable_bytes / 1024 / 1024 / 1024
100 - ((node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"}) * 100)
rate(node_network_receive_bytes_total[5m]) / 1024 / 1024

# Exercice 5 — Containers (cAdvisor)
rate(container_cpu_usage_seconds_total{name!=""}[5m])
container_memory_usage_bytes{name!=""} / 1024 / 1024

# Exercice 6 — Métriques custom
items_total
histogram_quantile(0.50, rate(items_price_histogram_bucket[5m]))
sum(rate(http_errors_total[5m])) by (type)
```

</details>

---

### 📚 Cheat Sheet PromQL

| Fonction               | Usage               | Exemple                         |
| ---------------------- | ------------------- | ------------------------------- |
| `rate()`               | Taux/seconde        | `rate(metric[5m])`              |
| `increase()`           | Augmentation totale | `increase(metric[1h])`          |
| `sum()`                | Somme               | `sum(metric)`                   |
| `avg()`                | Moyenne             | `avg(metric)`                   |
| `max()`                | Maximum             | `max(metric)`                   |
| `min()`                | Minimum             | `min(metric)`                   |
| `histogram_quantile()` | Percentile          | `histogram_quantile(0.95, ...)` |
| `by (label)`           | Regrouper           | `sum(...) by (endpoint)`        |
| `{label="value"}`      | Filtrer             | `metric{status="200"}`          |
| `{label=~"regex"}`     | Filtre regex        | `metric{status=~"5.."}`         |
| `irate()`              | Taux instantané     | `irate(metric[5m])`             |
| `absent()`             | Alerte si absent    | `absent(up{job="fastapi"})`     |

**Requêtes utiles node-exporter** :

| Métrique                  | Requête PromQL                                                                 |
| ------------------------- | ------------------------------------------------------------------------------ |
| CPU Usage %               | `100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)`             |
| RAM disponible (Go)       | `node_memory_MemAvailable_bytes / 1024^3`                                      |
| Disque utilisé (%)        | `100 - (node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"} * 100)` |
| Réseau entrant (Mo/s)     | `rate(node_network_receive_bytes_total[5m]) / 1024^2`                          |

**Requêtes utiles cAdvisor** :

| Métrique                  | Requête PromQL                                                     |
| ------------------------- | ------------------------------------------------------------------ |
| CPU par container         | `rate(container_cpu_usage_seconds_total{name!=""}[5m])`            |
| RAM par container (Mo)    | `container_memory_usage_bytes{name!=""} / 1024^2`                  |

---

### ✅ Validation Phase 2

- [ ] Prometheus déployé et accessible sur :9090
- [ ] Targets `fastapi`, `node-exporter` et `cadvisor` en statut UP
- [ ] Métriques de l'app visibles dans Prometheus
- [ ] Métriques système (node-exporter) et containers (cAdvisor) visibles
- [ ] Comprend et sait utiliser `rate()`, `sum()`, `by`
- [ ] Sait calculer des percentiles avec `histogram_quantile()`
- [ ] Exercices PromQL réussis

---

## 📊 Phase 3 : Dashboards Grafana (4h30 total)

![Durée](https://img.shields.io/badge/Durée-4h30-blue)
![Type](https://img.shields.io/badge/Type-TP_+_Exercices-purple)
![Difficulté](https://img.shields.io/badge/Difficulté-⭐⭐⭐_Difficile-orange)

### 📅 Répartition

- **Phase 3a** (Jour 1 - 1h30) : Premier dashboard guidé
- **Phase 3b** (Jour 2 - 3h) : 3 dashboards avec exercices

---

## 📈 Phase 3a : Premier Dashboard Grafana (Jour 1 - 1h30)

### 🎯 Objectif

Créer un dashboard Grafana fonctionnel pour les métriques HTTP.

### 🎓 Déroulement (1h30)

#### **00:00-00:20 | Setup Grafana**

**Ajouter Grafana au docker-compose.yml** :

```yaml
  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=admin
      - GF_USERS_ALLOW_SIGN_UP=false
    volumes:
      - grafana_data:/var/lib/grafana
    networks:
      - monitoring
    depends_on:
      - prometheus
```

**Lancer** :
```bash
docker compose up -d grafana
```

**Se connecter** :
- URL : http://localhost:3000
- Login : `admin` / `admin`

**Ajouter datasource Prometheus** :
1. Menu → Connections → Data sources
2. Add data source → Prometheus
3. URL : `http://prometheus:9090`
4. Save & Test ✅

---

#### **00:20-01:30 | Création du dashboard HTTP Overview (guidé)**

**Panel 1 : Requêtes par seconde** (Time series)

```
Query : sum(rate(http_requests_total[5m]))
Title : HTTP Requests per Second
Unit : req/s
```

**Panel 2 : Latence P95** (Time series)

```
Query : histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))
Title : Response Time P95
Unit : seconds (s)
```

**Panel 3 : Taux d'erreur** (Stat)

```
Query : (sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))) * 100
Title : Error Rate
Unit : Percent (0-100)
Thresholds : 🟢 0-1% | 🟡 1-5% | 🔴 >5%
```

**Panel 4 : Requêtes en cours** (Gauge)

```
Query : http_requests_inprogress
Title : Active Requests
Visualization : Gauge
```

**Panel 5 : CPU Usage** (Time series)

```
Query : 100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
Title : CPU Usage %
Unit : Percent (0-100)
Thresholds : 🟢 0-60% | 🟡 60-85% | 🔴 >85%
```

**Panel 6 : Memory Usage** (Gauge)

```
Query : (1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100
Title : Memory Usage %
Unit : Percent (0-100)
Visualization : Gauge
Thresholds : 🟢 0-70% | 🟡 70-90% | 🔴 >90%
```

**Sauvegarder** le dashboard : "HTTP Overview"

---

### ✅ Validation Phase 3a

- [ ] Grafana accessible
- [ ] Datasource Prometheus configurée
- [ ] Dashboard "HTTP Overview" créé avec 6 panels
- [ ] Panels affichent des données en temps réel
- [ ] Panels infra (CPU, RAM) fonctionnels via node-exporter

---

## 📊 Phase 3b : Création de Dashboard Personnalisé (Jour 2 - 3h)

### 🎯 Objectifs

**Créer VOTRE propre dashboard Grafana** en choisissant les métriques et visualisations qui vous semblent les plus pertinentes pour monitorer votre application.

> 🎨 **Philosophie** : Cette phase est **100% autonome et créative**. Il n'y a pas de "bonne" réponse unique. L'objectif est de développer votre capacité à concevoir des dashboards utiles et informatifs.

---

### 🎓 Déroulement (3h)

#### **Étape 1 : Analyse et planification (30min)**

**Mission** : Avant de créer quoi que ce soit, réfléchissez à ce que vous voulez monitorer.

**Questions à vous poser** :

1. **Quel est le but de mon dashboard ?**
   - Monitoring opérationnel (pour les équipes ops) ?
   - Métriques business (pour les product managers) ?
   - Performance technique (pour les développeurs) ?
   - Vue d'ensemble complète (pour tout le monde) ?

2. **Qui va utiliser ce dashboard ?**
   - Développeurs ? → Focus sur latence, erreurs, requêtes DB
   - Ops/SRE ? → Focus sur disponibilité, ressources, alertes
   - Business ? → Focus sur opérations, utilisateurs, transactions

3. **Quelles métriques sont disponibles ?**
   - Listez toutes vos métriques dans Prometheus : http://localhost:9090/graph
   - Explorez avec des queries simples pour voir ce qui est intéressant

**Livrable de cette étape** : Document `DASHBOARD_DESIGN.md` avec :
```markdown
# Design de mon Dashboard

## Objectif
[Décrire en 2-3 phrases le but de ce dashboard]

## Public cible
[Qui va l'utiliser ?]

## Métriques clés à afficher
1. [Métrique 1] - Pourquoi : [raison]
2. [Métrique 2] - Pourquoi : [raison]
3. [Métrique 3] - Pourquoi : [raison]
...

## Disposition prévue
[Croquis ou description de l'organisation des panels]
```

---

#### **Étape 2 : Création du dashboard (2h)**

**Mission** : Créez votre dashboard dans Grafana en suivant votre plan.

**Contraintes minimales** :
- ✅ Minimum **6 panels** (pas de maximum)
- ✅ Au moins **3 types de visualisation différents** (Time series, Stat, Gauge, Pie chart, Heatmap, etc.)
- ✅ Au moins **1 panel avec plusieurs queries** (pour comparer des métriques)
- ✅ Au moins **1 métrique custom** (que vous avez créée dans Phase 1)
- ✅ Au moins **1 panel infrastructure** (node-exporter ou cAdvisor)
- ✅ **Titre clair** pour chaque panel
- ✅ **Unités appropriées** (req/s, ms, %, etc.)

**Suggestions de métriques à explorer** :

<details>
<summary>💡 Idées de métriques HTTP</summary>

```promql
# Requêtes par seconde
sum(rate(http_requests_total[5m]))

# Requêtes par endpoint
sum(rate(http_requests_total[5m])) by (handler)

# Requêtes par méthode HTTP
sum(rate(http_requests_total[5m])) by (method)

# Requêtes par status code
sum(rate(http_requests_total[5m])) by (status)

# Latence moyenne
rate(http_request_duration_seconds_sum[5m]) / rate(http_request_duration_seconds_count[5m])

# Latence P95
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))

# Taux d'erreur (%)
(sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))) * 100

# Requêtes en cours
http_requests_inprogress
```

</details>

<details>
<summary>💡 Idées de métriques Business</summary>

```promql
# Opérations CRUD par seconde
rate(items_created_total[5m])
rate(items_read_total[5m])
rate(items_updated_total[5m])
rate(items_deleted_total[5m])

# Total d'opérations
sum(items_created_total + items_read_total + items_updated_total + items_deleted_total)

# Ratio lecture/écriture
rate(items_read_total[5m]) / (rate(items_created_total[5m]) + rate(items_updated_total[5m]) + rate(items_deleted_total[5m]))

# Nombre actuel d'items en base (Gauge)
items_total

# Distribution des prix — prix médian
histogram_quantile(0.50, rate(items_price_histogram_bucket[5m]))

# Distribution des prix — P95 (items les plus chers)
histogram_quantile(0.95, rate(items_price_histogram_bucket[5m]))

# Erreurs par type (validation, not_found, server_error)
sum(rate(http_errors_total[5m])) by (type)

# Ratio d'erreurs not_found vs total
rate(http_errors_total{type="not_found"}[5m]) / sum(rate(http_requests_total[5m]))
```

</details>

<details>
<summary>💡 Idées de métriques Database</summary>

```promql
# Durée des requêtes DB (P50, P95, P99)
histogram_quantile(0.50, rate(db_query_duration_seconds_bucket[5m]))
histogram_quantile(0.95, rate(db_query_duration_seconds_bucket[5m]))
histogram_quantile(0.99, rate(db_query_duration_seconds_bucket[5m]))

# Requêtes lentes (> 1s)
sum(rate(db_query_duration_seconds_bucket{le="1.0"}[5m]))

# Taille du pool de connexions
db_connection_pool_size
```

</details>

<details>
<summary>💡 Idées de métriques Infrastructure (node-exporter)</summary>

```promql
# CPU Usage %
100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# CPU par mode (user, system, iowait)
avg(rate(node_cpu_seconds_total[5m])) by (mode)

# RAM utilisée (%)
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100

# Espace disque disponible (Go)
node_filesystem_avail_bytes{mountpoint="/"} / 1024 / 1024 / 1024

# Trafic réseau (Mo/s)
rate(node_network_receive_bytes_total[5m]) / 1024 / 1024
rate(node_network_transmit_bytes_total[5m]) / 1024 / 1024

# Load average (1 min)
node_load1
```

</details>

<details>
<summary>💡 Idées de métriques Containers (cAdvisor)</summary>

```promql
# CPU par container
rate(container_cpu_usage_seconds_total{name!=""}[5m])

# Mémoire par container (Mo)
container_memory_usage_bytes{name!=""} / 1024 / 1024

# Mémoire limite vs utilisée par container
container_memory_usage_bytes{name!=""} / container_spec_memory_limit_bytes{name!=""} * 100

# Réseau par container (octets/s)
rate(container_network_receive_bytes_total{name!=""}[5m])
rate(container_network_transmit_bytes_total{name!=""}[5m])

# I/O disque par container
rate(container_fs_reads_bytes_total{name!=""}[5m])
rate(container_fs_writes_bytes_total{name!=""}[5m])
```

</details>

**Conseils de design** :

1. **Organisation spatiale** :
   - Métriques les plus importantes en haut
   - Stats simples (nombres) en haut, graphiques détaillés en bas
   - Regrouper les métriques liées ensemble

2. **Couleurs et seuils** :
   - Utilisez des couleurs pour indiquer la santé (vert = bon, jaune = attention, rouge = problème)
   - Définissez des seuils réalistes (ex: latence > 500ms = warning)

3. **Lisibilité** :
   - Titres clairs et descriptifs
   - Légendes compréhensibles
   - Pas trop de données sur un seul panel

**Exemples d'approches possibles** :

- **Approche "SRE"** : Dashboard focalisé sur les SLIs (Service Level Indicators) - disponibilité, latence, taux d'erreur
- **Approche "Product"** : Dashboard focalisé sur l'usage - nombre d'opérations, types d'actions, tendances
- **Approche "Performance"** : Dashboard focalisé sur les temps de réponse - latences, slow queries, goulots
- **Approche "Overview"** : Dashboard général avec un peu de tout
- **Approche "RED"** : Rate, Errors, Duration pour chaque endpoint

**Vous êtes libre de choisir votre approche ou d'en inventer une nouvelle !**

---



### 📚 Bonus : Variables de dashboard

**Exercice avancé** :

1. Créer une variable `interval` (Interval type)
2. Créer une variable `endpoint` (Query type)
3. Utiliser dans les queries : `rate(metric[$interval])`

---

### ✅ Validation Phase 3b

- [ ] Dashboard "Business Metrics" créé
- [ ] Dashboard "Database Performance" créé
- [ ] Dashboard "RED Metrics" créé (autonome)
- [ ] Total de 4 dashboards fonctionnels
- [ ] Exercices réussis

---

## 💥 Phase 4 : Stress Testing avec Locust (2h) Optionnel

![Durée](https://img.shields.io/badge/Durée-2h-blue)
![Type](https://img.shields.io/badge/Type-Guidé_+_Tests-purple)
![Difficulté](https://img.shields.io/badge/Difficulté-⭐⭐_Moyen-yellow)

### 🎯 Objectif

Effectuer des tests de charge et observer le comportement de l'application dans Grafana.

### 📁 Script à créer

**📄 Exemple de code : `locustfile.py`**

```python
from locust import HttpUser, task, between
import random

class ItemsAPIUser(HttpUser):
    """Utilisateur complet - Opérations CRUD"""

    wait_time = between(1, 3)
    item_ids = []

    def on_start(self):
        for i in range(3):
            response = self.client.post("/items", json={
                "nom": f"Initial Item {i}",
                "prix": round(random.uniform(10, 100), 2)
            })
            if response.status_code == 201:
                data = response.json()
                self.item_ids.append(data["id"])

    @task(5)
    def list_items(self):
        self.client.get("/items")

    @task(3)
    def get_item(self):
        if self.item_ids:
            item_id = random.choice(self.item_ids)
            self.client.get(f"/items/{item_id}", name="/items/{id}")

    @task(2)
    def create_item(self):
        response = self.client.post("/items", json={
            "nom": f"Item {random.randint(1, 10000)}",
            "prix": round(random.uniform(10, 1000), 2)
        })
        if response.status_code == 201:
            data = response.json()
            self.item_ids.append(data["id"])

    @task(1)
    def update_item(self):
        if self.item_ids:
            item_id = random.choice(self.item_ids)
            self.client.put(f"/items/{item_id}", json={
                "nom": f"Updated {random.randint(1, 10000)}",
                "prix": round(random.uniform(10, 1000), 2)
            }, name="/items/{id}")

    @task(1)
    def delete_item(self):
        if len(self.item_ids) > 10:
            item_id = self.item_ids.pop()
            self.client.delete(f"/items/{item_id}", name="/items/{id}")

class LightUser(HttpUser):
    """Utilisateur léger - Lecture seule"""

    wait_time = between(2, 5)

    @task(10)
    def read_items(self):
        self.client.get("/items")

    @task(5)
    def read_single_item(self):
        item_id = random.randint(1, 50)
        self.client.get(f"/items/{item_id}", name="/items/{id}")
```

---

### 🎓 Déroulement (2h)

#### **00:00-00:20 | Installation et démo**

```bash
pip install locust

cp stress-testing/locustfile.py .

locust -f locustfile.py
```

Interface : http://localhost:8089

---

#### **00:20-01:05 | Test 1 : Charge légère (20 users) - Guidé**

**Configuration** :
- Users : 20
- Spawn rate : 5
- Duration : 5 min

**IMPORTANT** : Grafana ouvert en parallèle !

**Observations à noter** :

| Métrique      | Valeur | Dashboard            |
| ------------- | ------ | -------------------- |
| RPS           | ___    | HTTP Overview        |
| Latence P95   | ___    | HTTP Overview        |
| Taux d'erreur | ___    | HTTP Overview        |
| DB Latency    | ___    | Database Performance |

---

#### **01:05-01:35 | Test 2 : Montée en charge (100 users) - Guidé**

**Configuration** :
- Users : 100
- Spawn rate : 10
- Duration : 5 min

**Questions** :
- À quel moment la latence augmente ?
- Y a-t-il des erreurs ?

---

#### **01:35-02:00 | 💪 EXERCICE : Test 3 - Stress (autonome)**

**Mission** : Trouver le point de rupture de l'application

**Instructions** :

1. Lancer un test avec 200 users (spawn rate : 20)
2. Observer les dashboards Grafana
3. Noter quand l'application commence à crasher
4. Identifier le goulot d'étranglement

**Livrable** :
- Point de rupture : ___ users
- Symptôme principal : ___
- Métrique critique : ___

---

### ✅ Validation Phase 4

- [ ] Locust installé et testé
- [ ] 3 tests effectués (20, 100, 200 users)
- [ ] Dashboards Grafana observés en temps réel
- [ ] Métriques relevées
- [ ] Point de rupture identifié

---

## 📐 Phase 5 : Analyse & Optimisation (1h15) Optionnel

![Durée](https://img.shields.io/badge/Durée-1h15-blue)
![Type](https://img.shields.io/badge/Type-Discussion-purple)
![Difficulté](https://img.shields.io/badge/Difficulté-⭐⭐_Moyen-yellow)

### 🎯 Objectif

Analyser les résultats des tests et proposer des optimisations.

### 📄 Template de rapport à créer

**Fichier : `RAPPORT_STRESS_TEST.md`**

### 🎓 Déroulement (1h15)

#### **00:00-00:30 | Remplir le rapport (par groupe)**

Compléter le template avec vos résultats.

---

#### **00:30-00:50 | Présentation des résultats (5min par groupe)**

Chaque groupe présente :
- RPS maximal atteint
- Point de rupture
- Goulot d'étranglement identifié

---

#### **00:50-01:05 | 💪 EXERCICE : Optimisations**

**Mission** : Proposer 3 optimisations concrètes

Exemples :
1. Augmenter le pool de connexions DB
2. Ajouter du caching Redis
3. Optimiser les requêtes SQL
4. Scaler horizontalement

**Livrable** : Document avec :
- Optimisation proposée
- Impact attendu
- Complexité d'implémentation

---

#### **01:05-01:15 | Synthèse formateur - Bonnes pratiques**

**Métriques critiques en production** :

| Métrique       | Seuil   | Action       |
| -------------- | ------- | ------------ |
| Latence P95    | < 200ms | ✅ OK         |
| Latence P99    | < 500ms | ⚠️ Surveiller |
| Taux d'erreur  | < 1%    | ✅ OK         |
| DB Latency P95 | < 50ms  | ✅ OK         |

**Méthodologie RED** :
- **R**ate : Surveiller le débit
- **E**rrors : Surveiller les erreurs
- **D**uration : Surveiller la latence

---

### ✅ Validation Phase 5 

- [ ] Rapport de stress test complété
- [ ] Résultats présentés
- [ ] Point de rupture documenté
- [ ] 3 optimisations proposées
- [ ] Comprend les métriques à surveiller en prod

---

## 🚨 Phase 6 (BONUS) : Alerting avec Prometheus (Optionnel)

![Difficulté](https://img.shields.io/badge/Difficulté-⭐⭐⭐_Difficile-orange)
![Durée](https://img.shields.io/badge/Durée-2h-blue)
![Status](https://img.shields.io/badge/Status-Bonus-orange)

> ⚠️ **Cette phase est optionnelle** et peut être faite après la formation principale.

### 🎯 Objectif

Mettre en place des alertes pour être notifié des problèmes de performance.

### 📋 Contenu (si temps disponible)

**Créer des règles d'alerte** :

```yaml
# prometheus/alerts.yml
groups:
  - name: fastapi_alerts
    rules:
      - alert: HighErrorRate
        expr: |
          (sum(rate(http_requests_total{status=~"5.."}[5m])) /
           sum(rate(http_requests_total[5m]))) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Taux d'erreur élevé (> 5%)"

      - alert: HighLatency
        expr: |
          histogram_quantile(0.95,
            rate(http_request_duration_seconds_bucket[5m])
          ) > 1.0
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Latence P95 > 1s"
```

**Configurer Alertmanager** (optionnel)

**Tester les alertes** dans Grafana

---

## 🎓 Critères de Réussite Globaux

### ✅ Niveau Fondamental (Obligatoire)

- [ ] Concepts d'observabilité compris
- [ ] Application instrumentée avec métriques
- [ ] Prometheus déployé et fonctionnel
- [ ] Au moins 2 dashboards Grafana créés
- [ ] Tests Locust exécutés
- [ ] Rapport d'analyse complété

### ✅ Niveau Intermédiaire (Attendu)

- [ ] Tous les critères fondamentaux
- [ ] 4 dashboards Grafana complets
- [ ] Maîtrise des requêtes PromQL
- [ ] Exercices autonomes réussis
- [ ] Point de rupture identifié
- [ ] Optimisations proposées

### ✅ Niveau Avancé (Bonus)

- [ ] Tous les critères intermédiaires
- [ ] Variables dans dashboards Grafana
- [ ] Alerting configuré
- [ ] Optimisations implémentées et testées

---

## 📚 Ressources Globales

### 🔗 Documentation officielle

| Catégorie         | Ressource                                 | Lien                                                                  |
| ----------------- | ----------------------------------------- | --------------------------------------------------------------------- |
| **Observabilité** | Red Hat - Qu'est-ce que l'observabilité ? | [Lien](https://www.redhat.com/fr/topics/devops/what-is-observability) |
| **Prometheus**    | Documentation officielle                  | [Lien](https://prometheus.io/docs/)                                   |
| **Prometheus**    | PromQL Basics                             | [Lien](https://prometheus.io/docs/prometheus/latest/querying/basics/) |
| **Grafana**       | Documentation                             | [Lien](https://grafana.com/docs/grafana/latest/)                      |
| **Locust**        | Documentation                             | [Lien](https://docs.locust.io/)                                       |

### 📄 Ressources du projet

- 📄 **Documentation** : `images/Observabilité_Performance_et_Stress_Testing.pdf` (si disponible)
- 💻 **Exemples de code** : Disponibles dans le brief
- ⚙️ **Exemples de configurations** : Disponibles dans le brief

### 🎥 Vidéos recommandées

- "Prometheus monitoring tutorial 2024"
- "Grafana dashboard tutorial 2024"
- "PromQL queries explained"

---

## 🎯 Conseils pour Réussir

### ✅ À Faire

1. **Suivre la progression** - Respecter l'ordre des phases
2. **Faire les exercices** - C'est en pratiquant qu'on apprend
3. **Poser des questions** - N'hésitez pas !
4. **Observer Grafana** - Pendant les tests, c'est essentiel
5. **Documenter** - Prenez des notes sur ce qui fonctionne

### ❌ À Éviter

1. **Ne pas sauter la veille** - Les concepts sont la base
2. **Ne pas copier sans comprendre** - Lisez les annotations
3. **Ne pas négliger PromQL** - C'est la clé de Prometheus
4. **Ne pas oublier Grafana** - Observer en temps réel pendant Locust

---

## 📦 Livrables Finaux

À la fin de la formation :

### Code et configurations

- [ ] Application FastAPI instrumentée
- [ ] `docker-compose.yml` avec stack complète
- [ ] `prometheus/prometheus.yml` configuré
- [ ] `locustfile.py` fonctionnel

### Dashboards Grafana

- [ ] Dashboard "HTTP Overview"
- [ ] Dashboard "Business Metrics"
- [ ] Dashboard "Database Performance"
- [ ] Dashboard "RED Metrics"

### Documentation

- [ ] Rapport de stress test complété
- [ ] Notes personnelles sur PromQL
- [ ] Propositions d'optimisations

---

<div align="center">

**📊 Bonne formation ! 📊**

*"You can't improve what you don't measure."* - Peter Drucker

![Footer](https://img.shields.io/badge/Formation-14h_mixte-blue?style=for-the-badge)
![Made with](https://img.shields.io/badge/Made_with-❤️_Prometheus_Grafana-E6522C?style=for-the-badge)

</div>
