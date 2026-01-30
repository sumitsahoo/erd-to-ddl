# ℹ️ ERD2DDL
Generate DDLs (PostgreSQL) from an ER diagram using OpenAI Vision.<br>
OpenAI Vision Documentation: https://platform.openai.com/docs/guides/vision

## 📖 Medium Article
TBD

## 📦 Dependency Installation

You need `Python 3.12.4` installed in your system. If you are using `pyenv` then check the version using the command: `pyenv version`

1. Install poetry
    ```bash
    # Using pip
    pip install poetry
    
    # Using brew (macOS), if you are using pyenv you should use `pip install poetry`
    brew install poetry
    ```
2. Set poetry to create virtual environment within project folder
    ```bash
    poetry config virtualenvs.in-project true
    ```
3. Install dependency and create the virtual environment
    ```bash
    poetry install
    ``` 
4. Run the app with poetry
    ```python
    poetry run python main.py
    ```
    or launch the app via VS Code debug menu. VS Code launch config file is also provided for easy debugging 🤓


To update dependencies use: `poetry update`<br>
If you want to update dependencies in `pyproject.toml`, then you need to install plugin `poetry-plugin-up`. Use command below:
```
poetry self add poetry-plugin-up
```
Once installed, use command `poetry up` to install updates and edit `pyproject.toml` automatically.<br>
To view virtual environment location, use: `poetry env info --path`<br>
To generate `requirements.txt` using poetry, you need to have an export plugin installed.<br>

Install the plugin:
```bash
poetry self add poetry-plugin-export
```
Once the plugin is installed, use the `export` command to generate `requirements.txt`
```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
```


## 🔑 Environment Variable
There are 2 environment variables you can specify.
1. OPENAI_API_KEY: This is your OpenAI API key.
2. GRADIO_SERVER_PORT: This is the Gradio server port. This is optional if not specified in the `launch` method.

## 🚢 Docker

If you are planning on deploying the app to the cloud, you need a Docker image. To build the same use the `Dockerfile` provided. The multi-stage build makes sure the resulting image is smaller in size and only includes the libraries that are needed. Also, the use of non-root user makes it more secure.<br>

Build arm64 image (Make sure cloud deployment supports arm64 images):
```bash
docker build --no-cache -t erd2ddl_latest .
```
For amd64 image (most common and widely supported):
```bash
docker buildx build --no-cache --platform linux/amd64 -t erd2ddl_latest .
```

Once the image is built, you can push the same to any cloud provider and use a serverless service to deploy the same easily.

To run the Docker image locally use the below command:
```bash
docker run -it \
-e GRADIO_SERVER_PORT=8080 \
-e OPENAI_API_KEY=your_key_here \
-p 8080:8080 \
--name erd2ddl \
erd2ddl_latest
```

## 🙏🏻 Attributions
1. <a href="https://www.gradio.app/" title="gradio ui">UI is built using Gradio</a><br>
2. <a href="https://www.flaticon.com/free-icons/sql-file" title="sql file icons">Sql file icons created by Muhammad_Usman - Flaticon</a>

## 📜 License

MIT License

Copyright © 2026 Sumit Sahoo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
