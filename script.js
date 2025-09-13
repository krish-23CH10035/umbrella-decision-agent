// Find the button and the input box in the HTML
const checkBtn = document.getElementById('checkBtn');
const cityInput = document.getElementById('cityInput');
const resultDiv = document.getElementById('result');

// Add an event listener that runs a function when the button is clicked
checkBtn.addEventListener('click', async () => {
    const city = cityInput.value; // Get the city name from the input box

    // Check if the user actually typed something
    if (!city) {
        alert('Please enter a city!');
        return; // Stop the function
    }

    resultDiv.innerHTML = 'Checking the skies... ☁️';
    resultDiv.className = ''; // Reset the color

    try {
        // This is the magic part: it calls our backend agent.
        // The `?city=${city}` part sends the city name to the backend.
        const response = await fetch(`/api/weather?city=${city}`);
        const data = await response.json(); // Get the response from the backend

        // Display the result
        if (data.error) {
            resultDiv.innerHTML = data.error;
            resultDiv.className = 'yes'; // Show error in red
        } else {
            resultDiv.innerHTML = `${data.icon} ${data.suggestion}`;
            resultDiv.className = data.bringUmbrella ? 'yes' : 'no'; // Set color based on result
        }
    } catch (error) {
        resultDiv.innerHTML = 'Failed to get weather data. Please try again.';
        resultDiv.className = 'yes';
    }
});