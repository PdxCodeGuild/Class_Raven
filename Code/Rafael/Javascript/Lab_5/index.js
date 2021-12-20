// LAB:05 API - Class Raven - Rafael Medina
/*--- axios.post() to make an HTTP POST request, requires 2 parameters ---*/

let button = document.querySelector('#submit-btn'),
    h1 = document.querySelector('.result')

/**(Shorthand methods -Axios- )**
axios.request(config)
axios.get(url[, config])
axios.delete(url[, config])
axios.head(url[, config])
axios.options(url[, config])
axios.post(url[, data[, config]])
axios.put(url[, data[, config]])
axios.patch(url[, data[, config]])  
*/

button.addEventListener('click', ()=>{
/**(Shorthand method -Axios- )**/
/*---"axios.request(config)
axios.get(url[, config]) "  ---*/
const getQuote = () =>{
    axios
      .get("https://favqs.com/api/qotd")
      //.then(data => console.log(data.data.quote.body))
      .then(data => h1.innerHTML = (data.data.quote.body))
      .catch(error => console.log(error));     
};
getQuote();
})






/*
button.addEventListener('click', ()=>{
  console.log("Test Response");
  console.log(axios) 
})
*/

/**(

function fetchQuote (){
  //data : {
                //firstName: 'John'    ,
                //lastName : 'Williams'
            
  const headers = {
    Accept: 'application/json'
    }
    const url = 'https://favqs.com/api/qotd'
     // 'http://127.0.0.1:5500/index.html',
    
    return axios.get(url, {headers: headers})
    .then(response =>{
      console.log(response.data.quote.body)
    })

    .catch(error => console.log('error'. error))
            /*-- one advantage of axios is that you don't need to convert to JSON --*/
            /*--
            }--*/
//          }
//          fetchQuote()
          

//  ) 
//  */