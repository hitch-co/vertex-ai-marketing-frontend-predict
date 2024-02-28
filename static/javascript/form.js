function submitForm() {

    var formData = {
        duration: document.getElementById('duration').value,
        poutcome: document.getElementById('poutcome').value,
        pdays: document.getElementById('pdays').value,
        housing: document.getElementById('housing').value,
        previous: document.getElementById('previous').value,
        marital: document.getElementById('marital').value,
        job: document.getElementById('job').value,
        campaign: document.getElementById('campaign').value,
        education: document.getElementById('education').value,
        age: document.getElementById('age').value,
        balance: document.getElementById('balance').value,
        default: document.getElementById('default').value,
        loan: document.getElementById('loan').value
    };

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        console.log(`This is the response.json (data): ${data}`)
        
        var displayed_results = JSON.stringify(data.prediction, null, 2)
        console.log(`This is the results for display: ${displayed_results}`)
        _displayResult(result = displayed_results)
        
        var runtime = data.runtime
        console.log(`This is the runtime: ${runtime}`)
        _displayRuntime(runtimeInfo = runtime)

        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function _displayResult(result) {
    resultValue = document.getElementById('resultValue');
    resultValue.innerHTML = '';
    resultValue.innerHTML = result;
}

function _displayRuntime(runtimeInfo) {
    var runtimeElement = document.getElementById('resultRuntimeValue');
    runtimeElement.innerHTML = runtimeInfo;
}
