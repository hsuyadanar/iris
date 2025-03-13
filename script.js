const form = document.getElementById('irisForm');
const result = document.getElementById('result');

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    console.log("Sending request to FastAPI...");

    // Gather form data
    const sepal_length = parseFloat(document.getElementById('sepal_length').value);
    const sepal_width = parseFloat(document.getElementById('sepal_width').value);
    const petal_length = parseFloat(document.getElementById('petal_length').value);
    const petal_width = parseFloat(document.getElementById('petal_width').value);

    const irisData = { sepal_length, sepal_width, petal_length, petal_width };
    console.log(irisData)
    // Send POST request to FastAPI
    try {
        console.log("in try")
        const response = await fetch('https://myeonn.pythonanywhere.com/predict/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(irisData),
        });

        const resultData = await response.json();
        result.textContent = `Predicted Species: ${resultData.species}`;
    } catch (error) {
        console.error('Error:', error);
        result.textContent = 'Error occurred while predicting.';
    }
});
