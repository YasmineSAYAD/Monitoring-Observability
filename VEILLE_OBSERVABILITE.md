# 🔍 Veille Technologique — Monitoring & Observabilité

> _Stack Prometheus / Grafana — Concepts, Architecture et Bonnes Pratiques_

---

## 1. Monitoring vs Observabilité — Quelle différence ?

### Le Monitoring (surveillance traditionnelle)

Le monitoring consiste à **surveiller des indicateurs prédéfinis** pour détecter si un système est dans un état attendu ou non. On pose la question : _"Est-ce que ça marche ?"_

- Approche réactive : on définit à l'avance ce qu'on veut surveiller
- Basé sur des seuils et des alertes fixes
- Répond à des questions connues à l'avance
- Exemple : "CPU > 90% → alerte"

### L'Observabilité (Observability)

L'observabilité, issue de la théorie du contrôle, désigne la **capacité à inférer l'état interne d'un système à partir de ses sorties externes**. On pose la question : _"Pourquoi ça ne marche pas ?"_

- Approche proactive et exploratoire
- Permet d'investiguer des problèmes **inconnus à l'avance** (_unknown unknowns_)
- S'applique particulièrement aux architectures distribuées et microservices
- Repose sur trois piliers complémentaires

> **En résumé** : le monitoring surveille ce que vous savez déjà mesurer. L'observabilité vous permet de comprendre ce que vous ne saviez pas encore chercher.

---

## 2. Les 3 Piliers de l'Observabilité

### 📊 Métriques (Metrics)

Les métriques sont des **valeurs numériques agrégées dans le temps**. Elles permettent de mesurer l'état et les performances d'un système de manière efficace et peu coûteuse.

- Légères à stocker (valeurs numériques)
- Idéales pour les alertes et les tableaux de bord
- Exemples : taux de requêtes, latence moyenne, utilisation CPU, taux d'erreur

### 📝 Logs (Journaux)

Les logs sont des **enregistrements textuels horodatés d'événements** produits par une application ou un système.

- Riches en information contextuelle
- Plus coûteux en stockage et en traitement
- Indispensables pour le débogage fin
- Outils courants : ELK Stack (Elasticsearch, Logstash, Kibana), Loki

### 🔗 Traces (Traces distribuées)

Les traces permettent de **suivre le cheminement d'une requête** à travers les différents services d'une architecture distribuée.

- Chaque trace est composée de **spans** (unités de travail dans un service)
- Permettent d'identifier les goulots d'étranglement dans les microservices
- Outils courants : Jaeger, Zipkin, OpenTelemetry

> **OpenTelemetry** est devenu le standard ouvert pour instrumenter les trois piliers de manière unifiée.

---

## 3. Prometheus — Architecture Pull

### Présentation

Prometheus est un système de **monitoring open-source** né chez SoundCloud en 2012, puis adopté par la CNCF (Cloud Native Computing Foundation) en 2016. Il est aujourd'hui le standard de facto pour la collecte de métriques dans les environnements cloud-native.

### Architecture Pull (scraping)

Contrairement à une architecture **push** (où les services envoient leurs données), Prometheus adopte un modèle **pull** : c'est lui qui va chercher périodiquement les métriques.

```
┌─────────────────────────────────────────────────────────┐
│                      PROMETHEUS                         │
│                                                         │
│  ┌─────────────┐    scrape HTTP     ┌────────────────┐  │
│  │   Scrape    │ ─────────────────▶│ /metrics       │ │
│  │   Engine    │    (toutes les     │  endpoint      │  │
│  └─────────────┘    15s par défaut) └────────────────┘  │
│         │                              Service cible     │
│         ▼                                               │
│  ┌─────────────┐                                        │
│  │  TSDB       │ ← Time Series Database                 │
│  │  (stockage) │                                        │
│  └─────────────┘                                        │
│         │                                               │
│         ▼                                               │
│  ┌─────────────┐    ┌──────────────┐                   │
│  │  PromQL     │    │ Alertmanager │                    │
│  │  Query API  │    │  (alertes)   │                    │
│  └─────────────┘    └──────────────┘                   │
└─────────────────────────────────────────────────────────┘
```

