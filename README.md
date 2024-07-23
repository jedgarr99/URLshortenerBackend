# URL Shortener Backend Server

This project is a URL Shortener service implemented using Flask. It provides an API for shortening URLs and redirecting to the original URLs.

## Features

- **Shorten URLs**: Accepts an original URL and returns a shortened URL.
- **Redirect URLs**: Redirects to the original URL based on the shortened URL.
- **Swagger Documentation**: Provides API documentation using Swagger.

## Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package installer)
- Git (optional, for cloning the repository)

### Installation

1. **Clone the repository** (or download the source code):

    ```sh
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```

2. **Create and activate a virtual environment**:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

### Configuration

- **Environment Variables**: Create a `.env` file in the project root with the following content:

    ```env
    FLASK_APP=run.py
    FLASK_ENV=development
    ```

- **Database Configuration**: The project is configured to use SQLite by default. If you want to use a different database, update the `SQLALCHEMY_DATABASE_URI` in `config.py`.

### Database Setup

1. **Initialize the database**:

    ```sh
    flask db init
    ```

2. **Create the initial migration**:

    ```sh
    flask db migrate -m "Create URL table"
    ```

3. **Apply the migration**:

    ```sh
    flask db upgrade
    ```

### Running the Server

1. **Start the Flask server**:

    ```sh
    flask run
    ```

    The server will start on `http://localhost:5000`.

### API Documentation

- **Swagger UI**: Once the server is running, you can access the API documentation at `http://localhost:5000/apidocs`.

## Testing

Make sure you have `pytest` installed:
```sh
    pip install pytest
```

1. **Run the tests**:

    ```sh
    pytest
    ```



    

## Deployment

You can deploy the server on various platforms, including AWS, Heroku, or any other cloud service provider. Below is a brief overview of deploying to an AWS EC2 instance:

1. **Launch an EC2 instance** with an appropriate AMI (e.g., Ubuntu).
2. **SSH into the instance** and set up your environment.
3. **Clone your repository** and set up your virtual environment.
4. **Install dependencies** and run your Flask app.
5. **Configure a web server (e.g., Nginx)** to proxy requests to your Flask app.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- Flask
- SQLAlchemy
- Flask-Migrate
- Flask-CORS
- Flasgger

Feel free to contribute to this project by submitting issues or pull requests.