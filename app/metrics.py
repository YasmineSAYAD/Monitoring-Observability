from prometheus_client import Counter, Gauge, Histogram

# CRUD operation counter
crud_operations_total = Counter(
    "crud_operations_total",
    "Nombre total d'opérations CRUD",
    ["operation"]  # create, read, update, delete
)

# Gauge: number of items in database
items_total = Gauge(
    "items_total",
    "Nombre d'items actuellement stockés"
)

# Histogram : price distribution
item_price_distribution = Histogram(
    "item_price_distribution",
    "Distribution des prix des items",
    buckets=[1, 5, 10, 20, 50, 100, 200, 500]
)

# HTTP error counter
http_errors_total = Counter(
    "http_errors_total",
    "Nombre total d'erreurs HTTP",
    ["route", "method", "status"]
)