### Avantages du modèle Pull

- **Contrôle centralisé** : Prometheus sait exactement quelles cibles sont "up" ou "down"
- **Pas de surcharge réseau** côté service (pas de reconnexion)
- **Simplicité de debug** : on peut interroger manuellement le endpoint `/metrics`
- **Sécurité** : le serveur tire les données, pas l'inverse

### Composants clés

| Composant             | Rôle                                                                           |
| --------------------- | ------------------------------------------------------------------------------ |
| **Prometheus Server** | Collecte, stocke, expose les métriques                                         |
| **Exporters**         | Exposent les métriques d'applications tierces (Node Exporter, MySQL Exporter…) |
| **Pushgateway**       | Permet aux jobs éphémères de pousser leurs métriques                           |
| **Alertmanager**      | Gère le routage et la déduplication des alertes                                |
| **Service Discovery** | Détection automatique des cibles (Kubernetes, Consul, DNS…)                    |

### Configuration `prometheus.yml`

```yaml
global:
  scrape_interval: 15s # Fréquence de scraping
  evaluation_interval: 15s # Fréquence d'évaluation des règles

scrape_configs:
  - job_name: "my-service"
    static_configs:
      - targets: ["localhost:8080"]
```

---

## 4. Les 4 Types de Métriques Prometheus

### 🔢 Counter (Compteur)

Un compteur est une **valeur qui ne fait qu'augmenter** (ou se réinitialiser à 0 au redémarrage).

- Représente un cumul d'événements
- Ne jamais l'utiliser pour des valeurs qui peuvent diminuer
- Suffixe conventionnel : `_total`

```
# Exemples
http_requests_total{method="GET", status="200"}  → 42358
http_errors_total{type="500"}                    → 127
```

**Requête typique** : utiliser `rate()` pour obtenir le taux d'évolution

```promql
rate(http_requests_total[5m])   # Requêtes par seconde sur 5 min
```

---

### 📈 Gauge (Jauge)

Une gauge est une **valeur numérique arbitraire** qui peut monter ou descendre.

- Représente un état instantané
- Pas de suffixe spécifique requis

```
# Exemples
node_memory_MemAvailable_bytes  → 4294967296
go_goroutines                   → 42
temperature_celsius             → 23.4
```

**Requête typique** : lecture directe ou agrégation

```promql
avg(node_memory_MemAvailable_bytes) by (instance)
```

---

### 📊 Histogram (Histogramme)

Un histogramme **échantillonne des observations** et les regroupe dans des buckets prédéfinis. Il génère automatiquement trois séries :

- `_bucket{le="..."}` : nombre d'observations ≤ à la borne
- `_sum` : somme de toutes les observations
- `_count` : nombre total d'observations

```
# Exemple pour des durées de requêtes HTTP
http_request_duration_seconds_bucket{le="0.1"}  → 850
http_request_duration_seconds_bucket{le="0.5"}  → 1200
http_request_duration_seconds_bucket{le="1.0"}  → 1350
http_request_duration_seconds_bucket{le="+Inf"} → 1400
http_request_duration_seconds_sum               → 523.4
http_request_duration_seconds_count             → 1400
```

**Requête typique** : calcul de percentiles

```promql
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))
# → p95 de la latence sur les 5 dernières minutes
```

> ⚠️ Les buckets sont définis **côté serveur** à l'instrumentation. Bien les choisir selon les SLOs attendus.

---

### 📉 Summary (Résumé)

Un summary est similaire à l'histogramme mais calcule les **quantiles côté client**, directement dans l'application instrumentée.

- Génère `_sum`, `_count`, et des quantiles pré-calculés
- Avantage : précis sans configuration de buckets
- Inconvénient : **impossible d'agréger les quantiles** entre plusieurs instances

