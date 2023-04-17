let table = document.getElementById('posts-table');
let params = (new URL(document.location)).searchParams;
let employeer_id = params.get("id");
console.log(employeer_id)
let url = `http://127.0.0.1:8000/api/lcard?id=${employeer_id}`;
let url_posts = `http://127.0.0.1:8000/api/posts/`;

let id = document.getElementById('id')
let lastname = document.getElementById('lastname');
let firstname = document.getElementById('firstname');
let surname = document.getElementById('surname');
let post_selector = document.getElementById('inputGroupSelect')
let cat = document.getElementById('cat');
let age = document.getElementById('age');
let gender = document.getElementById('gender');
let genders = document.querySelectorAll('.gender__opt')


async function getEmployeer() {
    try{
        let response = await fetch(url);
        let data = await response.json();
        let postsResponse = await fetch(url_posts)
        let posts = await postsResponse.json()
        posts.forEach(item => {
            if (data['post_id'] === item.id) {
                post_selector.innerHTML += `<option value="${item.id}" selected>${item.post}</option>`
            } else {
                post_selector.innerHTML += `<option value="${item.id}">${item.post}</option>`
            }
        })
        genders.forEach(item => {
            if (item.value === data['gender']) {
                item.setAttribute('selected', 'true')
            }
        })
        id.setAttribute('value', employeer_id)
        lastname.setAttribute('value', data['lastname'])
        firstname.setAttribute('value', data['firstname'])
        surname.setAttribute('value', data['surname'])
        cat.setAttribute('value', data['category'])
        age.setAttribute('value', data['age'])
        gender.setAttribute('value', data['gender'])

    } catch (error){
        console.log(error)
    }
}
getEmployeer()