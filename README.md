# 🌟 K-Drama Recommendation System 📺💻

Welcome to the **K-Drama Recommendation System** project! This web application helps users discover new K-drama shows based on their preferences. Built using Python, Flask, and a bit of data magic with pandas and scikit-learn, the system provides personalized recommendations for K-drama fans worldwide! 🎉

---

## 📝 Project Overview

This project leverages **content-based filtering** to recommend K-dramas based on user input, such as genre preferences. It uses **TF-IDF vectorization** and **cosine similarity** to analyze a dataset of K-dramas and return suggestions that closely match the user’s input.

💾 **Dataset**: The project is powered by a K-drama dataset, which you can check out [here](https://example.com/kdrama_dataset.csv).

### **Key Features**:
- 🔍 **Search by K-Drama Title**: Enter the title of a show you like, and the system will recommend similar shows.
- 📊 **Recommendations Based on Genres, Tags, and Synopses**: The system analyzes drama content and tags to make recommendations.
- 📱 **Responsive User Interface**: The interface adapts to mobile and desktop screens for ease of use.
- 🌟 **Displays Show Details**: Recommendations come with detailed information like genre, score, and episode count.

---

## 🚀 Getting Started

### **Prerequisites**

Before running this project, ensure you have the following installed:
- **Python 3.x** 
- **Flask** 
- **Pandas**
- **Scikit-learn**

You can install the necessary dependencies using the following command:

```bash
pip install flask pandas scikit-learn
```

### **Clone the Repository**

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/kdrama-recommendation-system.git
cd kdrama-recommendation-system
```

### **Dataset**

Make sure the **`kdrama_list.csv`** file is placed in the project directory. The dataset contains K-drama details like:
- Title
- Genre
- Main Cast
- Synopsis
- Tags
- Score
- Content Rating
- Episode Count
- Image URL

💾 **Dataset**: You can download the dataset from [here](https://example.com/kdrama_dataset.csv).

### **Run the App**

Once everything is set up, you can run the Flask server using the following command:

```bash
python app.py
```

Navigate to `http://127.0.0.1:5000/` in your browser to use the app.

---

## 🛠 Project Structure

Here's a quick overview of the project structure:

```bash
kdrama-recommendation-system/
│
├── templates/
│   └── index.html        # Frontend HTML file
│
├── static/
│   ├── styles.css        # Styling for the app
│   └── script.js         # JavaScript to handle user interaction
│
├── app.py                # The main Flask app
├── kdrama_list.csv       # Dataset of K-dramas
└── README.md             # Project documentation
```

### **How It Works**

1. **User Input**: Users enter a K-drama title or choose from suggestions.
2. **Content-Based Filtering**: Using **TF-IDF vectorization** and **cosine similarity**, the app compares shows based on the combination of genres, tags, and synopses.
3. **Recommendations**: A list of similar K-dramas is presented with details like the title, genre, score, and episode count. 🎬

---

## 📈 Future Improvements

- **User Accounts**: Add user authentication so users can save their favorite K-dramas and recommendations.
- **Advanced Filters**: Allow filtering by actors, moods, or specific themes like "high school drama" or "historical fiction."
- **Integration with Streaming Platforms**: Provide direct links to streaming services like Netflix or Viki for recommended shows.
- **Improved Image Handling**: Fix any broken image links or missing images for K-dramas that don’t provide an `img_url`.

---

## 💻 Tech Stack

- **Backend**: Flask (Python)
- **Data Handling**: Pandas
- **Machine Learning**: Scikit-learn (TF-IDF Vectorizer, Cosine Similarity)
- **Frontend**: HTML, CSS, JavaScript
- **Data**: CSV dataset of K-dramas

💾 **Dataset**: You can find the dataset [here](https://example.com/kdrama_dataset.csv).

---

## 🏗 Contributing

Contributions are welcome! If you'd like to contribute to this project, feel free to submit a pull request or open an issue with any ideas or improvements.

---

## 📧 Contact

If you have any questions or feedback, feel free to reach out at **tushtisavran@gmail.com**.

---

### **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

🌟 **Thank you for checking out the K-Drama Recommendation System!** 🌟  
Feel free to fork, star, or contribute to the project. I hope you enjoy discovering your next favorite K-drama! ✨

---

