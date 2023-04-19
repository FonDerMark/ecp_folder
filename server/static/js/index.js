// Асинхронная функция для получения данных с сервера и их парсинга
async function getData() {
    let table = document.getElementById('main-table')
    let url = 'http://127.0.0.1:8000/api/staff/' // Адрес для запроса
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
            fullnameCell.innerHTML = `<a href='/employeer_edit?id=${item.id}'>
                                            ${item.lastname} ${item.firstname} ${item.surname}
                                      </a>`;
            postCell.innerHTML = item.post;
            catCell.innerHTML = item.category;
            ageCell.innerHTML = item.age;
            genderCell.innerHTML = item.gender;
        });
    }catch (error){
        console.log(error);
    }
}
getData()
