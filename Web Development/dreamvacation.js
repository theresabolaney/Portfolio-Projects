var express = require("express");
var app = express();

var handlebars = require("express-handlebars").create({defaultLayout:'main'});

var path = require("path");

app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', 4007);

app.use(express.static('public'));

app.get('/', function(req, res){
    res.render("home");
})

app.get("/activities", function(req, res){
    res.render("activities");
})

app.get("/places-to-stay", function(req, res){
    res.render("placesToStay");
})

app.get("/feedback", function(req, res){
    res.render("feedback");
})

app.listen(app.get('port'), function(){
    console.log('Web page is up and running on http://localhost:' + app.get('port') + '. Press Ctrl+C to stop.');
})