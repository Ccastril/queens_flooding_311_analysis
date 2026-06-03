 SELECT
            unique_key,
            created_date,
            closed_date,
            agency,
            complaint_type,
            descriptor,
            incident_zip,
            borough,
            latitude,
            longitude,
            status,
            resolution_description
        WHERE borough = 'QUEENS'
          AND (
            upper(complaint_type) LIKE '%FLOOD%'
            OR upper(descriptor) LIKE '%FLOOD%'
            OR upper(complaint_type) LIKE '%SEWER%'
          )
        LIMIT {limit}