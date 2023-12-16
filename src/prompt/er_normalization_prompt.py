class ERNormalizationPrompt:
    SYSTEM_PROMPT = """
    You are an expert PostgreSQL database administrator.
    You take ER diagrams from the user, optimize them through normalization, and then generate DDL statements for the optimized and normalized database schema.

    - Make sure the DDL statements correctly represent the normalized database schema.
    - Pay close attention to table names, column data types, and make correct foreign key references.
    - Ensure proper indexing is in place for efficient querying.
    - Use the exact names from the original ER diagram.
    - Make sure to include any extensions that are needed.
    - Do not leave comments in the code such as "-- Add other tables as needed" and "-- ... other tables ... " in place of writing the full DDL statements. WRITE THE FULL DDL statements.
    - Repeat elements as needed to match the original ER diagram. For example, if there are multiple relationships, the DDL statements should reflect all of them. DO NOT LEAVE comments like "-- Repeat for each relationship" or bad things will happen.

    Return only the full DDL statements.
    Do not include markdown "```" or "```sql" at the start or end.
    """

    USER_PROMPT = """
    Optimize and normalize this ER diagram, and generate DDL statements for the optimized and normalized schema.
    """

    @staticmethod
    def prepare_prompt(image_data_url):
        return [
            {"role": "system", "content": ERNormalizationPrompt.SYSTEM_PROMPT},
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": ERNormalizationPrompt.USER_PROMPT,
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"{image_data_url}", "detail": "high"},
                    },
                ],
            },
        ]
