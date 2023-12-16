from dotenv import load_dotenv
from src.ui.erd_to_ddl_ui import ERD2DDL

# Launch the Gradio UI

if __name__ == "__main__":
    # Take environment variables from .env.
    load_dotenv()
    ui = ERD2DDL()
    ui.launch_ui()
