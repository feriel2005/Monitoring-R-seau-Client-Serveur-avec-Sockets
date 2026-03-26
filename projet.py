# ============================================================
#  config.py — Configuration centrale du projet
#  Modifier ces valeurs selon tes besoins
# ============================================================

# --- Réseau ---
HOST = "0.0.0.0"       # Le serveur écoute sur toutes les interfaces
SERVER_IP = "127.0.0.1" # Adresse que les clients utilisent pour se connecter
PORT = 9999             # Port TCP du serveur

# --- Timing ---
T = 5                   # Intervalle entre chaque REPORT (en secondes)
TIMEOUT_AGENT = 3 * T  # Un agent est inactif si aucun REPORT reçu pendant 3×T secondes

# --- Seuils d'alerte (pour les extensions) ---
CPU_ALERT_THRESHOLD = 80.0   # Alerte si CPU > 80%
RAM_ALERT_THRESHOLD = 90.0   # Alerte si RAM > 90%

# --- Affichage serveur ---
STATS_INTERVAL = T           # Afficher les stats globales toutes les T secondes

# --- Encodage ---
ENCODING = "utf-8"
BUFFER_SIZE = 1024