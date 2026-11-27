const API_KEY = "YOUR_API_KEY";

async function loadNews(query = "india") {
    const news = document.getElementById("news");
    news.innerHTML = "Loading news...";

    try {
        const url = `https://newsapi.org/v2/everything?q=${encodeURIComponent(query)}&language=en&sortBy=publishedAt&apiKey=${API_KEY}`;

        const response = await fetch(url);
        const data = await response.json();

        if (data.status !== "ok") {
            throw new Error(data.message);
        }

        news.innerHTML = "";

        data.articles.forEach(article => {
            news.innerHTML += `
                <div class="news">
                    <img src="${article.urlToImage || 'https://placehold.co/400x200?text=No+Image'}">
                    <h3>${article.title}</h3>
                    <p>${article.description || "No description available"}</p>
                    <p><b>Source:</b> ${article.source.name}</p>
                    <p><b>Date:</b> ${new Date(article.publishedAt).toLocaleDateString()}</p>
                </div>
            `;
        });

        if (data.articles.length === 0) {
            news.innerHTML = "No news found";
        }

    } catch (error) {
        news.innerHTML = "Error loading news. Check API key.";
        console.log(error);
    }
}

function searchNews() {
    const query = document.getElementById("search").value;
    if (query.trim() !== "") {
        loadNews(query);
    }
}

loadNews();