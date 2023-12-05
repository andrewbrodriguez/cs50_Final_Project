// use this to prevent errors
'use strict';
document.querySelector('form').addEventListener('submit',function(event){
    // Make sure rick doesn't appear prematurely
    document.querySelector('.loading').style.display = 'block';
});
