let url = `http://127.0.0.1:8000/api/posts/`;
let post_selector = document.getElementById('inputGroupSelect')

async function getPosts() {
    try{
        let response = await fetch(url);
        let data = await response.json();
        data.forEach(item => {
                post_selector.innerHTML += `<option value="${item.id}">${item.post}</option>`
        });
        // id.setAttribute('value', data['id'])
    } catch (error){
        console.log(error)
    }
}
getPosts()