async function getPost() {
    let params = (new URL(document.location)).searchParams;
    let post_id = params.get("post_id");
    let url = `http://127.0.0.1:8000/api/post_get/?post_id=${post_id}`
    let hidden_id = document.getElementById('post_id')
    let post = document.getElementById('post')
    let categorys = document.querySelectorAll('.category__opt')
    let delete_post = document.getElementById('delete_post')
    try {
        let response = await fetch(url)
        let data = await response.json()
        console.log(data)
        hidden_id.setAttribute('value', data['id'])
        post.setAttribute('value', data['post'])
        categorys.forEach(item => {
            if (data['category'] === item.value) {
                item.setAttribute('selected', 'true')
            }
        })
        delete_post.setAttribute(`href`, `/api/post_delete/?id=${post_id}`)
    } catch (error) {
        console.log(error);
    }
}
getPost()