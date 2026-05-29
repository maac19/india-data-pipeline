SELECT
    state,
    avg_unemployment
FROM master_state_analysis
WHERE avg_unemployment IS NOT NULL
ORDER BY avg_unemployment DESC
LIMIT 10;