CREATE VIEW literacy_state_total AS
SELECT *
FROM literacy_analysis
WHERE tru = 'Total';