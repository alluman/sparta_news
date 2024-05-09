<template>
    <div>
    <h1>Comments</h1>
    <ul>
    <li v-for="comment in comments" :key="comment.id">
        {{ comment.text }}
    </li>
    </ul>
</div>
</template>

<script>
export default {
data() {
    return {
    comments: [
        { id: 1, text: "This is a comment." },
        { id: 2, text: "This is another comment." }
    ]
    };
}
};
</script>