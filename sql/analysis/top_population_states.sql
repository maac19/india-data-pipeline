SELECT
    state,
    total_population
FROM master_state_analysis
ORDER BY total_population DESC
LIMIT 10;