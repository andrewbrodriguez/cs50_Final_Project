// use this to prevent errors
'use strict';
document.querySelector('form').addEventListener('submit',function(event){
    // Make sure form doesn't submit before rick can join us
    event.preventDefault();
    document.querySelector('.loading').style.display = 'block';
});
