<template>
    <div>
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
    <router-link to="/comments">View Comments</router-link>
</div>
</template>

<script>
export default {
data() {
    return {
    post: {
        id: 1,
        title: "Post One",
        content: "Here is some content for the post."
    }
    };
}
};
</script>
