// Асинхронная функция для получения данных с сервера и их парсинга
async function getPosts() {
    let url = 'http://127.0.0.1:8000/api/posts/' // Адрес для запроса
    let table = document.getElementById('posts-table');
    try{
        let response = await fetch(url)
        let data = await response.json()
        console.log(data)
        data.forEach(item => {
            let newRow = table.insertRow(-1);
            let postCell = newRow.insertCell(0);
            let catCell = newRow.insertCell(1);
            postCell.innerHTML = `<a href='/post_edit/?post_id=${item.id}'>${item.post}</a>`;
            catCell.innerHTML = item.category;
        });
    }catch (error){
        console.log(error);
    }
}
getPosts()