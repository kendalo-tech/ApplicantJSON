# ApplicantJSON

Takes input using the open fucntion, taking a file named data.json as the input.

Puts the data into a JSON object using json.load and pass the new json object into the calc_data function

Calc_data gets the applicants and iterates over them, getting the name and score for each and appending it to a list

Using json.dumps, returns a json object with the scoredApplicants inside, uses indent 4 for formatting

For scoring, the code iterates over the attributes and divides the value by 20, adding them together

However for the spicyTolerance value, I divided by 100 to value that one less  

# Sample Output
```
{  
    "scoredApplicants": [  
        {  
            "name": "John",  
            "score": 0.56  
        },  
        {  
            "name": "Jane",  
            "score": 0.72  
        },  
        {  
            "name": "Joe",  
            "score": 0.25  
        }  
    ]  
}  


