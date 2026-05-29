CREATE VIEW master_state_analysis AS
SELECT
    l.state,
    l.tot_p AS total_population,
    ROUND(
        (l.p_lit::NUMERIC / l.tot_p) * 100,
        2
    ) AS literacy_rate,
    e.avg_unemployment,
    l.tot_work_p,
    l.non_work_p
FROM literacy_state_total l
LEFT JOIN (
    SELECT
        LOWER(region) AS state,
        AVG(estimated_unemployment_rate) AS avg_unemployment
    FROM employment_data
    GROUP BY LOWER(region)
) e
ON l.state = e.state;