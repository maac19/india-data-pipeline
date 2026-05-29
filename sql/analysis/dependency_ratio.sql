SELECT
    state,
    ROUND(
        (non_work_p::NUMERIC / tot_work_p),
        2
    ) AS dependency_ratio
FROM master_state_analysis
ORDER BY dependency_ratio DESC;