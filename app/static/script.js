// Add event listener to the submit button
document.getElementById('transaction-form').addEventListener('submit', (e) => {
    e.preventDefault();
    // Get the form data
    const formData = new FormData(e.target);
    // Send the data to the server
    fetch('/api/transactions/', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => {
        // Update the balance
        document.getElementById('balance').innerHTML = `Balance: ${data.balance}`;
    })
    .catch((error) => console.error(error));
});