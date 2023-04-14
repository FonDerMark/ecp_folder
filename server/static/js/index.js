let table = document.getElementById('main-table')
let url = 'http://127.0.0.1:8000/api/'
async function getData() {
    try{
        let response = await fetch(url);
        let data = await response.json();
        console.log(data)
        data.forEach(item => {
            let newRow = table.insertRow(-1);
            let nameCell = newRow.insertCell(0);
            let surnameCell = newRow.insertCell(1);
            let genderCell = newRow.insertCell(2);
            let ageCell = newRow.insertCell(3);
            let catCell = newRow.insertCell(4);
            let postCell = newRow.insertCell(5);
            nameCell.innerHTML = item.id;
            surnameCell.innerHTML = item.lastname + ' ' + item.firstname + ' ' + item.surname;
            genderCell.innerHTML = item.gender;
            ageCell.innerHTML = item.age;
            catCell.innerHTML = item.category;
            postCell.innerHTML = item.post;

        });
    }catch (error){
        console.log(error)
    }
}
getData()
