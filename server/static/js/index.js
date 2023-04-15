async function getData() {
    let table = document.getElementById('main-table')
    let url = 'http://127.0.0.1:8000/api/staff/'
    try{
        let response = await fetch(url);
        let data = await response.json();
        data.forEach(item => {
            let newRow = table.insertRow(-1);
            let idCell = newRow.insertCell(0)
            let fullnameCell = newRow.insertCell(1);
            let postCell = newRow.insertCell(2);
            let catCell = newRow.insertCell(3);
            let ageCell = newRow.insertCell(4);
            let genderCell = newRow.insertCell(5);
            idCell.innerHTML = item.id;
            fullnameCell.innerHTML = `<a href='card_edit?id=${item.id}'>${item.lastname} ${item.firstname} ${item.surname}</a>`;
            postCell.innerHTML = item.post;
            catCell.innerHTML = item.category;
            ageCell.innerHTML = item.age;
            genderCell.innerHTML = item.gender;
        });
    }catch (error){
        console.log(error)
    }
}
async function getPosts() {
    let url = 'http://127.0.0.1:8000/api/posts/'
    let table = document.getElementById('posts-table')
    try{
        let response = await fetch(url);
        let data = await response.json();
        console.log(data)
        data.forEach(item => {
            let newRow = table.insertRow(-1);
            let postCell = newRow.insertCell(0);
            let catCell = newRow.insertCell(1);
            postCell.innerHTML = `<a href='#'>${item.post}</a>`;
            catCell.innerHTML = `<a href='#'>${item.category}</a>`;
        });
    }catch (error){
        console.log(error)
    }
}
