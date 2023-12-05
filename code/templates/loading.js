// Duck told me this was a good idea to handle errors
'use strict'; 
var loadingDiv = document.querySelector('.loading');
var progressBar = document.getElementById('progress-bar');
document.querySelector('form').addEventListener('submit', function(event)
{
    event.preventDefault();
    // Show the loading screen
    document.querySelector('.loading img').style.display = 'block';
    document.querySelector('.loading #progress-container').style.display = 'block';
    document.querySelector('.loading #progress-bar').style.display = 'block';
    // Update the progress bar
    var width = 0;
    var interval = setInterval(function() 
    {
        if (width >= 100) 
        {
            clearInterval(interval);
            // Hide the loading screen
            loadingDiv.style.display = 'none';
        } 
        else 
        {
            width++; 
            progressBar.style.width = width + '%'; 
        }
    }, 100);
});