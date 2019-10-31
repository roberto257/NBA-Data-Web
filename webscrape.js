//Require the package we need to work with text files
const fs = require('fs');
//Require our two webscraping packages
const axios = require('axios');
const cheerio = require('cheerio');

//URL for our to start...this is the link to the page for the Charlotte Hornets
const url = 'https://www.basketball-reference.com/teams/CHO/2020.html';

//Use axios to make our request
axios.get(url).then(response => {
    console.log(response.data);
    //Catch any errors thrown
}).catch(error => {
    console.log(error);
});