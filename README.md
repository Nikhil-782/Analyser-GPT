# 🤖 Analyser-GPT

Analyser-GPT is an AI-powered CSV Data Analysis Assistant built using Streamlit, AutoGen, Docker, and Python.

Upload a CSV file, ask questions in natural language, generate visualizations, and receive insights from your data through an AI-powered multi-agent workflow.

---

## Features

- Upload CSV files
- Ask questions about CSV data
- Generate graphs and visualizations
- AI-powered data analysis
- Automatic Python code execution in Docker

---

## 🏗 Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
Data Analyzer Agent
 │
 ▼
Code Executor Agent
 │
 ▼
Docker Environment
 │
 ▼
Insights & Visualizations
```

---

## 🛠 Tech Stack

* Python
* Streamlit
* AutoGen
* Docker
* Pandas
* Matplotlib
* OpenRouter

---

## 📋 Prerequisites

### Python

This project was tested with Python 3.14.4.

Verify installation:

```bash
python --version
```

### Docker

Verify Docker installation:

```bash
docker --version
```

Start Docker Desktop before running the application.

The Code Executor Agent requires Docker to execute AI-generated Python code.
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Nikhil-782/Analyser-GPT.git
cd Analyser-GPT
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application

Start Docker.

Run the Streamlit application:

```bash
streamlit run
```

Open the URL shown in the terminal (typically):

```text
http://localhost:8501
```

---

## 📊 Example Questions

After uploading a CSV file, try:

### Dataset Exploration

* What are the column names?
* Explain each column.
* Show the first 10 rows.
* How many records are in the dataset?
* Are there any missing values?

### Statistical Analysis

* What is the average value of each numeric column?
* Show descriptive statistics.
* What is the highest and lowest value?

### Visualizations

* Create a histogram of grades.
* Generate a scatter plot comparing two columns.
* Create a pie chart of category distribution.
* Generate a bar chart of top performers.

### Insights

* Summarize the dataset.
* Identify patterns and trends.
* Find outliers.
* Explain the generated graph.

---

## 📁 Project Structure

```text
Analyser-GPT/
│
├── app.py
├── config/
├── models/
├── teams/
├── temp/
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

---

## 🔐 Environment Variables

Required:

```env
OPENROUTER_API_KEY=your_api_key_here
```


## 👨‍💻 Author

**Nikhil Abotula**

B.Tech Student | Python Developer | AI Enthusiast

GitHub: https://github.com/Nikhil-782

---