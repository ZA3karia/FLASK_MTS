-- SQLite
-- SELECT id,  longitude, latitude
-- FROM clients;

SELECT id, client, round(quantity)
FROM expedition_clients
WHERE delivery_state is "en cour"