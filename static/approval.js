document.getElementById('return-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting normally
    
    // Perform AJAX request to submit the form data to the backend
    // Include appropriate field values for the return form
    
    // Example AJAX request using Fetch API
    fetch('/submit_return/', {
      method: 'POST',
      body: new FormData(document.getElementById('return-form'))
    })
      .then(response => response.json())
      .then(data => {
        // Handle the response data
        // Display success message, show notifications, etc.
      })
      .catch(error => {
        // Handle any errors that occurred during the request
      });
  })