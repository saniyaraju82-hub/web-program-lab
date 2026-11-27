let users = [];

fetch("https://jsonplaceholder.typicode.com/users")
.then(response => response.json())
.then(data => {
    users = data;
    display(users);
});

function display(data) {
    let result = document.getElementById("result");
    result.innerHTML = "";

    if (data.length === 0) {
        result.innerHTML = "No results found";
        return;
    }

    data.forEach(user => {
        result.innerHTML += `
            <div class="item">
                <h3>${user.name}</h3>
                <p>${user.email}</p>
                <p>${user.address.city}</p>
            </div>
        `;
    });
}

function searchData() {
    let value = document.getElementById("search").value.toLowerCase();

    let filtered = users.filter(user =>
        user.name.toLowerCase().includes(value)
    );

    display(filtered);
}