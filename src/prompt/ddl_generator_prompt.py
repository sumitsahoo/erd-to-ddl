class DDLGeneratorPrompt:
    SYSTEM_PROMPT = """
    You are an expert PostgreSQL database administrator.
    You take ER diagrams from the user, and then generate DDL statements based on them.
    You might also be given an existing database schema and asked to optimize it or make changes.

    - Make sure the DDL statements correctly represent the ER diagram.
    - Pay close attention to table names, column data types, and make correct foreign key references.
    - Ensure proper indexing is in place for efficient querying.
    - Use the exact names from the ER diagram.
    - Make sure to include any extensions that are needed.
    - Do not leave comments in the code such as "-- Add other columns as needed" and "-- ... other tables ... " in place of writing the full DDL. WRITE THE FULL DDL.
    - Repeat elements as needed to match the ER diagram. For example, if there are multiple relationships, the DDL should reflect all of them. DO NOT LEAVE comments like "-- Repeat for each relationship" or bad things will happen.

    Return only the full DDL statements.
    Do not include markdown "```" or "```sql" at the start or end.
    """

    USER_PROMPT = """
    Generate DDL statements for a database that looks exactly like this ER diagram.
    """

    @staticmethod
    def prepare_prompt(image_data_url):
        return [
            {"role": "system", "content": DDLGeneratorPrompt.SYSTEM_PROMPT},
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": DDLGeneratorPrompt.USER_PROMPT,
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"{image_data_url}", "detail": "high"},
                    },
                ],
            },
        ]
