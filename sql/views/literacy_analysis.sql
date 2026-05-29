CREATE VIEW literacy_analysis AS
SELECT
    LOWER(
        CASE
            WHEN name = 'NCT OF DELHI' THEN 'delhi'
            WHEN name = 'ORISSA' THEN 'odisha'
            WHEN name = 'PONDICHERRY' THEN 'puducherry'
            WHEN name = 'JAMMU & KASHMIR' THEN 'jammu and kashmir'
            WHEN name = 'DADRA & NAGAR HAVELI' THEN 'dadra and nagar haveli'
            WHEN name = 'DAMAN & DIU' THEN 'daman and diu'
            WHEN name = 'ANDAMAN & NICOBAR ISLANDS' THEN 'andaman and nicobar islands'
            ELSE LOWER(name)
        END
    ) AS state,
    tru,
    tot_p,
    tot_m,
    tot_f,
    p_lit,
    m_lit,
    f_lit,
    p_ill,
    m_ill,
    f_ill,
    tot_work_p,
    tot_work_m,
    tot_work_f,
    non_work_p,
    non_work_m,
    non_work_f
FROM literacy_data
WHERE level = 'STATE';