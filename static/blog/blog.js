var blog = new Vue({
    el: '#blog',
    data: {
        title: null,
        author: null,
        time: null,
        content: null
    }
})

$(document).ready(function(){
    
    $.ajax({
        url: '/blog/api/blog/1',
        success: function(res){
            var data = res;
            blog.title = data.title
            blog.author = data.author
            blog.time = data.time
            blog.content = data.content
        },
        error: function(_, err){
            console.log(err);
        }
    })
})