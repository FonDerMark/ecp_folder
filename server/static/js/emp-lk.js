let table = document.getElementById('posts-table');
let params = (new URL(document.location)).searchParams;
let employeer_id = params.get("id");
let url = `http://127.0.0.1:8000/api/lcard?id=${employeer_id}`;
let lastname = document.getElementById('lastname');
let firstname = document.getElementById('firstname');
let surname = document.getElementById('surname');
let post = document.getElementById('post');
let cat = document.getElementById('cat');
let age = document.getElementById('age');
let gender = document.getElementById('gender');
async function getEmployeer() {
    try{
        let response = await fetch(url);
        let data = await response.json();
        console.log(data);
        lastname.setAttribute('value', data['lastname'])
        firstname.setAttribute('value', data['firstname'])
        surname.setAttribute('value', data['surname'])
        post.setAttribute('value', data['post'])
        cat.setAttribute('value', data['category'])
        age.setAttribute('value', data['age'])
        gender.setAttribute('value', data['gender'])
    } catch (error){
        console.log(error)
    }
}
getEmployeer()