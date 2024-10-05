const form = document.getElementById('kdramaForm');
const titleInput = document.getElementById('kdramaTitle');
const suggestionsList = document.getElementById('suggestions');
const recommendationsDiv = document.getElementById('recommendations');

// Event listener for typing in the input field to trigger autocomplete
if (titleInput) {
    titleInput.addEventListener('input', function() {
        const query = titleInput.value;
        if (query.length > 1) {
            fetch(`/autocomplete?q=${query}`)
                .then(response => response.json())
                .then(data => {
                    suggestionsList.innerHTML = '';  // Clear existing suggestions
                    data.forEach(suggestion => {
                        const li = document.createElement('li');
                        li.textContent = suggestion;
                        li.addEventListener('click', () => {
                            titleInput.value = suggestion;
                            suggestionsList.innerHTML = '';  // Clear suggestions after selection
                        });
                        suggestionsList.appendChild(li);
                    });
                });
        } else {
            suggestionsList.innerHTML = '';  // Clear suggestions if input is less than 2 characters
        }
    });
}

// Event listener for form submission to fetch K-drama recommendations
if (form) {
    form.addEventListener('submit', function(event) {
        event.preventDefault();  // Prevent default form submission
        const title = titleInput.value;
        if (title) {
            fetch('/recommend', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ title: title })
            })
            .then(response => response.json())
            .then(data => {
                recommendationsDiv.innerHTML = '';  // Clear previous recommendations
                data.forEach(drama => {
                    const div = document.createElement('div');
                    div.classList.add('recommendation');
                    
                    // Title
                    const name = document.createElement('h3');
                    name.textContent = drama.Name;
                    name.classList.add('title');

                    // Genre
                    const genre = document.createElement('p');
                    genre.innerHTML = `<strong>Genre:</strong> ${drama.Genre}`;
                    genre.classList.add('genre');

                    // Synopsis
                    const synopsis = document.createElement('p');
                    synopsis.textContent = drama.Sinopsis;
                    synopsis.classList.add('synopsis');
                    
                    // Append elements to div
                    div.appendChild(name);
                    div.appendChild(genre);
                    div.appendChild(synopsis);

                    // Append div to recommendations container
                    recommendationsDiv.appendChild(div);
                });
            });
        }
    });
}
