async function getWeather() {
    let city = document.getElementById("city").value;
    let result = document.getElementById("result");

    if (city.trim() === "") {
        result.innerHTML = "Please enter a city name";
        return;
    }

    let apiKey = "YOUR_API_KEY";
    let url = `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(city)}&appid=${apiKey}&units=metric`;

    try {
        let response = await fetch(url);

        if (!response.ok) {
            throw new Error("City not found");
        }

        let data = await response.json();

        result.innerHTML = `
            <h3>${data.name}</h3>
            <p>Temperature: ${data.main.temp} °C</p>
            <p>Humidity: ${data.main.humidity}%</p>
            <p>Weather: ${data.weather[0].description}</p>
        `;
    } catch (error) {
        result.innerHTML = "Unable to fetch weather. Check city name and API key.";
    }
}
