<template>
<div>
    <h1>Posts</h1>
    <ul>
    <li v-for="comment in comments" :key="post.id">
        <div>
        <p>
            {{ comment.author }}
        </p>
        <p>
            {{ comment.created_at }}
        </p>
        <p>
            {{ comment.content }}  
        </p>
        <p>
            {{ comment.liked }}
        </p>
        </div>
    </li>
    </ul>
</div>
</template>

<script>
import axios from 'axios';

export default {
data() {
    return {
    posts: []
    };
},
created() { 
    axios.get('http://localhost:8000/api/posts/comments/') 
    .then(response => {
        this.posts = response.data;
    })
    .catch(error => console.error('Error:', error));
}
};
</script>

<style>
/* Optional: Some styling for your posts */
</style>
