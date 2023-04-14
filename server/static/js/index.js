async function getData() {
    let table = document.getElementById('main-table')
    let url = 'http://127.0.0.1:8000/api/staff/'
    try{
        let response = await fetch(url);
        let data = await response.json();
        data.forEach(item => {
            let newRow = table.insertRow(-1);
            let nameCell = newRow.insertCell(0);
            let surnameCell = newRow.insertCell(1);
            let genderCell = newRow.insertCell(2);
            let ageCell = newRow.insertCell(3);
            let catCell = newRow.insertCell(4);
            let postCell = newRow.insertCell(5);
            nameCell.innerHTML = item.id;
            // surnameCell.innerHTML = item.lastname + ' ' + item.firstname + ' ' + item.surname;
            surnameCell.innerHTML = `<a href='#'>${item.lastname} ${item.firstname} ${item.surname}</a>`;
            genderCell.innerHTML = item.gender;
            ageCell.innerHTML = item.age;
            catCell.innerHTML = item.category;
            postCell.innerHTML = item.post;
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
