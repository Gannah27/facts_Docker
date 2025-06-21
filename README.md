# 💡 Fun Facts Generator API & Frontend

A full-stack project that serves random fun facts via a Flask REST API, backed by a PostgreSQL database, and presented through a simple web interface styled with TailwindCSS — all containerized with Docker.

---

## 🚀 Features

* 🐍 Flask API with random fun facts
* 🐘 PostgreSQL database to store facts
* 🌐 Nginx frontend serving a minimalist UI
* 🐳 Dockerized with multi-container setup
* 🔄 CORS-enabled API for frontend communication

---

## 📁 Project Structure

```
project-root/
├── docker-compose.yml
├── db/
│   └── init.sql              # SQL to create and populate funfacts table
├── facts-service/
│   ├── Dockerfile
│   ├── FunFactsapi.py        # Flask API
│   └── requirements.txt
└── FactsUI/
    ├── Dockerfile
    └── index.html            # Frontend using TailwindCSS
```

---

## ⚙️ Technologies Used

* Python (Flask)
* PostgreSQL
* Docker & Docker Compose
* HTML + TailwindCSS
* Nginx

---

## 📊 Endpoints

| Method | Endpoint | Description               |
| ------ | -------- | ------------------------- |
| GET    | `/fact`  | Returns a random fun fact |

Example Response:

```json
{ "fact": "Octopuses have three hearts." }
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fun-facts-app.git
cd fun-facts-app
```

### 2. Start with Docker

Make sure Docker is installed, then:

```bash
docker-compose up --build
```

The services will be available at:

* API: [http://localhost:5001/fact](http://localhost:5001/fact)
* UI: [http://localhost:5008/](http://localhost:5008/)

---

## 🗓️ SQL Setup

The `db/init.sql` file automatically runs on container startup. It:

* Creates a `funfacts` table
* Inserts several random fun facts

Make sure the file uses **PostgreSQL syntax** and single quotes (`'`) for strings.

---

## 🛮️ Troubleshooting

* **Database not initializing?**
  Run: `docker-compose down -v` to reset volumes, then restart.
* **API not returning facts?**

  * Check container logs: `docker-compose logs -f`
  * Ensure `funfacts` table exists in PostgreSQL.

---

## 📚 Example `init.sql`

```sql
CREATE TABLE funfacts (
  id SERIAL PRIMARY KEY,
  facts VARCHAR(250)
);

INSERT INTO funfacts (facts) VALUES
('Octopuses have three hearts.'),
('Bananas are berries, but strawberries aren''t.'),
('There''s a species of jellyfish that can live forever.');
```


