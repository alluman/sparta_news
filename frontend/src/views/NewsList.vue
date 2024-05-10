<template>
<div>
    <h1>Posts</h1>
    <ul>
    <li v-for="post in posts" :key="post.id">
        <div>
        <p>
            {{ post.type }}
        </p>
        <p>
            {{ post.title }}
        </p>
        <p>
            {{ post.content }}  
        </p>
        <p>
            {{ post.link }}
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
    axios.get('http://localhost:8000/api/posts/news/')
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
