# PyDomus
# Plateforme de supervision domotique — Projet INFO PRO 8501

Application web (basée sur python) de domotique permettant de superviser et piloter un domicile depuis une interface centralisée, à partir de capteurs et d'actionneurs **Zigbee**.

## Présentation

La plateforme permet à l'utilisateur de :

- visualiser **en temps réel** les mesures remontées par ses capteurs ;
- consulter l'**historique** des mesures ;
- être **alerté** en cas d'anomalie (dépassement de seuil ou capteur silencieux) ;
- **commander un actionneur** (prise électrique connectée) depuis l'interface.

Les grandeurs supervisées sont la **température**, le **taux d'humidité** et l'**ouverture des portes**.

## Fonctionnalités

| ID    | Fonction                                                                  |
|-------|---------------------------------------------------------------------------|
| BF-01 | Le système doit collecter les mesures de N capteurs (température, humidité, ouverture) |
| BF-02 | Le système doit afficher l'état courant et l'historique sur une interface graphique rafraîchie en temps réel |
| BF-03 | Le système doit lever une alerte visuelle en cas de dépassement de seuil ou de silence d'un capteur |
| BF-04 | Le système doit permettre à l'utilisateur de commander un actionneur depuis l'interface (prise électrique dans notre cas) |
| BF-05 | Le système doit communiquer en réseau avec les capteurs et actionneurs |

**Hors périmètre :** application mobile, capteurs non compatibles Zigbee.