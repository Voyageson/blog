var blog = new Vue({
    el: '#blog',
    data: {
        title: null,
        author: null,
        time: null,
        content: null
    }
})

var data = {
    title: 'this is blog title',
    author: 'Voy',
    time: '20-1-10',
    content: 'this is blog content'
}

blog.title = data.title
blog.author = data.author
blog.time = data.time
blog.content = data.content