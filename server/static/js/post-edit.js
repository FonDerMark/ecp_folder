async function getPost() {
    let params = (new URL(document.location)).searchParams;
    let post_id = params.get("post_id");
    let url = `http://127.0.0.1:8000/api/post_edit/?post_id=${post_id}`
    let hidden_id = document.getElementById('post_id')
    let post = document.getElementById('post')
    let category = document.getElementById('category')
    try {
        let response = await fetch(url)
        let data = await response.json()
        hidden_id.setAttribute('value', data['id'])
        post.setAttribute('value', data['post'])
        category.setAttribute('value', data['category'])
    } catch (error) {
        console.log(error);
    }
}
getPost()