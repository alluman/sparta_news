<template>
<div>
    <h1>Posts</h1>
    <ul>
    <li v-for="post in posts" :key="post.id">
        <router-link :to="'/post/' + post.id">{{ post.title }}</router-link>
    </li>
    </ul>
</div>
</template>

<script>
export default {
data() {
    return {
    posts: [
        { id: 1, title: "Post One" },
        { id: 2, title: "Post Two" }
    ]
    };
}
};
</script>