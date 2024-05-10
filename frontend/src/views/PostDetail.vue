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
        axios.get('http://localhost:8000/api/posts/<int:post_id>')// commentslist, replislist 같이 가져와서 정렬해서 보여줘야함, 데이터 받아서 저장할 수 있나? 송신됨?
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
    