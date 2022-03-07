var xhr = new XMLHttpRequest();
xhr.open("POST", "http://140.116.39.76:8000/member_info2/", true);
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.send(JSON.stringify({
    "test": "value"
}));