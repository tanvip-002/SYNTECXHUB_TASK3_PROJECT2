import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Load dataset
df = pd.read_csv("data/netflix_titles.csv")

# -------------------------
# Basic Information
# -------------------------

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nNumerical Statistics:")
print(df.describe())

print("\nCategorical Statistics:")
print(df.describe(include="str"))

# -------------------------
# Step 4: Data Cleaning
# -------------------------

# Create a copy of the dataset
clean_df = df.copy()

# Check missing values
print("\nMissing Values Before Cleaning:")
print(clean_df.isnull().sum())

# Remove duplicate rows
clean_df.drop_duplicates(inplace=True)

# Convert 'date_added' to datetime format
# Remove leading/trailing spaces
clean_df["date_added"] = clean_df["date_added"].str.strip()

# Convert to datetime
clean_df["date_added"] = pd.to_datetime(
    clean_df["date_added"],
    format="%B %d, %Y",
    errors="coerce"
)
# Check the first few converted dates
print("\nFirst 5 Date Added Values:")
print(clean_df["date_added"].head())

# Check data types after conversion
print("\nDataset Information After Cleaning:")
clean_df.info()

# Verify dataset shape after cleaning
print("\nDataset Shape After Cleaning:")
print(clean_df.shape)


# Count the number of Movies and TV Shows
type_counts = clean_df["type"].value_counts()

print("\nMovies vs TV Shows:")
print(type_counts)

plt.figure(figsize=(6, 5))

type_counts.plot(kind="bar")

plt.title("Number of Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("images/movies_vs_tvshows.png")

plt.show()

plt.figure(figsize=(6, 6))

type_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.ylabel("")

plt.title("Distribution of Netflix Content")

plt.tight_layout()

plt.savefig("images/content_distribution.png")

plt.show()

# -------------------------
# Step 6: Release Year Trends
# -------------------------

# Count titles released each year
year_counts = clean_df["release_year"].value_counts().sort_index()

print("\nContent Released Each Year:")
print(year_counts)

plt.figure(figsize=(12, 6))

plt.plot(year_counts.index, year_counts.values)

plt.title("Netflix Content by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.tight_layout()

plt.savefig("images/release_year_trend.png")

plt.show()

top_10_years = clean_df["release_year"].value_counts().head(10)

print("\nTop 10 Release Years:")
print(top_10_years)

plt.figure(figsize=(10, 6))

top_10_years.sort_values().plot(kind="barh")

plt.title("Top 10 Release Years on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Release Year")

plt.tight_layout()

plt.savefig("images/top10_release_years.png")

plt.show()

# -------------------------
# Step 7: Top Genres
# -------------------------

# Split genres into individual entries
genres = clean_df["listed_in"].str.split(", ")

# Convert list of genres into separate rows
genres = genres.explode()

genre_counts = genres.value_counts()

print("\nTop Genres:")
print(genre_counts)

top_10_genres = genre_counts.head(10)

print("\nTop 10 Genres:")
print(top_10_genres)

plt.figure(figsize=(10, 6))

top_10_genres.sort_values().plot(kind="barh")

plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")

plt.tight_layout()

plt.savefig("images/top10_genres.png")

plt.show()

# -------------------------
# Step 8: Runtime Distribution
# -------------------------

movies = clean_df[clean_df["type"] == "Movie"].copy()
movies["duration"] = movies["duration"].str.replace(" min", "", regex=False)
movies["duration"] = pd.to_numeric(movies["duration"], errors="coerce")
print(movies["duration"].head())
plt.figure(figsize=(10,6))

plt.hist(movies["duration"].dropna(), bins=30)

plt.title("Distribution of Movie Runtime")
plt.xlabel("Runtime (Minutes)")
plt.ylabel("Number of Movies")

plt.tight_layout()

plt.savefig("images/movie_runtime_distribution.png")

plt.show()

tv_shows = clean_df[clean_df["type"] == "TV Show"].copy()
tv_shows["duration"] = (
    tv_shows["duration"]
    .str.replace(" Seasons", "", regex=False)
    .str.replace(" Season", "", regex=False)
)

tv_shows["duration"] = pd.to_numeric(tv_shows["duration"], errors="coerce")
season_counts = tv_shows["duration"].value_counts().sort_index()

print("\nTV Show Seasons:")
print(season_counts)

plt.figure(figsize=(10,6))

season_counts.plot(kind="bar")

plt.title("Number of TV Shows by Seasons")
plt.xlabel("Number of Seasons")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("images/tv_show_seasons.png")

plt.show()

# -------------------------
# Step 9: Generate Summary Report
# -------------------------

# Get summary statistics
total_titles = len(clean_df)
movies_count = clean_df[clean_df["type"] == "Movie"].shape[0]
tvshows_count = clean_df[clean_df["type"] == "TV Show"].shape[0]

top_genre = genre_counts.idxmax()
top_genre_count = genre_counts.max()

top_year = year_counts.idxmax()
top_year_count = year_counts.max()

# Create summary text
summary = f"""
===============================
NETFLIX DATASET EDA SUMMARY
===============================

Total Titles: {total_titles}

Movies: {movies_count}
TV Shows: {tvshows_count}

Most Common Genre:
{top_genre} ({top_genre_count} titles)

Release Year with Most Titles:
{top_year} ({top_year_count} titles)

Dataset Columns:
{', '.join(clean_df.columns)}

Missing Values:
{clean_df.isnull().sum()}

===============================
End of Report
===============================
"""

# Save report
with open("reports/summary_report.txt", "w", encoding="utf-8") as file:
    file.write(summary)

print("\nSummary report saved successfully!")