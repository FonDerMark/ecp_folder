let url = `http://127.0.0.1:8000/api/posts/`; // Адрес для запроса
let post_selector = document.getElementById('inputGroupSelect')
// Асинхронная функция для получения данных с сервера и их парсинга
async function getPosts() {
    try{
        let response = await fetch(url);
        let data = await response.json();
        data.forEach(item => {
                post_selector.innerHTML += `<option value="${item.id}">${item.post}</option>`
        });
    } catch (error){
        console.log(error)
    }
}
getPosts()