```
# Exemple
rpc_duration_seconds{quantile="0.5"}  → 0.048
rpc_duration_seconds{quantile="0.9"}  → 0.092
rpc_duration_seconds{quantile="0.99"} → 0.144
```

### Histogram vs Summary — Comparaison

| Critère                    | Histogram             | Summary             |
| -------------------------- | --------------------- | ------------------- |
| Calcul des quantiles       | Côté serveur (PromQL) | Côté client         |
| Agrégation multi-instances | ✅ Possible           | ❌ Impossible       |
| Précision des quantiles    | Approximative         | Exacte              |
| Configuration              | Buckets à définir     | Quantiles à définir |
| **Recommandation**         | ✅ Préférer           | Usage limité        |

---

## 5. PromQL — Prometheus Query Language

### Présentation

PromQL est un **langage de requête fonctionnel** conçu pour interroger et agréger des séries temporelles. Il opère sur deux types de vecteurs :

- **Instant vector** : valeur la plus récente de chaque série
- **Range vector** : ensemble des valeurs sur une fenêtre temporelle `[5m]`

### Sélecteurs et filtres par labels

```promql
# Sélection simple
http_requests_total

# Filtrage par label exact
http_requests_total{method="GET"}

# Filtrage par regex
http_requests_total{status=~"5.."}

# Exclusion
http_requests_total{method!="POST"}
```

### Fonctions essentielles

| Fonction                        | Description                         | Usage               |
| ------------------------------- | ----------------------------------- | ------------------- |
| `rate(counter[5m])`             | Taux de variation par seconde       | Counters uniquement |
| `irate(counter[5m])`            | Taux instantané (2 derniers points) | Pics de charge      |
| `increase(counter[1h])`         | Augmentation totale sur la période  | Volumes             |
| `avg_over_time(gauge[10m])`     | Moyenne temporelle                  | Gauges              |
| `histogram_quantile(0.95, ...)` | Calcul de percentile                | Histogrammes        |
| `sum by (label)`                | Agrégation par label                | Toutes métriques    |
| `topk(5, metric)`               | Top N séries                        | Classements         |

### Exemples de requêtes concrètes

```promql
# Taux d'erreur HTTP (ratio erreurs 5xx)
sum(rate(http_requests_total{status=~"5.."}[5m]))
/
sum(rate(http_requests_total[5m]))

# p99 de la latence par service
histogram_quantile(0.99,
  sum by (le, service) (
    rate(http_request_duration_seconds_bucket[5m])
  )
)

# Disponibilité mémoire en %
(node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100

# Comparer avec il y a 24h (offset)
rate(http_requests_total[5m]) offset 24h
```

### Recording Rules — Optimisation

Pour les requêtes coûteuses exécutées fréquemment, les **Recording Rules** pré-calculent et stockent des métriques dérivées :

```yaml
groups:
  - name: http_rules
    rules:
      - record: job:http_requests:rate5m
        expr: sum by (job) (rate(http_requests_total[5m]))
```

Convention de nommage des recording rules : `level:metric:operations`

---

## 6. Bonnes Pratiques de Nommage

### Convention officielle Prometheus

```
<namespace>_<name>_<unit>_<suffix>
```

### Règles fondamentales

**1. Namespace applicatif en préfixe**

```
✅ myapp_http_requests_total
✅ node_cpu_seconds_total
❌ requests_total          (trop générique)
```

**2. Unité dans le nom — toujours en unité de base SI**

```
✅ http_request_duration_seconds    (pas milliseconds)
✅ process_memory_bytes             (pas kilobytes)
✅ filesystem_size_bytes
❌ request_duration_ms
```

**3. Suffixes selon le type de métrique**

```
Counter   → _total           (http_requests_total)
Gauge     → aucun suffixe ou état descriptif
Histogram → _seconds, _bytes (+ auto: _bucket, _sum, _count)
Summary   → idem histogram
```

**4. Snake_case exclusivement**

