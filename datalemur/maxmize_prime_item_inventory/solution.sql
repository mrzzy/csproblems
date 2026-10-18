--
-- CSProblems
-- Datalemur
-- DL4. Maximize Prime Item Inventory
--

-- determine the size of each batch
WITH batch_size AS (
    SELECT
        item_type,
        SUM(square_footage) AS batch_footage,
        COUNT(item_id) AS item_count
    FROM inventory
    GROUP BY 1
),

-- transpose batch sizes: pivot from rows to columns
batch_size_t AS (
    SELECT
        (
            SELECT batch_footage FROM batch_size
            WHERE item_type = 'prime_eligible'
        ) AS prime_footage,
        (
            SELECT batch_footage FROM batch_size
            WHERE item_type = 'not_prime'
        ) AS non_prime_footage
),

-- compute max no. of prime batches that can be stored
max_prime_batches AS (
    SELECT FLOOR((500000 - non_prime_footage) / prime_footage) AS n_prime
    -- ensure at least one non-prime batch is allocated by checking
    -- removing 1 non-prime batch from allocated spacef
    FROM batch_size_t
),

-- compute no. of non-prime allocations
batch_allocations AS (
    SELECT
        m.n_prime,
        FLOOR((500000 - m.n_prime * b.prime_footage) / b.non_prime_footage)
            AS n_non_prime
    FROM max_prime_batches AS m, batch_size_t AS b
)

SELECT
    b.item_type,
    CASE
        WHEN b.item_type = 'prime_eligible'
            THEN a.n_prime * b.item_count
        WHEN b.item_type = 'not_prime'
            THEN a.n_non_prime * b.item_count
        ELSE 0
    END AS item_count
FROM batch_size AS b, batch_allocations AS a
