import gradio as gr

from src.llm.custom_llm import CustomLLM
from src.util.log_util import LogUtil


class ERD2DDL:
    def __init__(self):
        self.log = LogUtil()
        self.llm = CustomLLM()
        self.primary_color = "#00A0F6"

        self.theme = gr.themes.Base(
            primary_hue="purple",
            secondary_hue="purple",
        ).set(
            # button_primary_background_fill="*secondary_500",
            button_primary_background_fill=self.primary_color,
            button_primary_background_fill_dark="*primary_500",
            button_primary_text_color="white",
            loader_color=self.primary_color,
        )

    def launch_ui(self):
        # Check if index is built

        with gr.Blocks(
            title="ERD2DDL",
            theme=self.theme,
            # css=custom_css,
        ) as erd_to_ddl:
            gr.Image(
                "./images/logo.svg",
                height=50,
                width=210,
                interactive=False,
                container=False,
                show_download_button=False,
            )

            with gr.Tab("Generate DDL from ERD"):
                gr.Textbox(
                    value="Upload an image of an ERD to generate DDL. Make sure the ERD has proper naming conventions for tables and columns with data types.",
                    show_label=False,
                    interactive=False,
                    container=False,
                )

                gr.Interface(
                    fn=self.llm.generate_ddl_using_vision,
                    inputs=[
                        gr.Image(
                            label="Select Image",
                            sources=["upload"],
                            type="filepath",
                            height=400,
                        ),
                    ],
                    outputs=[
                        gr.Code(
                            label="Generated DDL",
                        ),
                    ],
                    examples=[
                        "./images/example/customer.png",
                    ],
                    allow_flagging="never",
                )
            # with gr.Tab("Normalize ERD"):
            #     gr.Textbox(
            #         value="Upload an image of an ERD to normalize it. Make sure the ERD has proper naming conventions for tables and columns with data types.",
            #         show_label=False,
            #         interactive=False,
            #         container=False,
            #     )
            #     gr.Interface(
            #         fn=self.llm.normalize_erd_using_vision,
            #         inputs=[
            #             gr.Image(
            #                 label="Select Image",
            #                 sources=["upload"],
            #                 type="filepath",
            #                 height=400,
            #             ),
            #         ],
            #         outputs=[
            #             gr.Code(
            #                 label="Generated DDL",
            #             ),
            #         ],
            #         examples=[
            #             "./images/example/customer.png",
            #         ],
            #         allow_flagging="never",
            #     )

        erd_to_ddl.queue().launch(
            favicon_path="./images/favicon.ico",
            debug=False,
            show_api=False,
            server_name="0.0.0.0",
            server_port=8080,
            share=False,
            allowed_paths=["./images/", "./outputs/"],
        )
