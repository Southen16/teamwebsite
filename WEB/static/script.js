const express = require('express');
const app = express();
const port = 3000;

// Implement your routes and database connections here

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

document.addEventListener('DOMContentLoaded', function () {
    const navToggle = document.getElementById('navToggle');
    const navList = document.querySelector('.nav-list');

    navToggle.addEventListener('click', function () {
        navList.classList.toggle('show');
    });
});

// script.js
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;
    
    // Simulated login logic (replace this with actual server-side code)
    // This is just an example of how it might work on the server
    simulateLogin(email, password)
      .then(response => {
        if (response.success) {
          window.location.href = '/dashboard'; // Redirect on successful login
        } else {
          console.error('Login failed');
          // You can show an error message on the page here
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
  });
  
  // Simulated login function (replace this with actual server-side authentication)
  function simulateLogin(email, password) {
    return new Promise((resolve, reject) => {
      // Simulate a server response (replace with actual server communication)
      setTimeout(() => {
        if (email === 'user@example.com' && password === 'password') {
          resolve({ success: true }); // Successful login
        } else {
          resolve({ success: false }); // Failed login
        }
      }, 1000); // Simulate delay of 1 second for server response
    });
  }
  const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/chittinadDB', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('Error connecting to MongoDB:', err));