```
✅ http_request_duration_seconds
❌ httpRequestDurationSeconds
❌ http-request-duration-seconds
```

**5. Labels : cardinalité maîtrisée**

```
✅ {method="GET", status="200"}
❌ {user_id="12345"}    → cardinalité explosif, détruira les perfs
```

**6. Labels : valeurs stables**

```
✅ {env="production", region="eu-west-1"}
❌ {timestamp="..."}   → valeur changeante = explosion de séries
```

### Anti-patterns à éviter

| Anti-pattern               | Problème                 | Solution                               |
| -------------------------- | ------------------------ | -------------------------------------- |
| Noms trop génériques       | Collision entre apps     | Ajouter un namespace                   |
| Unité non spécifiée        | Ambiguïté                | Toujours suffixer l'unité              |
| Haute cardinalité          | Crash mémoire Prometheus | Limiter les labels dynamiques          |
| Encode le type dans le nom | Redondance               | Utiliser le mécanisme natif Prometheus |

---

## 7. Grafana — Visualisation et Dashboards

### Rôle

Grafana est la **couche de visualisation** de la stack. Il se connecte à Prometheus (et à de nombreuses autres sources) via son API pour afficher des tableaux de bord interactifs.

### Fonctionnalités clés

**Tableaux de bord**

- Panels configurables : graphiques temporels, jauges, heatmaps, stat panels
- Variables dynamiques pour filtrer par environnement, service, instance
- Import/export de dashboards JSON (communauté : grafana.com/dashboards)

**Alerting**

- Définition de règles d'alerte directement dans Grafana (depuis v8)
- Intégration avec PagerDuty, Slack, OpsGenie, email, webhooks
- Silence et inhibition des alertes redondantes

**Explore**

- Mode d'exploration ad hoc pour investiguer sans tableau de bord pré-construit
- Compatible PromQL, LogQL (Loki), TraceQL (Tempo)

### Architecture type — Stack complète

```
Applications & Infrastructure
        │
        │  expose /metrics
        ▼
  ┌──────────────┐    scrape    ┌─────────────┐
  │  Exporters   │ ────────────▶│  Prometheus │
  │  (Node, k8s, │              │   Server    │
  │   MySQL...)  │              └──────┬──────┘
  └──────────────┘                     │
                                       │  PromQL
                                       ▼
                               ┌───────────────┐
                               │    Grafana    │
                               │  Dashboards   │
                               └───────┬───────┘
                                       │
                               ┌───────▼───────┐
                               │ Alertmanager  │
                               │ Slack/PD/Mail │
                               └───────────────┘
```

### Dashboards communautaires populaires

| Dashboard          | ID Grafana | Usage                    |
| ------------------ | ---------- | ------------------------ |
| Node Exporter Full | 1860       | Métriques systèmes Linux |
| Kubernetes Cluster | 315        | Monitoring K8s           |
| Spring Boot        | 4701       | Apps Java Spring         |
| Go Runtime         | 240        | Applications Go          |

---

## 8. Résumé — Points Clés à Retenir

| Concept                         | Essence                                                       |
| ------------------------------- | ------------------------------------------------------------- |
| **Observabilité vs Monitoring** | Explorer l'inconnu vs surveiller le connu                     |
| **3 Piliers**                   | Métriques (quoi), Logs (pourquoi), Traces (où)                |
| **Architecture Pull**           | Prometheus scrape activement les endpoints `/metrics`         |
| **Counter**                     | Monotone croissant → toujours utiliser `rate()`               |
| **Gauge**                       | Valeur instantanée → lecture directe                          |
| **Histogram**                   | Distribution + percentiles côté serveur → préférer au Summary |
| **Summary**                     | Quantiles côté client → non agrégeable                        |
| **PromQL**                      | Langage fonctionnel puissant pour requêter les time series    |
| **Nommage**                     | `namespace_name_unit_suffix` en snake_case, unités SI         |
| **Grafana**                     | Couche de visualisation, alerting et exploration              |

---
