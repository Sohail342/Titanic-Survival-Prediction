# 🚢 Titanic Survival Prediction API

A production-ready FastAPI application that implements three machine learning models for predicting Titanic passenger survival rates using classification algorithms.

## 🎯 Project Overview

This project provides a RESTful API service for predicting Titanic passenger survival using three distinct machine learning algorithms:

- 🔹 **Naive Bayes (NB)** - Probabilistic classifier based on Bayes' theorem
- 🔹 **Logistic Regression (LR)** - Linear model for binary classification  
- 🔹 **K-Nearest Neighbors (KNN)** - Instance-based learning algorithm

## ✨ Features

- **🤖 Multiple ML Models**: Three optimized classification algorithms
- **🔒 Secure API**: JWT-based authentication with user management
- **📊 Comprehensive Data Schema**: Validated input with Pydantic models
- **🐳 Containerized Deployment**: Docker support for easy deployment
- **⚡ Async Processing**: Celery integration for background tasks
- **📚 Auto-generated Documentation**: Interactive API docs with FastAPI
- **🧪 Production Ready**: Pre-commit hooks, linting, and testing setup

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Docker and Docker Compose (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Titanic
   ```

2. **Install dependencies**
   ```bash
   pip install -e .
   ```

3. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Access the API**
   - API Documentation: `http://localhost:8000/docs`
   - Health Check: `http://localhost:8000/health`

### Docker Deployment

**Development Environment:**
```bash
docker-compose -f docker-compose.dev.yml up
```

**Production Environment:**
```bash
docker-compose -f docker-compose.prod.yml up
```

## 📖 API Usage

### Authentication

All prediction endpoints require authentication. First, register a user:

```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword"
  }'
```

Then login to get an access token:

```bash
curl -X POST "http://localhost:8000/auth/jwt/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=securepassword"
```

### Making Predictions

Use the access token to make predictions:

```bash
curl -X POST "http://localhost:8000/api/predict" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model_name": "KNN",
    "features": {
      "Pclass": 1,
      "Sex": 1,
      "Age": 29.0,
      "SibSp": 0,
      "Parch": 0,
      "Fare": 71.2833,
      "Embarked_C": 1,
      "Embarked_Q": 0,
      "Embarked_S": 0
    }
  }'
```

### Model Input Schema

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| `Pclass` | integer | 1-3 | Passenger class (1 = 1st, 2 = 2nd, 3 = 3rd) |
| `Sex` | integer | 0-1 | Gender (0 = male, 1 = female) |
| `Age` | float | ≥ 0 | Age of passenger in years |
| `SibSp` | integer | ≥ 0 | Number of siblings/spouses aboard |
| `Parch` | integer | ≥ 0 | Number of parents/children aboard |
| `Fare` | float | ≥ 0 | Passenger fare |
| `Embarked_C` | integer | 0-1 | Embarked at Cherbourg |
| `Embarked_Q` | integer | 0-1 | Embarked at Queenstown |
| `Embarked_S` | integer | 0-1 | Embarked at Southampton |

### Available Models

- **KNN**: K-Nearest Neighbors classifier
- **LR**: Logistic Regression classifier  
- **NB**: Naive Bayes classifier

## 🏗️ Project Structure

```
Titanic/
├── app/                          # Main application package
│   ├── core/                     # Core configurations
│   │   ├── config.py            # Application settings
│   │   ├── security.py          # Authentication setup
│   │   └── users.py             # User management
│   ├── database/                # Database configurations
│   ├── ml_models/               # Pre-trained ML models
│   │   ├── titanic_KNN_model.pkl
│   │   ├── titanic_LR_model.pkl
│   │   └── titanic_NB_model.pkl
│   ├── routers/                 # API route handlers
│   │   └── prediction.py        # Prediction endpoint
│   ├── schemas/                 # Pydantic data models
│   │   └── ml_models.py       # ML input/output schemas
│   ├── services/                # Business logic
│   │   └── prediction.py       # Prediction service
│   └── main.py                  # FastAPI application factory
├── tests/                       # Test suite
├── docker/                      # Docker configurations
├── alembic/                     # Database migrations
└── pyproject.toml              # Project dependencies
```

## 🔧 Development

### Setting up Development Environment

1. **Install development dependencies**
   ```bash
   pip install -e ".[dev]"
   ```

2. **Set up pre-commit hooks**
   ```bash
   pre-commit install
   ```

3. **Run tests**
   ```bash
   pytest
   ```

### Code Quality

This project uses several tools for code quality:

- **Ruff**: Fast Python linter and formatter
- **MyPy**: Static type checker
- **Pre-commit**: Git hook framework

### Environment Variables

Create a `.env` file in the root directory:

```env
ENVIRONMENT=development
DATABASE_URL=sqlite+aiosqlite:///./app.db
SYNC_DATABASE_URL=sqlite:///./app.db
SECRET_KEY=your-secret-key-here
FIRST_SUPERUSER=admin@example.com
FIRST_SUPERUSER_PASSWORD=admin
```

## 📊 Model Performance

The three pre-trained models have been optimized for the Titanic dataset:

- **Data Preprocessing**: Comprehensive feature engineering and data cleaning
- **Model Training**: Each model has been fine-tuned for optimal performance
- **Evaluation Metrics**: Models are evaluated using accuracy, precision, recall, and F1-score

*Note: Detailed performance metrics and training code can be found in the model training notebooks (available separately).*

## 🐳 Docker Configuration

The project includes two Docker Compose configurations:

### Development (`docker-compose.dev.yml`)
- SQLite database
- Hot-reload enabled
- Debug mode

### Production (`docker-compose.prod.yml`)  
- PostgreSQL database
- Gunicorn WSGI server
- Redis for Celery
- Optimized for performance

## 🔒 Security Features

- JWT-based authentication
- Password hashing with bcrypt
- CORS middleware configuration
- Environment-based configuration
- Secure database connections

## 🚀 Deployment

### Production Deployment Checklist

1. Set `ENVIRONMENT=production`
2. Configure PostgreSQL database
3. Set strong `SECRET_KEY`
4. Configure SMTP settings for email
5. Set up Redis for Celery
6. Enable HTTPS with SSL certificates
7. Configure proper CORS origins

### Scaling Considerations

- Use PostgreSQL for production database
- Configure Redis for Celery task queue
- Implement load balancing with multiple workers
- Use Gunicorn for production WSGI server
- Monitor with appropriate logging and metrics
