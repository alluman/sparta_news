<template>
    <nav>
    <router-link to="/">Home</router-link>
    <router-link to="/signup-login">Login/Signup</router-link>
    </nav>
</template>

    <script>
    export default {
    name: 'MainNavbar'
};
</script>

<style>
    nav {
    display: flex;
    justify-content: space-between;
    background-color: #333;
    padding: 1rem;
    color: white;
}
</style>
