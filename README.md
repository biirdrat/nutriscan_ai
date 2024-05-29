# Nutriscan AI

Nutriscan AI is a Qt-based application for reading and analyzing nutrition labels using AI.

## Requirements
This project currently is only meant to support Windows development/executation
To set up and run this project, ensure you have the following installed:

- Python 3.11.x
- PyInstaller 6.6.0
- PyQt5 5.15.10

### Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/biirdrat/nutriscan_ai.git
    cd nutriscan_ai
    ```

2. **Create and Activate a Virtual Environment:**

    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install Dependencies:**

    ```sh
    # Install repository directory
    pip install -e .

    # Install external libraries
    pip install -r requirements.txt
    ```


### Running the Application

To run the application, execute the following commands:

```sh
cd src
python -m GUI.main
```
