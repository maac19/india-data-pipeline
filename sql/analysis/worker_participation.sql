SELECT
    state,
    ROUND(
        (tot_work_p::NUMERIC / total_population) * 100,
        2
    ) AS worker_participation_rate
FROM master_state_analysis
ORDER BY worker_participation_rate DESC;