const products = [
    { name: "Laptop", price: 50000, category: "Electronics" },
    { name: "Mobile", price: 15000, category: "Electronics" },
    { name: "Shirt", price: 800, category: "Clothing" },
    { name: "Jeans", price: 1200, category: "Clothing" },
    { name: "Python Book", price: 500, category: "Books" }
];

function displayProducts() {
    let search = document.getElementById("search").value.toLowerCase();
    let category = document.getElementById("category").value;

    let result = products.filter(function(product) {
        return product.name.toLowerCase().includes(search) &&
               (category === "All" || product.category === category);
    });

    let output = "";

    result.forEach(function(product) {
        output += `
            <div class="product">
                <h3>${product.name}</h3>
                <p>Price: ₹${product.price}</p>
                <p>Category: ${product.category}</p>
            </div>
        `;
    });

    document.getElementById("products").innerHTML =
        output || "<p>No products found</p>";
}

displayProducts();
