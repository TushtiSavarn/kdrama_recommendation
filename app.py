from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Step 1: Load the K-drama dataset
data = pd.read_csv('kdrama_list.csv')

# Step 2: Data Cleaning
def clean_data(df):
    df = df.drop_duplicates(subset='Name').reset_index(drop=True)
    df['Genre'] = df['Genre'].fillna('')
    df['Sinopsis'] = df['Sinopsis'].fillna('')
    df['Tags'] = df['Tags'].fillna('')
    df['Sinopsis'] = df['Sinopsis'].str.replace('[^a-zA-Z0-9 ]', '', regex=True).str.lower()
    df['Genre'] = df['Genre'].str.lower()
    df['Tags'] = df['Tags'].str.lower()
    return df

data = clean_data(data)

# Step 3: Feature Engineering
def combine_features(df):
    df['combined_features'] = (df['Genre'] + ' ') * 2 + df['Tags'] + ' ' + df['Sinopsis']
    return df

data = combine_features(data)

# Step 4: TF-IDF Vectorizer and Cosine Similarity
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Step 5: Recommendation System Function
def get_recommendations(title, num_recommendations=5):
    try:
        idx = data.index[data['Name'] == title].tolist()[0]
    except IndexError:
        return [], "K-drama not found in the dataset. Here are some popular suggestions:", data.sample(5).to_dict(orient='records')

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations + 1]  # Exclude the input title
    kdrama_indices = [i[0] for i in sim_scores]
    recommendations = data.iloc[kdrama_indices].to_dict(orient='records')
    return recommendations, ""

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Recommendation Endpoint
@app.route('/recommend', methods=['POST'])
def recommend():
    req_data = request.get_json()
    title = req_data.get('title', '')
    print(f"Received title: {title}")

    if title:
        recommendations, message = get_recommendations(title)
        print(f"Recommendations: {recommendations}, Message: {message}")

        if recommendations:
            return jsonify(recommendations)
        else:
            return jsonify({"message": message, "recommendations": []})
    return jsonify({"message": "Title is required."})

# Autocomplete Endpoint
@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    query = request.args.get('q', '').lower()
    suggestions = data[data['Name'].str.lower().str.contains(query)]['Name'].tolist()
    return jsonify(suggestions[:10])

if __name__ == '__main__':
    app.run(debug=True)
