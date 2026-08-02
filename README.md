# Netflix / Media Dataset - Exploratory Data Analysis (EDA)

## Project Overview

This project performs **Exploratory Data Analysis (EDA)** on the Netflix Movies and TV Shows dataset. The objective is to analyze the dataset, discover trends, visualize important insights, and generate a summary report.

The analysis includes exploring the distribution of Movies and TV Shows, release year trends, genre popularity, runtime distributions, and exporting visualizations along with a summary report.

---

## Dataset

**Dataset:** Netflix Movies and TV Shows

Source: https://www.kaggle.com/datasets/shivamb/netflix-shows

---

## Project Structure

```text
Netflix-EDA/
│
├── data/
│   └── netflix_titles.csv
│
├── images/
│   ├── movies_vs_tvshows.png
│   ├── content_distribution.png
│   ├── release_year_trend.png
│   ├── top10_release_years.png
│   ├── top10_genres.png
│   ├── movie_runtime_distribution.png
│   └── tv_show_seasons.png
│
├── reports/
│   └── summary_report.txt
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Features

* Load and inspect the Netflix dataset
* Perform data cleaning
* Analyze Movies vs TV Shows
* Explore release year trends
* Identify the Top 10 release years
* Analyze the most popular genres
* Visualize movie runtime distribution
* Visualize TV show season distribution
* Generate a summary report
* Save all visualizations as images

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn

---

## Installation

1. Clone or download this repository.

2. Install the required libraries:

```bash
pip install pandas matplotlib seaborn
```

or

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the project using:

```bash
python main.py
```

The program will:

* Load and clean the dataset
* Perform exploratory data analysis
* Display visualizations
* Save charts in the `images` folder
* Generate a summary report in the `reports` folder

---

## Visualizations Generated

* Movies vs TV Shows (Bar Chart)
* Content Distribution (Pie Chart)
* Release Year Trend (Line Chart)
* Top 10 Release Years
* Top 10 Genres
* Movie Runtime Distribution
* TV Show Season Distribution

---

## Key Insights

* Netflix contains significantly more Movies than TV Shows.
* Most titles in the dataset were released in recent years.
* Drama, International Movies, and Comedy are among the most common genres.
* Most movies have runtimes between approximately 80 and 120 minutes.
* Most TV Shows consist of only one season.

---

## Output

After running the project:

* Charts are saved inside the `images/` folder.
* A summary report is generated in `reports/summary_report.txt`.

---

## Author

Tanvi Pardeshi
